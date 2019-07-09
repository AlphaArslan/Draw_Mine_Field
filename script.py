#################### NOTATION
# we assume the field is mapped like follows

# A1    A2    A3    A4    .  .  .      NORTH
# B1    B2    B3    B4                   ^
# C1    C2    C3    C4                   |
# D1    D2    D3    D4                   |
# .                                    LENGTH
# .                                      |
# .                                      |
#-----------------WIDTH-------------------

#################### IMPORT
from PIL import Image                           # python image lib
import numpy as np

#################### GLOBAL VARIABLES
MINE_COLOR      = (255, 0, 0)                   # red
WIDTH           = 8                             # count of squares
LENGTH          = 8                             # count of squares

IMAGE_PATH      = "Mine_Map.jpg"
IMAGE_WIDTH     = 512
IMAGE_HEIGHT    = 512

rgb_array = np.zeros((IMAGE_WIDTH, IMAGE_HEIGHT, 3), 'uint8')
rgb_array[...] = 255 

#################### FUNCTION
def draw_image(mine_locations):
    for location in mine_locations:
        y = ord(location[0])-ord('A') + 1
        x = ord(location[1]) - 48               # ord('1') = 49
        draw_pixels(x,y)
    img = Image.fromarray(rgb_array)
    img.save(IMAGE_PATH)

def draw_pixels(x,y):                           # coordinates of mine square
    #pixel coordinates
    x_start_pixel = (x-1) * int(IMAGE_WIDTH/WIDTH)
    x_end_pixel = (x) * int(IMAGE_WIDTH/WIDTH)

    y_start_pixel = (y-1) * int(IMAGE_HEIGHT/LENGTH)
    y_end_pixel = (y) * int(IMAGE_HEIGHT/LENGTH)

    # red channel
    rgb_array[x_start_pixel:x_end_pixel , y_start_pixel:y_end_pixel, 0] = MINE_COLOR[0]

    # green channel
    rgb_array[x_start_pixel:x_end_pixel , y_start_pixel:y_end_pixel, 1] = MINE_COLOR[1]

    # blue channel
    rgb_array[x_start_pixel:x_end_pixel , y_start_pixel:y_end_pixel, 2] = MINE_COLOR[2]

#################### Main
if __name__ == '__main__':
    draw_image(("A1", "B4" , "C3" , "H8"))
