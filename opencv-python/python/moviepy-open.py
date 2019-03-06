#
from moviepy.editor import *
import cv2
import numpy as np

videofile = 'data/avideo.mov'
video = VideoFileClip(videofile)
audio = video.audio
duration = video.duration # == audio.duration, presented in seconds, float
#note video.fps != audio.fps
print ('video.duration: ', video.duration, video.fps)
print ('audio.duration: ', audio.duration, audio.fps)

step = 0.1
for t in range(int(duration / step)): # runs through audio/video frames obtaining them by timestamp with step 100 msec
    t = t * step
    if t > audio.duration or t > video.duration: break
    audio_frame = audio.get_frame(t) #numpy array representing mono/stereo values
    video_frame = video.get_frame(t) #numpy array representing RGB/gray frame

    cv2.imshow ('display', video_frame)
    if cv2.waitKey(25) == 27: break
#
