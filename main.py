"""
To be used as the main of the program, currently being used to test pygame functionalities
"""

import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Falling Sand")

#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

fill.screen(BLACK)
#flip function makes pygame actually draw the changes
pygame.display.flip()

block_type='sand'

pos = pygame.mouse.get_pos()

class grid:



# -------- Main Program Loop -----------
while not done:
    #Goes through for loop if the user did something
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN
            if event.button == 0
                print(0)
            elif event.button == 1
                print(1)
            elif event.button == 2
                print(2)
            elif event.button == 3
                print(3)
            
            #place_block(pos, block_type, grid)
        #elif event.type == pygame.
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        # Limit to 60 frames per second
        clock.tick(60)

pygame.quit
