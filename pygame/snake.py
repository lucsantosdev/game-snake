import pygame
from sys import exit # terminate the program
import random

ROWS = 25
COLUMNS = ROWS
CELL_SIZE = 25
GAME_WIDTH = CELL_SIZE * COLUMNS
GAME_HEIGHT = CELL_SIZE * ROWS

pygame.init() # initialize pygame
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) # create game window
pygame.display.set_caption("Snake Game (pygame version) by @lucsantosdev") # title of the window
clock = pygame.time.Clock() # used for frame rate control

def get_random(limit):
        return random.randint(0, limit - 1) * CELL_SIZE # get a random position for the food, multiplied by CELL_SIZE to align with the grid

food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE) # create a rectangle for the food
snake = []
snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)) # create a rectangle for the snake's head and add it to the snake list
snake_velocity = (0, 0) # initial velocity of the snake (not moving)

#game loop
while True: 
    for event in pygame.event.get(): # listen for all user events (button, key, mouse)
        if event.type == pygame.QUIT: #user clicks on x button of window
            pygame.quit() # exit pygame
            exit() # terminate the program

        if event.type == pygame.KEYDOWN: # user presses a key
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -CELL_SIZE) # set velocity to move up
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, CELL_SIZE) # set velocity to move down
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-CELL_SIZE, 0) # set velocity to move left
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (CELL_SIZE, 0) # set velocity to move right

    # move the snake
    for i in range(len(snake)-1, 0, -1): # iterate through the snake parts in reverse order (from tail to head)
        snake[i] = snake[i-1].copy() # move each part to the position of the previous part
    snake[0].move_ip(snake_velocity) # move the snake's head by the current velocity

    if snake[0].center == food.center:
         snake.append(food)
         food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE) # create a new food rectangle at a random position

    if not window.get_rect().contains(snake[0]): # check if the snake's head is outside the window boundaries
        snake.clear() # clear the snake list (reset the snake)
        snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)) # create a new snake head at a random position
        food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE) 


    window.fill("black") # fill the window with black color (background)
    pygame.draw.rect(window, "red", food) # draw the food rectangle on the window (red color)

    # draw the snake rectangles on the window (green color)
    for snake_part in snake:
         pygame.draw.rect(window, "green", snake_part)
    pygame.display.update() # update the display, refresh the screen
    clock.tick(10) # set the frame rate to 10 fps (frames per second)
