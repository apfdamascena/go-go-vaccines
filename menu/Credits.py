from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
import pygame
import sys


class Credits:

    def __init__(self, background):
        self.__start = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__vaccines_background = background

    def main(self):
        action = True
        while action:
            font = pygame.font.SysFont('Consolas', 30, bold=True)
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()

            alex_user = font.render('@APFDAMASCENA', True, (255, 255, 255))
            sofia_user = font.render('@SOFIAMDL', True, (255, 255, 255))
            igor_user = font.render('@IGRPHILLIPE', True, (255, 255, 255))
            back_action = font.render(
                'BACK TO MENU', True, (255, 255, 255))

            mouse_coords = pygame.mouse.get_pos()

            self.__screen.blit(alex_user, (380, 300))
            self.__screen.blit(sofia_user, (420, 350))
            self.__screen.blit(igor_user, (390, 400))
            self.__screen.blit(back_action, (390, 500))

            if 390 <= mouse_coords[0] <= 590 and 500 <= mouse_coords[1] <= 525:
                back_option = font.render('BACK TO MENU', True, (255, 255, 0))
                self.__screen.blit(back_option, (390, 500))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse_coords[0] <= 590 and 500 <= mouse_coords[1] <= 525:
                        return 'MENU'

            pygame.display.update()


if __name__ == "__main__":
    Credits().main()
