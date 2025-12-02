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

# defining the tiles  

class Tile:
    COLORS = [
        (237, 229, 218),    #2
        (238, 225, 201),    #4
        (243, 178, 122),    #8
        (246, 150, 101),    #16
        (247, 124, 95),     #32
        (247, 95, 59),      #64
        (237, 208, 115),    #128
        (237, 204, 99),     #256
        (236, 202, 80),     #512
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):

        # for n in N, every time n increases in number = 2^n, the index in COLORS increases
        # --> index c in COLORS corresponds to log(2)(number)
        # careful : log(2)(2) = 1, so we have to substract 1 to get the 0 index 

        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        # draws the tile on the screen 
        # draw the rectangle with its respective color + the value in the middle on top of it

        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        # text generation
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        # location of the number 
        """
                      W
         - - - - - - - - - - - - - -
        |             W/2            |
        |              |             |
        |    -W/4  <---|             |
        |       |      |             |
        |       |      |             |
        |       |      |             |
        |       |      |             |
        |       |      |             |
         - - - - - - - - - - - - - -
        
        """

        window.blit(
            text,
            (
                self.x + (RECT_WIDTH/2 - text.get_width()/2),
                self.y + (RECT_HEIGHT/2 - text.get_height()/2),
            ),
        )   # blit is how you put a surface on a screen 
        

    def set_pos(self):
        pass

    def move(self):
        pass

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


def draw (window, tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)
    
    
    pygame.display.update()         #as soon as update is called, it makes the updates with the orders in which they are called 


# Create main loop that runs the game

def main(window):
    clock = pygame.time.Clock()
    run = True
    tiles = {"00": Tile(4,0,0), "20": Tile(128,2,0)}

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():  # check for events that occur (key press for ex)
            if event.type == pygame.QUIT :
                run = False
                break

        
        draw(window, tiles)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)
