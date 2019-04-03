# filename: kmeans-colors.py
# yndk@sogang.ac.kr
# ref: https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html

import collections
import numpy as np
import matplotlib.pyplot as plt
import skimage
from sklearn.cluster import KMeans
from time import time

# Load the Summer Palace photo
china = skimage.io.imread ('data/nature-500x375.jpg')
china = china.astype(np.float32) / 255

# Load Image and transform to a 2D numpy array.
assert china.shape[2] == 3 # Color image only
image_array = china.reshape(-1, 3)
print ('image_array_shape = ', image_array.shape)

# Count the number of distinct colors
colorlist = []
for c in image_array:
    colorlist.append ( (c[0], c[1], c[2]) )
pixelCounter = collections.Counter (colorlist)
n_src_colors = len(pixelCounter)
print ('The number of distinct colors in src image: ', n_src_colors)

mostCommon10 = pixelCounter.most_common(10)
print ('The most frequent color is {}'.format(mostCommon10[0][0]))

plt.imshow(china)
plt.axis('off'); plt.title('Original image ({}) colors'.format(n_src_colors))
plt.pause(1); plt.close()

# Apply kmeans clustering
print("Perform k-means clustering on {} pixels ... ".format(china.shape[0]*china.shape[1]), end=' ')
t0 = time()
n_colors = 10 # the num. of clusters
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array)
print ('done in %0.3f seconds.' % (time() - t0))

# labels is the array of index labels to cluster center
labels = kmeans.predict(image_array)
print ('labels ({}) = {}'.format(type(labels), labels))

labelsCounter = collections.Counter (labels)

maxLabel = labelsCounter.most_common()
print ('The label of maximum population: ', maxLabel)

plt.bar (labelsCounter.keys(), labelsCounter.values())
plt.title ('the number of labes for {} cluster centers.'.format(n_colors))
plt.pause(1); plt.close()

print ('cluster_centers: \n', kmeans.cluster_centers_)
print ('The most common color is ', kmeans.cluster_centers_[maxLabel[0][0]])

def recreate_image(codebook, labels, ishape):
    """Recreate the (compressed) image from the code book & labels"""
    image = np.zeros(ishape)
    label_idx = 0
    for i in range(ishape[0]):
        for j in range(ishape[1]):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

plt.imshow(recreate_image(kmeans.cluster_centers_, labels, china.shape))
plt.title('Quantized image ({}) colors by K-Means'.format(n_colors)); plt.axis('off')
plt.pause(1); plt.close()


# Apply kmeans clustering for k=2
print("Perform k-means clustering on {} pixels ... ".format(china.shape[0]*china.shape[1]), end=' ')
t0 = time()
n_colors = 2 # the num. of clusters
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array)
print ('done in %0.3f seconds.' % (time() - t0))

# labels is the array of index labels to cluster center
labels = kmeans.predict(image_array)
print ('labels ({}) = {}'.format(type(labels), labels))

labelsCounter = collections.Counter (labels)

maxLabel = labelsCounter.most_common()
print ('The label of maximum population: ', maxLabel)

plt.bar (labelsCounter.keys(), labelsCounter.values())
plt.title ('the number of labes for {} cluster centers.'.format(n_colors))
plt.pause(1); plt.close()

print ('cluster_centers: \n', kmeans.cluster_centers_)
print ('The most common color is ', kmeans.cluster_centers_[maxLabel[0][0]])

plt.imshow(recreate_image(kmeans.cluster_centers_, labels, china.shape))
plt.title('Quantized image ({}) colors by K-Means'.format(n_colors)); plt.axis('off')
plt.pause(1); plt.close()

# remove or change `random_state=0` & try the program again
# Its purpose is to get an identical result from KMeans procedure.
# You should remove it in practice.
