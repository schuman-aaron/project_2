import pygame

def set_color(screen, color, point):
    x = point[0] * 2
    y = point[1] * 2
    
    for i in range(2):
        for j in range(2):
            screen.set_at((x + i, y + j), color)
