import pygame, os
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
WIDTH = int(os.getenv('WIDTH'))
HEIGHT = int(os.getenv('HEIGHT'))

velocityx_y = [7, 7]

class Disc: 
    def __init__(self,speedx, speedy, positionx, positiony,surf_image, color):
        self.color = color
        self.x = positionx
        self.y = positiony
        self.speedx = speedx
        self.speedy = speedy
        self.surf = pygame.image.load(f'{surf_image}').convert_alpha()
        self.rect = self.surf.get_rect(midbottom = (positionx,positiony))
        self.top = self.rect.top
        self.bottom = self.rect.bottom
        self.left = self.rect.left
        self.right = self.rect.right



    def disc_animation(self):
        global velocityx_y
        self.x += velocityx_y[0]
        self.y += velocityx_y[1]

        if self.top <= 0 or self.bottom >= HEIGHT:
            velocityx_y[1] *= -1
        if self.left <= 0 or self.right >= WIDTH:
            velocityx_y[0] *= -1

    def display(self, screen):
        screen.blit(self.surf,self.rect)
    
# Player animation
class Player:
    
    def __init__(self, positionx, positiony, speed, color, surf_image ):
        self.color = color
        self.speed = speed
        self.y = positiony
        self.x = positionx
        self.surf = pygame.image.load(f'{surf_image}').convert_alpha()
        self.rect = self.surf.get_rect(midbottom = (self.x, self.y))
        self.top = self.rect.top
        self.bottom = self.rect.bottom

    def display(self, screen):
        screen.blit(self.surf,self.rect)   

    def player_animation(self):
        self.rect.y += self.speed 
        if self.rect.top <= 0:
            self.rect.top =0            
        if self.rect.bottom >=HEIGHT:
            self.rect.bottom =HEIGHT 
