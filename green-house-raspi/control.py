# Actual control
from time import sleep
from api.firebase import firebase

from device.sensor.dht import dht as dht_sensor
from device.sensor.moisture import moisture as moisture_sensor
from device.switch.light import light
from device.switch.heater import heater
from device.motor.window_servo import window_servo
from device.motor.humidity_pump import humidity_pump
from device.motor.watering_pump import watering_pump
from device.camera.picture import picture
from device.camera.sprout_detect import sprout_detect

from config_provider import config
from logger import logger
import datetime

ACTION_ON = 1
ACTION_OFF = 0
ACTION_OPEN = 1
ACTION_CLOSED = 0


def run():
    try:
        # current hour
        now = datetime.datetime.now()
        current_hour = now.hour

        # take picture
        picture.take()

        # get sensor values
        humidity, temperature = dht_sensor.get_values()
        moisture = moisture_sensor.get_moisture()
        light_state = light.get_state()
        heater_state = heater.get_state()

        # log sensor values
        logger.info("humidity: " + str(humidity))
        logger.info("temperature: " + str(temperature))
        logger.info("moisture: " + str(moisture))
        logger.info("light_status: " + str(light_state))
        logger.info("heater_status: " + str(heater_state))

        # determine app actions
        actions = {"timestamp": now}

        # light
        if config.get_config('CONTROL/LIGHT/START') < current_hour < config.get_config('CONTROL/LIGHT/END'):
            actions["light_control"] = ACTION_ON
        else:
            actions["light_control"] = ACTION_OFF

        # temperature
        if temperature <= config.get_config('CONTROL/TEMPERATURE/MIN'):
            actions["heating_control"] = ACTION_ON
        else:
            actions["heating_control"] = ACTION_OFF

        # humidity
        actions["humidity_control"] = ACTION_OFF
        if humidity <= config.get_config('CONTROL/HUMIDITY/MIN') and \
                config.get_config('CONTROL/PUMP/START') < current_hour < config.get_config('CONTROL/PUMP/END'):
            # run pumps only in defined hours for security reasons.
            actions["humidity_control"] = ACTION_ON
            actions["window_control"] = ACTION_CLOSED
            window_servo.close_window()
        elif humidity >= config.get_config('CONTROL/HUMIDITY/MAX'):
            actions["window_control"] = ACTION_OPEN
        else:
            actions["window_control"] = ACTION_OFF

        # moisture
        if float(moisture) >= float(config.get_config('CONTROL/MOISTURE/THRESHOLD')):
            actions["watering_control"] = ACTION_ON
            actions["humidity_control"] = ACTION_ON
        else:
            actions["watering_control"] = ACTION_OFF

        # watering time
        watering_start_hour, watering_start_minute = config.get_config('CONTROL/WATERING_TIME/START').split(':')
        watering_end_hour, watering_end_minute = config.get_config('CONTROL/WATERING_TIME/END').split(':')
        watering_start = now.replace(hour=int(watering_start_hour), minute=int(watering_start_minute))
        watering_end = now.replace(hour=int(watering_end_hour), minute=int(watering_end_minute))

        if watering_start < now < watering_end:
            actions["watering_control"] = ACTION_ON
            actions["humidity_control"] = ACTION_ON

        # get app actions
        actions["heating_app"], actions["heating_override"] = get_app_action("override_heating")
        actions["light_app"], actions["light_override"] = get_app_action("override_light")
        actions["humidity_app"], actions["humidity_override"] = get_app_action("override_humidity")
        actions["watering_app"], actions["watering_override"] = get_app_action("override_watering")
        actions["window_app"], actions["window_override"] = get_app_action("override_window")

        # light
        if should_be_active(actions, "light"):
            logger.info("Light On")
            light.turn_on()
            light_state = "On"
        else:
            logger.info("Light Off")
            light.turn_off()
            light_state = "Off"

        # heater
        if should_be_active(actions, "heating"):
            logger.info("Heating On")
            heater.turn_on()
            heater_state = "On"
        else:
            logger.info("Heating Off")
            heater.turn_off()
            heater_state = "Off"

        # window
        if should_be_active(actions, "window"):
            logger.info("Window Open")
            window_servo.open_window()
            window_state = "Open"
        else:
            logger.info("Window Closed")
            window_servo.close_window()
            window_state = "Off"

        # humidity
        if should_be_active(actions, "humidity"):
            logger.info("Humidity On")
            humidity_pump.run(15)

        # watering
        if should_be_active(actions, "watering"):
            logger.info("Watering On")
            watering_pump.run(15)

        # get app actions
        firebase.add_document("actions", actions)

        classify_result = sprout_detect.detect(picture.file_path)

        # Update Database
        # Environment dict
        environment = {
            "humidity": str(humidity),
            "temperature": str(temperature),
            "moisture": str(moisture),
            "light_state": str(light_state),
            "heating_state": str(heater_state),
            "window_state": str(window_state),
            "image_path": str(picture.get_blob_name()),
            "classify_result": str(classify_result),
            "timestamp": now
        }
        firebase.add_document("environment", environment)
        firebase.upload_file(picture.get_blob_name(), picture.get_file_path())

    except Exception as e:
        logger.error(str(e))


def get_app_action(document_name):
    doc = firebase.get_document("override", document_name)
    counter = doc['counter']
    if counter > 0:
        doc["counter"] = counter - 1
        result = doc['status']
        override = True
    else:
        result = ACTION_OFF
        override = False

    firebase.update_document("override", document_name, doc)
    return result, override


def should_be_active(actions, keyword):
    if actions[keyword + "_override"]:
        return True if actions[keyword + "_app"] > 0 else False
    else:
        return True if actions[keyword + "_control"] > 0 else False

