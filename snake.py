import pygame, random
from pygame.locals import *
import os

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game')

#Set file save location
save_file_name = os.environ['USERPROFILE']+"\score.dat"

#Save high score to file
def save_hi_score(file_name, value):
    try:
        save_file = open(file_name,"w")
        save_file.write(str(value))
        save_file.close()
    except:
        print("Error to save data!!!")

#Read high score from file
def get_hi_score(file_name):
    points = 0
    try:
        save_file = open(file_name,"r+")
        points = int(save_file.read())
        save_file.close()
    except:
        print("Error to read data!!!, attempting to create a new save file...")
        save_file = open(file_name,"w")
        if(save_file):
            print("Save game file created!")
            save_file.write(str(points))
            save_file.close()

    return points

#Restart Function
def restart_game():
    restart_font = pygame.font.Font('freesansbold.ttf',50)
    restart_screen = restart_font.render('Press Space to Restart', True, (100, 100, 100))
    restart_rect = restart_screen.get_rect()
    restart_rect.midtop = (300, 300)
    
    screen.blit(restart_screen, restart_rect)
    
    while True:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game()
                    
        pygame.display.update()  
              
#The game itself
def start_game():
    snake = [(200, 200),(210, 200), (220, 200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))
    snake_speed = 20

    food_pos = on_grid_random()
    food = pygame.Surface((10,10))
    food.fill((255,0,0))

    my_direction = LEFT

    
    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0

    high_score = get_hi_score(save_file_name)

    game_over = False

    while not game_over:
        clock.tick(snake_speed)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            #Movements Comamands 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == pygame.K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == pygame.K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                if event.key == pygame.K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT
            
        
            
        #Adding points, speed and the new part of the snake        
        if collision(snake[0], food_pos):
            food_pos = on_grid_random()
            snake.append((0,0))
            score = score + 1
            snake_speed = snake_speed + 6
    
        
            
        # Check if the snake has collided with boundaries
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake [0][1] < 0:
            game_over = True
            break
        
        # Check if the snake has collided with itself
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game_over = True
                break
            
        if game_over:
            break

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])


        #Snake movements 
        if my_direction ==  UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction ==  DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction ==  RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction ==  LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])            
                
        screen.fill((0,0,0))
        screen.blit(food, food_pos)
        
        # Draw horizontal lines
        for x in range(0, 600, 10): 
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
        # Draw vertical lines
        for y in range(0, 600, 10): 
            pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
        
        #Displaying Score
        score_font = font.render('Score: %s' % (score), True, (255,255,255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (20, 10)
        screen.blit(score_font, score_rect)
        
        #Displaying Highscore
        high_score_font = font.render('Highscore: %s'% (high_score), True, (255,255,255))
        high_score_rect = score_font.get_rect()
        high_score_rect.topright = (520, 10)
        screen.blit(high_score_font, high_score_rect)
        
        if score > high_score:
            high_score = score
            save_hi_score(save_file_name, high_score)
        
        for pos in snake: 
            screen.blit(snake_skin, pos)
                
        pygame.display.update()
        
    while True:
        #Displaying Game Over
        game_over_font = pygame.font.Font('freesansbold.ttf', 75)
        game_over_screen = game_over_font.render('Game Over', True, (255,255,255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (600 / 2, 100)
        
        screen.blit(game_over_screen, game_over_rect)
        restart_game()
        pygame.display.update()
        pygame.time.wait(500)
        
        
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    
start_game()