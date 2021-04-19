import pygame
from Images import Images


class VaccineBackground:

    def __init__(self):
        self.__images = Images()

    def draw(self, window, axis_begin, axis_end):
        window.blit(self.__images.top_city, self.__images.top_city.get_rect())
        window.blit(self.__images.stars, (axis_begin, 0))
        window.blit(self.__images.stars, (axis_end, 0))
        window.blit(self.__images.bottom_city, (axis_begin, 0))
        window.blit(self.__images.bottom_city, (axis_end, 0))
        # pygame.display.update()
