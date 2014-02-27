#!/usr/bin/env python
# -*- cording: utf-8 -*-
from pygame import camera
from pygame import image
import time

class CamSer():
    def __init__(self):
        cameraNames = camera.list_cameras()
        self.cam = camera.Camera(cameraNames[0])
        self.cam.start()
        print cameraNames, '\n'

    def __exit__(self):
        self.cam.stop()
        print "Exit 0"

    def capture(self):
        # get the image from video & save as ./capimg.jpg
        surface = self.cam.get_image()
        if surface is None:
            print "Could not obtain image from webcam."
            return
        print "Saving curent image..."
        image.save(surface, './mntimg.jpg')

    def run(self):
        while(1):
            time.sleep(2)
            self.capture()

if __name__ == "__main__":
    camera.init()
    camser = CamSer()
    camser.run()
