
######################################################################################
#
#       James's Physics Particle Sim
#       Prototype Mk 1
#
#####################################################################################

#Importing External Modules
import sys, pygame, threading
from pygame.locals import *


#Importing Internal Modules

import Particle
from Particle import *

#Initialising Pygame Objects
pygame.init()
screen = pygame.display.set_mode([1920,1080],pygame.FULLSCREEN)
Clock = pygame.time.Clock()
pygame.display.set_caption("Physics Sim Prototype Mk1")




bottomwall = [Particleob([i,50], "Stone") for i in range(15,25)]

#Event Handling



def handle(selected):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                Particle.wipe()


    add_particle(Playing,selected)
    update(screen)



selected = "Water"
font = pygame.font.Font(None, 36)

Playing = True




while Playing:
    screen.fill([0,0,0])
    Clock.tick(60)
    handle(selected)



    #Graphics Printing


    pygame.display.update()




