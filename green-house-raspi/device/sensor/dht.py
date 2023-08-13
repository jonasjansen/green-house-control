import statistics
from time import sleep

import adafruit_dht

from config_provider import config
from logger import logger


class DHT:

    def __init__(self):
        self.gpio = config.get_config('GPIO/DHT/DATA_PIN')
        self.humidity = 70
        self.temperature = 0
        self.dhtDevice = adafruit_dht.DHT22(self.gpio)

    def read_values(self):
        try:
            # The DHT sensor returns often None values. This loop is done for managing 10 retries
            for counter in range(20):
                humidity_vals = []
                temperature_vals = []
                # get 10 values and calculate median. Lowers the chances of wrong data.
                for i in range(3):
                    try:
                        humidity = self.dhtDevice.humidity
                        temperature = self.dhtDevice.temperature
                        humidity_vals.append(humidity)
                        temperature_vals.append(temperature)

                        sleep(0.1)
                    except Exception as error:
                        # Errors happen fairly often, DHT's are hard to read, just keep going
                        logger.debug(str(error))
                        sleep(0.1)
                        continue

                median_temperature = int(statistics.median(temperature_vals))
                median_humidity = int(statistics.median(humidity_vals))
                if median_temperature and median_humidity:
                    self.temperature = median_temperature
                    self.humidity = median_humidity
                    self.dhtDevice.exit()
                    return

        except Exception as e:
            self.dhtDevice.exit()
            logger.error(str(e))

        # Return default values
        self.temperature = 0
        self.humidity = 70

    def get_temperature(self):
        self.read_values()
        return self.temperature

    def get_humidity(self):
        self.read_values()
        return self.humidity

    def get_values(self):
        self.read_values()
        return self.humidity, self.temperature


dht = DHT()
