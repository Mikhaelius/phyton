import pygame
from pygame.locals import *
import random
import os
import math
import sys
from pathlib import Path


#https://happycoding.io/tutorials/processing/collision-detection#circle-point-collision
#https://coolors.co/000000-3d2645-832161-da4167-f0eff4
#https://coderslegacy.com/python/python-pygame-tutorial/
#https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection

#WindiowOptions
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,600))
WindowColor = color3 = pygame.Color(61, 38, 69) 
RedColor = color3 = pygame.Color(218, 65, 103)
WhiteColor = color3 = pygame.Color(240, 39, 244)
print (os.path.dirname(__file__))
parent = Path(__file__).parent
TargetTexture = pygame.image.load(os.path.join(parent, 'target.png'))
DISPLAYSURF.fill(WindowColor)
pygame.display.set_caption("SlickAmingLab")
font = pygame.font.SysFont('Consolas', 30)
drawtarget = True

#FPSFestlegen
FPS = 30
FramePerSec = pygame.time.Clock()

#Clock
start_ticks=pygame.time.get_ticks()
clocktime = 0.0
clockactive = True

#Score
showscore = False
score = 0

#CalssesDefintions
class TargetSpawn(pygame.sprite.Sprite):
    def __init__(self, Texture, TargetNumber, TargetCords):
        self.texture = Texture
        self.coords = TargetCords
        #self.hitbox = pygame.Surface((50, 100))
        #self.box = self.hitbox.get_rect()
        self.radius = 21
    
    def draw(self, surface):
        surface.blit(self.texture, self.coords)
    
    def __del__(self): 
        print("Object was deleted.")

#target spawn
t1 = TargetSpawn(TargetTexture, 1, (300,255))

#Game loop begins
while True:
    pygame.display.update()
    
    #eventChecker
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #check for mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #format mouse click
            mx, my = pygame.mouse.get_pos()
            #format target coords
            tx, ty = t1.coords
            #calulate distance between target and mouse
            dist = math.hypot(tx+20-mx, ty+20-my)
            print(dist)
            #check if hit target and spawn new target
            if dist <= t1.radius:
                print("clicked")
                t1.coords = (random.randrange(1, 560, 1), random.randrange(1, 560, 1))
                score = score + 1
                print (score)

    #timer
    if clockactive:
        clocktime=25 - (pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if clocktime<0: # if less then 0 end game and show score
            print(str(clocktime))
            clockactive = False
            clocktime = "Time is up"
            scoredisplay = font.render("Score:" + str(score), False, RedColor)
            showscore = True
            drawtarget = False
            
    #update screen
    DISPLAYSURF.fill(WindowColor)
    if  drawtarget:
        t1.draw(DISPLAYSURF)
    textsurface = font.render(str(clocktime), False, RedColor)
    DISPLAYSURF.blit(textsurface,(0,0))
    if showscore:
        DISPLAYSURF.blit(scoredisplay,(440,0))
    FramePerSec.tick(FPS)