#!/usr/bin/python

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Setting up figure
fig = plt.figure(figsize=(32,8))
FIG_ROWS = 1
FIG_COLUMNS = 3

# prepare object points
nx = 8#TODO: enter the number of inside corners in x
ny = 6#TODO: enter the number of inside corners in y

# Make a list of calibration images
fname = 'calibration_test.png'
img = cv2.imread(fname)
a = fig.add_subplot(FIG_ROWS,FIG_COLUMNS,1)
a.set_title('Original')
a.imshow(img)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
b = fig.add_subplot(FIG_ROWS,FIG_COLUMNS,2)
b.imshow(gray, cmap='gray')
b.set_title('Gray')

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

# If found, draw corners
if ret == True:
    # Draw and display the corners
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    c = fig.add_subplot(FIG_ROWS,FIG_COLUMNS,3)
    c.imshow(img)
    c.set_title('Gray Blur')
    fig.suptitle('Finding Corners')
    plt.show()
