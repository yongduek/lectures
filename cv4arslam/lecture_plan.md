# Plan

0. Introduction to Computer Vision & AR
    - Demo: 
        1. Marker-based: ARToolkit, ARSketchBook
        2. Natural Marker-based
        3. SFM/SLAM based
            - `bundang.avi`
        4. AR Foundation in Unity: 
            - https://www.youtube.com/watch?v=FuKzngwzDYI 
        5. Blender VFX: https://youtu.be/O67P0uzbQBk 
        6. Google Maps AR: https://youtu.be/XWbY5jdJnHg 
        7. In-Camera VFX in Unreal Engine: https://youtu.be/ebf1rRkYFmU 
        9. AR and SLAM: https://youtu.be/50quWrNKB0w 
        8. Work assistance or re-education: https://youtu.be/0m67O1Em7dY 
    - What we will do mainly in the course:
        - Fundamentals of linear algebra, geometry, computer vision, slam

1. 2D geometry & transformations & image transform
    - linear algebra revisted
        - matrix, vector, inner product
        - representation w.r.t a new basis (frame change)
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
        - specify 3 correspondences, compute H, and apply backward mapping to produce the result.

3. 2D projective geometry & transformations:
    - H: 3x3
    - project: perspective rectification
        - take a picture of a wall, with slanted viewing angle
        - specify 4 correspondences, compute homography matrix
            - for the rectified image, choose four corners of a rectangle.
        - warp the source image to produce a rectified image
            - apply the backward mapping developed before

4. Pin-hole camera model, lens distortion, and camera calibration
    - pin-hole projection
    - normalized image plane
    - lens distortion model
    - image space scaling by `K`
    - calibration by a chess-board pattern
        - parametrization
        - formulation of a nonlinear optimization problem
        - optimization
    - project
        1. camera calibration with opencv
        2. DIY undistort by backward mapping

5. 3D geometry and transformations
    - R, t, basis change
    - projection through a camera
        - Understand the meaning of the pose matrix from camera calibration
    - project: display all the camera poses in a graphic world 
        - understand where is the camera location and what is the camera direction and the meaning of the pose matrices.

6. 2D projective transformation by camera rotation in 3D
    - Problem: Given an image in general, apply a 3D rotation to the camera and obtain a new image.
        - `K`, use a guessed version or use a calibrated camera.
    - Project: rotate the camera for rectification
        - $ H = K R K^{-1} $
        - Choose appropriate $R$ so that the view of the rectangle in the image may warp to a rectangle.

7. Image feature detection: Keypoints & Descriptors
    - Corner features
        - Harris, FAST
    - Descriptors:
        - BRIEF, ORB, SIFT 
    - Automatic homography computation between two images of pure rotation or a planr scene
        - Descriptor matching
        - RANSAC
    - project: automatic panorama image stitching

8. Two View Geometry
    - Epipolar geometry
    - Essential matrix / fundamental matrix
    - Project: 3D reconstruction from correspondences
        1. collect correspondences
        1. Compute `E`
        2. compute $R$ and $t$
        3. compute 3D coordinates of the correspondences

9. Stereo Vision
    - Theory: Formulation for a well-aligned canonical stereo sytem.
    - $ d = f T / Z $
    - stereo camera calibration
        1. internal/external calibration
        2. stereo rectification: aligning the two views into a canonical system
            - Formulation to obtain the retification homographies.
            - constraint: 
                1. the two $x$-axes must be parallel to $t_{12}$.
                2. the rotation matrices
    - project: stereo rectification DIY
        - show that the views are rectified by displaying the two images in parallel and poinitng several correspondences lying on the same $y$ scan lines.
        - display the two rectified camera frames through Pangolin.
        - compare the result with the output of opencv






