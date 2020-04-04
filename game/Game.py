import pygame
import random

import Player
from Config import GAME_FPS
from ShootBehavior import ShootBehavior
from PlayGround import PlayGround
from animation_utils import ImageRegistry
from game.EnemyController import EnemyController



class Game:
    def __init__(self, screen):

        self.__clock = pygame.time.Clock()

        self.__scr = screen.surface

        self.__playground = ImageRegistry().load_image('data/playground.png')
        self.__scr.blit(ImageRegistry().load_image('data/background.png'),
                        (0, 0))

        self.playground = PlayGround(self.__playground)
        self.pshots = ShootBehavior(self.__playground, 10)
        self.player = Player.Doctor(self.__playground,
                                    self.pshots.create)
        self.enemycontroller = EnemyController(self.__playground)

    def run(self):

        while 1:

            self.__clock.tick(GAME_FPS)

            if random.randint(1, 20) == 3:
                self.enemycontroller.spaw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif (event.type == pygame.KEYDOWN and
                      event.key == pygame.K_ESCAPE):
                    return
                elif (event.type == pygame.KEYDOWN and
                      event.key == pygame.K_LEFT):
                    self.player.go_left()
                elif (event.type == pygame.KEYDOWN and
                      event.key == pygame.K_RIGHT):
                    self.player.go_right()
                elif ((event.type == pygame.KEYUP) and
                      (event.key == pygame.K_LEFT)):
                    self.player.no_left()
                elif ((event.type == pygame.KEYUP) and
                      (event.key == pygame.K_RIGHT)):
                    self.player.no_right()
                elif (event.type == pygame.KEYDOWN and
                      event.key == pygame.K_SPACE) and self.pshots.can_shoot:
                    self.player.shoot()

            # Draw everything
            self.playground.update()
            self.pshots.update()
            self.enemycontroller.update(self.pshots,self.player)
            self.player.update()

            self.__scr.blit(self.__playground, (150, 0))
            pygame.display.flip()
