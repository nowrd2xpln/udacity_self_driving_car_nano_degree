#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
image = mpimg.imread('test.jpg')

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)
line_image = np.copy(image)
base_center_pos = xsize/2
lane_width_from_center = 450
road_hoizon_level = 400

# Define color selection criteria
# MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
red_threshold = 200
green_threshold = 200
blue_threshold = 200

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Define the vertices of a triangular mask.
# Keep in mind the origin (x=0, y=0) is in the upper left
# MODIFY THESE VALUES TO ISOLATE THE REGION
# WHERE THE LANE LINES ARE IN THE IMAGE
left_bottom = [base_center_pos-lane_width_from_center, ysize-1]
right_bottom = [base_center_pos+lane_width_from_center, ysize-1]
apex = [base_center_pos, road_hoizon_level]

# Perform a linear fit (y=Ax+B) to each of the three sides of the triangle
# np.polyfit returns the coefficients [A, B] of the fit
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Mask pixels below the threshold
color_thresholds = (image[:,:,0] < rgb_threshold[0]) | \
                    (image[:,:,1] < rgb_threshold[1]) | \
                    (image[:,:,2] < rgb_threshold[2])

# Find the region inside the lines
# Matplotlib has rescaled the 8 bit data from each channel to floating point
# data between 0.0 and 1.0.
# https://matplotlib.org/1.5.3/Matplotlib.pdf
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
print('fit_left: ', type(fit_left), '\n', fit_left)
print('XX*fit_left[0]: ', type(fit_left[0]), '\n', fit_left[0])
print('XX*fit_left[0]+fit_left[1]: ', type(fit_left[1]), '\n', fit_left[1])
print('XX: ', type(XX), '\n', XX)
print('XX*fit_left[0]: ', type(XX), '\n', XX*fit_left[0])
print('XX*fit_left[0]+fit_left[1]: ', type(XX), '\n', XX*fit_left[0]+fit_left[1])
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

# Mask color and region selection
color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]
print('color_select: ', type(color_select), '\n', color_select)
plt.imshow(color_select)
plt.show()
print('color_thresholds: ', type(color_thresholds), '\n', color_thresholds)
plt.imshow(color_thresholds)
plt.show()
print('region_thresholds: ', type(region_thresholds), '\n', region_thresholds)
plt.imshow(region_thresholds)
plt.show()
print('~region_thresholds: ', type(~region_thresholds), '\n', ~region_thresholds)
plt.imshow(~region_thresholds)
plt.show()
# Color pixels red where both color and region selections met
line_image[~color_thresholds & region_thresholds] = [255, 0, 0]

# Display the image and show region and color selections
plt.imshow(image)
x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw=2)
plt.imshow(color_select)
plt.imshow(line_image)
plt.show()
mpimg.imsave("test-l2.8-after.png", color_select)
