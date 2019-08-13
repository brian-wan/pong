
import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):

    def __init__(self, screen, x, y):
        self.screen = screen
        self.speed = 25
        self.height = 100
        self.width = 10
        self.color = (0,0,0)

        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        

        self.moving_up = False
        self.moving_down = False

        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
    def update(self):
        
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= self.speed 

        if self.moving_down and self.rect.y < 700:
            self.rect.y += self.speed
            
        
        
    def move_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)        
       

         
