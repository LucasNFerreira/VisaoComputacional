#!/usr/bin/env python
# coding=UTF-8

from SimpleCV import *

'''
Identifica linhas retas em um streaming de vídeo
'''
def findLinesCam(): 
	display = SimpleCV.Display()
	cam = SimpleCV.Camera()
	 
	while display.isNotDone():
	    img = cam.getImage().flipHorizontal()
	    lines = img.findLines() 
	    if (lines):
		lines.daw((255,0,0))
	    img.show()

'''
Identifica linhas retas em uma imagem
'''
def findLinesImage(img):
	display = SimpleCV.Display()
	
	while display.isNotDone():
	    img = Image(img).flipHorizontal()
	    lines = img.findLines() 
	    if (lines):
		lines.draw((255,0,0))
	    img.show()
	

# findLinesCam()
findLinesImage('imagem.jpg')
