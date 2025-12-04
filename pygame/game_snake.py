import pygame
import random
import math

pygame.init()
# Initialising main constants
# Frames per second:
FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS = 20
COLS = 20

RECT_HEIGHT = HEIGHT//ROWS
RECT_WIDTH = WIDTH // COLS

# RGB COLORS
OUTLINE_COLOR = (0,0,0)
OUTLINE_THICKNESS = 15
BACKGROUND_COLOR = (255,255,255)
FONT_COLOR = (119,110,101)

FONT = pygame.font.SysFont("comicsans", 60, bold = True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")



def main(window):
    clock = pygame.time.Clock()
    run = True
    

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():  # check for events that occur (key press for ex)
            if event.type == pygame.QUIT :
                run = False
                break
        
        


if __name__ == "__main__":
    main(WINDOW)
