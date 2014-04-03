import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)
GREY = (200,200,200)

def place_blocks(mpos, block_type, the_grid, update_pos, screen):
    #if the position the user clicked on is empty
    if the_grid.pos[mpos[0]][mpos[1]].block == 'None':
        #that position now contains whatever block type was selected at the time
        the_grid.pos[mpos[0]][mpos[1]].block = block_type
        update_pos.append([mpos[0],mpos[1]])
        #update that position to contain sand
        if the_grid.pos[mpos[0]][mpos[1]].block == 'Sand':
            the_grid.pos[mpos[0]][mpos[1]].density == 1
            screen.set_at((mpos[0],mpos[1]), TAN)
        #update that position to contain block
        if the_grid.pos[mpos[0]][mpos[1]].block == 'Block':
            #block type blocks do not get transposed
            the_grid.pos[mpos[0]][mpos[1]].density == None
            screen.set_at((mpos[0],mpos[1]), GREY)            
    return update_pos
