from constants.BackgroundConstants import BackgroundConstants
from constants.PlayerConstants import PlayerConstants
from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from player.Player import Player
import pygame


class Game:

    def __init__(self):
        self.__game_over = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__player = Player()
        self.__vaccines_background = VaccineBackground()
        pygame.init()

    def play(self):
        axis_x = PlayerConstants.INITIAL_X
        axis_y = PlayerConstants.INITIAL_Y
        while not self.__game_over:
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()
            self.__player.draw(self.__screen, axis_x, axis_y)
            axis_x, axis_y = self.__player.move(axis_x, axis_y)



if __name__ == "__main__":
    Game().play()
