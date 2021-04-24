import os
import pygame

class ObstacleAssets:

    BOX_OBSTACLE = os.path.join('assets', 'obstacles', 'box.png')
    BOXES_OBSTACLE = os.path.join('assets', 'obstacles', 'box_on_top.png')

    def __init__(self):
        self.__box_obstacle = pygame.image.load(self.BOX_OBSTACLE)
        self.__boxes_obstacle = pygame.image.load(self.BOXES_OBSTACLE)

    @property
    def box_obstacle(self):
        return self.__box_obstacle

    @property
    def boxes_obstacle(self):
        return self.__boxes_obstacle