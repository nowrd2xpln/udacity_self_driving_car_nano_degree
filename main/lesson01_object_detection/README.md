# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Concepts
Lesson4: Computer Vison Fundamentals
1. Power of Cameras
2. Setting up the Problem
3. Color Selection
4. Color Selection Code Example
5. Quiz: Color Selection
6. Region Masking
7. Color and Region Combined
8. Quiz: Color Region
9. Finding Lines of Any Colors
10. What is Computer Vision?
11. Canny Edge Detection
12. Canny to Detect Lane Lines
13. Quiz: Canny Edges
14. Hough Transform
15. Hough Transform to Find Lane Lines
16. Quiz: Hough Transform
17. Parameter Tuning

Self-Driving Car Engineer Preview 2.0
Lesson 4: Object Detection
1. Intro to Vehicle Tracking
2. Arpan and Drew
3. Finding Cars
4. Object Detection Overview
5. Manual Vehicle Detection
6. Features
7. Feature Intuition
8. Color Features
9. Template Matching
10. Template Matching Quiz
11. Color Histogram Features
12. Histograms of Color
13. Histogram Comparison
14. Color Spaces
15. Explore Color Spaces
16. Spatial Binning of Color
17. Gradient Features
18. HOG Features
19. Data Exploration
20. scikit-image HOG
21. Combining Features
22. Combine and Normalize Features
23. Build a Classifier
24. Labeled Data
25. Data Preparation

Lesson 6: Camera Calibration
1. The Challenges with Cameras
2. Welcome to Computer Vision
3. Overview
4. Getting Started
5. Distortion Correction
6. Quiz: Effects of Distortion
7. Pinhole Camera Model
8. Quiz: Image Formation
9. Measuring Distortion
10. Finding Corners
11. Calibrating Your Camera
12. Correcting for Distortion
13. Lane Curvature
14. Perspective Transform
15. Quiz: Curvature and Perspective
16. Transform a Stop Sign
17. Intuitions
Camera Calibration - To compute the transformation between 3D object points in the world and 2D image points.
Distortion Correction - To ensure that the geometrical shape of objects is represented consistently, no matter where they appear in an image.
Perspective Transform - To transform an image such that we are effectively viewing objects from a different angle or direction.
18. Undistort and Transform
19. How I Did It
20. Coming Up

Need balanced data set or run the risk of classifier trying to predict everything belonging to the majority class.

Need a training set for training and check on unseen examples with test set.

Shuffle data set randomly to avoid any ordering effects.

Always testing your classifier on a separate dataset will prevent against overfitting and provide a more realistic estimate of accuracy and error.

Normalizing ensures that your classifier's behavior isn't dominated by just a subset of the features, and that the training process is as efficient as possible.

To avoid having your algorithm sumply classify everything as belonging to the majority class, prepare a balanced dataset, i.e., have as many positive as negative examples, or in the case of multi-class problems, roughly the same number of cases of each class.

To avoid problems due to ordering of the data, randomly shuffle the data.

To estimate generalization of the model to new data, split the data into a training and testing set.

To avoid individual features of sets of features dominating the response of your classifier, normalize the features to zero mean and unit variance.
26. Train a Classifier
Training phase:
Extract features from training set and supplying feature vectors to the training algorithm.
The training algorithm initializes a model, and tweaks it's parameters using the feature vectors and labels.

27. Parameter Tuning
Support Vector Machine vehicle detection model tuning involves searching fro a kernel, a gamma value and a C value that minimize predicition error.
Scikit-learn includes two algorithms for auto parameter search, GridSearchCV and RandomizedSearchCV. GridSearchCV works through multiple parameter combinations and cross-validating as it goes. RandomizedSearchCV is similar except it takes a random sample of parameter combinations and is faster.
GridSearchCV uses 3-fold cross validation to determine the best performing parameter set. It uses accuracy as an error metric by averaging the accuracy for each partition. For every possible parameter combination, GridSearchCV calculates an accuracy score.

Four lines of code for a fitted classifier:
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)
Create parameter.
Create the SVC (support vector classifier) SVM (support vector machine)
Create the classifier.
Try all parameter combinations and return fitted classifier.

The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a "best fit" hyperplane that divides, or categorizes, your data.

