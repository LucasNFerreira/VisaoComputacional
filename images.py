from SimpleCV import *

'''
Demonstrate simple functions of SimpleCV  
Framework saving the result images in the Directory
where this file is located.
'''

def funcoesBasicas(img):
	_binarized = img.binarize()
	_binarized.drawText("Hello World!")
	_binarized.save("binarized.jpg")

	_eroded = img.erode()
	_eroded.save("eroded.jpg")

	_threshold = img.binarize(90).invert()
	_threshold.save("thresholded.jpg")

	_edged = img.edges(t1=160)
	_edged.save("edged.jpg")

	_croped = img.crop(300,300, 500, 500)
	_croped.save("croped.jpg")

	_warped = img.warp(((100,10),(300,10), (450,300), (10,300)))
	_warped.save("warped.jpg")

	_negative = img.invert()
	_negative.save("negative.jpg")

	_grey = img.greyscale()
	_grey.save("greyscale.jpg")

	_blobs = img.findBlobs()
	_blobs.draw()
	img.save("blobs.jpg")

'''
verify if exists a yellow car in th lot
'''

def isCar(carInLot, noCarInLot):

	_car = carInLot.crop(470,200,200,200)
	_yellow_car = _car.colorDistance(Color.YELLOW)
	_only_car = _car - _yellow_car
	_img1 = _only_car.meanColor()

	_no_car = noCarInLot.crop(470,200,200,200) 
	_yellow_car = _no_car.colorDistance(Color.YELLOW)
	_only_car = _car - _yellow_car
	_img2 = _only_car.meanColor()
	if (_img1==_img2):
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

	_cam = Camera()
	_threshold = 5.0 # if exceed this value do an action

	while True:
		_previous = _cam.getImage() #capture a frame
		time.sleep(0.5) #wait 0,5 sec
		_current = _cam.getImage() #capture another frame
		_diff = _current - _previous 
		_matrix = _diff.getNumpy()
		_mean = _matrix.mean()

		_diff.save("image.jpg")

		if _mean >= _threshold:
		        print "Motion Detected"