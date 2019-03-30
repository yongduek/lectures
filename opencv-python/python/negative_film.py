# filename negative_film.py

import sys
import numpy as np 
import cv2 
import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot as plt 
import imageio # this will be used to load an image file

# show the image
def imshow (img, title=None):
    plt.imshow (img)
    if title is None: title = 'imshow'
    plt.title (title)
    plt.pause (1)
    plt.close ()
#

def negative_film (img):
#    return 255 - img  # simple way using numpy.
    neg = np.zeros_like (img)
    for r in range (img.shape[0]):
        for c in range (img.shape[1]):
            for d in range (img.shape[2]):
                neg[r,c,d] = 255 - img[r,c,d]
    return neg
#

img = imageio.imread ('data/torres-del-paine.jpg')

imshow (img, 'source image')

neg = negative_film (img)

imshow (neg, 'negative film')

# EOF 