#!/usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
import time

import GraphData

cap = cv2.VideoCapture(0)

# define range of green color in HSV
lower_green = np.array([29, 86, 6], dtype=np.uint8)
upper_green = np.array([64, 255, 255], dtype=np.uint8)

name = "mean/teste" + ".txt"

def params():
    # Setup SimpleBlobDetector parameters.
    _params = cv2.SimpleBlobDetector_Params()
 
    # Change thresholds
    #_params.minThreshold = 10;
    #_params.maxThreshold = 200;
     
    # Filtering by Area.
    _params.filterByArea = True
    _params.minArea = 1500
     
    # Filtering by Circularity
    _params.filterByCircularity = False
    _params.minCircularity = 0.1
     
    # Filtering by Convexity
    _params.filterByConvexity = False
    _params.minConvexity = 0.87
     
    # Filtering by Inertia
    _params.filterByInertia = False
    _params.minInertiaRatio = 0.01

    return _params

def run(data):

	values = [['frame', 'Luminance']]

	i = 0

	while True:

	    # Take each frame
	    _, frame = cap.read()

	    #filtring the frame with a Gausian filter:
	    blur = cv2.blur(frame,(5,5))

	    # Convert BGR to HSV
	    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

	    # Threshold the HSV image to get only green colors
	    mask = cv2.inRange(hsv, lower_green, upper_green)

 	    mask = 255-mask

	    # Set up the detector with default parameters.
	    detector = cv2.SimpleBlobDetector_create(params())
	    
	    # Detect blobs.
	    keypoints = detector.detect(mask)

	    '''
	    Draw detected blobs as blue circles.
	    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle
	    corresponds to the size of blob
	    '''

	    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, frame, (255,0,0),
	                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	 

	    #grayscale the frame
	    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    mask = 255 - mask

	    # Bitwise-AND mask and original image
	    #frame = cv2.bitwise_and(frame,frame, mask= mask)

	    hist = cv2.calcHist([grayscale],[0],mask,[256],[0,256])
	    mean = np.mean(hist)
	    if mean > 10:
	    	data.values.append([i, int(mean)])
	        if i > 30:
	            data.values.pop(1)
	            #print data.values
	            #print len(data.values)
	        i+=1
	    else:
	        data.values.append([i,0])
	        if i > 30:
	            data.values.pop(1)
	            #print data.values
	            #print len(data.values)
	        i+=1

	    cv2.imshow('frame', frame)
	    #cv2.imshow('mask', mask)
	    #cv2.imshow('edges', edges)
	    #cv2.imshow('res', res)
	    k = cv2.waitKey(5) & 0xFF
	    if k == 27:
	        break

        cv2.destroyAllWindows()
  