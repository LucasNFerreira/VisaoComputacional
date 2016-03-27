from SimpleCV import *

import sys
import select

PATH = "camera/"
EXT = ".png"
NAME = "snct_prot"

def heardEnter():
    
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return True
    return False

def start_camera(effect):

    x = 0
    cam = Camera()
    while True:
        if (effect==1):
            #negative effect
            img = cam.getImage().invert()
        elif (effect==2):
            #grayscale effect
            img = cam.getImage().greyscale()
        elif (effect==3):
            #lighten effect
            img = sepia_effect(cam.getImage())
        elif (effect==4):
            #darken effect
            img = cam.getImage()/3
        elif (effect==5):
            #nightvision effect
            img = nightvision_effect(cam.getImage())
        else:
            img = cam.getImage() 

        if heardEnter():
            name = NAME+str(x)
            img.save(PATH+name+EXT)
            print "saved: " + PATH + name + EXT
            x+=1

        img = draw_center_square_and_circle(img)
        img.show()

    del cam

def straight_lines():
    display = Display()
    cam = Camera()
 
    while display.isNotDone():
        img = cam.getImage().flipHorizontal()
        lines = img.findLines()
        if (lines):
            lines.draw((255,0,0))
        img.show()
    del cam
    del display

def draw_center_square_and_circle(img):

    from SimpleCV import DrawingLayer

    facelayer = DrawingLayer((img.width, img.height))
    facebox_dim = (200,200)
    center_point = (img.width / 2, img.height / 2)
    facebox = facelayer.centeredRectangle(center_point, facebox_dim)
    circlelayer = DrawingLayer((img.width, img.height))
    circlelayer.circle(center_point, 10)
    img.addDrawingLayer(circlelayer)
    img.addDrawingLayer(facelayer)
    img.applyLayers()
    return img

def nightvision_effect(img):
    (red ,green, blue) = img.splitChannels(False)
    return green

def sepia_effect(img):
    (red ,green, blue) = img.splitChannels(False)
    return (((green/2.2 + red)+img.greyscale()/2)/2.5)*1.3