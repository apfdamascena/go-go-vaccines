import pygame
import random
from obstacle.Box import Box
from obstacle.Boxes import Boxes


class Obstacles:
    def __init__(self):
        #self.__box = Box()
        self.__boxes = Boxes()

    def draw(self, window):
        options = ['box', 'boxes']
        choice = random.choice(options)

        if (choice == 'box'):
            self.__box.draw(window)
        else:
            self.__boxes.draw(window)
