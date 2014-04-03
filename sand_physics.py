import random

def sandphysics(grid, screen, point):
    x = point[0] - 1   # x-value to the left of the block
    y = point[1] + 1   # y-value below the block
    possible_x_points = []

    for i in range(3):
        if grid.pos[x + i][y].block == 'None':
            possible_x_points.append(i)

    if not possible_x_points:
        return None
    
    x += random.choice(possible_x_points)
    return [x, y]
