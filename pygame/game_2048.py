import pygame 
import random 
import math

pygame.init()
# Initialising main constants
# Frames per second:
FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT//ROWS
RECT_WIDTH = WIDTH // COLS

# RGB COLORS
OUTLINE_COLOR = (187,173,160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)

FONT = pygame.font.SysFont("comicsans", 60, bold = True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_grid(window):
    # draw a horizontal line for each row
    for row in range(1,ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0,y), (WIDTH,y), OUTLINE_THICKNESS)

    # draw a vertical line for each column 
    for col in range(1,COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x,0), (x,HEIGHT), OUTLINE_THICKNESS)
        
    # draw outside window square
    pygame.draw.rect(window, OUTLINE_COLOR, (0,0, WIDTH, HEIGHT), OUTLINE_THICKNESS) #rectangle coordinates starts at top left corner


def draw (window):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)
    
    
    pygame.display.update()         #as soon as update is called, it makes the updates with the orders in which they are called 

# Create main loop that runs the game

def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():  # check for events that occur (key press for ex)
            if event.type == pygame.QUIT :
                run = False
                break

        
        draw(window)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)
