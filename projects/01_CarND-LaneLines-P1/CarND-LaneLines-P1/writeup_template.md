# **Finding Lane Lines on the Road** 
[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"
[image2]: ./test_images_output/figure_1.png "Grayscale"
### Overview

In this project, we learn to apply basic computer vison techniques to find lane markings on the road. This consists of the following steps:

1. Convert to grayscale
2. Apply Gaussian smoothing
3. Use Canny Edge Detection
4. Mask region of interest
5. Apply Hough Transformation
6. Draw Lane Lines

These steps are implemented in a pipeline, tested on several images, and tuned until properly fitted on the lane lines. Once this initial goal was accomplished, the pipeline needed to be tested against videos which is essentially applying it to a stream of images. 

### Pipeline
In my pipeline, I go through several phases in order to identify and track lane lines.
[image2]
#### Convert to Grayscale
The first phase of processing an image was converting to gray scale to prepare the image for Canny algorithm to detect edges. This conversion will help discriminate between color changes between the color of the lane lines and road. In addition, it also has the benefit of reducing noise further.
#### Apply Gaussian smoothing
The second phase of image processing applies Gaussian smoothing (blurring). It is also used to prepare the image for Canny Edge Detection. This technique will essentialy smoothen edges of an image to further reduce noise in the image. This step reduces the number of lines detected to aid the the next phase in detecting significant lines.
#### Use Canny Edge Detection
The third phase uses Canny Edge Detection to finds edges. This technique finds strong edges/gradient pixels above a high threshold and rejects if pixels if they are below a low_threshold and intermediate pixels are included only if they are connected to strong edges.
#### Mask region of interest
The fourth phase simply applies a mask that isolate the pixels of interest.
#### Apply Hough Transformation
In the final stage of the pipeline, a Hough Transform is applied to the image that results in extracted lines detected in the masked region from the previous step.
#### Draw Lane Lines
As part of the last stage, the lanes are drawn on to the image. In order to draw the lines, they need to be sorted in to left/right lane lines, averaged, extrapolated, and finally drawn on to the image.



---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I .... 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
