# filename: image-mean.py

import sys
import numpy as np
import cv2

def calc_mean (frame):
    mean = np.zeros((3,))
    for r in range(frame.shape[0]):
        for c in range(frame.shape[1]):
            mean += frame[r,c]

    mean /= frame.shape[0]*frame.shape[1]
    return mean
#

cap = cv2.VideoCapture('data/avideo.mov')
if cap.isOpened() == False:
    return
#

ret, frame = cap.read() # read one frame
if ret == False:
    print ('cap.read() failed.')
    sys.exit()
#

mean = cv2.mean (frame)
print ('cv2.mean() = ', mean, type(mean), frame.shape)

cmean = calc_mean (frame)
print ('calc_mean: ', cmean, cmean.dtype)

npmean = np.mean(frame, axis=(0,1))
print ('npmean = ', npmean, type(npmean), npmean.dtype)

print ('np.sum/N = ', np.sum(frame, axis=(0,1))/frame.shape[0]/frame.shape[1])

while True:
    cv2.imshow ('display', frame)
    if cv2.waitKey(30) is 27:
        break
#

#EOF