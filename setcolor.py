import pygame

def set_color(screen, color, point):
    """
    Change the color of a tile by looping to change the color of the
    four pixels.
    """
    
    # multiply to find the pixel location(assuming a tile has 2 pixel width)
    x = point[0] * 2
    y = point[1] * 2
    
    # loop and set color
    for i in range(2):
        for j in range(2):
            screen.set_at((x + i, y + j), color)
