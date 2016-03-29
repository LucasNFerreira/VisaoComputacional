from SimpleCV import *

cam = Camera()

def detect_green_object():

    while TRUE:
    
        img = cam.getImage()

        dist = img.colorDistance(SimpleCV.Color.RED).dilate(2)
        blobs = dist.findBlobs(minsize=100)
        
        if blobs:
            blobs.draw()
            
            x = 0
            y = 0
            for blob in blobs:
                x = blob.coordinates()[0]
                y = blob.coordinates()[1]
            if isGreen(img.crop(x,y,50,50)):
            	print blob.coordinates()
            	img.drawRectangle(x-150,y-150,150,150,SimpleCV.Color.BLUE)

        img.show()

def isGreen(crop):
    (red, green, blue) = crop.splitChannels(False)
    red_histogram = red.histogram()
    green_histogram = green.histogram()
    blue_histogram = blue.histogram()
    if (green_histogram > blue_histogram) and (green_histogram > red_histogram):
        return True
    else:
	    return False 