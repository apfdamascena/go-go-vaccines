import pygame
from Images import Images


class Player:

    def __init__(self):
        self.__images = Images()

    def draw(self, window, axis_x, axis_y):
        window.blit(self.__images.main_character, (axis_x, axis_y, 100, 100))
        pygame.display.update()

    def move(self, axis_x, axis_y):
        axis_x = axis_x
        axis_y = axis_y

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    axis_x += 15

                if event.key == pygame.K_LEFT:
                    axis_x -= 15

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            axis_x += 15

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            axis_x -= 15

        return axis_x, axis_y
