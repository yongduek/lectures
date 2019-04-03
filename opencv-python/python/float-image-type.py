# filename: float-image-type.py

# image pixel data is represented normally by uint8
# but float32 is also a popular representation.
# Use TIF format to save a float32 RGB image
# Image Viewer for TIF float32 is ImageMagick/display

import imageio
import matplotlib.pyplot as plt 
import numpy as np 

im = imageio.imread ('data/imgKorea012.png')
plt.imshow (im)
plt.title('Original Image')
plt.pause(1); plt.close()

# convert to float type image in the rage [0, 1.]
im = np.float32(im / 255.)
print ('float32 image: ', im.dtype, im[100,100])
plt.imshow (im)
plt.title ('float32 type image can also be displayed by plt.')
plt.pause(1); plt.close()

# automatic conversion to uint8 is provided.
png_filename = 'data/imgKorea012-float32.png'
imageio.imwrite(png_filename, im)
im2 = imageio.imread(png_filename)
print ('png file reloaded: ', im2.dtype, im2[100,100])

#
tif_filename = 'data/imgKorea012-float32.tif'
imageio.imwrite (tif_filename, im)
imtif = imageio.imread(tif_filename)
print ('tif file reloaded: ', imtif.dtype, imtif[100,100])
plt.imshow (imtif)
plt.title ('TIF image format can save float32 type image.')
plt.pause(1); plt.close()

#
import cv2 
imcv = cv2.imread (tif_filename)
if imcv is None:
    print ('tif float32 cannot be loaded by cv2.imread()')
else:
    print ('tif loaded by cv2: {}'.format(imcv.shape))
#
# EOF
