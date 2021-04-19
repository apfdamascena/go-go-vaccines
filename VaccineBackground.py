import pygame
from Images import Images
from constants.BackgroundConstants import BackgroundConstants
from BackgroundImage import BackgroundImage

class VaccineBackground:

    def __init__(self):
        self.__images = Images()
        self.__stars = BackgroundImage(self.__images.stars, BackgroundConstants.SLOWING_STARS)
        self.__back_buildings = BackgroundImage(self.__images.back_buildings, BackgroundConstants.SLOWING_BACK_BUILDINGS)
        self.__bottom_city = BackgroundImage(self.__images.bottom_city, 1)

    def draw(self, window):
        window.blit(self.__images.top_city, self.__images.top_city.get_rect())
        window.blit(self.__stars.image, (self.__stars.axis_begin, 0))
        window.blit(self.__stars.image, (self.__stars.axis_end, 0))
        window.blit(self.__images.moon, self.__images.moon.get_rect())
        window.blit(self.__back_buildings.image, (self.__back_buildings.axis_begin, 0))
        window.blit(self.__back_buildings.image, (self.__back_buildings.axis_end, 0))
        window.blit(self.__bottom_city.image, (self.__bottom_city.axis_begin, 0))
        window.blit(self.__bottom_city.image, (self.__bottom_city.axis_end, 0))
        # pygame.display.update()

    def move(self):
        self.__stars.move()
        self.__back_buildings.move()
        self.__bottom_city.move()

