import random
from place_block import place_blocks
from remove_block import remove_blocks
from check_blocks import check_above

def sandphysics(grid, screen, point):
    x = point[0] - 1   # x-value to the left of the block
    y = point[1] + 1   # y-value below the block
    possible_x_points = []

    for i in range(3):
        if grid.pos[x + i][y].block == 'None':
            possible_x_points.append(i)

    if not possible_x_points:
        return [], point

    #remove original point first
    remove_blocks(point, grid, screen)
    update_blocks = check_above(point, grid)

    x += random.choice(possible_x_points)

    place_blocks((x, y),'Sand', grid, screen)
    update_blocks.append((x, y))
    return update_blocks, None
