#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2  #bringing in OpenCV libraries

# Read in the image
image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)
plt.show()
