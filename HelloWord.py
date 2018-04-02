# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:32:00 2018

@author: miguel
"""

import pygame, sys 
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()