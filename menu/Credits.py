from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from background.VaccineTransparentBackground import VaccineTransparentBackground
import pygame
import sys
import os
from sound.Sound import Sound


class Credits:

    def __init__(self):
        self.__start = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__vaccines_background = VaccineTransparentBackground()

    def main(self):
        action = True
        sound = Sound()

        while action:
            pinscher_font = os.path.join('font', 'SHPinscher-Regular.otf')
            font = pygame.font.Font(pinscher_font, 40, bold=True)
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background

            alex_user = font.render('@APFDAMASCENA', True, (206, 206, 206))
            sofia_user = font.render('@SOFIAMDL', True, (206, 206, 206))
            igor_user = font.render('@IGRPHILLIPE', True, (206, 206, 206))
            back_action = font.render(
                'BACK TO MENU', True, (206, 206, 206))

            mouse_coords = pygame.mouse.get_pos()

            self.__screen.blit(alex_user, (380, 300))
            self.__screen.blit(sofia_user, (420, 350))
            self.__screen.blit(igor_user, (395, 400))
            self.__screen.blit(back_action, (393, 500))

            if 390 <= mouse_coords[0] <= 590 and 500 <= mouse_coords[1] <= 540:
                back_option = font.render('BACK TO MENU', True, (51, 200, 132))
                self.__screen.blit(back_option, (393, 500))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse_coords[0] <= 590 and 500 <= mouse_coords[1] <= 540:
                        sound.select_option_play()
                        return 'MENU'

            pygame.display.update()


if __name__ == "__main__":
    Credits().main()
