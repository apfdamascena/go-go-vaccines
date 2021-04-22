import pygame
import random
from background.Images import Images
from constants.BackgroundConstants import BackgroundConstants


class Boxes:

    def __init__(self):
        self.__images = Images()
        self.__mult = 1
        self.__axis_begin = BackgroundConstants.WIDTH * 2

    def draw(self, window):
        window.blit(self.__images.boxes_obstacle,
                    (self.__axis_begin, 480, 100, 100))
        pygame.display.update()

    def move(self):
        self.__axis_begin -= BackgroundConstants.VELOCITY * self.__mult

        if self.__axis_begin < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            self.__axis_begin = BackgroundConstants.WIDTH + \
                random.randint(200, 900)
