# filename: bbox.py

# ref: http://d2l.ai/chapter_computer-vision/index.html

import os, sys 
import imageio 
import matplotlib.pyplot as plt 
import numpy as np 

# This function has been saved in the d2l package for future use
def bbox_to_rect(bbox, color):
    # Convert the bounding box (top-left x, top-left y, bottom-right x,
    # bottom-right y) format to matplotlib format: ((upper-left x,
    # upper-left y), width, height)
    return plt.Rectangle(
        xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1],
        fill=False, edgecolor=color, linewidth=2)
#

img = imageio.imread ('./imgs/catdog.jpg')
dog_bbox, cat_bbox = [60, 45, 378, 516], [400, 112, 655, 493]

fig = plt.imshow (img)
fig.axes.add_patch (bbox_to_rect(dog_bbox, 'blue'))
fig.axes.add_patch (bbox_to_rect(cat_bbox, 'red'))
plt.pause(1)
plt.close()
# Multiple Anchor Boxes

h, w, ch = img.shape
sizes = np.array([0.75, 0.5, 0.25])
ratios = np.array([1, 2, 0.5])

def make_abox (sz, r):
    sqr = np.sqrt(r)
    hs = sz * sqr  # horizontal size
    vs = sz / sqr  # vertical size
    left, right = -hs/2. , hs/2
    top, bot = -vs/2. , vs /2
    return [left, top, right, bot, 's=%.2f r=%.1f'%(sz,r)] # [x, y, x, y]
#
def abox2bbox(abox, wh, loc):
    w = wh[0]; h = wh[1]
    x = loc[0]; y = loc[1]
    # the aspect ratio is w.r.t the height of the image
    return [ h*abox[0] + x, h*abox[1] + y, h*abox[2] + x, h*abox[3] + y]
#
def bbox2rect(bbox): # [x, y, w, h]
    return [bbox[0], bbox[1], bbox[2]-bbox[0], bbox[3]-bbox[1]] 

# centered at (0,0) = (r,c)
anchors = []
for r in ratios:
    anchors.append (make_abox(sizes[0], r))
for s in sizes[1:]:
    anchors.append (make_abox(s, ratios[0]))
#print (anchors)
#print (abox2bbox(anchors[0], (w,h), (250,250)))

fig = plt.imshow (img)
colors = ['b', 'g', 'r', 'm', 'c', 'y']
for i, a in enumerate(anchors):
    bbox = abox2bbox(a, (w,h), (250,250))
    rect = bbox2rect (bbox)
    #print (i, a)
    #print (i, 'bbox: ', bbox, 'rect: ', rect)
    fig.axes.add_patch (bbox_to_rect(abox2bbox(a, (w,h), (250,250)), colors[i]))
    fig.axes.text (rect[0], rect[1], a[-1], color='k', bbox=dict(facecolor=colors[i], lw=0) )
plt.title ('%d bounding boxes drawn at xy=(%d, %d)' % (len(anchors), 250, 250))
plt.pause(1)

