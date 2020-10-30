from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import imutils
import cv2
import time
import RPi.GPIO as GPIO
from variables import *


class Stepper:
    Stepp_seq = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
    ]
    step = 0
    control_pins = [7, 11, 13, 15]

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def step_back(self, nr):
        while nr > 0:
            self.step = self.step + 1
            if self.step == 8:
                self.step = 0
            self.move()
            nr = nr - 1

    def step_forward(self, nr):
        # print("to do: {}".format(nr))
        while nr > 0:
            self.step = self.step - 1
            if self.step == -1:
                self.step = 7
            # print("this: {} sequence: {}".format(nr, self.step))
            self.move()
            nr = nr - 1

    def move(self):
        try:
            for pin in range(4):
                GPIO.output(self.control_pins[pin], self.Stepp_seq[self.step][pin])
                time.sleep(0.001)
        except:
            print("clean up")
            GPIO.cleanup()  # cleanup all GPIO

    def cleanup(self):
        print("clean up")
        GPIO.cleanup()  # cleanup all GPIO

    def __exit__(self):
        print("clean up")
        GPIO.cleanup()  # cleanup all GPIO


class Camera:

    def __init__(self):
        global iso
        global exposure_comp
        # Capture Image
        self.camera = PiCamera()
        self.camera.rotation = rotate
        self.camera.resolution = image_size
        self.camera.iso = iso
        self.camera.meter_mode = 'matrix'
        self.camera.exposure_compensation = exposure_comp
        time.sleep(2)
        self.camera.exposure_mode = 'off'

    def find_sprock(self):
        image = self.capture_image()
        global sprock_x_min
        global sprock_x_max
        global sprock_w
        global sprock_h
        SX_left = 0
        SY_center = 0
        SP_found = False
        crop_image = 0
        # search for sprocket
        sprock_image = image[0:image.shape[0], sprock_x_min:sprock_x_max]
        Mask = cv2.inRange(sprock_image, sp_lower_val, sp_upper_val)
        cnts = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        # print("CS: Camera iso: {} , exposure: {}".format(self.camera.iso,self.camera.exposure_compensation))
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.imshow("Image", image)
        cv2.waitKey(10)
        cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
        cv2.imshow("Mask", Mask)
        cv2.waitKey(10)

        # search for sprock
        # print("nr of contours:{}  type{} ".format(len(cnts), type(cnts)))
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if w >= sprock_w and h >= sprock_h:
                print("Possible sprock center at  {}".format(y + (h/2)))
            if w >= sprock_w and h >= sprock_h and 600 < y < 1800:
                SY_center = int(y + (h / 2))
                SX_left = x  + sprock_x_min
                SP_found = True
                print("y: {}".format(SY_center))

        # if found , return 1,center of sprock and image
        return SP_found, SY_center, SX_left, image

    def capture_image(self):
        global sprock_exposure
        global sprock_iso
        rawcapture = PiRGBArray(self.camera)
        # self.camera.exposure_compensation = sprock_exposure
        # self.camera.iso = sprock_iso
        self.camera.capture(rawcapture, format="bgr")
        image = rawcapture.array
        return image

    def crop_image(self, sy_center, sx_left, image):
        global capture_exposure
        global capture_iso
        global sprock_x_max
        global crop_w
        global crop_h
        image = image[sy_center - int(crop_h / 2):sy_center + int(crop_h / 2),
                sx_left + crop_x_offset:sx_left + crop_x_offset + crop_w]
        cv2.namedWindow('Cimage', cv2.WINDOW_NORMAL)
        cv2.imshow("Cimage", image)
        cv2.waitKey(10)
        return image


def cross_hair(image, sx, sy, length, width):
    cv2.line(image, (sx, sy - length), (sx, sy + length), ch_color, width)
    cv2.line(image, (sx - length, sy), (sx + length, sy), ch_color, width)
    return image
