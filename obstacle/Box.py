import pygame
import random
from images.ObstacleAssets import ObstacleAssets
from constants.BackgroundConstants import BackgroundConstants


class Box:

    def __init__(self):
        self.__images = ObstacleAssets()
        self.__mult = 1
        self.__axis_begin = 900
        self.__axis_y =  580

    def draw(self, window):
        window.blit(self.__images.box_obstacle,
                    (self.__axis_begin, 580, 100, 100))           
        #pygame.display.update()

    def move(self):
        self.__axis_begin -= BackgroundConstants.VELOCITY * self.__mult

        if self.__axis_begin < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            self.__axis_begin = 900 + random.randint(200, 900)

    @property
    def axis_x(self):
        return self.__axis_begin
    
    @property
    def axis_y(self):
        return self.__axis_y
