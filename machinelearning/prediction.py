import cv2
import tensorflow as tf
import os
import matplotlib.pyplot as plt
import numpy as np
sess = tf.compat.v1.InteractiveSession()
CATEGORIES = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','del','nothing','space']

img = cv2.imread('C:/Users/mydif/frfr/img.png')

img = np.array(img)
newimg = cv2.resize(img, (64, 64))
newestimg = newimg.reshape(-1, 64, 64, 3)
plt.imshow(newimg)

model = tf.keras.models.load_model("legitmodel.model", compile=True)

prediction = model.predict(bruh)
print(prediction)
indexes = tf.argmax(prediction, axis=1)
print(indexes.numpy())
print(CATEGORIES[int(indexes.numpy())])
