import pygame
from Images import Images
from Constants import Constants


class VaccineBackground:

    def __init__(self):
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__images = Images()

    def draw(self, axis_begin, axis_end):
        self.__screen.blit(self.__images.top_city, self.__images.top_city.get_rect())
        self.__screen.blit(self.__images.stars, (axis_begin, 0))
        self.__screen.blit(self.__images.stars, (axis_end, 0))
        self.__screen.blit(self.__images.bottom_city, (axis_begin, 0))
        self.__screen.blit(self.__images.bottom_city, (axis_end, 0))
        pygame.display.update()


if __name__ == "__main__":
    axis_begin = Constants.ZERO
    axis_end = Constants.WIDTH
    while True:

        axis_begin -= Constants.VELOCITY
        axis_end -= Constants.VELOCITY

        if axis_begin < Constants.WIDTH * Constants.AXIS_ADJUSTMENT:
            axis_begin = Constants.WIDTH
        if axis_end < Constants.WIDTH * Constants.AXIS_ADJUSTMENT:
            axis_end = Constants.WIDTH

        VaccineBackground().draw(axis_begin, axis_end)
