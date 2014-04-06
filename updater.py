import pygame
from sand_physics import sandphysics

def update(the_grid, screen, update_pos):
    new_update_pos = list()
    remove_update_pos = list()
    #look at every value that needs to be updated
    """
    for i in range(len(update_pos)):
            x=update_pos[i][0]
            y=update_pos[i][1]
            #if marked for being sand
            if the_grid.pos[x][y].block == 'Sand':
                #update each individual positions of sand blocks
                alt_update_pos=sandphysics(the_grid, screen, update_pos[i])
                if alt_update_pos == None:
                    remove_update_pos += update_pos[i]
                else:
                    new_update_pos+=alt_update_pos
            #don't bother updating nothing
            elif the_grid.pos[x][y].block == 'None':
                remove_update_pos+=update_pos[i]
            #don't bother updating block
            elif the_grid.pos[x][y].block == 'Block':
                remove_update_pos+=update_pos[i]
                """
    #adds the new values that need to be update and
    #removes the values that intersect between update_pos and remove_update_pos           
    update_pos = new_update_pos+[val for val in update_pos if val not in remove_update_pos]
    pygame.display.update()
    return update_pos






