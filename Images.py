import os
import pygame


class Images:
    IMAGE_BOTTOM_CITY = os.path.join('assets', 'background', 'Background_layer_1.png')
    IMAGE_BACK_BUILDINGS = os.path.join('assets', 'background', 'Background_layer_2.png')
    STARS = os.path.join('assets', 'background', 'Stars.png')
    IMAGE_TOP_CITY = os.path.join('assets', 'background', 'Background_layer_3.png')
    MOON = os.path.join('assets', 'background', 'Moon.png')

    def __init__(self):
        self.__bottom_city = pygame.image.load(self.IMAGE_BOTTOM_CITY)
        self.__top_city = pygame.image.load(self.IMAGE_TOP_CITY)
        self.__starts = pygame.image.load(self.STARS)
        self.__back_buildings = pygame.image.load(self.IMAGE_BACK_BUILDINGS)
        self.__moon = pygame.image.load(self.MOON)
    @property
    def bottom_city(self):
        return self.__bottom_city

    @property
    def top_city(self):
        return self.__top_city

    @property
    def stars(self):
        return self.__starts

    @property
    def back_buildings(self):
        return self.__back_buildings

    @property
    def moon(self):
        return self.__moon