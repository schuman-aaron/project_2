import pygame
from setcolor import set_color
from check_blocks import check_above

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)
GREY = (200,200,200)

def remove_blocks(mpos, the_grid, screen):
    """
    Remove the block at 'mpos' from 'the_grid'.
    """

    # coordinates of block
    x = mpos[0]
    y = mpos[1]

    # exit function if we try to remove a block on the border of the screen
    if x >= len(the_grid.pos) - 1 or y >= len(the_grid.pos[0]) - 1:
        return None

    # the position the user clicked on is not empty and within boundary
    if the_grid.pos[x][y].block != 'None' and y>0 and x>0:

        #that position now contains nothing
        the_grid.pos[x][y].block = 'None'

        #set density
        the_grid.pos[x][y].density = 0

        #change color
        set_color(screen, BLACK, (x,y))

        return check_above((x, y), the_grid)
