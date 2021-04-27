import os
import sys
import pygame
from background.VaccineTransparentBackground import VaccineTransparentBackground
from images.LogoAssets import LogoAsset


class Menu:

    def __init__(self):
        self.__start = False
        self.__images = LogoAsset()
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__vaccines_background = VaccineTransparentBackground()
        pygame.init()

    def draw(self, window):
        window.blit(self.__images.logo, (200, 200))
        pygame.display.update()

    def main(self):

        while True:
            self.draw(self.__screen)
            pinscher_font = os.path.join('font', 'SHPinscher-Regular.otf')
            font = pygame.font.Font(pinscher_font, 40, bold=True)
            self.__vaccines_background.draw(self.__screen)

            start_option = font.render('START', True, (206, 206, 206))
            credits_option = font.render('CREDITS', True, (206, 206, 206))
            quit_option = font.render('QUIT', True, (206, 206, 206))

            mouse_coords = pygame.mouse.get_pos()

            self.__screen.blit(start_option, (465, 400))
            self.__screen.blit(credits_option, (450, 450))
            self.__screen.blit(quit_option, (473, 500))

            if 470 <= mouse_coords[0] <= 570 and 400 <= mouse_coords[1] <= 425:
                start_option = font.render('START', True, (51, 200, 132))
                self.__screen.blit(start_option, (465, 400))

            if 450 <= mouse_coords[0] <= 650 and 450 <= mouse_coords[1] <= 475:
                credits_option = font.render('CREDITS', True, (51, 200, 132))
                self.__screen.blit(credits_option, (450, 450))

            if 475 <= mouse_coords[0] <= 575 and 500 <= mouse_coords[1] <= 525:
                quit_option = font.render('QUIT', True, (51, 200, 132))
                self.__screen.blit(quit_option, (473, 500))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 470 <= mouse_coords[0] <= 570 and 400 <= mouse_coords[1] <= 425:
                        return 'START'

                    if 450 <= mouse_coords[0] <= 550 and 450 <= mouse_coords[1] <= 475:
                        return 'CREDITS'

                    if 475 <= mouse_coords[0] <= 575 and 500 <= mouse_coords[1] <= 525:
                        pygame.exit()


if __name__ == "__main__":
    Menu().main()
