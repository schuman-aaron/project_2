import random
from place_block import place_blocks
from remove_block import remove_blocks
from check_blocks import check_above

def sandphysics(grid, screen, point, block_type):
    x = point[0] - 1 # x-value to the left of the block
    y = point[1] + 1 # y-value below the block
    possible_x_points = []

    for i in range(3):
        if grid.pos[x + i][y].density < grid.pos[point[0]][point[1]].density:
            possible_x_points.append(i)

    if not possible_x_points:
        return [], point

    #remove original point
    remove_blocks(point, grid, screen)
    update_blocks = check_above(point, grid)

    x += random.choice(possible_x_points)

    block_below = grid.pos[x][y].block

    place_blocks(point,block_below, grid, screen)
    remove_blocks((x, y), grid, screen)

    place_blocks((x, y),block_type , grid, screen)
    update_blocks.append((x, y))
    return update_blocks, None
