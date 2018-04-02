# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:15:50 2018

@author: miguel
"""

import pygame, sys
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

DISPLAYSURF.fill(WHITE)

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.display.set_caption('Drawing')
while True:
    for event in pygame.event.get():
        print (event.type)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        pygame.display.update()