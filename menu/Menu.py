import sys
import pygame


class Menu:

    def __init__(self, background):
        self.__start = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__vaccines_background = background

        pygame.init()

    def main(self):
        while True:

            font = pygame.font.SysFont('Consolas', 30, bold=True)
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()

            start_option = font.render('START', True, (255, 255, 255))
            credits_option = font.render('CREDITS', True, (255, 255, 255))
            quit_option = font.render('QUIT', True, (255, 255, 255))

            mouse_coords = pygame.mouse.get_pos()

            self.__screen.blit(start_option, (470, 400))
            self.__screen.blit(credits_option, (450, 450))
            self.__screen.blit(quit_option, (475, 500))

            if 470 <= mouse_coords[0] <= 570 and 400 <= mouse_coords[1] <= 425:
                start_option = font.render('START', True, (255, 255, 0))
                self.__screen.blit(start_option, (470, 400))

            if 450 <= mouse_coords[0] <= 550 and 450 <= mouse_coords[1] <= 475:
                credits_option = font.render('CREDITS', True, (255, 255, 0))
                self.__screen.blit(credits_option, (450, 450))

            if 475 <= mouse_coords[0] <= 575 and 500 <= mouse_coords[1] <= 525:
                quit_option = font.render('QUIT', True, (255, 255, 0))
                self.__screen.blit(quit_option, (475, 500))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 470 <= mouse_coords[0] <= 570 and 400 <= mouse_coords[1] <= 425:
                        return 'START'

                    if 450 <= mouse_coords[0] <= 550 and 450 <= mouse_coords[1] <= 475:
                        return 'CREDITS'

                    if 475 <= mouse_coords[0] <= 575 and 500 <= mouse_coords[1] <= 525:
                        pygame.exit()

            pygame.display.update()


if __name__ == "__main__":
    Menu().main()
