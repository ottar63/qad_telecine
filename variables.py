import numpy as np

# camera option 
image_size = (3280, 2464)
iso = 200
exposure_comp = -6
rotate = 180
# steps afte frame capture
frame_step = 265
# steps for finding next sprock
search_step = 20

# y value for sprocket is OK
sprock_y_min_OK = 1200
sprock_y_max_OK = 1500
# x value for sprock
sprock_x_min = 500
sprock_x_max = 700
# minimum size of sprock
sprock_w = 30
sprock_h = 250
# crop size of image
crop_w = 1600
crop_h = 1100
# crop x offset from sprock left side
crop_x_offset = 180
# min color for sprock
sp_lower_val = np.array([130, 130, 130])
sp_upper_val = np.array([255, 255, 255])
# crosshair color
ch_color = (0, 0, 0)
# colors
green = (0, 255, 0)
yellow = (0, 255, 255)
