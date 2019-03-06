# filename: video-lastframe.py

import sys
import numpy as np
import cv2

video_file = 'data/avideo.mov'
cap = cv2.VideoCapture(video_file)

if cap.isOpened() is False:
    print ('video file open error: ', video_file)
    sys.exit()
#
width = cap.get (cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get (cv2.CAP_PROP_FRAME_HEIGHT)
nframes = cap.get (cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get (cv2.CAP_PROP_FPS)
print (height, width, nframes, fps)

for i in range (int(nframes)):
    fcount = nframes - 1 - i
    cap.set (cv2.CAP_PROP_POS_FRAMES, int(nframes-1-i))
    ret, frame = cap.read()
    if frame is None:
        print ('frame None', i)
        continue
    if ret == False: 
        print ('ret False', i)
        continue
    print ('frame read: ', i)

    frame = cv2.resize(frame, dsize=None, fx=.25, fy=.25)

    cv2.imshow('frame', frame)
    if cv2.waitKey(3) == 27:
        break
#

cap.release()
cv2.destroyAllWindows()
# EOF