# Computer Vision for SFM, Visual SLAM and Augmented Reality
- Geometric approaches in Computer Vision
- Structure from Motion
- Vision-based Motion Analysis
- Augmented Reality
  
## References
1. Computer Vision: Algorithms and Applications, 2nd ed., Richard Szeliski, https://szeliski.org/Book/
3. Multiple View Geometry in Computer Vision, Richard Hartley and Andrew Zisserman
4. Computer Graphics Using OpenGL (2nd Ed.), Francis S. Hill 
1. Slambook 2 https://github.com/gaoxiang12/slambook-en   
1. Programming Computer Vision with Python: Tools and Algorithms for Analyzing Images, Erik Solem, http://programmingcomputervision.com/ 
2. Augmented Reality: Principle and Practice, Dieter Schmalstieg, Tobias Hollerer, 2016 https://arbook.icg.tugraz.at/ 
3.   https://vnav.mit.edu/ MIT 16.485 - Visual Navigation for Autonomous Vehicles, 2022
4.   https://rpg.ifi.uzh.ch/teaching.html Vision Algorithms for Mobile Robotics, 2021
5.   

## Basic Development libraries
1. OpenCV
2. Eigen 3
3. g2o

## Image Processing
1. Image data structure
2. RGB vs HSI
3. Spatial Filtering - Window Operations
    - Blurring, Gaussian smoothing
    - Sobel, Derivative
5. Tracking a chessboard pattern
6. Geometric transformations & 3D motion
    - Similarity
    - Projective
    - 2D projective transformation = 2D homography transformation
      - perspective transformation of 2D planes
      - purely rotating camera
      - Experiment. Rectangle drawing on the chessboard
  
7. Image interpolation & Warping
    - Bilinear interpolation
    - forward / backward
    - video warping on the virtual display pannel 

8. Feature detection
   - Harris corner detector
   - Sparse optical flow (good features to detect)
   - FAST corner
   - ORB descriptor
   - SIFT feature descriptor

9. RANSAC & Homography Estimation
    - outlier problem
    - random sample consensus
    - robust estimation of 2D homography; image mosaic

## Camera Calibration
1. Internal / External parameters
2. Rigid motion model, homogeneous coordinate system
3. Pin-hole model
4. Calibration pattern design 
5. Nonlinear optimization
    - parametrization of rotation matrix
    - initialization method
6. Applications with a calibrated camera.
   - How to virtually rotate the camera so that the viewing angle and the surface normal of chessboard is parallel.
     - Can do with 2D homography. Find it.

## Two View Reconstruction / Stereo Vision
1. Epipolar geometry
   - Eight point algorithm by Hartley
2. Rectification of two views for scan-line matching
3. block matching: CC, NCC
4. stereo matching with random dot active illumination (Kinect, realsense stereo)
5. Intermediate view generation


## Camera Pose Estimation
1. PnP: Perspective n-Point Algorithms
2. OpenGV by Kneip
2. ICP Algorithm

## Triangulation

## Structure From Motion
- BA: Bundle-Adjustment

## Loop Closure 
1. Bag of Words Algorithm
2. DBoW3

## Stereo Visual Odometry
- Project based on Slambook2

## Planar Marker AR
- based on OpenCV `findChessboardMarker` or similar.
- Project based on ORBSlam 2/3

## Long Video Sequence 3D Reconstruction
- Motion & 3D map/environment
- Project based on ORBSlam 2/3 or slambook2

## Projects
1. Video on the pannel 
2. Automatic stitching of multiple views
4. Virtual object display on your desk with opengl
5. 3D reconstruction of an office, building or the whole school
6. Self-designed.



## Reference Sites
1. ETH Zurich, Vision algorithms for Mobile Robotics by David Scaramuzza.
  - https://rpg.ifi.uzh.ch/teaching.html

2. SLAM Book: Introduction to Visual SLAM: From Theory to Practice
  - https://github.com/gaoxiang12/slambook2
  - https://github.com/gaoxiang12/slambook-en
  - 

3. Computer Vision Lectures
  - 컴퓨터비전 특강: ORB SLAM, 한동대 황성수 (https://youtu.be/tDfAbqQQO0o)
  - 컴퓨터비전 강의 by 경북대 정순기 (https://youtu.be/N0jD7RKIzVU)
  - Georgia 6476 (https://omscs.gatech.edu/cs-6476-computer-vision-course-videos)
  - Brown 1430(https://browncsci1430.github.io/webpage/index.html), python



### Ref to Camera Calibration (OpenCV)
- LearnOpenCV.com
  - https://learnopencv.com/geometry-of-image-formation/
  - https://learnopencv.com/camera-calibration-using-opencv/
  - https://learnopencv.com/understanding-lens-distortion/

- https://github.com/kaustubh-sadekar/VirtualCam
    - Virtual camera is created only using OpenCV and numpy. It simulates a camera where we can control all its parameters intrinsic and extrinsic to get a better understanding how each component in the camera projection matrix affects the final image of the object captured by the camera.


### Linear Algebra
1. Immersive Linear Algebra (http://immersivemath.com/ila/index.html)