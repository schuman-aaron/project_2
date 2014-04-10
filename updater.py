import pygame
from sand_physics import sandphysics

def update(the_grid, screen, update_pos):
    """
    Function iterates through every block in 'update_pos' and calls 'sandphysics' on it to
    determine the blocks next location. This new location is added to the list 'new_update_pos'
    which is added to 'update_pos' at the end. If the block no longer needs to be tracked (because
    it stopped moving), it is added to 'remove_update_pos' to be removed from 'update_pos'.
    """
    new_update_pos = list()
    remove_update_pos = list()

    #look at every value that needs to be updated
    for point in update_pos:
        # coordinates of the block
        x = point[0]
        y = point[1]

        #if marked for being sand
        if the_grid.pos[x][y].block == 'Sand' or the_grid.pos[x][y].block == 'Stone':
            #update each individual positions of sand blocks
            moved_sand, stopped_sand = sandphysics(the_grid, screen, point, the_grid.pos[x][y].block)

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

    # removes the values that intersect between 'update_pos' and 'remove_update_pos'
    for old_point in remove_update_pos:
        update_pos.remove(old_point)

    # adds the new values that need to be updated
    for new_point in new_update_pos:
        update_pos.add(new_point)

    pygame.display.update()
