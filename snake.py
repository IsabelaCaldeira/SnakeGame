import pygame 
from pygame.locals import *

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200),(210, 200), (220, 200)]
my_direction = LEFT

while True:
    0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()