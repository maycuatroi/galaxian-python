import pygame

from Bullet import Bullet


class ShootBehavior:
    def __init__(self, layout, max_shots=10):
        self.__layout = layout

        self.shoot_sound = pygame.mixer.Sound('data/shoot.wav')

        self.__max_shots = max_shots
        self.__shots = []

    @property
    def can_shoot(self):
        return len(self.__shots) < self.__max_shots

    def create(self, position):
        if self.can_shoot:
            self.__shots.append(Bullet(self.__layout, position))
            self.shoot_sound.play()

    def destroy_shot(self, sid):
        if sid < len(self.__shots):
            del (self.__shots[sid])

    def get_bullet_areas(self):
        areas = []
        for bullet in self.__shots:
            areas.append(bullet.area)
        return areas

    def update(self):
        destroy = []
        for sid in range(len(self.__shots)):
            if self.__shots[sid].destroy:
                destroy.append(sid)
            else:
                self.__shots[sid].update()
        for d in destroy:
            del (self.__shots[d])
