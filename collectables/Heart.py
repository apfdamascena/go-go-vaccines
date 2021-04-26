import pygame
from images.CollectablesAssets import CollectablesAssets
from constants.CollectablesConstants import CollectableConstants

class Heart:

    def __init__(self):
        self.__images = CollectablesAssets()
        self.__current_life = CollectableConstants.HEART_QUANTITY
        self.__x = CollectableConstants.X_HEART
        self.__y = CollectableConstants.Y_HEART

    def draw(self, window):
        for x in range(self.__current_life):
            window.blit(self.__images.heart, (self.__x+(x*62), self.__y, 100, 100))
        for x in range(CollectableConstants.HEART_QUANTITY-1, self.__current_life -1, -1):
            window.blit(self.__images.grey_heart, (self.__x+(x*62), self.__y, 100, 100))

    def lost_life(self):
        self.__current_life -= 1

    def win_life(self):
        if self.__current_life < 3:
            self.__current_life += 1

    def draw_collectable_heart(self, axis_x, axis_y):
        window.blit(self.__images.heart, (axis_x, axis_y, 100, 100))




