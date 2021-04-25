import pygame
from images.CollectablesAssets import CollectablesAssets
from constants.CollectablesConstants import CollectableConstants
from constants.BackgroundConstants import BackgroundConstants
import time

class IndependentHeart:

    def __init__(self):
        self.__images = CollectablesAssets()
        self.__spawn_time = time.time()
        self.__spawn = False
        self.__colided = False
        self.__axis_x, self.__axis_y = CollectableConstants.INITIAL_X, CollectableConstants.INITIAL_Y 

    def draw(self, window):
        self.organize_spawn()
        if self.__spawn:
            window.blit(self.__images.heart, (self.__axis_x, self.__axis_y, 100, 100))
            self.move()
    
    def organize_spawn(self):
        current_time = time.time()
        if self.__spawn <= current_time - CollectableConstants.SPAWN_TIME:
            self.__spawn = True
            self.__spawn = current_time
    
    def move(self):
        self.__axis_x -= BackgroundConstants.VELOCITY
        if self.__axis_x <= 0 or self.__colided:
            self.__spawn = True
            self.__axis_x = CollectableConstants.INITIAL_X
            self.__axis_y = CollectableConstants.INITIAL_Y 
            self.__colided = False

    def colided(self):
        self.__colided = True

    @property
    def axis_x(self):
        return self.__axis_x

    @property
    def axis_y(self):
        return self.__axis_y






