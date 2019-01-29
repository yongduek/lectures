import cv2
import numpy as np
import matplotlib.pyplot as plt

rows = 5
cols = 7
im = 255 * np.ones( (rows, cols, 3), dtype=np.uint8)
im[2,3] = [255,0,0]
print ('im.shape = ', im.shape)
cv2.imshow ('disp', im)
cv2.waitKey (0)