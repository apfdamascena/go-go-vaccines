import os
import pygame


class ObstacleAssets:

    BOX_OBSTACLE = os.path.join('assets', 'obstacles', 'box.png')

    def __init__(self):
        self.__box_obstacle = pygame.image.load(self.BOX_OBSTACLE)

    @property
    def box_obstacle(self):
        return self.__box_obstacle
