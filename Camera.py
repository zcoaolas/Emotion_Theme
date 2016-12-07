# -*- coding: utf-8 -*-
from VideoCapture import Device
import sys, pygame, time
from pygame.locals import *
#from PIL import ImageEnhance,ImageDraw


def capture():
    pygame.init()

    size = width, height = 620, 485
    speed = [2, 2]
    black = 0, 0, 0
    shots = 0

    #pygame.display.set_caption('Capture')

    #screen = pygame.display.set_mode(size)

    SLEEP_TIME_LONG = 0.05

    cam = Device(devnum=0, showVideoWindow=0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keyinput = pygame.key.get_pressed()

        if keyinput[K_q]:
            cam.displayCapturePinProperties()
        if keyinput[K_w]:
            cam.displayCaptureFilterProperties()

        if shots <= 2:
            if shots == 0:
                time.sleep(1.6)
            else:
                time.sleep(0.5)
            filename = 'face'+str(shots) + ".jpg"
            cam.saveSnapshot(filename, quality=80, timestamp=0)
            shots += 1
            print("Photo " + str(shots) + " captured.")
            if shots == 3:
                return

        #cam.saveSnapshot('test.jpg', timestamp=3, boldfont=1, quality=75)

        #image = pygame.image.load('test.jpg')

        #screen.blit(image, speed)

        #pygame.display.flip()

#capture()