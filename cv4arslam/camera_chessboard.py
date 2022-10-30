import cv2, numpy as np 

camera = cv2.VideoCapture(2)  # try 0, 1, 2, ... if you have multiple cameras

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = camera.get(cv2.CAP_PROP_FPS)  # this may be float such as 29.97
nframes = int(camera.get(cv2.CAP_PROP_FRAME_COUNT))
fourcc = int(camera.get(cv2.CAP_PROP_FOURCC))

print(camera, width, height, fps, nframes, fourcc)
square_size = 10 # mm
pattern_size = (9, 6)
pwidth, pheight = pattern_size
objp = np.zeros((pwidth*pheight, 3), np.float32)       # array of (X,Y,Z)
objp[:,:2] = np.indices(pattern_size).T.reshape(-1,2)  # you may use for-loop instead
objp *= square_size 

print(objp, objp.shape)

while True:
    ret, frame = camera.read()
    if ret == False:
        continue 

    found, corners = cv2.findChessboardCorners(frame, pattern_size)
    # shape of corners is Nx1x2 
    def drawLine(im, p, q, color):
        cv2.line(im, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, thickness=3)
    if found:
        # print(corners.shape)
        # continue 
        for i in range(corners.shape[0]):
            x, y = corners[i,0,0], corners[i,0,1]
            # print("corners: ", x, y)
            cv2.drawMarker(frame, (int(x), int(y)), (128, 128, 255), markerType=2)
            drawLine(frame, corners[0,0], corners[pattern_size[0]-1,0], (0,0,255))
            drawLine(frame, corners[0,0], corners[pattern_size[0]*(pattern_size[1] - 1),0], (0,255,0))
        # print("----------------------")
    cv2.imshow("disp", frame)
    if cv2.waitKey(30) == 27:
        break 
#
