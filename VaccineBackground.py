import pygame
from Images import Images
from Constants import Constants
from BackgroundImage import BackgroundImage

class VaccineBackground:

    def __init__(self):
        self.__images = Images()
        self.__top_city1 = BackgroundImage(self.__images.top_city, 1, Constants.ZERO, Constants.WIDTH)
        self.__stars = BackgroundImage(self.__images.stars, Constants.SLOWING_STARS, Constants.ZERO, Constants.WIDTH)

    def draw(self, window):
        window.blit(self.__top_city1.image, self.__top_city1.image.get_rect())
        window.blit(self.__stars.image, (self.__stars.axis_begin, 0))
        window.blit(self.__stars.image, (self.__stars.axis_end, 0))
        self.__stars.move()
        # window.blit(self.__images.back_city, (axis_begin*Constants.SLOWING_BACK_CITY, 0))
        # window.blit(self.__images.bottom_city, (axis_begin, 0))
        # window.blit(self.__images.bottom_city, (axis_end, 0))
        pygame.display.update()
