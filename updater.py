import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)

def update(the_grid, screen, update_pos):
    new_update_pos = list()
    remove_update_pos = list()
    #look at every value that needs to be updated
    for i in range(len(update_pos)):
            x=update_pos[i][0]
            y=update_pos[i][1]
            #if marked for being sand
            if the_grid.pos[x][y].block == 'Sand':
                pass
                #update each individual positions of sand blocks if sand block
                #alt_update_pos=sandphysics(the_grid, screen, update_pos[i])
                #if alt_update_pos == None
                    #remove_update_pos += update_pos[i]
                #new_update_pos=alt_update_pos+new_update_pos
            elif the_grid.pos[x][y].block == 'None':
                remove_update_pos+=update_pos[i]
            else: #elif the_grid.pos[x][y].block == 'Block', similar to above
                pass
 
    #adds the new values that need to be update and
    #removes the values that intersect between update_pos and remove_update_pos           
    update_pos = new_update_pos+[val for val in update_pos if val not in remove_update_pos]
    pygame.display.flip()
    return update_pos






