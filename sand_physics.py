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
    x += random.choice(possible_x_points)
    #temp = place_blocks([x,y],'Sand', grid, temp_list, screen)
    return [[x, y]]
