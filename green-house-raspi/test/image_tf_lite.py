"""Main script to run the object detection routine."""
import sys

import tflite_runtime.interpreter as tflite
import numpy as np
import cv2
from tflite_runtime.interpreter import Interpreter
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
from tflite_support.metadata_writers import object_detector
from tflite_support.metadata_writers import writer_utils
from tflite_support import metadata

#MODEL_NO_META = '/home/pi/green-house-control/test/saved_model_with_meta.tflite'
MODEL = '/home/pi/green-house-control/test/saved_model.tflite'
# seed 0.844312310218811
#IMAGE = '/home/pi/green-house-control/test/img_sprout.jpg'
#IMAGE = '/home/pi/green-house-control/data/picture/2023-04-27/2023-04-27__15-31-03__picture.jpg'
# seed 0.8449552059173584
IMAGE = '/home/pi/green-house-control/test/img_seed.jpg'


def load_image():
    image_raw = cv2.imread(IMAGE, 3)
    resized_image = cv2.resize(image_raw, (180, 180))
    image = np.expand_dims(resized_image, axis=0)
    #tensor_image = vision.TensorImage.create_from_array(image)
    # result = new_model.predict(image)
    # resized_image = cv2.resize(img, (180, 180))
    # rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # rgb_image = resized_image
    # tensor_image = vision.TensorImage.create_from_array(rgb_image)
    return image

def classify(image):
    interpreter = Interpreter(MODEL)
    interpreter.allocate_tensors()
    interpreter.set_tensor(0, image)
    interpreter.invoke()



    test = 1

def detect():
    try:


        # Initialize the image classification model
        base_options = core.BaseOptions(
            file_name=MODEL,
            use_coral=False,
            num_threads=1
        )

        # Enable Coral by this setting
        classification_options = processor.ClassificationOptions(
            max_results=5,
            score_threshold=0.5
        )
        options = vision.ImageClassifierOptions(
            base_options=base_options,
            classification_options=classification_options
        )
        classifier = vision.ImageClassifier.create_from_options(options)

        image = load_image()
        classify(image)

        categories, final_prediction = classifier.classify(image)

        # Show classification results on the image
        for idx, category in enumerate(categories):
            class_name = category.label
            score = round(category.score, 2)
            result_text = class_name + ' (' + str(score) + ')'
            print("Prediction: {}, Probability: {}".format(class_name, str(score)))

        print("Final prediction: ", final_prediction)

        '''
        # List classification results
        categories = classifier.classify(tensor_image)

        for classification in categories.classifications:
            for category in classification.categories:
                result_class = category.category_name
                result_score = category.score

                print("Result:", result_class)
                print("Score:", result_score)
        '''

    except Exception as e:
        print("Error")
        print(e)


if __name__ == '__main__':
    detect()
