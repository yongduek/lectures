import cv2 as cv
import numpy as np
import imageio 
import matplotlib.pyplot as plt 

def copy(dst, ij, im, iijj, ws):
    i, j = ij
    ii, jj = iijj 
    for r in range(ws):
        di = i + r
        si = ii + r 
        if di < 0 or di >= dst.shape[0] or si < 0 or si >= im.shape[0]: continue
        for c in range(ws):
            dj = j + c
            sj = jj + c 
            if dj < 0 or dj >= dst.shape[1] or sj < 0 or sj >= im.shape[1]: continue 

            dst[di,dj,:] = im[si,sj,:]
#

def transform(im, dst, angle):
    h, w = int(im.shape[0]), int(im.shape[1])
    winsize = 20
    irange = range(0, im.shape[0], winsize)
    jrange = range(0, im.shape[1], winsize)

    for i in irange:
        # ii = i
        ii = int(i + winsize*np.sin(angle + i*.01)*.9 + .5) + winsize
        for j in jrange:
            jj = int(j + winsize*np.sin(angle + j*.01) + .5)

            copy(dst, (i, j), im, (ii, jj), winsize)

    return 
#

src = cv.imread('liquid.bmp')
src = cv.resize(src, (src.shape[1]*4, src.shape[0]*4), )

dst = np.empty_like(src)

angle = 0
while True:

    angle += .1
    transform(src, dst, angle)

    cv.imshow('win', dst)
    if cv.waitKey(30) == 27: break
#