import cv2
import numpy as np
import imageio 
import matplotlib.pyplot as plt

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

img = imageio.imread('data/karakoram-imgur.com.jpg')
if img is None:
    print ('image file open error')
    sys.exit ()
#
print (img.shape)
imshow (img, 'Source Image')


# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)

# display
imshow(color, "color")
imshow(edges, "edges")
imshow(cartoon, "Cartoon-like")

# EOF
