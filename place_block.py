import pygame

def place_blocks(mpos, block_type, the_grid, update_pos):
    #if the position the user clicked on is empty
    if the_grid.pos[mpos[0]][mpos[1]].block == 'None':
        #that position now contains whatever block type was selected at the time
        the_grid.pos[mpos[0]][mpos[1]].block = block_type
        update_pos.append([mpos[0],mpos[1]])
        #set density
        if the_grid.pos[mpos[0]][mpos[1]].block == 'Sand':
            the_grid.pos[mpos[0]][mpos[1]].density == 1
            screen.set_at((x,y), TAN)
    return update_pos
