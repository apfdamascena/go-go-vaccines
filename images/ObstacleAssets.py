import os
import pygame

class ObstacleAssets:

    __OBSTACLE = os.path.join('assets', 'obstacles', 'box.png')

    def __init__(self):
        self.__obstacle = pygame.image.load(self.__OBSTACLE)

    @property
    def obstacle(self):
        return self.__obstacle