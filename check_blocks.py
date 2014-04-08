def check_above(point, grid):
    something_there = []
    x = point[0] - 1
    y = point[1] - 1
    for i in range(3):
        block_type = grid.pos[x + i][y].block
        if block_type != 'None' and block_type != 'Block':
            something_there.append((x + i, y))
    return something_there
