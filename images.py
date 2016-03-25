from SimpleCV import *

'''
Demonstrate simple functions of SimpleCV  
Framework saving the result images in the Directory
where this file is located.
'''

def funcoesBasicas(img):
    binarized = img.binarize()
    binarized.drawText("Hello World!")
    binarized.save("binarized.jpg")

    eroded = img.erode()
    eroded.save("eroded.jpg")

    threshold = img.binarize(90).invert()
    threshold.save("thresholded.jpg")

    edged = img.edges(t1=160)
    edged.save("edged.jpg")

    croped = img.crop(300,300, 500, 500)
    croped.save("croped.jpg")

    warped = img.warp(((100,10),(300,10), (450,300), (10,300)))
    warped.save("warped.jpg")

    negative = img.invert()
    negative.save("negative.jpg")

    grey = img.greyscale()
    grey.save("greyscale.jpg")

    blobs = img.findBlobs()
    blobs.draw()
    img.save("blobs.jpg")

'''
verify if exists a yellow car in the lot
'''

def isCar(carInLot, noCarInLot):

    car = carInLot.crop(470,200,200,200)
    yellow_car = car.colorDistance(Color.YELLOW)
    only_car = car - yellow_car
    img1 = only_car.meanColor()

    no_car = noCarInLot.crop(470,200,200,200) 
    yellow_car = no_car.colorDistance(Color.YELLOW)
    only_car = car - yellow_car
    img2 = only_car.meanColor()
    if (img1==img2):
        return False
    else:
        return True


'''
Motion Detector: Capture two frames from the webcam,
with a interval of 0,5 sec. If the diference between
them exceed a value save the diference image and print
"Motion Detected".
'''

def motionDetector():

    cam = Camera()
    threshold = 5.0 # if exceed this value do an action

    while True:
        previous = cam.getImage() #capture a frame
        time.sleep(0.5) #wait 0,5 sec
        current = cam.getImage() #capture another frame
        diff = current - previous 
        matrix = diff.getNumpy()
        mean = matrix.mean()

        diff.show()

        if mean >= threshold:
            print "Motion Detected"