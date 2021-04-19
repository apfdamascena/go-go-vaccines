import pygame
from Images import Images


class Player:

    def __init__(self):
        self.__images = Images()

    def draw(self, window, x, y):
        window.blit(self.__images.main_character, (x, y, 100, 100))
        pygame.display.update()

    def move(self, x, y):
        axis_x = x
        axis_y = y

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
