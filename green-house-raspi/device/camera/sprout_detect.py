import time
from datetime import datetime
from pathlib import Path

from picamera2 import Picamera2

from config_provider import config
import numpy as np
import cv2
import tensorflow as tf

CLASS_SEED = 'seed'
CLASS_SPROUT = 'sprout'
CLASS_NOTHING = 'nothing'


class SproutDetect:

    def __init__(self):
        self.model = tf.keras.models.load_model(config.get_config('DATA/PATH/MODEL'))
        self.image = None

    def load_image(self, image_path):
        # preprocess image
        image_raw = cv2.imread(image_path, 3)
        resized_image = cv2.resize(image_raw, (180, 180))
        self.image = np.expand_dims(resized_image, axis=0)

    def detect(self, image_path):
        self.load_image(image_path)
        result = self.model.predict(self.image)

        # convert result
        predict_seed = result[0][0]
        predict_sprout = result[0][1]
        if predict_seed > 1 and predict_seed > predict_sprout:
            return CLASS_SEED
        elif predict_sprout > 1 and predict_sprout > predict_seed:
            return CLASS_SPROUT
        else:
            return CLASS_NOTHING


sprout_detect = SproutDetect()
