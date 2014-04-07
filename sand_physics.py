import random
from place_block import place_blocks
from remove_block import remove_blocks

def sandphysics(grid, screen, point):
    x = point[0] - 1   # x-value to the left of the block
    y = point[1] + 1   # y-value below the block
    possible_x_points = []

    for i in range(3):
        if grid.pos[x + i][y].block == 'None':
            possible_x_points.append(i)

    if not possible_x_points:
        return None

    
    #temp_list = list()    
    #remove original point first
    remove_blocks((point[0], point[1]), grid, screen)
    
    x += random.choice(possible_x_points)

    place_blocks((x, y),'Sand', grid, screen)
    return (x, y)
