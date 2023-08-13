import requests

from config_provider import config


class Zigbee:
    api_url = ""
    api_key = ""

    def __init__(self):
        self.api_url = config.get_config('ZIGBEE/API_IP')
        self.api_key = config.get_config('ZIGBEE/API_KEY')

    def get_api_url(self):
        return ''.join(('http://', self.api_url, '/api/', self.api_key, '/lights/'))

    def get_state(self, device_id):
        result = ''
        try:
            request_url = ''.join((self.get_api_url(), str(device_id)))
            result = requests.get(request_url)
        except Exception as e:
            print("Could not get State from zigbee device", device_id, ":", e)
        return result

    def set_state(self, device_id, payload):
        result = ''
        try:
            request_url = ''.join((self.get_api_url(), str(device_id), '/state/'))
            result = requests.put(request_url, data=payload)
        except Exception as e:
            print("Could not set State to zigbee device", device_id, ":", e)
        return result


zigbee = Zigbee()
