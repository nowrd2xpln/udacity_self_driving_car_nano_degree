#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image and print some stats
image = mpimg.imread('test.jpg')
print('This image is: ',type(image), 'with dimensions:', image.shape)

# Pull out the x and y sizes and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)

# Define a triangle region of interest
# Keep in mind the origin (x=0, y=0) is in the upper left in image processing
# Note: if you run this code, you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz
left_bottom = [0,539]
right_bottom = [900, 300]
apex = [400, 0]

# Fit lines (y=Ax+B) to identify the 3 sided region of interest
# np.polyfit() returns the coefficients [A, B] of the Fit
fit_left   = np.polyfit((left_bottom[0],  apex[0]), (left_bottom[1],  apex[1]), 1)
fit_right  = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0],  right_bottom[0]), (left_bottom[1],  right_bottom[1]), 1)

# Find the region inside the lines
# meshgrid returns coordinate matrices from coordinate vectors
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
print('XX is: ', type(XX))
print(XX)
print('YY is: ', type(YY))
print(YY)

region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
print('region_thresholds is: ', type(region_thresholds))
print('dimensions: ', region_thresholds.ndim)
print('shape: ', region_thresholds.shape)
print(region_thresholds)
region_select[region_thresholds] = [255,0,0]

# Display the image
plt.imshow(region_select)
plt.show()

# uncomment if plot does not display
# plt.show()

# Save processed image
mpimg.imsave("test-l2.8.png", region_select)
