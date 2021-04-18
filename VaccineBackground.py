import pygame
from Images import Images
from Constants import Constants

class VaccineBackground:

    def __init__(self):
        self.__images = Images()
        self.__top_city1 = BackgroundImage(self._images.top_city, 1, Constants.ZERO, Constants.WIDTH)

    def draw(self, window, axis_begin, axis_end):
        window.blit(self.__top_city1.image, self.__top_city1.image.get_rect())
        # window.blit(self.__images.stars, (axis_begin*Constants.SLOWING_STARS, 0))
        # window.blit(self.__images.stars, (axis_end*Constants.SLOWING_STARS, 0))
        # window.blit(self.__images.back_city, (axis_begin*Constants.SLOWING_BACK_CITY, 0))
        # window.blit(self.__images.bottom_city, (axis_begin, 0))
        # window.blit(self.__images.bottom_city, (axis_end, 0))

        pygame.display.update()
    
