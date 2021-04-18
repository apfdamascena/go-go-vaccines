import os
import pygame


class Images:

    IMAGE_BOTTOM_CITY = os.path.join('assets', 'background', 'Background_camada1.png')
    IMAGE_BACK_CITY = os.path.join('assets', 'background', 'Background_camada2.png')
    STARS = os.path.join('assets', 'background', 'stars.png')
    IMAGE_TOP_CITY = os.path.join('assets', 'background', 'top_background_without_stars.png')

    def __init__(self):
        self.__bottom_city = pygame.image.load(self.IMAGE_BOTTOM_CITY)
        self.__top_city = pygame.image.load(self.IMAGE_TOP_CITY)
        self.__starts = pygame.image.load(self.STARS)
        self.__back_city = pygame.image.load(self.IMAGE_BACK_CITY)

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
    def back_city(self):
        return self.__back_city
