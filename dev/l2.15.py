#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image
image = mpimg.imread('exit-ramp.jpg')

#plt.imshow(image)
#plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
#plt.imshow(gray, cmap='gray')
#plt.show()

# Define a kernel size for Gaussian smoothing / blurring
# Note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
# You can choose the kernel_size for Gaussian smoothing to be any odd number
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)
#plt.imshow(blur_gray)
#plt.show()

# Define parameters for Canny and run it
# NOTE: if you try running this code you might want to change these!
low_threshold = 50
high_threshold = 150
masked_edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
# rho takes a minimum value of 1
# a reasonable starting place for theta is 1 degree (pi/180 in radians)
# Scale these values up to be more flexible in your definition of what constitutes a line.
# threshold parameter specifies the minimum number of votes (intersections in a
# given grid cell) a candidate line needs to have to make it into the output.
# min_line_length is the minimum length of a line (in pixels) that you will accept in the output
# max_line_gap is the maximum distance (again, in pixels) between segments that
# you will allow to be connected into a single line.
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image)*0 #creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), \
                        min_line_length, max_line_gap)
print('lines: ', type(lines), '\n', lines)

# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
print('lines: ', type(lines), '\n', lines)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((masked_edges, masked_edges, masked_edges))
plt.imshow(color_edges)
plt.show()

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
plt.imshow(combo)
plt.show()
