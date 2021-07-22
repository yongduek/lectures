import cv2 
import numpy as np

def getinfo(cap):
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    print(length, width, height, fps, length/fps)
    return length, width, height, fps

def main0():
    cap = cv2.VideoCapture(0)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(width, height)
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        cv2.imshow('win', frame)

        if cv2.waitKey(33) == ord('q'): break 
    #
    cv2.destroyAllWindows()

def main1():
    cap = cv2.VideoCapture(0)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(width, height)
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    col = width // 2
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        col = (col + 1) % width 
        canvas[:, col, :] = frame[:,col, :]

        cv2.imshow('win', canvas)

        if cv2.waitKey(33) == ord('q'): break 
    #
    cv2.destroyAllWindows()

def main2():
    cap = cv2.VideoCapture(0)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    rng = np.random.default_rng(2021)
    rs, cs = 10, 20
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        r = rng.integers(0, height - rs)
        c = rng.integers(0, width - cs)
        canvas[r:r+rs, c:c+cs, :] = frame[r:r+rs,c:c+cs, :]

        cv2.imshow('win', canvas)

        if cv2.waitKey(1) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#
def main2_2(vfilename):
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    rng = np.random.default_rng(2021)
    rs, cs = 120, 20
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        for _ in range(50):
            r = rng.integers(0, height - rs)
            c = rng.integers(0, width - cs)
            canvas[r:r+rs, c:c+cs, :] = frame[r:r+rs,c:c+cs, :]

            canvas[r:r+rs,c,:] = 255
            canvas[r:r+rs,c+cs,:] = 255
            canvas[r,c:c+cs,:] = 255
            canvas[r+rs,c:c+cs,:] = 255

        cv2.imshow('win', canvas)

        if cv2.waitKey(10) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main3(vfilename=None):
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    rng = np.random.default_rng(2021)
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        rs, cs = 50, 100

        for _ in range(30):
            r = rng.integers(-rs//2, height)
            c = rng.integers(-cs//2, width)
            
            rrs = r + rs
            ccs = c + cs 
            if r < 0: r = 0
            if rrs >= height: rrs = height-1
            if c < 0: c = 0
            if ccs >= width: ccs = width - 1

            canvas[r:rrs, c:ccs, :] = np.clip( (.5*canvas[r:rrs, c:ccs, :] + .5*frame[r:rrs,c:ccs, :]), 0, 255)
        cv2.imshow('win', canvas)

        if cv2.waitKey(30) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main4(vfilename=None):  # vertical edge by pixel difference
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    rng = np.random.default_rng(2021)
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        # horizontal difference -> vertical edge
        for i in range(1, height-1):
            for j in range(1, width-1):
                canvas[i, j] = np.abs(frame[i, j+1] - frame[i, j-1])

        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main5(vfilename=None):  # vertical edge with filtering
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    # horizontal difference -> vertical edge
    kernel = np.array([ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    print('kernel: ', kernel)

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = np.abs( cv2.filter2D(frame, ddepth=-1, kernel=kernel) )
        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main6(vfilename=None):  # horizontal edge with filter
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    # horizontal difference -> vertical edge
    kernel = np.array([ [-1, -2, -1], [0, 0, 0], [1, 2, 1]]) # transpose
    print('kernel: ', kernel)

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = np.abs( cv2.filter2D(frame, ddepth=-1, kernel=kernel) )
        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main7(vfilename=None):  # horizontal + vertical edge
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    # horizontal difference -> vertical edge
    vkernel = np.array([ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]).T # transpose
    hkernel = np.array([ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = ( np.abs( cv2.filter2D(frame, ddepth=-1, kernel=hkernel) ) + np.abs( cv2.filter2D(frame, ddepth=-1, kernel=vkernel) ) ) // 2

        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main8(vfilename=None):  # canny edge detector
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 100, 200 )  # only gray scale input accepted.

        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main9(vfilename=None):  # canny edge detector + color
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 100, 200 )  # only gray scale input accepted.
    
        canvas = np.expand_dims(canvas, 2) * frame
        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main10(vfilename=None):  # blurring: box filtering
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = cv2.boxFilter(frame, ddepth=-1, ksize=(31, 3))

        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main11(vfilename=None):  # morphological operation
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(width, height)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (17,17))

    while True:
        ret, frame = cap.read()
        if ret == False: break 

        canvas = cv2.morphologyEx(frame, cv2.MORPH_DILATE, kernel)

        cv2.imshow('win', canvas)

        if cv2.waitKey(15) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#

def main12(vfilename=None):
    cap = cv2.VideoCapture(0 if vfilename == None else vfilename)  # open video camera
    if vfilename is None:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)

    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (17,17))

    rng = np.random.default_rng(2021)
    rs, cs = 620, 20
    while True:
        ret, frame = cap.read()
        if ret == False: break 

        frame = cv2.morphologyEx(frame, cv2.MORPH_DILATE, kernel)

        for _ in range(2):
            r = rng.integers(0, height - rs)
            c = rng.integers(0, width - cs)
            canvas[r:r+rs, c:c+cs, :] = frame[r:r+rs,c:c+cs, :]

            canvas[r:r+rs,c,:] = 255
            canvas[r:r+rs,c+cs,:] = 255
            canvas[r,c:c+cs,:] = 255
            canvas[r+rs,c:c+cs,:] = 255

        cv2.imshow('win', canvas)

        if cv2.waitKey(10) == ord('q'): break 
    #
    cv2.destroyAllWindows()
#


# main2_2('street_720.mp4')
# main3('street_720.mp4')
# main4('street_720.mp4')
# main5('street_720.mp4')
# main6('street_720.mp4')
# main7('street_720.mp4')
# main8('street_720.mp4')
# main9('street_720.mp4')
# main11('street_720.mp4')
# main12()
main12('street_720.mp4')
