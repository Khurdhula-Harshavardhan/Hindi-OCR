"""
Module Description: This module serves an API, for using CNN and a RNN.
"""
from joblib import load
import base64
import numpy as np
from PIL import Image
from io import BytesIO
import json

class Image_Processor():
    """
    This Module acts as a middleware between the api and the model.
    Specifically the models should use this class to read image information,
    Get binary image data which is needed for their processing.

    Attributes:

        raw_image_data (base64): Has encoded image information.
        image_data (bytes): Stores decoded bytes.
        image (np.array): Stores the image in np array form.
    """
    raw_image_data = None
    image_data = None
    image = None

    def read_image(self, image_data: bytes) -> float:
        """
        Image_Processor.read_image(): takes in the encoded image data and then converts into an numpy array for further processing of the image.
        """
        try:
            self.raw_image_data = image_data
            self.image_data = base64.b64decode(self.raw_image_data)
            self.image = Image.open(BytesIO(image_data))
            self.image = np.array(self.image)

            return self.image
        except Exception as e:
            return {"Result": "Failed",
                    "ERROR": str(e),
                    "ERR at": "hindi_ocr.Image_Processor.read_image"}

class CNN(Image_Processor):
    """
    The CNN class is the API for the previously trained model. Which uses CNN.joblib that was trained previously by @Harsha Vardhan Khurdula.
    """
    cnn = None
    base_image_data = None

    def __init__(self) -> None:
        """
        The constructor should initialize the model.
        """
        try:
            self.cnn = load("Models/CNN.joblib")

            if self.cnn is None:
                raise FileNotFoundError("Cannot load pretrained CNN, please check /Models/ to verify if the model does exist.")
            else:
                print("[SUCCESS] The pretrained CNN model has been loaded successfully.")
        except FileNotFoundError as e:
            print("[ERROR] The following error occured while trying to load the model: "+str(e))

    def extract_character(self, image: bytes) -> dict:
        """
        Extract character is a CNN method that should accept bytes image data and then makes prediction for it. 
        """
        try:
            pass
        except Exception as e:
            pass
obj = CNN()

