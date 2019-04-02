# filename: moviepy_textoverlay.py

# ref: https://zulko.github.io/moviepy/getting_started/quick_presentation.html


# Import everything needed to edit video clips
from moviepy.editor import *

# Load a movie file
clip = VideoFileClip("./data/avideo.mov")

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')

# Say that you want it to appear at the center of the screen
# The same duration of the video
txt_clip = txt_clip.set_pos('center').set_duration(clip.duration)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available !)
# 'mp4' was OK. 
# Other extensions caused system error: 
# Could not load source '</usr/local/lib/python3.6/site-packages/decorator.py:decorator-gen-49>': Source unavailable.

video.write_videofile("./data/avideo_overlay_text.mp4")

# EOF