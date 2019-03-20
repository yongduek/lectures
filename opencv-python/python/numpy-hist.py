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

plt.imshow (frame[:,:,::-1]) ## cv2's BGR -> RGB
plt.title ('Input Image')
plt.pause (1)
plt.close()

x = range(0,256,1)
plt.plot (x, bluehist, 'b', x, redhist, 'r', x, greenhist, 'g')
plt.grid(True)
plt.title ('Histograms for R,G,B, respectively')
plt.pause (1)
plt.close ()

#EOF
