#
from moviepy.editor import *
import numpy as np

videofile = 'data/avideo.mov'
movie = VideoFileClip(videofile)
audio = movie.audio
duration = movie.duration # == audio.duration, presented in seconds, float
#note video.fps != audio.fps
print ('video.duration: {} seconds with fps= {}'.format(movie.duration, movie.fps))
print ('audio.duration: ', audio.duration, audio.fps)

step = 0.1
for t in range(int(duration / step)): # runs through audio/video frames obtaining them by timestamp with step 100 msec
    t = t * step
    if t > audio.duration or t > movie.duration: break
    audio_frame = audio.get_frame(t) #numpy array representing mono/stereo values
    video_frame = movie.get_frame(t) #numpy array representing RGB/gray frame

    movie.show(t)
#
# EOF
