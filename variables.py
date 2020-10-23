import numpy as np

# y value for sprocket is OK
sprock_y_min_OK = 1200
sprock_y_max_OK = 1500
# x value for sprock
sprock_x_min = 730
sprock_x_max = 830
# minimum size of sprock
sprock_w = 90
sprock_h = 250
# crop size of image
crop_w = 1600
crop_h = 1100
# crop x offset from sprock center
crop_x_offset = 100
# camera option 
image_size = (3280, 2464)
iso = 400
exposure_comp = 0
rotate = 180
# min color for sprock
sp_lower_val = np.array([150, 150, 150])
sp_upper_val = np.array([255, 255, 255])
# crosshair color
ch_color = (0, 0, 0)
# colors
green = (0, 255, 0)
yellow = (0, 255, 255)
