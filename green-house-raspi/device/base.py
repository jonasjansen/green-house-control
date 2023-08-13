import json
import time

import pigpio

from api.zigbee import zigbee
from config_provider import config


class ZigbeeBase:
    device_id = 0

    def get_state(self):
        try:
            response = zigbee.get_state(self.device_id)
            response_json = json.loads(response.content)

            if "state" in response_json and "on" in response_json["state"]:
                return bool(response_json["state"]["on"])

        except Exception as e:
            print(e)

        return False

    def turn_on(self):
        try:
            result = zigbee.set_state(self.device_id, json.dumps({"on": True}))
        except Exception as e:
            print("Could not turn on Zigbee device", self.device_id, ":", e)

    def turn_off(self):
        try:
            result = zigbee.set_state(self.device_id, json.dumps({"on": False}))
        except Exception as e:
            print(e)


class BasePump(ZigbeeBase):
    device_id = 0
    gpio_direction = 0
    gpio_step = 0

    def run(self, drive_time=0):
        if drive_time > 0:
            self.turn_on()
            time.sleep(0.5)
            self.turn_motor(drive_time)
            time.sleep(0.5)
            self.turn_off()

    def turn_motor(self, drive_time):
        # Connect to pigpiod daemon
        pi = pigpio.pi()

        # Set up pins as an output
        pi.set_mode(self.gpio_direction, pigpio.OUTPUT)
        pi.set_mode(self.gpio_step, pigpio.OUTPUT)

        # Micro step Resolution for pins 14,15,18
        # Full: 0 0 0
        # Half: 1 0 0
        # 1/4:  0 1 0
        # 1/8:  1 1 0
        # 1/16: 0 0 1
        # 1/32: 1 0 1

        pi.write(config.get_config('GPIO/PUMP/MODE_1'), 0)
        pi.write(config.get_config('GPIO/PUMP/MODE_2'), 0)
        pi.write(config.get_config('GPIO/PUMP/MODE_3'), 0)

        # Set duty cycle and frequency
        pi.set_PWM_dutycycle(self.gpio_step, 128)
        pi.set_PWM_frequency(self.gpio_step, 500)

        start_time = time.time()

        while time.time() < start_time + drive_time:
            # set direction and move
            pi.write(self.gpio_direction, 1)
            time.sleep(.1)

        pi.set_PWM_dutycycle(self.gpio_step, 0)  # PWM off
        pi.stop()
