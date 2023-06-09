# CS410_FlyEM
This repository hosts the segmentation pipeline to segment fly retina images using traditional segmentation algorithms.


## Authors

* [Prof. Daniel Haehn](https://github.com/haehn)
* [Sai Harshavardhan Reddy Kona](https://github.com/kshvr16)
* [Nikhila Yadav Lankela](https://github.com/Nikhila1003)
* [Varshitha Hantur Dinakar](https://github.com/varshi-123)
* [Varuni Manjunath](https://github.com/Varunii)
* [Kiran Sandilya](https://github.com/Kiransandilya)
* [Kunal Jain](https://github.com/jainkhere)


## Package Installation

Install this python package by executing the following command.
```bash
  pip install flyem_segmentation_pipeline
```
If the above command throws any error, please run the following command and install the dependency packages individually.
```bash
pip install flyem_segmentation_pipeline --no-deps
```


## Required Python packages

* [numpy](https://pypi.org/project/numpy/)
* [mahotas](https://pypi.org/project/mahotas/)
* [matplotlib](https://pypi.org/project/matplotlib/)
* [scikit-image](https://pypi.org/project/scikit-image/)

    ## Dependency package issues
All the above-mentioned packages are required to use this package, but due to the version issues with numpy and mahotas, during installation only matplotlib and scikit-image are installed; numpy and mahotas has to be installed separately.


## Package Description
Anyone can use this package to perform various computer vision algorithms to segment the fly retina images.

The package followed MVC(Model-View-Controller) design pattern.

All the functionalities can be used by importing them using the following command.
```python
from segmentationMVC.controller import ImageController
```

## Functions

**ImageController.read():** reads an image from the given path.

**ImageController.normalize():** returns an normalized image of the input image to [0, 255].

**ImageController.center_crop():** crops an image to a default size of (512, 512).

**ImageController.smooth():** smoothens the image using Gaussian filter.

**ImageController.threshold():** applies thresholding of an input image.

**ImageController.binary_mask():** creates an binary mask of the image.

**ImageController.display():** display the image.

## Sample Usage
The below sample code reads an image from the input path. 
```python
from segmentationMVC.controller import ImageController
image_data = ImageController.read("..")
```
Output:

![input image](https://raw.githubusercontent.com/kshvr16/CS410_FlyEM_PyPi/master/docs/sample_input.png)

The below sample code normalized the input image.
```python
from segmentationMVC.controller import ImageController
normalized_data = ImageController.normalize(image_data)
```
Output:

![normalized image](https://raw.githubusercontent.com/kshvr16/CS410_FlyEM_PyPi/master/docs/sample_normalize.png)


The below sample code crops the input image.
```python
from segmentationMVC.controller import ImageController
crop_data = ImageController.normalize(normalized_data)
```
Output:

![crop image](https://raw.githubusercontent.com/kshvr16/CS410_FlyEM_PyPi/master/docs/sample_crop.png)


The below sample code smoothens the input image.
```python
from segmentationMVC.controller import ImageController
smoothed_data = ImageController.smooth(crop_data)
```
Output:

![smoothens image](https://raw.githubusercontent.com/kshvr16/CS410_FlyEM_PyPi/master/docs/sample_smoothen.png)


To get the complete segmented image, the following will serve as an example.
```python
from segmentationMVC.controller import ImageController

image_data = ImageController.read("..")

normalized_data = ImageController.normalize(image_data)

crop_data = ImageController.normalize(normalized_data)

smoothed_data = ImageController.smooth(crop_data)

threshold_data = ImageController.threshold(smoothed_data, threshold_value=73)
labeled_data, nr_count = ImageController.label(threshold_data)
selected_labeled_data = ImageController.select_regions(labeled_data, region_size=1500)
binary_mask_data = ImageController.binary_mask(selected_labeled_data)
closed_binary_mask_data = ImageController.close_binary_mask(binary_mask_data)
segmented_image = ImageController.binary_image(closed_binary_mask_data)
```
The variable **segmented_image** in the above sample code stores the result of the segmented image.


Output:

![output image](https://raw.githubusercontent.com/kshvr16/CS410_FlyEM_PyPi/master/docs/sample_output.png)
