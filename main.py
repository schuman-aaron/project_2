import pygame
from setcolor import set_color
from place_block import place_blocks
from remove_block import remove_blocks
from updater import update

#Global colours
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)
GREY = (200,200,200)
LGREY = (100,100,100)

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

#initial block type
block_type='Sand'

#initial mouse position
mpos = pygame.mouse.get_pos()

class grid_element:
    def __init__(self):
        #default values
        self.block = 'None'
        self.density = 0

class grid:
    def __init__(self, screen_size,screen, GREY):

	#each block is 2x2 pixels large
        y = screen_size[1] // 2
        x = screen_size[0] // 2

        self.pos = list()
        #setting the position as a list of lists
        for i in range(x):
            self.pos.append(list())
            for j in range(y):
                elt = grid_element()
                # set up attributes of the grid element
                self.pos[i].append(elt)
                #setup a block barrier around the screen
                if j==0 or i==0 or j== y-1 or i == x-1:
                    self.pos[i][j].block = 'Block'
                    self.pos[i][j].density = 99
                    set_color(screen, GREY, (i,j))

#initialize the grid
the_grid = grid(size,screen, GREY)
mouse_down1 = 0
mouse_down2 = 0
#store the position of the block that has been changed or could be, here
update_pos = set()


# -------- Main Program Loop -----------
while not done:
    #Goes through for loop if the user did something
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            break
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] // 2, mpos[1] //2)
        #check to see if the user left or right clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_down1 = 1
            elif event.button == 3:
                mouse_down2 = 1
        #check to see if the user released the left mouse button

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_down1 = 0
        #if the b button is pressed then change block type
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            if block_type == 'Sand':
                block_type = 'Block'
            elif block_type == 'Block':
                block_type = 'Stone'
            else:
                block_type = 'Sand'
        #check to see if the user released the right mouse button
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            mouse_down2 = 0
    #left mouse button is being held down
    if mouse_down1 == 1:
        if block_type == 'Block':
            #each block type block is twice as long and wide as a regular block
            #so place block in each of positions on screen 
            for i in range(2):
                for j in range(2):
                    point = (mpos[0] + i, mpos[1] + j)
                    new_block = place_blocks(point, block_type, the_grid, screen)
                    #update what is at that position only if there was nothing from before
                    if new_block:
                        update_pos.add(new_block)
        else:
            #if not a block type block then only place a single block of the current type
            new_sand = place_blocks(mpos, block_type, the_grid, screen)
            if new_sand:
                update_pos.add(new_sand)
        #right mouse button is being held down
    if mouse_down2 == 1:
        for i in range(2):
            for j in range(2):
                point = (mpos[0] + i, mpos[1] + j)
                #Set these blocks for being removed
                update_blocks = remove_blocks(point, the_grid, screen)
                if update_blocks:
                    for block in update_blocks:
                        update_pos.add(block)
        #illegal mouse operation, reset left and right mouse button is down variables
        #note: without this placing blocks would become slower and slower
        #each time the operation is executed
    if mouse_down1==1 and mouse_down2 == 1:
        mouse_down1 = 0
        mouse_down2 = 0
    #update function
    update(the_grid, screen, update_pos)

    # Limit to 400 frames per second

    clock.tick(400)

pygame.quit
