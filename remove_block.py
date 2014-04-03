import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)
GREY = (200,200,200)

def remove_blocks(mpos, the_grid, update_pos, screen):
    #the position the user clicked on is not empty and within boundary
    if the_grid.pos[mpos[0]][mpos[1]].block != 'None' and mpos[1]>0 and mpos[0]<len(the_grid.pos) and mpos[0]>0 and mpos[1]<len(the_grid.pos[0]):
        #that position now contains nothing
        the_grid.pos[mpos[0]][mpos[1]].block = 'None'
        #change in block type could require updating of other blocks
        update_pos.append([mpos[0],mpos[1]-1])
        update_pos.append([mpos[0]+1,mpos[1]-1])
        update_pos.append([mpos[0]-1,mpos[1]-1])
        #set density
        the_grid.pos[mpos[0]][mpos[1]].density == 0
        #change color
        screen.set_at((mpos[0],mpos[1]), BLACK)
    return update_pos
