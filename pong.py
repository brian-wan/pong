import pygame
from paddle import Paddle
import gamefunctions
from ball import Ball
from pygame.sprite import Group
import sys

def run_game():
    #main game function
    pygame.init()
    running = -1
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Pong!")
    screen.fill((255,255,255))
    
    paddle_one = Paddle(screen, 50, 300)
    paddle_two = Paddle(screen, 750, 300)

    score_one = 0
    score_two = 0
   
    
    bb = Ball(screen)

    while running == -1:
        screen.fill((255,255,255))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 70)
        secondfont = pygame.font.SysFont('Comic Sans MS', 50)
        titlesurface = myfont.render('Welcome to Pong', False, (0, 0, 0))
        screen.blit(titlesurface,(200,200))
        Infosurface = secondfont.render('Use Up/Down and W/S to move the paddle', False,(0,0,0))
        Infoosurface = secondfont.render('Don\'t let your opponent score! ', False,(0,0,0))
        screen.blit(Infosurface,(100,400))
        screen.blit(Infoosurface,(200,500))
        clicksurface = secondfont.render('click any key to continue',False,(0,0,0))
        screen.blit(clicksurface,(200,600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                running += 1

    while running == 0:
        screen.fill((255, 255, 255))

        scorefont = pygame.font.SysFont('Comic Sans MS', 50)
        score_one_screen = scorefont.render(str(score_one), False, (0, 0, 0))
        screen.blit(score_one_screen,(100, 50))

        score_two_screen = scorefont.render(str(score_two), False, (0, 0, 0))
        screen.blit(score_two_screen,(700, 50))

        if gamefunctions.check_lose(bb) == 1:
            score_two += 1
            bb.reset_ball()
        elif gamefunctions.check_lose(bb) == 2:
            score_one += 1
            bb.reset_ball()

        if gamefunctions.check_win(score_one, score_two) == 1:
            running += 1
        elif gamefunctions.check_win(score_one, score_two) == 2:
            running += 2
        
        gamefunctions.check_events(paddle_one, paddle_two)
        bb.collided_left(paddle_one)
        bb.collided_right(paddle_two)
        paddle_one.update()
        paddle_one.move_paddle()
        paddle_two.update()
        paddle_two.move_paddle()
        bb.update()
        bb.draw_ball()
        
        pygame.display.update()

    while running == 1:
        screen.fill((255,255,255))
        winfont = pygame.font.SysFont('Comic Sans MS', 100)
        win_screen = scorefont.render("Player One Wins!", False, (0, 0, 0))
        screen.blit(win_screen,(300, 300))
        pygame.display.update()
        clicksurface = secondfont.render('click any key to play again',False,(0,0,0))
        screen.blit(clicksurface,(200,600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

    while running == 2:
        screen.fill((255,255,255))
        winfont = pygame.font.SysFont('Comic Sans MS', 100)
        win_screen = scorefont.render("Player Two Wins!", False, (0, 0, 0))
        screen.blit(win_screen,(300, 300))
        pygame.display.update()
        clicksurface = secondfont.render('click any key to play again',False,(0,0,0))
        screen.blit(clicksurface,(200,600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            


        
        

run_game()
