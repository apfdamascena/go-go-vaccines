import pygame
from images.BackgroundAssets import BackgroundAssets
from background.BackgroundImage import BackgroundImage


class BlackBackground:

    def __init__(self):
        self.__images = BackgroundAssets()
        self.__black = BackgroundImage(self.__images.black_background, 1)

    def draw(self, window):
        window.blit(self.__black.image, (0, 0))
