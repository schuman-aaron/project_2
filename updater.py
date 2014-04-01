import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)

def update(the_grid, screen, update_pos):
    #look at every value that needs to be updated
    for i in range(len(update_pos)):
            x=update_pos[i][0]
            y=update_pos[i][1]
            #if marked for being sand
            if the_grid.pos[x][y].block == 'Sand':
                #despite the screen is black at that point
                if tuple(screen.get_at((x,y)))==(0,0,0,255):
                    #draw the sand block
                    screen.set_at((x,y), TAN)
                else:
                    pass
                    #sandphysics(the_grid, screen, update_pos), change the position in update pos if moved; that way even if it does move it will not be recounted
            else: #elif the_grid.pos[x][y].block == 'Block', similar to above
                pass
                
            #note, it will be the effect of both physics that will remove items from update_pos
            temp=update_pos.pop()
    pygame.display.flip()
    return update_pos
