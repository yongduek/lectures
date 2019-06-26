import os
import imageio 
import matplotlib.pyplot as plt
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk

selem = disk(6)
print (type(selem), selem.dtype, selem.shape, '\n', selem)
plt.imshow (selem, cmap='gray')
plt.pause(2)

