import os
import pygame

class BackgroundAssets:

    __IMAGE_BOTTOM_CITY = os.path.join('assets', 'background', 'Background_layer_1.png')
    __IMAGE_BACK_BUILDINGS = os.path.join('assets', 'background', 'Background_layer_2.png')
    __STARS = os.path.join('assets', 'background', 'Stars.png')
    __IMAGE_TOP_CITY = os.path.join('assets', 'background', 'Background_layer_3.png')
    __MOON = os.path.join('assets', 'background', 'Moon.png')

    def __init__(self):
        self.__bottom_city = pygame.image.load(self.__IMAGE_BOTTOM_CITY)
        self.__top_city = pygame.image.load(self.__IMAGE_TOP_CITY)
        self.__starts = pygame.image.load(self.__STARS)
        self.__back_buildings = pygame.image.load(self.__IMAGE_BACK_BUILDINGS)
        self.__moon = pygame.image.load(self.__MOON)

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