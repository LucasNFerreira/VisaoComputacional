from SimpleCV import *

'''
Funcao que demonstra algumas funcionalidades do SimpleCV quanto a manipulacao das imagens.
Tem como parametro a imagem a ser mofificada.
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


'''
  Motion Detector: Captura 2 imagens da tela e verifica as direfencas entre elas, se for notada uma alteracao maior que o limite 
  salva a diferenca entre as 2 imagens e imprime uma mensagem na tela.
'''

def motionDetector():

	cam = Camera()
	threshold = 5.0 # se exceder esse falor ele faz alguma coisa

	while True:
		previous = cam.getImage() #captura um frame
		time.sleep(0.5) #espera por meio segundo
		current = cam.getImage() #captura outro frame
		diff = current - previous
		matrix = diff.getNumpy()
		mean = matrix.mean()

		diff.save("image.jpg")

		if mean >= threshold:
		        print "Motion Detected"