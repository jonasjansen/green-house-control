from config_provider import config
from ..base import BasePump


class WateringPump(BasePump):
    def __init__(self):
        self.device_id = config.get_config('ZIGBEE/ID/PUMP')
        self.gpio_direction = config.get_config('GPIO/PUMP_WATERING/DIRECTION')
        self.gpio_step = config.get_config('GPIO/PUMP_WATERING/STEP')


watering_pump = WateringPump()
