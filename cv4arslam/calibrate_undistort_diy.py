#!/usr/bin/env python

'''
camera calibration for distorted images with chess board samples
reads distorted images, calculates the calibration and write undistorted images

usage:
    calibrate.py [--debug <output path>] [--square_size] [<image mask>]

default values:
    --debug:    ./output/
    --square_size: 1.0
    <image mask> defaults to ./data/left*.jpg
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

# local modules
from common import splitfn

# built-in modules
import os

def main():
    import sys
    import getopt
    from glob import glob

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['debug=', 'square_size=', 'threads='])
    args = dict(args)
    args.setdefault('--debug', './output/')
    args.setdefault('--square_size', 1.0)
    args.setdefault('--threads', 4)
    if not img_mask:
        img_mask = './data/left??.jpg'  # default
    else:
        img_mask = img_mask[0]

    img_names = glob(img_mask)
    debug_dir = args.get('--debug')
    if debug_dir and not os.path.isdir(debug_dir):
        os.mkdir(debug_dir)
    square_size = float(args.get('--square_size'))

    pattern_size = (9, 6)
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = cv.imread(img_names[0], cv.IMREAD_GRAYSCALE).shape[:2]  # TODO: use imquery call to retrieve results

    def processImage(fn):
        print('processing %s... ' % fn)
        img = cv.imread(fn, 0)
        if img is None:
            print("Failed to load", fn)
            return None

        assert w == img.shape[1] and h == img.shape[0], ("size: %d x %d ... " % (img.shape[1], img.shape[0]))
        found, corners = cv.findChessboardCorners(img, pattern_size)
        if found:
            term = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 30, 0.1)
            cv.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

        if debug_dir:
            vis = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
            cv.drawChessboardCorners(vis, pattern_size, corners, found)
            _path, name, _ext = splitfn(fn)
            outfile = os.path.join(debug_dir, name + '_chess.png')
            cv.imwrite(outfile, vis)

        if not found:
            print('chessboard not found')
            return None

        print('           %s... OK' % fn)
        return (corners.reshape(-1, 2), pattern_points)

    threads_num = int(args.get('--threads'))
    if threads_num <= 1:
        chessboards = [processImage(fn) for fn in img_names]
    else:
        print("Run with %d threads..." % threads_num)
        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(threads_num)
        chessboards = pool.map(processImage, img_names)

    chessboards = [x for x in chessboards if x is not None]
    for (corners, pattern_points) in chessboards:
        img_points.append(corners)
        obj_points.append(pattern_points)

    # calculate camera distortion
    rms, camera_matrix, dist_coefs, _rvecs, _tvecs = cv.calibrateCamera(obj_points, img_points, (w, h), None, None)

    print("\nRMS:", rms)
    print("camera matrix:\n", camera_matrix)
    print("distortion coefficients: ", dist_coefs.ravel())

    # undistort the image with the calibration
    print('')
    for fn in img_names if debug_dir else []:
        _path, name, _ext = splitfn(fn)
        img_found = os.path.join(debug_dir, name + '_chess.png')
        outfile = os.path.join(debug_dir, name + '_undistorted.png')

        img = cv.imread(img_found)
        if img is None:
            continue

        h, w = img.shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

        dst = cv.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

        # crop and save the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]

        print('Undistorted image written to: %s' % outfile)
        print('New K:', newcameramtx)
        cv.imwrite(outfile, dst)

## DIY undistort ---
    def interp1d(f, I, J):  # 0 <= f <= 1
        val = I * (1. - f) + J * f 
        return val 

    def interp2d(ud, vd, im):
        ui = int(ud)
        uf = ud - ui 
        vi = int(vd)
        vf = vd - vi
        I0 = interp1d(uf, im[vi, ui], im[vi, ui+1])
        I1 = interp1d(uf, im[vi+1, ui], im[vi+1, ui+1])
        I = interp1d(vf, I0, I1);
        I = np.clip(I, 0, 255).astype(np.uint8)
        return I 
    #

    def diy_undistort(im, K, dcoef, Knew):
        k1, k2, p1, p2, k3 = dcoef[0] # distortion coeffs.
        if len(im.shape) == 1: nchannels = 1
        else:
             if len(im.shape) == 3: nchannels = 3
             else: print("Wrong channel number: ", len(im.shape), im.shape)

        oim = im.copy()
        for r in range(oim.shape[0]):
            for c in range(oim.shape[1]):
                # new (x, y) is the point without distortion (imaginary)
                xnew = (c - Knew[0,2]) / Knew[0,0]
                ynew = (r - Knew[1,2]) / Knew[1,1]
                #
                r2 = xnew**2 + ynew**2
                r4 = r2**2
                r6 = r2 * r4
                radial = (1 + k1 * r2 + k2 * r4 + k3 * r6)
                xd = xnew * radial + 2 * p1 * xnew * ynew + p2 * (r2 + 2 * xnew**2)
                yd = ynew * radial + p1 * (r2 + 2 * ynew**2) + 2 * p2 * xnew * ynew 
                ud = xd * K[0,0] + K[0, 2]
                vd = yd * K[1,1] + K[1, 2]
                # print(c, r, ud, vd)
                if ud < 0 or vd < 0 or vd >= im.shape[0]-1 or ud >= im.shape[1]-1:
                    # print("Out of bound: ", c, r, " --> ", ud, vd)
                    color = 0 if nchannels == 1 else np.array([0,0,0])
                else:
                    color = interp2d(ud, vd, im)   # get interpolated color
                oim[r, c] = color 
        return oim 
    #

    ## 
    newcameramtx = camera_matrix.copy()
    newcameramtx[0,0] *= 0.8 
    newcameramtx[1,1] *= 0.8
    
    for fn in img_names if debug_dir else []:
        _path, name, _ext = splitfn(fn)
        img_found = os.path.join(debug_dir, name + '_chess.png')
        outfile = os.path.join(debug_dir, name + '_undistorted_diy.png')

        img = cv.imread(img_found)
        if img is None:
            continue

        dst = diy_undistort(img, camera_matrix, dist_coefs, newcameramtx)

        # crop and save the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]

        print('Undistorted image written to: %s' % outfile)
        cv.imwrite(outfile, dst)
## DIY undistort ----------------------------------------------------------------------------------------

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
