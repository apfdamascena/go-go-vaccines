import pygame
import sys
import os
import time
from background.BlackBackground import BlackBackground


class GameOver:

    def __init__(self):
        self.__start = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__initial_time = time.time()
        self.__black_background = BlackBackground()
        pygame.init()

    def main(self):
        current_time = time.time()
        index = 0
        game_over = True
        while game_over:
            pinscher_font = os.path.join('font', 'SHPinscher-Regular.otf')
            font = pygame.font.Font(pinscher_font, 70, bold=True)
            subtitle_font = pygame.font.Font(pinscher_font, 40, bold=True)
            self.__black_background.draw(self.__screen)

            gameover = font.render('GAME OVER', True, (51, 200, 132))
            self.__screen.blit(gameover, (370, 250))

            back = subtitle_font.render(
                'Press any key to back to menu', True, (206, 206, 206))
            self.__screen.blit(back, (290, 500))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_over = False

            pygame.display.update()


if __name__ == "__main__":
    GameOver().main()
