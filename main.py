#!/usr/bin/env python3

from ast import Delete
import random, pygame
from pygame.locals import *
from sys import exit

pygame.init()
clock = pygame.time.Clock()
screenwidth, screenheight = 600, 700
display = pygame.display.set_mode((screenwidth, screenheight))
grass = '#4ddb73'

dogimage = pygame.image.load("dog.png")
dog2image = pygame.image.load("dog2.0.png")
ballimage = pygame.image.load("ball.png")
rectcolor = (255, 255, 255, 100)
rect_width, rect_height = 149, 146
recta = pygame.Rect((screenwidth/2 - rect_width/2),(screenheight/2 - rect_height/2), rect_height,rect_width)
rectb = pygame.Rect((screenwidth/2 - rect_width/2 + 100),(screenheight/2 - rect_height/2 + 100), rect_height,rect_width)
recta.x = (screenwidth/2 - rect_width/2)
recta.y = (screenheight/2 - rect_height/2)
rectb.x = (screenwidth/2 - rect_width/2 +100)
rectb.y = (screenheight/2 - rect_height/2 + 100)
ball = pygame.Rect(200, 233, 47, 49)
ball.x = 233
ball.y = 200
move_speed = 20
leftboarder = pygame.Rect(-10, 0, 10, 700)
rightboarder = pygame.Rect(600, 0, 10, 700)
topboarder = pygame.Rect(0, -10, 600, 10)
bottomboarder = pygame.Rect(0, 700, 600, 10)
font = pygame.font.Font(None, 36)
count = 0
count2 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #move with key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                recta.x += move_speed
            if event.key == pygame.K_LEFT:
                recta.x -= move_speed
            if event.key == pygame.K_DOWN:
                recta.y += move_speed
            if event.key == pygame.K_UP:
                recta.y -= move_speed 
            if event.key == pygame.K_d:
                rectb.x += move_speed
            if event.key == pygame.K_a:
                rectb.x -= move_speed
            if event.key == pygame.K_s:
                rectb.y += move_speed
            if event.key == pygame.K_w:
                rectb.y -= move_speed 
            #collide with boarder
            if recta.colliderect(leftboarder):
                move_speed = 0
                recta.x = recta.x + 20
                move_speed = 20
            if recta.colliderect(rightboarder):
                move_speed = 0
                recta.x = recta.x - 20
                move_speed = 20
            if recta.colliderect(topboarder):
                move_speed = 0
                recta.y = recta.y + 20
                move_speed = 20
            if recta.colliderect(bottomboarder):
                move_speed = 0
                recta.y = recta.y - 20
                move_speed = 20
            if rectb.colliderect(leftboarder):
                move_speed = 0
                rectb.x = rectb.x + 20
                move_speed = 20
            if rectb.colliderect(rightboarder):
                move_speed = 0
                rectb.x = rectb.x - 20
                move_speed = 20
            if rectb.colliderect(topboarder):
                move_speed = 0
                rectb.y = rectb.y + 20
                move_speed = 20
            if rectb.colliderect(bottomboarder):
                move_speed = 0
                rectb.y = rectb.y - 20
                move_speed = 20
            #collide with ball
            if recta.colliderect(ball):
                count += 1
            if recta.colliderect(ball):
                ball.x = (0 + random.randint(0, 550))
                ball.y = (0 + random.randint(0,650))
            if rectb.colliderect(ball):
                count2 += 1
            if rectb.colliderect(ball):
                ball.x = (0 + random.randint(0, 550))
                ball.y = (0 + random.randint(0,650))

            
    display.fill((grass))
    pygame.draw.rect(display, (grass), recta)
    pygame.draw.rect(display, (grass), rectb)
    pygame.draw.rect(display, (grass), ball)
    pygame.draw.rect(display, ('black'), leftboarder)
    pygame.draw.rect(display, ('black'), rightboarder)
    pygame.draw.rect(display, ('black'), topboarder)
    pygame.draw.rect(display, ('black'), bottomboarder)
    display.blit(dogimage, recta)
    display.blit(ballimage, ball)
    display.blit(dog2image, rectb)
    text_surface = font.render("brown dog score: {}".format(count), True, ('black'))
    text_surface2 = font.render("white dog score: {}".format(count2), True, ('white'))
    display.blit(text_surface, (0, 0))
    display.blit(text_surface2, (375, 0))
    clock.tick(60)
    pygame.display.update() 
 