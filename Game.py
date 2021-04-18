from Constants import Constants
from VaccineBackground import VaccineBackground
from Player import Player
import pygame


class Game:

    def __init__(self):
        self.__game_over = False
        self.__screen = pygame.display.set_mode((1000, 700))
        pygame.init()

    def play(self):
        vaccines = VaccineBackground()
        while not self.__game_over:
            vaccines.draw(self.__screen)
            Player().draw(self.__screen)


if __name__ == "__main__":
    Game().play()
