# filename: moviepy_get_audio.py

from moviepy.editor import *

moviefile = 'data/dooly.mp4'
video = VideoFileClip(moviefile) # open a movie file

audio = video.audio  # get the audio part

audiofile = 'data/dooly_audio_extracted.mp3'
audio.write_audiofile(audiofile) # file save

import os
os.listdir ('data/*.mp3')

# EOF
