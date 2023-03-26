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
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))
my_direction = LEFT

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    screen.fill((0,0,0))
    for pos in snake: 
        screen.blit(snake_skin, pos)
            
    pygame.display.update()