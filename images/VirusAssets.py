import os
import pygame

class VirusAssets:

    VIRUS_BLUE = os.path.join('assets', 'virus', 'corona_blue.png')
    VIRUS_GREEN = os.path.join('assets', 'virus', 'corona_green.png')
    VIRUS_RED = os.path.join('assets', 'virus', 'corona_red.png')
    VIRUS_YELLOW = os.path.join('assets', 'virus', 'corona_yellow.png')

    def __init__(self):
        self.__virus_blue = pygame.image.load(self.VIRUS_BLUE)
        self.__virus_green = pygame.image.load(self.VIRUS_GREEN)
        self.__virus_red = pygame.image.load(self.VIRUS_RED)
        self.__virus_yellow = pygame.image.load(self.VIRUS_YELLOW)

    @property
    def virus_blue(self):
        return self.__virus_blue
    
    @property
    def virus_green(self):
        return self.__virus_green
    
    @property
    def virus_red(self):
        return self.__virus_red
    
    @property
    def virus_yellow(self):
        return self.__virus_yellow