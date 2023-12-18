import pygame as p, sys
import random as rand


BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
ORANGE = (255,165,0)

TICKSPEED  = 60
WIDTH = 1200
HEIGHT = 800

def player_animation(player):
    player.y += player_speed   
    if player.top <= 0:
        player.top =0            
    if player.bottom >= HEIGHT:
        player.bottom =HEIGHT 

def opponent_animation(opponent):
    opponent.y += opponent_speed   
    if opponent.top <= 0:
        opponent.top =0            
    if opponent.bottom >= HEIGHT:
        opponent.bottom =HEIGHT                       


p.init()
clock = p.time.Clock()
screen= p.display.set_mode((WIDTH,HEIGHT))

#compnents
opponent = p.Rect(60,HEIGHT/2,70,130)
player = p.Rect(WIDTH-100, HEIGHT/2, 70,130)
orangedisc_surf = p.image.load('Disc_Wars/assets/OrangeTronRing_1.png').convert_alpha()
bluedisc_surf = p.image.load('Disc_Wars/assets/BlueTronRing_1.png').convert_alpha()

blueuser_surf = p.image.load('Disc_Wars/assets/BlueTronGuy_2.png').convert_alpha()
orangeuser_surf = p.image.load('Disc_Wars/assets/TronGuyOrange_1.png').convert_alpha()

orangedisc_rect = orangedisc_surf.get_rect(midbottom = (120,HEIGHT/2))
bluedisc_rect = bluedisc_surf.get_rect(midbottom = (WIDTH-120,HEIGHT/2))

blueuser_rect = blueuser_surf.get_rect(midbottom = (WIDTH -50, HEIGHT/2))
orangeuser_rect = orangeuser_surf.get_rect(midbottom = (120, HEIGHT/2))



# Variables
player_speed = 0
opponent_speed = 0

orangedisc_speed_y = 7
orangedisc_speed_x = 7

# disc animation
vectors = [7, 7]


    

# def disc_restart(disc, xspeed, yspeed, player):
#     disc.center = player.center
#     xspeed *= rand.choice ((1,-1))
#     yspeed *= rand.choice ((1,-1))
#     return xspeed, yspeed

# def disc_restart():
#     global orangedisc_speed_x, bluedisc_speed_x, orangedisc_speed_y, bluedisc_speed_y
#     orangedisc_speed_x *= rand.choice((1,-1))
#     orangedisc_speed_y*= rand.choice((1,-1))
#     bluedisc_speed_x*= rand.choice((1,-1))
#     bluedisc_speed_y*= rand.choice((1,-1))
#     bluedisc_rect.center = (WIDTH/2, HEIGHT/2)
#     orangedisc_rect.center = (WIDTH/2, HEIGHT/2)

        




    
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    # player moveset
        if event.type == p.KEYDOWN:
            if event.key == p.K_DOWN:
                player_speed += 7 
            if event.key == p.K_UP: 
                player_speed -= 7    
        if event.type == p.KEYUP:
            if event.key == p.K_DOWN:
                player_speed -= 7    
            if event.key == p.K_UP:
                player_speed += 7     
        # opponent moveset 
        if event.type == p.KEYDOWN:
            if event.key == p.K_s:
                opponent_speed += 7 
            if event.key == p.K_w: 
                opponent_speed -= 7    
        if event.type == p.KEYUP:
            if event.key == p.K_s:
                opponent_speed -= 7    
            if event.key == p.K_w:
                opponent_speed += 7     
            
    opponent_animation(orangeuser_rect)
    player_animation(blueuser_rect)
    disc_animation(bluedisc_rect)
                       
#visuals
    screen.fill(BLACK)
    screen.blit(orangedisc_surf,orangedisc_rect)
    screen.blit(bluedisc_surf,bluedisc_rect)
    screen.blit(orangeuser_surf,orangeuser_rect)
    screen.blit(blueuser_surf,blueuser_rect)
   
    p.draw.aaline(screen,WHITE,start_pos=(WIDTH/2,0),end_pos=(WIDTH/2,HEIGHT))
    











    p.display.flip()
    clock.tick(TICKSPEED)

    




