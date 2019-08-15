# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import cv2

image = cv2.imread('plane.jpg')
orig = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (32, 32))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network
model = load_model('model_saved.model')

# classify the input image
result = model.predict_classes(image)
print("result ",result)
#1= plane ,0 = bird
if result[[0]]==1:
	print("airplane")
else:
	print("bird")
