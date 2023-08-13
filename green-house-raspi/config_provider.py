# Entrypoint for greenhouse control
import yaml
import os

CONFIG_FILE = "config.yaml"
FIREBASE_CREDENTIALS_FILE = "google_service_account.json"


class ConfigProvider:
    def __init__(self):
        self.config = dict()

    def get_config(self, path=None):
        if not self.config:
            self.load_config()
        # Get config from path. Example path 'ZIGBEE/ID/LIGHT' for dict {'ZIGBEE': {'ID': {'LIGHT':0}}} returns 0
        if path:
            sub_config = self.config
            for part in path.split('/'):
                if part in sub_config:
                    sub_config = sub_config[part]
                else:
                    print("ERROR: could not find", part, "in", sub_config, "which is in", self.config)
                    return ''
            return sub_config
        else:
            return self.config

    def load_config(self):
        # get absolute file location.
        file = '/'.join((os.path.dirname(os.path.realpath(__file__)), CONFIG_FILE))
        with open(file, "r") as f:
            self.config = yaml.safe_load(f)

    def get_firebase_credentials_file(self):
        return '/'.join((os.path.dirname(os.path.realpath(__file__)), FIREBASE_CREDENTIALS_FILE))


config = ConfigProvider()
