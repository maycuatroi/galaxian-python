#!/usr/bin/env python

import os
import os.path
import sys

import pygame

from Game import Game
from animation_utils import Screen, ImageRegistry

sys.path.append('game')
sys.path.append(os.getcwd())

if __name__ == '__main__':
    pygame.init()
    screen = Screen(windowed=('-win' in sys.argv),
                                caption='Corona wars zone')

    # Load all images
    ImageRegistry().load_image('data/background.png')
    ImageRegistry().load_image('data/playground.png')
    ImageRegistry().load_image('data/shoot.png')
    ImageRegistry().load_images('data/shoot_')
    ImageRegistry().load_image('data/ship.png')
    ImageRegistry().load_images('data/ship_left_')
    ImageRegistry().load_images('data/ship_right_')
    ImageRegistry().load_images('data/ship_shoot_')
    ImageRegistry().load_images('data/ship_shoot_left_')
    ImageRegistry().load_images('data/ship_shoot_right_')
    ImageRegistry().load_images('data/asteroid_1_')
    ImageRegistry().load_image('data/star1.png')
    ImageRegistry().load_image('data/star2.png')
    ImageRegistry().load_image('data/star3.png')

    main_game = Game(screen)
    main_game.run()
