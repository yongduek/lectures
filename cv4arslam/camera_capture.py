import cv2, numpy as np 

camera = cv2.VideoCapture(2)  # try 0, 1, 2, ... if you have multiple cameras
print(camera)

while True:
    ret, frame = camera.read()
    if ret == False:
        continue 
    
    cv2.imshow("disp", frame)
    if cv2.waitKey(30) == 27:
        break 
#
