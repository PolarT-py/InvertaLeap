import sys
import pygame

pygame.init()

## Variables
screendata = {
    "size": (1000, 600),
    "width": 1000,
    "height": 600,
    "center": (500, 300),
    "cenright": (750, 300),
    "cenleft": (250, 300),
    "centop": (500, 150),
    "cenbottom": (500, 450),
}
screen = pygame.display.set_mode(screendata["size"])

## Images & Audio


## Functions
def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
