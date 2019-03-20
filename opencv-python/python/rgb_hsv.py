# filename rgb_hsv.py
# http://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_rgb_to_hsv.html

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

rgb = imageio.imread ('data/nature.jpg') #https://wallpapercave.com/pretty-nature-wallpapers
if rgb is None:
    print ('image file open error')
    sys.exit ()
#

imshow (rgb, 'RGB Image')

# The conversion assumes an input data range of [0, 1] for all color components.

hsv = skimage.color.rgb2hsv (rgb/255.) 
hue = hsv[:,:,0]
saturation = hsv[:,:,1]
value = hsv[:,:,2]

imshow (hue, 'Hue Image')
imshow (saturation, 'Saturation Image')
imshow (value, 'Value Image (== Gray Scale)')

print ('HSV(Red) = ', skimage.color.rgb2hsv([[[1.,0,0]]]))
print ('HSV(Yellow) = ', skimage.color.rgb2hsv([[[1.,1.,0]]]))
print ('HSV(Green) = ', skimage.color.rgb2hsv([[[0,1.,0]]]))
print ('HSV(Blue) = ', skimage.color.rgb2hsv([[[0,0,1.]]]))
print ('HSV(White) = ', skimage.color.rgb2hsv([[[1.,1.,1.]]]))

hsvpixel = [[[0.999, 1., 1.]]]
print ('RGB({}) = '.format(hsvpixel), skimage.color.hsv2rgb (np.array(hsvpixel)))
# EOF