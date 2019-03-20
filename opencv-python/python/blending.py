# filename blending.py

import sys
import numpy as np 
import cv2 
import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot as plt 


size = (256, 300)
# read two images

file1 = 'data/dooly.jpeg'
i1 = cv2.imread (file1)
if i1 is None:
    print ('image file read error: ', file1)
    sys.exit()

i1 = cv2.resize(i1, size)

file2 = 'data/pororo.jpeg'
i2 = cv2.imread (file2)
if i2 is None:
    print ('image file read error: ', file2)
    sys.exit()

i2 = cv2.resize (i2, size)

results = []
alphas = np.linspace(0, 1, 6)  # allocate alpha values
print ('alpha: ', alphas)
for a in alphas:
    J = a * i1 + (1. - a) * i2
    J = np.clip(J, 0, 255).astype(np.uint8)
    results.append (J)
    print (a)
    plt.imshow (J)
    plt.title ('alpha = %.2f' % a)
    plt.pause (1)
#

fig, axes = plt.subplots (2, 3)
for i, ax in enumerate(axes.ravel()):
    ax.imshow (results[i][:,:,::-1]) # BGR -> RGB
    ax.set_title ('alpha = {}'.format(alphas[i]))
#
plt.pause (2)
plt.close()

# EOF