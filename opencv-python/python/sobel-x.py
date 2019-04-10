# filename: sobel-x.py
# ref: https://docs.opencv.org/3.4.3/d2/d2c/tutorial_sobel_derivatives.html

import cv2
import matplotlib
matplotlib.use ('TkAgg') # my linux machine requires this, but your may not!
import matplotlib.pyplot as plt 
import imageio
import skimage 
import numpy as np 

def imshow (gray, title=None):
    plt.imshow (gray, cmap='gray')
    if title == None: title='imshow'
    plt.title(title)
    plt.pause(5); plt.close() 
#

src = imageio.imread ('data/imgKorea012.png')
gray = skimage.color.rgb2gray(src)
gray = skimage.filters.gaussian (gray/255., sigma=1) 

grad_x = skimage.filters.sobel_v(gray)  # vertical edge comes from x-gradient
grad_y = skimage.filters.sobel_h(gray)  # horizontal edge from y-grad
sobel = skimage.filters.sobel(gray)     # sobel-magnitude

mag = np.sqrt( grad_x**2 + grad_y**2 ) / np.sqrt(2.)

imshow (gray, 'gray scale input')
imshow (np.abs(grad_x), 'sobel x')
imshow (np.abs(grad_y), 'sobel y')
imshow (mag, 'sobel maginitude')
imshow (sobel, 'skimage.filters.sobel() returns sobel-mag')

# EOF
