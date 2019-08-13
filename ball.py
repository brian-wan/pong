import pygame
from pygame.sprite import Sprite
from random import randrange
from random import randint

class Ball(Sprite):

    def __init__(self, screen):
        self.screen = screen
        self.x = 400
        self.y = 400
        self.r = 10
        self.color = (0,0,0)

        self.xspeed = -3
        self.yspeed = 3

        self.multiplier = 1.1

        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        
    def update(self):
       

        if self.y < 10 or self.y > 790:
            self.yspeed *= -1

        self.x += self.xspeed
        self.y += self.yspeed
        
    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def collided_left(self, paddle):
        if self.x < 70 and -30 < self.y - paddle.rect.y < 115:
            self.xspeed *= -1

    def collided_right(self, paddle):
        if self.x > 740 and -30 < self.y - paddle.rect.y < 115:
            self.xspeed *= -1

    def reset_ball(self):
        self.x = 400
        self.y = 400
        randx = randrange(-1,2,2)
        randy = randrange(-1,2,2)
        
        
        self.xspeed *= randx
        self.yspeed *= randy

        if self.xspeed < 0 and self.xspeed > -7:
            self.xspeed -= 1
        elif self.xspeed > 0 and self.xspeed < 7:
            self.xspeed += 1

        if self.yspeed < 0 and self.yspeed > -7:
            self.yspeed -= 1
        elif self.yspeed > 0 and self.yspeed < 7:
            self.yspeed += 1

        
