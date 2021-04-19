from constants.BackgroundConstants import BackgroundConstants
from constants.PlayerConstants import PlayerConstants
from MovingBackground import MovingBackground
from VaccineBackground import VaccineBackground
from Player import Player
import pygame


class Game:

    def __init__(self):
        self.__game_over = False
        self.__screen = pygame.display.set_mode((1000, 700))
        pygame.init()

    def play(self):
        axis_begin = BackgroundConstants.ZERO
        axis_end = BackgroundConstants.WIDTH

        axis_x = PlayerConstants.INITIAL_X
        axis_y = PlayerConstants.INITIAL_Y

        while not self.__game_over:
            axis_begin, axis_end = MovingBackground().move(axis_begin, axis_end)
            VaccineBackground().draw(self.__screen, axis_begin, axis_end)
            Player().draw(self.__screen, axis_x, axis_y)
            axis_x, axis_y = Player().move(axis_x, axis_y)


if __name__ == "__main__":
    Game().play()
