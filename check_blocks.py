def check_above(point, grid):
    """
    Given a block called 'point' in 'grid', the function determines if any of the
    3 blocks above 'point' have a block type that is movable ("Sand", "Stone", etc).
    Returns a list that contains the coordinates for the movable blocks.
    """
    movable_block = []
    
    x = point[0] - 1  # block to the left of 'point'
    y = point[1] - 1  # block above 'point'
    
    # loop and add the coordinates to a list if the block type isn't 'None' or 'Block'
    for i in range(3):
        block_type = grid.pos[x + i][y].block
        if block_type != 'None' and block_type != 'Block':
            movable_block.append((x + i, y))
    return movable_block
