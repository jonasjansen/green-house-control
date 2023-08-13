# Actual control
import time

from device.sensor.dht import dht as dht_sensor
from device.sensor.moisture import moisture as moisture_sensor
from device.switch.light import light
from device.switch.heater import heater
from device.motor.window_servo import window_servo
from device.motor.humidity_pump import humidity_pump
from device.motor.watering_pump import watering_pump
from logger import logger

def run():
    print("Run component test")
    print("\n")
    print("Step 1: Sensors")
    print("\n")

    # get sensor values
    humidity, temperature = dht_sensor.get_values()
    moisture = moisture_sensor.get_moisture()
    light_status = light.get_state()
    heater_status = heater.get_state()

    # log sensor values
    logger.info("humidity: " + str(humidity))
    logger.info("temperature: " + str(temperature))
    logger.info("moisture: " + str(moisture))
    logger.info("light_status: " + str(light_status))
    logger.info("heater_status: " + str(heater_status))

    print("\n")
    print("Step 2: Power Switches")
    print("\n")

    time.sleep(1)
    print("Turn Heater On.")
    heater.turn_on()
    time.sleep(1)
    print("Turn Heater Off.")
    heater.turn_off()
    time.sleep(1)

    time.sleep(1)
    print("Turn Light On.")
    light.turn_on()
    time.sleep(1)
    print("Turn Heater Off.")
    light.turn_off()
    time.sleep(1)

    print("\n")
    print("Step 3: Motors")
    print("\n")

    time.sleep(1)
    print("Open Window.")
    window_servo.open_window()
    time.sleep(1)
    print("Close Window.")
    window_servo.close_window()
    time.sleep(1)

    print("Run Humidity Pump for 5 seconds.")
    humidity_pump.run(5)
    time.sleep(1)
    print("Run Watering Pump for 5 seconds.")
    watering_pump.run(5)
    time.sleep(1)

    print("\n")
    print("Finished")
    print("\n")
