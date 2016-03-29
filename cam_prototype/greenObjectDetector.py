#coding:utf-8
from SimpleCV import *

cam = Camera()

def detect_green_object():

    while TRUE:
    
        img = cam.getImage()

        dist = img.colorDistance(SimpleCV.Color.RED).dilate(2)
        segmented = dist.stretch(200,255)
        blobs = dist.findBlobs(minsize=100)
        
        if blobs:
            blobs.draw()
            x = 0
            y = 0
            for blob in blobs:
                x = blob.coordinates()[0]
                y = blob.coordinates()[1]
            print '['+str(x)+','+str(y)+']'
            img.drawRectangle(x-150,y-150,150,150,SimpleCV.Color.BLUE)
            
        img.show()    
