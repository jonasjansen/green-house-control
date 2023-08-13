# Logger - Entry point for logging information to file and into database.

from datetime import datetime
from pathlib import Path

from config_provider import config


class Logger:

    def __init__(self):
        self.now = datetime.now()

    def set_log_level(self):
        pass

    def log(self, message):
        self.now = datetime.now()
        message = ':'.join((self.now.strftime("%Y-%m-%d %H:%M:%S"), message))
        self.write_to_console(message)
        self.write_to_file(message)

    def write_to_console(self, message):
        print(message)

    def write_to_file(self, message):
        file_name = self.get_file_name()
        with open(file_name, 'a') as fd:
            fd.write(f'\n{message}')

    def get_file_name(self):
        folder_name = '/'.join((config.get_config('DATA/PATH/LOG'), self.now.strftime("%Y-%m-%d")))
        file_name = '-'.join((self.now.strftime("%Y-%m-%d"), 'green-house-control.log'))

        # create folder if it does not exist
        Path(folder_name).mkdir(parents=True, exist_ok=True)

        return '/'.join((folder_name, file_name))

    def debug(self, message):
        self.log(''.join(("DEBUG: ", message)))

    def info(self, message):
        self.log(''.join(("INFO: ", message)))

    def warning(self, message):
        self.log(''.join(("DEBUG: ", message)))

    def error(self, message):
        self.log(''.join(("INFO: ", message)))


logger = Logger()
