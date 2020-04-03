from game.Config import MAX_STARS
import random
from animation_utils import ImageRegistry


class Space:
    def __init__(self, destination):
        self.__layout = destination

        self.__maxx = self.__layout.get_rect().width
        self.__maxy = self.__layout.get_rect().height

        self.bg = ImageRegistry().get_image('data/playground.png')

        self.stars_spr = []
        self.stars_spr.append((ImageRegistry().load_image('data/star1.png'),
                               6, 8))
        self.stars_spr.append((ImageRegistry().load_image('data/star2.png'),
                               3, 5))
        self.stars_spr.append((ImageRegistry().load_image('data/star3.png'),
                               1, 2))

        self.stars = []
        for i in range(MAX_STARS):
            star = random.choice(self.stars_spr)
            self.stars.append((random.randint(0, self.__maxx),
                               random.randint(0, self.__maxy),
                               random.randint(star[1], star[2]),
                               star[0]))

    def update(self):
        self.__layout.blit(self.bg, (0, 0))

        for i in range(MAX_STARS):
            if random.randint(0, 50) != 5 or self.stars[i][2] > 4:
                self.__layout.blit(self.stars[i][3],
                                   (self.stars[i][0], self.stars[i][1]))
            self.stars[i] = (self.stars[i][0],
                             self.stars[i][1] + self.stars[i][2],
                             self.stars[i][2],
                             self.stars[i][3])
            if self.stars[i][1] > (self.__maxy + 10):
                star = random.choice(self.stars_spr)
                self.stars[i] = (random.randint(0, self.__maxx), -5,
                                 random.randint(star[1], star[2]),
                                 star[0])
