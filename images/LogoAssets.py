import os
import pygame


class LogoAsset:
    LOGO = os.path.join('assets', 'logo', 'logo.png')

    def __init__(self):
        self.__logo = pygame.image.load(self.LOGO)

    @property
    def logo(self):
        return self.__logo
