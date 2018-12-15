# IGCG: Image Generation, Processing, Computer Vision, Pattern Recognition, Machine Learning, Data Science, Python 3, etc

Main issue is to play with computers using the Python language to communicate with the computers.

The computer will be asked to do some works related to images mainly.

It will cover any topics related to the achievement of the main goal of displaying an image in the screen.



## Pixel based Operation
1. histogram concept and plot
1. color quantization: c = c / div + div/2
1. color channel exchange
1. negative film effect: c = 255 - c
1. color conversion: RGB, HSV, Gray scale
1. Thresholding (binarization)
1. Intensity slicing: g = 255 if t1 < I < t2
1. gamma correction: g = I^{1/\gamma}
1. histogram expansion for contrast enhancement
1. histogram equalization (use direct CDF mapping): I = cdf (I), I \in [0,1]


## Window based Operation
1. Erosion
1. Dilation
1. smoothing  (convolution)
1. image gradient
1. image enhancement by LoG (Laplacian of Gaussian)

## References

1. [opencv python tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html)
