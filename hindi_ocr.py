"""
Module Description: This module serves an API, for using CNN and a RNN.
"""
from joblib import load
import base64

class Image_Processor():
    pass

class CNN():
    """
    The CNN class is the API for the previously trained model. Which uses CNN.joblib that was trained previously by @Harsha Vardhan Khurdula.
    """
    cnn = None
    base_image_data = None

    def __init__(self, image: base64) -> None:
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


obj = CNN()

