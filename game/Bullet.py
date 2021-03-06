#!/usr/bin/env python


import pygame
from animation_utils import ImageRegistry

class Bullet(object):
    def __init__(self, layout, position):
        self.__layout = layout
        self.position = position

        self.__images = ImageRegistry().load_images('data/shoot_')


        self.__sw = self.__images[0].get_rect().width
        self.__sh = self.__images[0].get_rect().height

        self.__current = 0
        self.__f_size = len(self.__images)
        self.__destroy = False

    @property
    def destroy(self):
        return self.__destroy

    @property
    def area(self):
        return pygame.Rect(self.position[0], self.position[1],
                           self.__sw, self.__sh)
    def update(self):
        if self.position[1] < -self.__sh:
            self.__destroy = True
        else:
            self.__layout.blit(self.__images[self.__current],
                               self.position)
            self.position = (self.position[0],
                             self.position[1] - 9)
            self.__current += 1
            if self.__current == self.__f_size:
                self.__current = 0

