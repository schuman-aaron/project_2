import pygame
from place_block import place_blocks
from updater import update

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = ()

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Falling Sand")

#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen.fill(BLACK)
#flip function makes pygame actually draw the changes
pygame.display.flip()

block_type='Sand'

mpos = pygame.mouse.get_pos()

class grid_element:
    def __init__(self):
        #default values
        self.block = 'None'
        self.density = 0

class grid:
    def __init__(self, screen_size):
        y = screen_size[1]
        x = screen_size[0]
        self.pos = list() 
        #to get a certain position and attribute call for grid.pos[x][y].attribute  
        for i in range(x):
            self.pos.append(list())
            for j in range(y):
                elt = grid_element()
                # set up attributes of the grid element
                self.pos[i].append(elt)


the_grid = grid(size)
mouse_down = 0
#store the position of the block that has been changed or could be here
update_pos = list()


# -------- Main Program Loop -----------
while not done:
    #Goes through for loop if the user did something
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:               
                mouse_down = 1
            elif event.button == 3:
                pass
                #remove_block(mpos, the_grid)
        if event.type == pygame.MOUSEBUTTONUP and mouse_down == 1:
            mouse_down = 0
        if mouse_down == 1:
            update_pos = place_blocks(mpos, block_type, the_grid, update_pos)
                
        #if event.type == pygame.K_b

    update_pos = update(the_grid, screen, update_pos)
            
    mpos = pygame.mouse.get_pos()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit
