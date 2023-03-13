#!/usr/bin/env python3

import random, pygame
from pygame.locals import *
from sys import exit

pygame.init()
#initialization^
pygame.display.set_caption('dog_ball')
#display name^
clock = pygame.time.Clock()
#clock
color = '#6ec270'
display = pygame.display.set_mode((600,700))
dog = pygame.draw.rect(display,'brown',(0,0,50,50))
#ball = pygame.Surface((50,50))
#ball.fill('#eb4034')
w = 300
h = 350
#sprites and sprite colors
#starting location
left = 0
right = 0
up = 0
down = 0
#default movement 
while True:
    if left:
        w += 1
    elif right:
        w -= 1
    elif up:
        h -= 1
    elif down:
        h += 1
    display.fill(color)
    #display.blit(ball, (0,0))
    for event in pygame.event.get():#get all the events in pygame
        if event.type == pygame.QUIT:#when they quit, the game closes and exits
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:#press any key
            if event.key == pygame.K_LEFT:#when the press the left, right, up, and down arrow move in the aforementioned directions
                pygame.Rect.move(1, 1)
            if event.key == pygame.K_RIGHT:
                right = 0
                left = 1
            if event.key == pygame.K_UP:
                up = 1
                down = 0
            if event.key == pygame.K_DOWN:
                down = 1
                up = 0
        if event.type == pygame.KEYUP:#when not pressing key, dont move
            left = 0
            right = 0
            down = 0
            up = 0
        

    pygame.display.update()
    clock.tick(180)
 