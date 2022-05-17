import sys

from random import randint

import pygame
from pygame import K_UP, K_RIGHT, K_LEFT, K_DOWN
from colors import Color

pygame.init()

height = 800
width = 600

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Snake-game')
direction = K_RIGHT 
game_over = False

clock = pygame.time.Clock()

body = list()

steps = 10 
def switch(old, new):
    old[0] = new[0]
    old[1] = new[1]

def rand_x():
    global steps
    global height
    x_ = randint(0, height)
    return x_ - (x_ % steps)

def rand_y():
    global steps
    global width
    y_ = randint(0, width)
    return y_ - (y_ % steps)

def move_snake(key_pressed = None):
    global snake_head
    global body
    global steps

    if body:
        tam_corpo = len(body)
        if tam_corpo >= 2:
            i = 2
            for j in reversed(body):
                if (tam_corpo - i) == 0:
                    switch(j, body[0])
                    break

                switch(j, body[tam_corpo - i])
                i += 1

        switch(body[0], snake_head)

    if key_pressed == K_UP:
        snake_head[1] -= steps
    elif key_pressed == K_DOWN:
        snake_head[1] += steps
    elif key_pressed == K_LEFT:
        snake_head[0] -= steps
    elif key_pressed == K_RIGHT:
        snake_head[0] += steps

allowed_keys = [K_UP, K_RIGHT, K_LEFT, K_DOWN]

fruit = pygame.draw.rect(screen, Color.fruit_melon, (rand_x(), rand_y(), 10, 10))
snake_head = pygame.draw.rect(screen, Color.head, (400, 300, 10, 10))

while not game_over:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): 
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            pressed_key = event.key 
            if (pressed_key in allowed_keys):
                move_snake(pressed_key)
                direction = pressed_key

    move_snake(direction)

    # Verifica se não encostou/ultrapassou o limite da tela
    if snake_head.x < 0 or snake_head.y < 0 or snake_head.x >= 800 or snake_head.y >= 600:
        game_over = True
    
    if body:
        # Verifica se houve colisão com o próprio corpo
        if len(snake_head.collidelistall(body)) > 0:
            game_over = True
            break

        # desenha todos os componentes do corpo
        for i in body:
            pygame.draw.rect(screen, Color.body, i)

    # Verifica se houve colisão da cabeça com a fruta 
    if (fruit.colliderect(snake_head)):
        if not body:
            body.append(snake_head.move(-11, 0))
        else:
            body.append(tail.move(-11, 0))

        tail = body[-1]
        fruit.x = rand_x()
        fruit.y = rand_y()

    snake_head = pygame.draw.rect(screen, Color.head, snake_head)
    fruit = pygame.draw.rect(screen, Color.fruit_melon, fruit)
            
    clock.tick(15)
    pygame.display.flip()
    screen.fill(Color.bg_color)

pygame.quit()

