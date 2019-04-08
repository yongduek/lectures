# filename: filter-box-blur.py

import time
import numpy as np 
import imageio 
import skimage 
import cv2 # opencv
import matplotlib.pyplot as plt 

def imshow (im, title=None, ptime=1):
    if im.ndim == 2:
        plt.imshow (im, cmap='gray')
    elif im.ndim == 3:
        plt.imshow (im)
    else:
        print ('strage image.')
        return
    #
    if title==None: title='image'
    plt.title (title)
    plt.pause(ptime)
    plt.close()
#
def convolution (im, k):
    dst = np.zeros_like (im)
    for d in range (im.shape[2]):
        for r in range (im.shape[0] - k.shape[0] + 1):
            for c in range (im.shape[1] - k.shape[1] + 1):
                # convolution = inner product at (r,c,d), pivot is at left-top
                inner = 0.
                for ii in range (k.shape[0]):
                    for jj in range (k.shape[1]):
                        inner +=  im[r+ii, c+jj, d] * k[ii,jj]
                dst[r,c,d] = np.clip(inner+0.5, 0, 255)           # why complicated ?
    #
    return dst
#
im = imageio.imread ('data/img536.jpg')    # read an image file
im = im[:120, 0:150, :]

imshow (im, title='source image')

kernel = np.ones((5,5), np.float32) / 25.  # filter kernel

t0 = time.time()
blurred = cv2.filter2D (im, -1, kernel)    # filtering
print ('blurred: shape={}, pixel[0,0]={}'.format(blurred.shape, blurred[0,0]), ' %.2f seconds' % (time.time() - t0))
imshow (blurred, 'blurred by 5x5 box filter, cv2')
print ('Q. How can you produce a motion blurred image?')

t0 = time.time()
myblurred = convolution (im, kernel)        # filtering of my own
print ('myblurred: shape={}, pixel[0,0]={}'.format(myblurred.shape, myblurred[0,0]), ' %.2f seconds.'%(time.time() - t0))
imshow (myblurred, 'blurred by 5x5 box filter, myconvolution(), %.2f sec' % (time.time()-t0))
print ('Q. Why are the pixel colors different?')

# Gaussian Blurring

blurr_g = cv2.GaussianBlur (im, (5,5), 0) # 0 means automatic 5x5 Gaussian kernel
imshow (blurr_g, 'Gaussian blur with 5x5')


# Median blur

im2 = im.copy()
imshow (im2, 'source image')
## speckle noise (black or white)
for i in range(im.shape[0]*im.shape[1]//10): # 10 % noise
    r = np.random.randint(0, im.shape[0])
    c = np.random.randint(0, im.shape[1])
    if np.random.rand() < 0.5:
        im2[r,c] = 0 # black
    else:
        im[r,c] = 255 # white
#
imshow (im2, 'noised image', ptime=3)
##

median = cv2.medianBlur (im2, 3)
imshow (median, 'Median blur with 5x5')
print ('Q. Try various sizes and observe differences.')

# Bilateral Filtering
im = imageio.imread ('data/filter_input.jpg')
t0 = time.time()
bf_out = cv2.bilateralFilter (im, 15, 80, 80)
imshow (im, 'source image')
imshow (bf_out, 'bilateral_filter(): {:.2f} seconds'.format(time.time()-t0))
print ('Q. Try other parameters for bilateral Filter.')

# EOF
