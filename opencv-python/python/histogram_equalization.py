# filename: histogram_equalization.py
# https://en.wikipedia.org/wiki/Histogram_equalization

import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

imagefilename = 'data/300px-Unequalized_Hawkes_Bay_NZ.jpg'
img = cv2.imread(imagefilename, cv2.IMREAD_GRAYSCALE)
print ('image size (gray scale): ', img.shape)

plt.imshow (img, cmap='gray')
plt.pause (1)
plt.close()

def histogram (ii):
    h = np.zeros(256)
    for val in ii.flatten():
        h[val] += 1
    return h
#

def make_cdf (pmf):
    cdf = np.zeros (pmf.shape)
    print ('cdf: ', cdf.shape)
    cdf[0] = pmf[0]
    for x in range(1, cdf.shape[0]):
        cdf[x] = cdf[x-1] + pmf[x]  
    return cdf
#

# compute histogram
h = histogram (img)

# normalize to get PMF, Probability Mass Function
pmf = h / float(img.shape[0]*img.shape[1])

# Accumulate to get CDF, Cumulative Distribution Function
cdf = make_cdf (pmf)

plt.plot (h); plt.title ('histogram (counts)') # show the histogram
plt.pause (1) # seconds
plt.close()

plt.plot (cdf); plt.title('CDF') # check the CDF
plt.pause (1)
plt.close()

#
pmf_max = pmf.max()
print ('max of pmf: ', pmf_max)
plt.plot (range(cdf.shape[0]), cdf, 'b-', range(cdf.shape[0]), pmf*0.7/pmf_max, 'r-'); 
plt.title ('CDF, PMF')
plt.pause(1)
plt.close()

def histogram_equalization (img, cdf):
    ieq = np.zeros_like (img)
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            pixelvalue = img[r,c]
            ieq[r,c] = np.clip(255. * cdf[pixelvalue], 0, 255).astype (np.uint8)
    #
    return ieq
#

# do it now
img_eq = histogram_equalization (img, cdf)

plt.imshow (img_eq, cmap='gray'); plt.title('histogram equalized')
plt.pause(1)
plt.close()

# check the histogram of the equalized image.
# verify what you did.

heq = histogram (img_eq)

plt.bar (range(0,256), heq, width=4)
plt.title('histogram of histogram-equalized image')
plt.pause (1)
plt.close()

# Now, make & plot the CDF of heq


# EOF
