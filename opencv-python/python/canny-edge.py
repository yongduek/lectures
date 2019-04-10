# canny-edge.py
# ref: http://scikit-image.org/docs/dev/auto_examples/edges/plot_canny.html#sphx-glr-auto-examples-edges-plot-canny-py

import numpy as np
import matplotlib
matplotlib.use ('TkAgg') # my linux machine requires this, but your may not!
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import imageio
import skimage
from skimage import feature


# Generate noisy image of a square
im = np.zeros((128, 128)) # black image
im[32:-32, 32:-32] = 1 # white square

im = ndi.rotate(im, 15, mode='constant') # rotate
im = ndi.gaussian_filter(im, 4)          # smoothing/blurring
im += 0.2 * np.random.random(im.shape)   # noise

# Compute the Canny filter for two values of sigma
# output: binary edge map (1: edge pixel, 0: non-edge pixel)
edges1 = feature.canny(im)               # sigma = 1, default
edges2 = feature.canny(im, sigma=3)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, 
                                    figsize=(8, 3),
                                    sharex=True, sharey=True)

ax1.imshow(im, cmap=plt.cm.gray)
ax1.axis('off'); ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off'); ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off'); ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()
plt.pause(1); plt.close()

# Apply Canny to a natural Image
im = imageio.imread('data/img536.jpg')
gray = skimage.color.rgb2gray (im)
sigma = 1.
edge = skimage.feature.canny(gray, sigma=sigma)
print ('edge: ', edge.shape)
plt.imshow (edge, cmap='gray')
plt.title ('Canny edge map, sigma={:.1f}'.format(sigma)); plt.pause(1); plt.close()

# Get edge color, just for displaying
imedge = im.copy()
for i in range(3):
    imedge[:,:,i] = im[:,:,i] * edge
print (imedge.shape) 
plt.imshow (imedge)
plt.title ('RGB * edgemap '); plt.pause(1); plt.close()

# EOF
