from SimpleCV import *

cam = Camera()
x = 0
y = 0

def detect_green_object():

    while TRUE:
    
        img = cam.getImage().flipHorizontal()

        dist = img.colorDistance(SimpleCV.Color.RED)
        
        segmented = dist.stretch(200,255)
        blobs = segmented.findBlobs(minsize=50)
        
        if blobs:
            blobs.draw()
            
            blob = blobs[-1]
            x = blob.coordinates()[0]
            y = blob.coordinates()[1]
            
            print blob.coordinates()
            img.drawRectangle(x-150,y-150,150,150,SimpleCV.Color.RED)
            
        img.show()
