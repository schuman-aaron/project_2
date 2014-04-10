import pygame
from setcolor import set_color

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)
GREY = (200,200,200)
LGREY = (100,100,100)

def place_blocks(mpos, block_type, the_grid, screen):
    """
    Place a block of type 'block_type' at position 'mpos' on 'the_grid'.
    """

    # coordinates of the block
    x = mpos[0]
    y = mpos[1]

    # leave function if trying to place a block on the border of the screen
    if x >= len(the_grid.pos) - 1 or y >= len(the_grid.pos[0]) - 1:
        return None
    
    #if the position the user clicked on is empty
    if the_grid.pos[x][y].block == 'None':
        #that position now contains whatever block type was selected at the time
        the_grid.pos[x][y].block = block_type

        #update that position to contain sand
        if the_grid.pos[x][y].block == 'Sand':
            the_grid.pos[x][y].density = 1
            set_color(screen, TAN, (x, y))

        #update that position to contain block
        if the_grid.pos[x][y].block == 'Block':
            #block type blocks do not get transposed
            the_grid.pos[x][y].density = 99
            set_color(screen, GREY, (x,y))

        #update that position to contain sand
        if the_grid.pos[x][y].block == 'Stone':
            the_grid.pos[x][y].density = 2
            set_color(screen, LGREY, (x, y))

    return (x, y)
