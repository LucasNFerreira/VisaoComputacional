from SimpleCV import *

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

	blobs = img.findBlobs()
	blobs.draw()
	img.save("blobs.jpg")

'''
 Verifica se ha um carro estacionado;
 Tem como parametro duas imagens de comparacao, uma com o parametro e outra a ser comparada

'''

def isCar(carInLot, noCarInLot):

	car = carInLot.crop(470,200,200,200)
	yellow_car = car.colorDistance(Color.YELLOW)
	only_car = car - yellow_car
	only_car.meanColor()
	img1 = only_car.meanColor()
	no_car = noCarInLot.crop(470,200,200,200) 
	yellow_car = no_car.colorDistance(Color.YELLOW)
	only_car = car - yellow_car
	img2 = only_car.meanColor()
	if (img1==img2):
		return True
	else:
		return False