import pygame


class Player:

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (20, 630, 50, 50))
        pygame.display.update()
