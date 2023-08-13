from ..base import BasePump
from config_provider import config


class HumidityPump(BasePump):
    def __init__(self):
        self.device_id = config.get_config('ZIGBEE/ID/PUMP')
        self.gpio_direction = config.get_config('GPIO/PUMP_HUMIDITY/DIRECTION')
        self.gpio_step = config.get_config('GPIO/PUMP_HUMIDITY/STEP')


humidity_pump = HumidityPump()
