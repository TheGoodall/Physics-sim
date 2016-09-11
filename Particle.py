#   The Main class for all particles
from random import randint
import pygame
import threading
#Particle Management
particles_list = []
def update(screen):
    for particle in particles_list:
        if not particle.on_screen([1920/5,1080/5]):
            particles_list.remove(particle)
        
        else:
            for other_particle in particles_list:
                if (particle.coords == other_particle.coords) and (particle != other_particle):
                    particles_list.remove(other_particle)
            threading.Thread(target =particle.handle_gravity())
            particle.render(screen)



particle_types = {"Sand":["powder", [245, 205, 162]],
                  "Water":["liquid",[0, 0, 255]],
                  "Stone":["solid",[150, 150, 150]]}

def wipe():
    for i in range(len(particles_list)):
        particles_list.pop()
def add_particle(Playing, selected):
        
        if pygame.mouse.get_pressed()[0] == True:
            click = [Particleob([int(pygame.mouse.get_pos()[0]/5),int(pygame.mouse.get_pos()[1]/5), [245, 205, 162]], "Sand")]
        if pygame.mouse.get_pressed()[1] == True:
            click = [Particleob([int(pygame.mouse.get_pos()[0]/5),int(pygame.mouse.get_pos()[1]/5), [245, 205, 162]], "Water")]
        if pygame.mouse.get_pressed()[2] == True:
            click = [Particleob([int(pygame.mouse.get_pos()[0]/5),int(pygame.mouse.get_pos()[1]/5), [245, 205, 162]], "Stone")]


class Particleob(object):
    def __init__(self, coords, type):
        
        self.coords = coords

        self.temperature = 22
        self.colour = particle_types[type][1]
        self.particle_class = particle_types[type][0]
        particles_list.append(self)
        

        

    def get_temp(self):
        return self.temperature


    def on_screen(self, screen_size):
        if self.coords[0] < 0 or self.coords[0] > screen_size[0]:
            return False
        elif self.coords[1] < 0 or self.coords[1] > screen_size[1]:
            return False
        else:
            return True
    def render(self, screen):
        pygame.draw.rect(screen,self.colour,(self.coords[0]*5, self.coords[1]*5, 5, 5))








    def handle_gravity(self):
        surr_parts = self.surrounding_particles()

        if self.particle_class == "powder":

            if surr_parts[6] == False:
                self.coords[1] += 1
            elif randint(1,2) == 1:
                if surr_parts[5] == False:
                    self.coords[0], self.coords[1] = self.coords[0] -1, self.coords[1] +1
                elif surr_parts[7] == False:
                    self.coords[0], self.coords[1] = self.coords[0] +1, self.coords[1] +1
            else:
                if surr_parts[7] == False:
                    self.coords[0], self.coords[1] = self.coords[0] +1, self.coords[1] +1
                elif surr_parts[5] == False:
                    self.coords[0], self.coords[1] = self.coords[0] -1, self.coords[1] +1

        elif self.particle_class == "liquid":

            if surr_parts[6] == False:
                self.coords[1] += 1
            elif randint(1,2) == 1:
                if surr_parts[5] == False:
                    self.coords[0], self.coords[1] = self.coords[0] -1, self.coords[1] +1
                elif surr_parts[7] == False:
                    self.coords[0], self.coords[1] = self.coords[0] +1, self.coords[1] +1
                else:
                    if surr_parts[3] == False:
                        self.coords[0], self.coords[1] = self.coords[0] -1, self.coords[1]
                    elif surr_parts[4] == False:
                        self.coords[0], self.coords[1] = self.coords[0] +1, self.coords[1]

            else:
                if surr_parts[7] == False:
                    self.coords[0], self.coords[1] = self.coords[0] +1, self.coords[1] +1
                elif surr_parts[5] == False:
                    self.coords[0], self.coords[1] = self.coords[0] -1, self.coords[1] +1
                else:
                    if surr_parts[4] == False:
                        self.coords[0], self.coords[1] = self.coords[0] +1, self.coords[1]
                    elif surr_parts[3] == False:
                        self.coords[0], self.coords[1] = self.coords[0] -1, self.coords[1]
        elif self.particle_class == "solid":
            pass
        elif self.particle_class == "gas":
            pass

    



    def surrounding_particles(self):

        #   [0] top left
        #   [1] top middle
        #   [2] top right
        #   [3] middle left
        #   [4] middle right
        #   [5] bottom left
        #   [6] bottom middle
        #   [7] bottom right

        positions = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
        positions_instances_bool = []

        for coordinate in positions:

            instances = [particle for particle in particles_list if (particle.coords[0]==self.coords[0]+coordinate[0] and particle.coords[1]==self.coords[1]+coordinate[1])]
            if instances == []:
                positions_instances_bool.append(False)
            else:
                positions_instances_bool.append(True)
        return positions_instances_bool



        






