# pil-font-drawtext-hangul.py
# ref: https://kalyanchakravarthy.net/blog/drawing-anti-aliased-unicode-text-with-python/

import PIL
from PIL import ImageFont, ImageDraw
import os
import imageio
import numpy as np 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
plt.ion() 

def imshow (rgb, title="imshow", p=2):
    plt.imshow(rgb)
    plt.title (title)
    plt.pause(p); plt.close()
#

print ('PIL version: ', PIL.__version__)
fontdir = '/home/yndk/.fonts'
fontfilename = 'NotoSansCJKkr-Medium.otf' #'NanumBarunGothicOTF_Semi_Bold.otf'

fontfile = os.path.join (fontdir, fontfilename) 

print ('fontfile = ', fontfile)
if os.path.exists (fontfile) == False:
    print ('font file not found: ', fontfile)
    quit()
#

imH = 32
imW = 256

# prepare font data
font24 = ImageFont.truetype(font=fontfile, size=24)
font14 = ImageFont.truetype(font=fontfile, size=14)

# drawing handler

texts = ['가나다', '나가다', '다나가', '나다가', '나나다', '나다다', '가가나', '가다나']
imgs = []
for text in texts:
    pilimg = PIL.Image.new ('RGB', (imW, imH))
    wh = font24.getsize(text) #draw.textsize (text, font=font24, language='kr')
    print ('text size in pixels: ', wh)
    draw = ImageDraw.Draw(pilimg)
    draw.text ((0,0), texts[0], font=font24, fill=(255,255,255), language='kr') # white color
    imgs.append (pilimg)

imshow (pilimg, title='PIL Image with Text Inserted.')

im = np.array(pilimg)
imshow (im, title='Numpy Image from PIL.')

with open ('data/gt.txt', 'wt') as f:
    for i, pil in enumerate(imgs):
        filename = './data/ko-%08d.png' % i
        pil.save(filename)
        f.write (filename + '\t' + texts[i] + '\n')

# EOF