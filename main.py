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

screen.fill(BLACK)
#flip function makes pygame actually draw the changes
pygame.display.flip()

block_type='sand'

mpos = pygame.mouse.get_pos()

class grid(screen_size):
    def __init__(self, screen_size):
        y = screen_size[1]
        x = screen_size[0]
        for j in range(y):
            for i in range(x):
                self.pos[x,y].block = None
                self.pos[x,y].update = 0


# -------- Main Program Loop -----------
while not done:
    #Goes through for loop if the user did something
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                place_block(mpos, block_type, grid)
            elif event.button == 3:
                remove_block(mpos, grid)
        #if event.type == pygame.K_b

    update(grid)
            
    mpos = pygame.mouse.get_pos()

        # Limit to 60 frames per second
        clock.tick(60)

pygame.quit
