import pygame
import random
from animation_utils import ImageRegistry


class Enviroment:
    def __init__(self, destination, max_viruses=10):
        self.__layout = destination
        self.__max_viruses = max_viruses

        self.virus = ImageRegistry().load_images('data/asteroid_1_')
        self.bacterias = ImageRegistry().load_images('data/bacterias_1_')
        self.__nvirus = len(self.virus)
        self.__maxx = (self.__layout.get_rect().width -
                       self.virus[0].get_rect().width)
        self.__maxy = self.__layout.get_rect().height

        self.__viruses = []

    def __walkdown(self, surface, angle):
        original_rect = surface.get_rect()
        rotated_image = pygame.transform.rotate(surface, angle)
        rotated_rect = rotated_image.get_rect()
        clipped_rect = pygame.Rect(
            (rotated_rect.width - original_rect.width) / 2,
            (rotated_rect.height - original_rect.height) / 2,
            original_rect.width, original_rect.height)
        return rotated_image.subsurface(clipped_rect)

    def create_corona(self, x=None, vy=None):
        if len(self.__viruses) >= self.__max_viruses:
            return
        if x is None:
            x = random.randint(0, self.__maxx)
        if vy is None:
            vy = random.randint(1, 3)
        self.__viruses.append((random.randint(0, self.__nvirus - 1),
                               x, -100, vy, 1))

    def update(self, shots=None, player=None):
        destroy = []
        for a in range(len(self.__viruses)):
            ast = self.__viruses[a]
            if ast[-1] == 1:
                virus = self.virus
            else:
                virus = self.bacterias
            self.__layout.blit(virus[ast[0]], (ast[1], ast[2]))
            self.__viruses[a] = ((ast[0] + 1) % self.__nvirus,
                                 ast[1], ast[2] + ast[3], ast[3])
            if ast[2] > self.__maxy + 10:
                destroy.append(a)

            if shots is not None:
                ar = pygame.Rect(ast[1], ast[2],
                                 virus[ast[0]].get_rect().width,
                                 virus[ast[0]].get_rect().height)
                collision = ar.collidelist(shots.areas())
                if collision != -1:
                    destroy.append(a)
                    shots.destroy_shot(collision)

            # if player is not None:
            #     ar = pygame.Rect(ast[1], ast[2],
            #                      virus[ast[0]].get_rect().width,
            #                      virus[ast[0]].get_rect().height)
            #     collision = ar.collidelist(player.areas())
            #     if collision!= 1:
            #         destroy.append(a)
            #         player.destroy(collision)

        for a in destroy:
            del (self.__viruses[a])
