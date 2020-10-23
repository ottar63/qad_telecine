from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import argparse
import imutils
import cv2
import time
from variables import *
from util import *

camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.rotation = rotate
camera.iso = iso
camera.exposure_compensation = exposure_comp
camera.meter_mode = 'matrix'
time.sleep(2)
camera.exposure_mode = 'off'
camera.resolution = (3280, 2464)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
# get image size
image_h, image_w, channels = image.shape
sprock_image = image[0:image.shape[0], sprock_x_min:sprock_x_max]
Mask = cv2.inRange(sprock_image, sp_lower_val, sp_upper_val)

# find the contours in the mask
cnts = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("I found {} white shapes".format(len(cnts)))
cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
cv2.imshow("Mask", Mask)
# draw line for sprock_x_min
print("Image: "+format(image.shape))
# image_rz=cv2.resize(image,(int(image_w/3),int(image_h/3)))
cv2.rectangle(image, (sprock_x_min, sprock_y_min_OK), (sprock_x_max, sprock_y_max_OK), (0, 0, 255), 4)
# draw line for sprock_x_max
image_preview = cv2.resize(image, (int(image_w/3), int(image_h/3)))
# cv2.line(image,(sprock_x_max,0),(sprock_x_max,image_h),(0,255,0))
cv2.namedWindow('Originale')
cv2.imshow("Originale", image_preview)
# loop over the contours
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    print("Contour: {} {} {} {}".format(x, y, w, h))
    # cv2.drawContours(image, [c], -1, (255, 0, 0), 2, offset=(sprock_x_min, 0))
    if w >= sprock_w and h >= sprock_h:
        # this contour is a sprock
        SX_center = int(x + (w/2)) + sprock_x_min
        SY_center = int(y + (h/2))
        print("Sprocket OK center  at : {} {} w:{} h:{}".
              format(SX_center, SY_center, w, h))
        # draw crosshair at sprock center
        if sprock_y_min_OK <= SY_center <= sprock_y_max_OK:
            # sprock center is within limits
            cv2.drawContours(image, [c], -1, green, 6, offset=(sprock_x_min, 0))
            # draw lines around crop area
            Xmin = SX_center + crop_x_offset
            Xmax = SX_center + crop_w + crop_x_offset
            Ymin = int(SY_center - (crop_h / 2))
            Ymax = int(SY_center + (crop_h / 2))
            cv2.rectangle(image, (Xmin, Ymin), (Xmax, Ymax), green, 4)
        else:
            cv2.drawContours(image, [c], -1, yellow, 6, offset=(sprock_x_min, 0))
        image = cross_hair(image, SX_center, SY_center, 10, 3)

        # crop_img = image[Ymin:Ymax, Xmin:Xmax]
        # cv2.imwrite(outfile_name, crop_img)
        # cv2.namedWindow("cropped",cv2.WINDOW_NORMAL)
        # cv2.imshow("cropped",crop_img)
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Image",image)
        # cv2.waitKey(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
image = cv2.resize(image, (int(image_w/3), int(image_h/3)))
cv2.imshow("Image", image)
cv2.waitKey(0)
