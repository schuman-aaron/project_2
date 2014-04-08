import random
from place_block import place_blocks
from remove_block import remove_blocks
from check_blocks import check_above

def sandphysics(grid, screen, point, block_type):
    """
    'sandphysics' switches the location of the block at 'point' in 'grid' with a
    block below it if the density of the lower block is smaller. If its density
    isn't higher, then the function doesn't switch the blocks. Function returns a
    tuple where the first element is a list of block points that may need to be
    updated because of the switch. The second element is a point that can't
    move down any further. If the original block can move down, then the second
    element in the return value is None. If the original block can't move down then
    the first element is an empty list.

    Compares the density of the block at 'point' in 'grid' with the density of the
    block directly below, below and left, and below and right. If the density for
    the original block is higher than one of these 3 blocks, we randomly choose
    one of them and switch it with the original block.
    """
    x = point[0] - 1 # x-value to the left of the block
    y = point[1] + 1 # y-value below the block
    possible_x_points = []

    # loop to find if any blocks below point have a lower density
    for i in range(3):
        if grid.pos[x + i][y].density < grid.pos[point[0]][point[1]].density:
            possible_x_points.append(i)

    # if block at 'point' has a lower density than the blocks below it, exit
    if not possible_x_points:
        return [], point

    # remove original block
    remove_blocks(point, grid, screen)
    update_blocks = check_above(point, grid)

    # choose which block to go down to and move it to the original block location
    x += random.choice(possible_x_points)
    block_below = grid.pos[x][y].block
    place_blocks(point, block_below, grid, screen)

    # move original block down to new tile
    remove_blocks((x, y), grid, screen)
    place_blocks((x, y), block_type , grid, screen)
    update_blocks.append((x, y))

    return update_blocks, None
