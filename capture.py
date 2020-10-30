#!/usr/bin/python3
import argparse
import glob
import ntpath
import os
import re

import cv2
import util
from variables import *



def capture(nr, jobname):
    tot_s = 0
    my_loop = 0
    # if directory jobname does not exist, create it
    if not os.path.isdir(jobname):
        os.mkdir(jobname)
    prev_nr = 0
    if os.path.isdir(jobname):
        # directory exists, find number of last file captured
        for name in glob.glob(jobname+'/*.jpg'):
            fname = (os.path.splitext(ntpath.basename(name))[0])
            num = int(fname.replace(jobname+"-", ""))
            if num > prev_nr:
                prev_nr = num
            # print("filename :{}  prev_nr: {}" .format(fname, prev_nr))

    print("Previous nr: {}".format(prev_nr))

    while my_loop < nr:
        sp_found, sy_center, sx_center, image = my_camera.find_sprock()
        if not sp_found:
            tot_s = tot_s + search_step
            my_stepper.step_forward(search_step)
        else:
            if sprock_y_min_OK <= sy_center <= sprock_y_max_OK:
                my_loop = my_loop + 1
                tot_s = tot_s + frame_step
                image = my_camera.crop_image(sy_center, sx_center, image)
                filename = jobname+'/'+jobname+"-"+str(my_loop+prev_nr)+'.jpg'
                print("write to {}  my_loop:{} nr: {}".format(filename, my_loop, nr))
                cv2.imwrite(filename, image)
                cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
                cv2.imshow("Image", image)
                cv2.waitKey(10)
                my_stepper.step_forward(frame_step)
            else:
                # print("Frame {} found  not in position at{}:{}".format(my_loop, sy_center,sx_cent))
                tot_s = tot_s + search_step
                my_stepper.step_forward(search_step)

    print("Finished")
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    avg_s_frame = tot_s / nr
    print("Avg step frame: {}".format(avg_s_frame))
    return avg_s_frame


my_stepper = util.Stepper()
my_camera = util.Camera()

parser = argparse.ArgumentParser()
parser.add_argument("--capture", type=int, help="Number of frames to Capture")
parser.add_argument("jobname", help="Name of job(folder/filenames")
args = parser.parse_args()

if args.capture:
    print("Capture {} frames".format(args.capture))
    capture(args.capture, args.jobname)
my_stepper.cleanup()
