from constants.BackgroundConstants import BackgroundConstants
from constants.PlayerConstants import PlayerConstants
from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from player.Player import Player
from obstacle.Box import Box
from obstacle.Boxes import Boxes
from obstacle.Obstacles import Obstacles
import pygame


class Game:

    def __init__(self):
        self.__game_over = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__player = Player()
        self.__vaccines_background = VaccineBackground()
        self.__Box = Box()
        self.__Boxes = Boxes()
        self.__Obstacles = Obstacles()
        pygame.init()

    def play(self):
        axis_x = PlayerConstants.INITIAL_X
        axis_y = PlayerConstants.INITIAL_Y
        while not self.__game_over:
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()
            self.__player.draw(self.__screen, axis_x, axis_y)
            axis_x, axis_y = self.__player.move(axis_x, axis_y)

            self.__Obstacles.drawObstacle(self.__screen)


"""             self.__Box.draw(self.__screen)
            self.__Box.move()
            self.__Boxes.draw(self.__screen)
            self.__Boxes.move() """


if __name__ == "__main__":
    Game().play()
