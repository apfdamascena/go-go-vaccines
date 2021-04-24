import pygame
import random
from images.ObstacleAssets import ObstacleAssets
from constants.BackgroundConstants import BackgroundConstants
from constants.BoxConstants import BoxConstants


class Box:

    def __init__(self, axis_x):
        self.__images = ObstacleAssets()
        self.__mult = 1
        self.__axis_x, self.__saved_axis_x = axis_x, axis_x
        self.__axis_y = BoxConstants.AXIS_Y

    def draw(self, window):
        window.blit(self.__images.box_obstacle,
                    (self.__axis_x, self.__axis_y, 100, 100))
        # pygame.display.update()

    def move(self):
        self.__axis_x -= BackgroundConstants.VELOCITY * self.__mult

        if self.__axis_x < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            self.__axis_x = self.__saved_axis_x + random.randint(200, 900)

    @property
    def axis_x(self):
        return self.__axis_x

    @property
    def axis_y(self):
        return self.__axis_y
