#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('test.jpg')

print('This image is: ',type(image), 'with dimensions:', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

red_threshhold = 0
green_threshold = 0
blue_threshold = 0
rgb_threshold = [red_threshhold, green_threshold, blue_threshold]

# Identify pixels below the threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] <rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])

# Display the image
plt.imshow(color_select)
plt.show()
