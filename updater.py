import pygame
from sand_physics import sandphysics

def update(the_grid, screen, update_pos):
    new_update_pos = list()
    remove_update_pos = list()
    #look at every value that needs to be updated
    
    for point in update_pos:
        x = point[0]
        y = point[1]

        #if marked for being sand
        if the_grid.pos[x][y].block == 'Sand':
            #update each individual positions of sand blocks
            moved_sand, stopped_sand = sandphysics(the_grid, screen, point)
            for sand_block in moved_sand:
                new_update_pos.append(sand_block)
            if stopped_sand:
                remove_update_pos.append(stopped_sand)

        #don't bother updating nothing
        elif the_grid.pos[x][y].block == 'None':
            remove_update_pos.append(point)

        #don't bother updating block
        elif the_grid.pos[x][y].block == 'Block':
            remove_update_pos.append(point)
   
    #adds the new values that need to be update and
    #removes the values that intersect between update_pos and remove_update_pos

    for old_point in remove_update_pos:
        update_pos.remove(old_point)

    for new_point in new_update_pos:
        update_pos.add(new_point)

    pygame.display.update()






