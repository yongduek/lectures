# filename: moviepy_filter.py

# https://zulko.github.io/moviepy/getting_started/effects.html

# Import everything needed to edit video clips
from moviepy.editor import *
import cv2 

# Load a movie file
clip = VideoFileClip("./data/avideo.mov")

# filter
def myFilter (frame):
    # print (frame.flags) # frame is read-only
    # frame: numpy array (rows, cols, 3) of np.uint8 type
    # print (type(frame), frame.dtype, frame.shape)
    # frame[10:20, 20:30,0] = 0 # frame is read-only
    edited = frame.copy()
    h,w,c = edited.shape
    # apply my own filter, remove red & green color, leave blue
    edited[h//2-100:h//2+100, w//2-50:w//2+50,0:2] = 0

    return edited # return the filtered image
#

# apply filter to every frame
video = clip.fl_image (myFilter)

# save to file
video.write_videofile("./data/avideo_myfilter.mp4")

# EOF