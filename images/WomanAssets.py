import os
import pygame

class WomanAssets:


    WOMAN_1 = os.path.join('assets', 'humans', 'woman_1.png')
    WOMAN_2 = os.path.join('assets', 'humans', 'woman_2.png')
    WOMAN_3 = os.path.join('assets', 'humans', 'woman_3.png')


    def __init__(self):
        self.__woman_1 = pygame.image.load(self.WOMAN_1)
        self.__woman_2 = pygame.image.load(self.WOMAN_2)
        self.__woman_3 = pygame.image.load(self.WOMAN_3)

    @property
    def woman(self):
        return [self.__woman_1, self.__woman_2, self.__woman_1, self.__woman_3]