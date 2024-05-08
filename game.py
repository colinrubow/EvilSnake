import pygame
import time
from fruit import Fruit
from avatar import Avatar
from snake import Snake


# pygame setup
pygame.init()
width=1023
height=1023
character_radius = 5
screen = pygame.display.set_mode((width, height))
running = True
score = 0

fruit = Fruit(height, width)
snake = Snake(height, width)
avatar = Avatar(height, width)

while running:
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('gray')

    avatar.update_location()
    snake.update_locations()

    pygame.draw.circle(screen, avatar.color, avatar.location, character_radius)
    # for loc in snake.locations:
    #     pygame.draw.circle(screen, snake.color, loc, character_radius)
    pygame.draw.circle(screen, fruit.color, fruit.location, character_radius)

    # check for collisions
    if avatar.location in snake.locations:
        # lost the game
        running = False
    if avatar.location == fruit.location:
        # update score and fruit location and snake length
        score += 1
        fruit.update_location()
        snake.grow()

    pygame.display.flip()
print(score)