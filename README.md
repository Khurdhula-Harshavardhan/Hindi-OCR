# Release Notes
## Convolutional Neural Network (CNN) Model - Version 1.0.0-beta
**Description:**

This release introduces my initial Convolutional Neural Network (CNN) model tailored for Hindi OCR. With simple-yet-accurate architecture aiming to be a mobile model, the model is designed to capture spatial hierarchies and is highly efficient for image data.

Key Features:

- Tailored for Hindi character recognition.
- Utilizes multiple convolutional and pooling layers.
- Improved accuracy on validation dataset.
- Changes from Previous Version:

**Initial release.**
Model Performance Metrics:
**Training accuracy: 94% | Accuracy on unseen samples: 97%**

**Dependencies:**

              -  _Tensorflow_
                      - Version: 2.14.0
                      - Summary: TensorFlow is an open source machine learning framework for everyone.
                      - Home-page: https://www.tensorflow.org/
                      - Author: Google Inc.
                      - Author-email: packages@tensorflow.org
                      - License: Apache 2.0
                      - Location: C:\Users\Sanju\AppData\Local\Programs\Python\Python311\Lib\site-packages
                      - Requires: tensorflow-intel

            - _Keras_
                  - Name: keras
                  - Version: 2.14.0
                  - Summary: Deep learning for humans.
                  - Home-page: https://keras.io/
                  - Author: Keras team
                  - Author-email: keras-users@googlegroups.com
                  - License: Apache 2.0
                  - Location: C:\Users\Sanju\AppData\Local\Programs\Python\Python311\Lib\site-packages
                  - Required-by: tensorflow-intel


 **Model Architecture:**
![CNN](https://github.com/Khurdhula-Harshavardhan/Hindi-OCR/assets/60458750/69ea72dd-e863-45b4-b34b-d4110f938c0d)


## Recurrent Neural Network (RNN) Model - Version 1.0.0-beta
**Description:**

Presenting a Recurrent Neural Network (RNN) model for Hindi OCR. Crafted for sequences, this model excels in recognizing patterns over time and space.

**Key Features**

  - Adapted for Hindi character sequences.
  - Incorporates SimpleRNN layers to process sequences.
  - Enhanced performance metrics on the validation set.
  - Changes from Previous Version:

**Initial release.**
Model Performance Metrics:
**Training accuracy: 88% | Accuracy on unseen samples: 90%**


 **Model Architecture:**
![RNN](https://github.com/Khurdhula-Harshavardhan/Hindi-OCR/assets/60458750/74419cc2-5964-419b-b0ee-f6fbbe932a47)

## Next Up: v0.2-beta

The next milestone is to create an API that can use these models, and make it simple for method calling and classification.


@Khurdhula-Harshavardhan 

