# pil-font-drawtext.py
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

fontdir = '/home/yndk/.fonts'
fontfilenames = [
    'NotoSansCJKkr-Medium.otf',
    'NanumBarunGothicOTF_Light.otf',
    'NanumBarunGothicOTF_Regular.otf',
    'NanumBarunGothicOTF_Semi_Bold.otf',
    'NanumBarunGothicOTF_YetHangul_Regular.otf',
    'NanumGothicOTF_Bold.otf',
    'NanumGothicOTF_Semi_Bold.otf',
    'NanumMyeongjoOTF_YetHangul_Regular.otf'
]

fontfiles = [ os.path.join (fontdir, f) for f in fontfilenames] 

for fontfile in fontfiles:
    print ('fontfile = ', fontfile)
    if os.path.exists (fontfile) == False:
        print ('font file not found: ', fontfile)
        quit()
    #

im = np.ones((500, 1200,3), dtype=np.uint8)*128 # numpy rgb, gray color 
pilimg = PIL.Image.fromarray (im)

# prepare font data
fonts = [ImageFont.truetype(font=fontfile, size=16) for fontfile in fontfiles]

draw = ImageDraw.Draw(pilimg)

with open ('data/fk050000000000.txt') as f:
    fk05 = f.read()
print (fk05)
for c in fk05:
    print ('c: {} {:5d} hex: {:7}'.format(c, ord(c), hex(ord(c))))

hun = [fk05]
for i, font in enumerate(fonts):
    draw.text ((8,10 + 50*i), fontfilenames[i] + hun[0], font=font, fill=(0,0,0), language='kr') # black color

imshow (pilimg, title='PIL Image with Text Inserted.')

im2 = np.array(pilimg)
imshow (im2, title='Numpy Image with Text Inserted thru PIL.', p=1)

w = '듀ᇰ귁'
for c in w:
    print ('c: {}  {:5d} hex: {:7}'.format(c, ord(c), hex(ord(c))))

imageio.imwrite ('data/font-drawings.png', im2)


# EOF