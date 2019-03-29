# filename: moviepy-1.py
# https://zulko.github.io/moviepy/getting_started/quick_presentation.html

# linux: $ sudo apt-get install ffmpeg

from moviepy.editor import VideoFileClip, ImageSequenceClip, VideoClip
import numpy as np 
import matplotlib.pyplot as plt
import cv2

# movie file open
clip = VideoFileClip('data/atomboy.mp4')
print ('clip: {}\nDuration: {}\nFPS: {}'.format(clip, clip.duration, clip.fps))

# get a subclip
subclip = clip.subclip (20, 30) # 20 ~ 30 sec
subclip.write_videofile ('atom-20-30.mov', codec='libx264')
subclip.close ()
print ('subclip duration: ', subclip.duration, ' seconds.')

subaudio = subclip.audio
subaudio.write () # !!!!

# make a gif sequence (for a social media?), no sound with gif
clip2 = clip.subclip (40,50)
clip2.speedx(2).to_gif ('atom-40-50.gif')

#
imagelist = []
for frame in clip.subclip (20, 30).iter_frames():
    # frame is read-only
    img = frame.copy()
    img[50:100, 30:120] = [255, 0, 0]
    imagelist.append (img)
    cv2.imshow ('disp', img)
    cv2.waitKey (30)
#

audio2030 = clip.subclip(20,30).audio

vclip = ImageSequenceClip(imagelist, fps=clip.fps)
vclip.set_audio (audio2030)
vclip.write_videofile ('out.mp4')
# EOF
