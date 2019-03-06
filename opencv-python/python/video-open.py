# filename: video-open.py
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-functions

import numpy as np
import cv2

video_file = 'data/avideo.mov'
cap = cv2.VideoCapture(video_file)

if cap.isOpened() is False:
    print ('video file open error: ', video_file)
#
width = cap.get (cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get (cv2.CAP_PROP_FRAME_HEIGHT)
nframes = cap.get (cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get (cv2.CAP_PROP_FPS)
print (height, width, nframes, fps)

outvideofile = 'data/outvideo.mov'
out_wh = (640, 480)
outVideo = cv2.VideoWriter (outvideofile, cv2.VideoWriter_fourcc(*'XVID'), 30.0, out_wh)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False: 
        break

    frame = cv2.resize(frame, dsize=out_wh)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text_xy = (100, 200)
    frame = cv2.putText (frame, 'OpenCV', text_xy, font, 4, (0,255,255), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    outVideo.write (frame)

    if cv2.waitKey(30) == 27:
        break
#

cap.release()
outVideo.release()

cv2.destroyAllWindows()

# EOF