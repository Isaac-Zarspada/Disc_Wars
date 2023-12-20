import pygame as p, sys
import random as rand
from objects import Disc, Player
import os
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

WIDTH = int(os.getenv('WIDTH'))
HEIGHT = int(os.getenv('HEIGHT'))
BLACK =[0 ,0, 0]
WHITE = [255, 255, 255]
TICKSPEED = int(os.getenv('TICKSPEED'))
print(type(BLACK))

# Variables
player_speed = 0
opponent_speed = 0

orangedisc_speed_y = 7
orangedisc_speed_x = 7

# disc animation

p.init()
clock = p.time.Clock()
screen= p.display.set_mode((WIDTH,HEIGHT))

# Class Objects
bluedisc = Disc(7, 7, WIDTH-120, HEIGHT/2, 'Disc_Wars/assets/BlueTronRing_1.png', 'blue')
orangedisc = Disc(7, 7, 120, HEIGHT/2, 'Disc_Wars/assets/OrangeTronRing_1.png', 'orange')
blueplayer = Player(WIDTH- 50, HEIGHT/2, 0, 'blue', 'Disc_Wars/assets/BlueTronGuy_2.png')
orangeplayer = Player(120, HEIGHT/2, 0, 'orange','Disc_Wars/assets/TronGuyOrange_1.png')




while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    # player moveset
        print(f'y {blueplayer.y}, speed {blueplayer.speed}, HEIGHT {HEIGHT}, bottom_rect {blueplayer.rect.bottom}')
        if event.type == p.KEYDOWN:
            if event.key == p.K_DOWN:
                blueplayer.speed += 7
            if event.key == p.K_UP: 
               blueplayer.speed -= 7
        if event.type == p.KEYUP:
            if event.key == p.K_DOWN:
                blueplayer.y -= 7 
            if event.key == p.K_UP:
               blueplayer.y += 7
        # opponent moveset 
        if event.type == p.KEYDOWN:
            if event.key == p.K_s:
                orangeplayer.move('down') 
            if event.key == p.K_w: 
                orangeplayer.move('up')   
        if event.type == p.KEYUP:
            if event.key == p.K_s:
                orangeplayer.move('up')   
            if event.key == p.K_w:
                orangeplayer.move('down') 
            
    blueplayer.player_animation()
    orangeplayer.player_animation()
    bluedisc.disc_animation()
    orangedisc.disc_animation()

#visuals
    screen.fill(BLACK)
    bluedisc.display(screen)
    orangedisc.display(screen)
    orangeplayer.display(screen)
    blueplayer.display(screen)
        
    p.draw.aaline(screen,WHITE,start_pos=(WIDTH/2,0),end_pos=(WIDTH/2,HEIGHT))
    p.display.flip()
    clock.tick(TICKSPEED)