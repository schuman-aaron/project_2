import random
from place_block import place_blocks
from remove_block import remove_blocks
from check_blocks import check_above

def sandphysics(grid, screen, point, block_type):
    x = point[0] - 1   # x-value to the left of the block
    y = point[1] + 1   # y-value below the block
    possible_x_points = []
    switch_sands = 0

    for i in range(3):
        if grid.pos[x + i][y].block == 'None':
            possible_x_points.append(i)

    if block_type == 'Heavy Sand' and not possible_x_points:
        switch_sands = 1
        for i in range(3):
            if grid.pos[x + i][y].block == 'Sand':
                possible_x_points.append(i)

    if not possible_x_points:
        return [], point

    #remove original point
    remove_blocks(point, grid, screen)
    update_blocks = check_above(point, grid)

    x += random.choice(possible_x_points)

    if switch_sands:
        place_blocks(point,'Sand', grid, screen)
        remove_blocks((x, y), grid, screen)

    place_blocks((x, y),block_type , grid, screen)
    update_blocks.append((x, y))
    return update_blocks, None
