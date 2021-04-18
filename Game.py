from Constants import Constants
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
        axis_begin = Constants.ZERO
        axis_end = Constants.WIDTH
        x = 1
        while not self.__game_over:
            axis_begin, axis_end = MovingBackground().move(axis_begin, axis_end, Constants.VELOCITY)
            VaccineBackground().draw(self.__screen, axis_begin, axis_end)
            Player().draw(self.__screen)


if __name__ == "__main__":
    Game().play()
