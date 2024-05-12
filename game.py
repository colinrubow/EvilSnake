import pygame
import numpy as np
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
color = pygame.Color(185, 121, 99, 255)
pressed_keys = []

while running:
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # quit
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_UP:
                pressed_keys.append(pygame.K_UP)
                avatar.update_location(0)
            elif event.key == pygame.K_RIGHT:
                pressed_keys.append(pygame.K_RIGHT)
                avatar.update_location(1)
            elif event.key == pygame.K_DOWN:
                pressed_keys.append(pygame.K_DOWN)
                avatar.update_location(2)
            elif event.key == pygame.K_LEFT:
                pressed_keys.append(pygame.K_LEFT)
                avatar.update_location(3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_keys.remove(pygame.K_UP)
            elif event.key == pygame.K_RIGHT:
                pressed_keys.remove(pygame.K_RIGHT)
            elif event.key ==  pygame.K_DOWN:
                pressed_keys.remove(pygame.K_DOWN)
            elif event.key == pygame.K_LEFT:
                pressed_keys.remove(pygame.K_LEFT)
    if pygame.K_UP in pressed_keys:
        avatar.update_location(0)
    if pygame.K_RIGHT in pressed_keys:
        avatar.update_location(1)
    if pygame.K_DOWN in pressed_keys:
        avatar.update_location(2)
    if pygame.K_LEFT in pressed_keys:
        avatar.update_location(3)
    
    screen.fill(color)

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
    if np.linalg.norm(avatar.location - fruit.location) <= 10:
        # update score and fruit location and snake length
        score += 1
        if score % 10 == 0:
            for snake in snakes:
                snake.grow()
        fruit.update_location()
        snakes.append(Snake(height, width))

    pygame.display.flip()
    
print(score)