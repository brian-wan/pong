import sys
import pygame
from paddle import Paddle


def check_keydown_events(event, paddle_one, paddle_two):
   
    if event.key == pygame.K_UP:
        paddle_two.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle_two.moving_down = True

    if event.key == pygame.K_w:
        paddle_one.moving_up = True
    elif event.key == pygame.K_s:
        paddle_one.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, paddle_one, paddle_two):
    if event.key == pygame.K_UP:
        paddle_two.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle_two.moving_down = False

    if event.key == pygame.K_w:
        paddle_one.moving_up = False
    elif event.key == pygame.K_s:
        paddle_one.moving_down = False



def check_events(paddle_one, paddle_two):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_one, paddle_two)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_one, paddle_two)


def check_lose(bb):
        if bb.x < 30:
            return 1
        elif bb.x > 780:
            return 2

def check_win(score_one, score_two):
    if score_one == 7:
        return 1
    if score_two == 7:
        return 2
        
