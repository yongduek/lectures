# filename: numpy-hist.py

import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2

imagefile = 'data/torres-del-paine.jpg'

frame = cv2.imread(imagefile)

bluehist = np.zeros((256), dtype=np.float)
redhist = np.zeros((256), dtype=np.float)
greenhist = np.zeros((256), dtype=np.float)

# make histograms, one for each color
for r in range(frame.shape[0]):
    for c in range(frame.shape[1]):
        blue_intensity = frame[r,c][0]
        bluehist[blue_intensity] += 1
        redhist[frame[r,c,2]] += 1
        greenhist[frame[r,c][1]] += 1
#

# convert to ratio = count / num_pixels
num_pixels = frame.shape[0] * frame.shape[1]
bluehist /= num_pixels
greenhist /= num_pixels
redhist /= num_pixels

fig, ax = plt.subplots(2,1)
ax[0].imshow (frame)
ax[0].set(xticks=[], yticks=[])
ax[0].set_title ('Input Image')
x = range(0,256,1)
ax[1].plot (x, bluehist, 'b', x, redhist, 'r', x, greenhist, 'g')
ax[1].grid(True)
ax[1].set_title ('Histograms for R,G,B, respectively')
plt.show()
#EOF
