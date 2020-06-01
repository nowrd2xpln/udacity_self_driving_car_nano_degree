#!/usr/bin/python

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('bbox-example-image.jpg')

# Define a function that takes an image, a list of bounding boxes,
# and optional color tuple and line thickness as inputs
# then draws boxes in that color on the output

def draw_boxes(img, bboxes, color=(0, 0, 255), thick=6):
    # make a copy of the image
    draw_img = np.copy(img)
    # draw each bounding box on your image copy using cv2.rectangle()
    for bbox in bboxes:
        print bbox
        cv2.rectangle(draw_img, bbox[0], bbox[1], color, thick)
        print bbox[0]
        print bbox[1]
    # return the image copy with boxes drawn
    return draw_img # Change this line to return image copy with boxes
# Add bounding boxes in this format, these are just example coordinates.
bboxes = [((250, 500), (400, 575)), ((450, 500), (550, 575)), ((590, 500), (635, 550)),
            ((825, 500), (1125, 675))]

result = draw_boxes(image, bboxes)
plt.imshow(result)
plt.show()
