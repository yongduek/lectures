# Plan

1. 2D geometry & transformations & image transform
    - reference frame, rotation, translation, basis change
    - project: rotate an image
        - understand R & t
        - linear/bilinear interpolation & forwrad/backward mapping

2. 2D affine transformations:
    - R, t, shear, scale
    - homogeneous coordinate representation
    - project: triangular texture mapping
        - H: {p0, p1, p2} -> {q0, q1, q2}
        - apply a sequence of transformations to obtain H
        - specify 4 correspondences, compute H, and apply backward mapping to produce the result.

3. 2D projective transformation:
    - H: 3x3
    - project: perspective rectification
        - take a picture of a wall, with slanted viewing angle
        - specify 4 correspondences, compute homography matrix
            - for the rectified image, choose four corners of a rectangle.
        - warp the source image to produce a rectified image
            - apply the backward mapping developed before