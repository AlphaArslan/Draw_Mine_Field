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
SUR_MINE_COLOR  = (255, 0, 0)                   # red
BUR_MINE_COLOR  = (0, 0, 255)                   # blue
FIELD_WIDTH     = 12                             # count of squares
FIELD_LENGTH    = 12                             # count of squares

IMAGE_PATH      = "Mine_Map.jpg"
IMAGE_WIDTH     = 512
IMAGE_HEIGHT    = 512

rgb_array = np.zeros((IMAGE_WIDTH, IMAGE_HEIGHT, 3), 'uint8')
rgb_array[...] = 255                            # white background

#################### FUNCTION
def draw_image(sur_mine_loc , bur_mine_loc):
    for location in sur_mine_loc:
        x = ord(location[0])-ord('A') + 1               # x and y swapped so that it can work properly
        y = int(location[1:])
        draw_pixels(x, y, SUR_MINE_COLOR)

    for location in bur_mine_loc:
        x = ord(location[0])-ord('A') + 1
        y = int(location[1:])
        draw_pixels(x, y, BUR_MINE_COLOR)


    draw_lines()
    img = Image.fromarray(rgb_array)
    img.save(IMAGE_PATH)


def draw_pixels(x, y, color):                           # coordinates of mine square
    #pixel coordinates
    x_start_pixel = (x-1) * ( IMAGE_WIDTH // FIELD_WIDTH )
    x_end_pixel = x * ( IMAGE_WIDTH // FIELD_WIDTH )

    y_start_pixel = (y-1) * ( IMAGE_HEIGHT // FIELD_LENGTH )
    y_end_pixel = y * ( IMAGE_HEIGHT // FIELD_LENGTH )

    # red channel
    rgb_array[x_start_pixel:x_end_pixel , y_start_pixel:y_end_pixel, 0] = color[0]

    # green channel
    rgb_array[x_start_pixel:x_end_pixel , y_start_pixel:y_end_pixel, 1] = color[1]

    # blue channel
    rgb_array[x_start_pixel:x_end_pixel , y_start_pixel:y_end_pixel, 2] = color[2]


def draw_lines():
    # horizontal
    for y in range(0, FIELD_LENGTH ):
        rgb_array[: , y * ( IMAGE_HEIGHT // FIELD_LENGTH ) , :] = 0

    # vertical
    for x in range(0, FIELD_WIDTH ):
        rgb_array[x * ( IMAGE_WIDTH // FIELD_WIDTH ) , : , :] = 0

#################### Main
if __name__ == '__main__':
    draw_image(("A7" , "F9" , "C3" , "J5"), ("K2" , "D8", "H8" , "L9"))

    #  , "B4"
