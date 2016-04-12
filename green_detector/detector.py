#!/usr/bin/env python

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Setup SimpleBlobDetector parameters.
_params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
#_params.minThreshold = 10;
#_params.maxThreshold = 200;
 
# Filter by Area.
_params.filterByArea = True
_params.minArea = 1500
 
# Filter by Circularity
_params.filterByCircularity = False
_params.minCircularity = 0.1
 
# Filter by Convexity
_params.filterByConvexity = False
_params.minConvexity = 0.87
 
# Filter by Inertia
_params.filterByInertia = False
_params.minInertiaRatio = 0.01

while(1):

    # Take each frame
    _, frame = cap.read()

    #filtring the frame with a Gausian filter:
    blur = cv2.blur(frame,(5,5))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_green = np.array([29, 86, 6], dtype=np.uint8)
    upper_green = np.array([64, 255, 255], dtype=np.uint8)
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    mask = 255-mask

    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create(_params)
    
    # Detect blobs.
    keypoints = detector.detect(mask)

    #edges = cv2.Canny(mask,100,200)

    '''
    Draw detected blobs as blue circles.
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle
    corresponds to the size of blob
    '''
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, frame, (255,0,0),
                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 

    #edges = cv2.Canny(mask,100,200)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= edges)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('edges', edges)
    #cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