28. Color Classify
*** Revisit
Using spatial binning of: 32 and 32 histogram bins
Feature vector length: 3168
2.1 Seconds to train SVC...
Test Accuracy of SVC =  0.9833
My SVC predicts:  [1. 1. 1. 0. 0. 0. 0. 0. 0. 1.]
For these 10 labels:  [1. 1. 1. 0. 0. 0. 0. 0. 0. 1.]
0.0007 Seconds to predict 10 labels with SVC
Using spatial binning of: 16 and 32 histogram bins
Feature vector length: 864
0.4 Seconds to train SVC...
Test Accuracy of SVC =  0.9875
My SVC predicts:  [0. 0. 1. 0. 0. 0. 1. 0. 0. 0.]
For these 10 labels:  [0. 0. 1. 0. 0. 0. 1. 0. 0. 1.]
0.00069 Seconds to predict 10 labels with SVC
Using spatial binning of: 8 and 32 histogram bins
Feature vector length: 288
0.1 Seconds to train SVC...
Test Accuracy of SVC =  0.9896
My SVC predicts:  [0. 0. 1. 0. 1. 0. 1. 0. 0. 1.]
For these 10 labels:  [0. 0. 1. 0. 1. 0. 1. 0. 0. 1.]
0.00068 Seconds to predict 10 labels with SVC

Using spatial binning of: 32 and 16 histogram bins
Feature vector length: 3120
2.64 Seconds to train SVC...
Test Accuracy of SVC =  0.9708
My SVC predicts:  [1. 1. 0. 1. 1. 1. 1. 0. 1. 1.]
For these 10 labels:  [1. 1. 0. 1. 1. 1. 1. 0. 1. 1.]
0.0007 Seconds to predict 10 labels with SVC
Using spatial binning of: 16 and 16 histogram bins
Feature vector length: 816
0.66 Seconds to train SVC...
Test Accuracy of SVC =  0.9812
My SVC predicts:  [1. 1. 0. 1. 0. 1. 1. 0. 1. 1.]
For these 10 labels:  [1. 1. 0. 1. 0. 1. 1. 0. 1. 1.]
0.00117 Seconds to predict 10 labels with SVC
Using spatial binning of: 8 and 16 histogram bins
Feature vector length: 240
0.13 Seconds to train SVC...
Test Accuracy of SVC =  0.9708
My SVC predicts:  [0. 1. 1. 1. 0. 0. 1. 0. 1. 1.]
For these 10 labels:  [0. 1. 1. 1. 0. 1. 1. 0. 1. 1.]
0.00069 Seconds to predict 10 labels with SVC

Using spatial binning of: 32 and 8 histogram bins
Feature vector length: 3096
2.91 Seconds to train SVC...
Test Accuracy of SVC =  0.9562
My SVC predicts:  [1. 0. 1. 0. 1. 0. 0. 1. 1. 0.]
For these 10 labels:  [1. 0. 1. 0. 1. 0. 0. 1. 1. 0.]
0.0007 Seconds to predict 10 labels with SVC
Using spatial binning of: 16 and 8 histogram bins
Feature vector length: 792
0.49 Seconds to train SVC...
Test Accuracy of SVC =  0.9582
My SVC predicts:  [0. 1. 1. 0. 1. 0. 0. 1. 1. 1.]
For these 10 labels:  [0. 1. 0. 0. 1. 0. 0. 1. 1. 1.]
0.00067 Seconds to predict 10 labels with SVC
Using spatial binning of: 8 and 8 histogram bins
Feature vector length: 216
0.15 Seconds to train SVC...
Test Accuracy of SVC =  0.9582
My SVC predicts:  [0. 0. 1. 1. 0. 1. 1. 1. 0. 1.]
For these 10 labels:  [0. 0. 1. 1. 0. 1. 1. 1. 0. 1.]
0.00064 Seconds to predict 10 labels with SVC

29. HOG Classify
*** Revisit
30. Sliding Windows
31. How many windows?
32. Sliding Window Implementation
33. Multi-scale Windows
34. Search and Classify
35. Hog Sub-sampling Window Search
36. False Positives
37. Multiple Detections & False Positives
38. Tracking Pipeline
39. Summary
40. Traditional vs. Deep Learning Ap

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
