# filename gamma_correction.py
# https://en.wikipedia.org/wiki/Gamma_correction
# The image used from wikipedia seems to be from https://www.art.com/gallery/id--c23951/black-and-white-photography-prints.htm 

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

img = imageio.imread ('data/art.com.jpg') # it is an RGB format even though ...
if img is None:
    print ('image file open error')
    sys.exit ()
#
print (img.shape)
imshow (img, 'Source Image')

gammas = [2, 1, 1./2, 1./3, 1./4]

for gamma in gammas:
    ii = np.power(img/255., gamma)
    imshow (ii, 'gamma = {}'.format(gamma))
#

# Q. Plot histograms

# EOF
