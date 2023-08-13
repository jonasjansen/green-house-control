import time
from datetime import datetime
from pathlib import Path

from picamera2 import Picamera2

from config_provider import config


class Picture:

    def __init__(self):
        self.picam2 = Picamera2()
        self.file_path = None
        self.file_name = ""
        self.folder_name = ""
        self.blob_name = None

    def take(self):
        self.picam2.start_and_capture_file(self.get_file_path(), show_preview=False)

    def get_file_path(self):
        if not self.file_path:
            self.generate_file_path()
        return self.file_path

    def generate_file_path(self):
        now = datetime.now()
        self.folder_name = '/'.join((config.get_config('DATA/PATH/PICTURE'), now.strftime("%Y-%m-%d")))
        self.file_name = '_'.join((now.strftime("%Y-%m-%d__%H-%M-%S"), '_picture.jpg'))

        # create folder if it does not exist
        Path(self.folder_name).mkdir(parents=True, exist_ok=True)
        self.blob_name = '/'.join((now.strftime("%Y-%m-%d"), self.file_name))
        self.file_path = '/'.join((self.folder_name, self.file_name))

    def get_blob_name(self):
        if not self.blob_name:
            self.generate_file_path()
        return self.blob_name


picture = Picture()
