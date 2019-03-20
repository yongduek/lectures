# filename: non-photorealistic.py

# https://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/
# https://docs.opencv.org/trunk/df/dac/group__photo__render.html

import sys
import numpy as np 
import cv2 
import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot as plt 
import imageio # this will be used to load an image file
import skimage # rgb <-> hsv conversion in [0,1] pixel scale

# show the image
def imshow (img, title=None):
    if img.ndim == 3: 
        plt.imshow (img)
    else:
        plt.imshow (img, cmap='gray')

    if title is None: title = 'imshow'
    plt.title (title)
    plt.pause (1)
    plt.close ()
#

src = imageio.imread ('data/petinsider.com.jpg') # it is an RGB format even though ...
if src is None:
    print ('image file open error')
    sys.exit ()
#
print (src.shape)
imshow (src, 'Source Image')


epf = cv2.edgePreservingFilter(src, flags=1, sigma_s=60, sigma_r=0.8)
imshow (epf, 'OpenCV Edge Preserving Filter')

detf = cv2.detailEnhance (src, sigma_s = 10, sigma_r=0.2)
imshow (detf, 'Detail Enhancement Filter')

pencil_g, pencil_c = cv2.pencilSketch (src, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
imshow (pencil_c, 'Pencil Sketch Color')
imshow (pencil_g, 'Pencil Sketch Gray')

styl = cv2.stylization (src, sigma_r=0.05, sigma_s=50)
imshow (styl, 'OpenCV Stylizatin')

# EOF
