#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2  #bringing in OpenCV libraries

# Read in the image
image = mpimg.imread('exit-ramp.jpg')

plt.imshow(image)
plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
plt.imshow(gray, cmap='gray')
plt.show()
