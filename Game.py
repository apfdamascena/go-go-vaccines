from menu.Menu import Menu
from menu.Credits import Credits
from collectables.Heart import Heart
from GamePlay import GamePlay
import pygame


class Game:

    def __init__(self):
        self.__menu = Menu()
        self.__credits = Credits()
        self.__game_play = GamePlay()
        self.__start = False
        self.__credits_action = False
        self.__menu_action = False
        pygame.init()

    def load(self):

        while True:
            action = self.__menu.main()

            if action == 'START':
                self.__menu_action = False
                self.__start = True

            if action == 'CREDITS':
                self.__credits_action = True

            if action == 'MENU':
                self.__menu_action = True

            while self.__menu_action:
                action = self.__menu.main()

            while self.__credits_action:
                action = self.__credits.main()
                self.__credits_action = False
                self.__menu_action = True

            self.__game_play.playing(self.__start)


if __name__ == "__main__":
    Game().load()
