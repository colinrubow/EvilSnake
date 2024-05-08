import pygame
import numpy as np
import time
from fruit import Fruit
from avatar import Avatar
from snake import Snake


# pygame setup
pygame.init()
# the cartesian sensor only senses 1006 in x and 996 in y different values
width = 1500
height = 800
screen = pygame.display.set_mode((width, height))
running = True
score = 0

fruit = Fruit(height, width)
snakes = [Snake(height, width)]
avatar = Avatar(height, width)

while running:
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # quit
            if event.key == pygame.K_q:
                running = False
    
    screen.fill('gray')

    avatar.update_location()
    for snake in snakes:
        snake.update_locations()

    pygame.draw.circle(screen, avatar.color, avatar.location, avatar.radius)
    for snake in snakes:
        for loc in snake.locations:
            pygame.draw.circle(screen, snake.color, loc, snake.radius)
    pygame.draw.circle(screen, fruit.color, fruit.location, fruit.radius)

    # check for collisions
    for snake in snakes:
        for loc in snake.locations:
            if np.linalg.norm(loc - avatar.location) <= 5:
                running = False
    if np.linalg.norm(avatar.location - fruit.location) <= 7:
        # update score and fruit location and snake length
        score += 1
        if score % 10 == 0:
            for snake in snakes:
                snake.grow()
        fruit.update_location()
        snakes.append(Snake(height, width))

    pygame.display.flip()
    
print(score)