import os
import pygame

class OldLadyAssets:


    OLD_LADY_1 = os.path.join('assets', 'humans', 'old_lady_1.png')
    OLD_LADY_2= os.path.join('assets', 'humans', 'old_lady_2.png')
    OLD_LADY_3 = os.path.join('assets', 'humans', 'old_lady_3.png')

    def __init__(self):
        self.__old_lady_1 = pygame.image.load(self.OLD_LADY_1)
        self.__old_lady_2 = pygame.image.load(self.OLD_LADY_2)
        self.__old_lady_3 = pygame.image.load(self.OLD_LADY_3)

    @property
    def old_lady(self):
        return [self.__old_lady_1, self.__old_lady_2, self.__old_lady_1, self.__old_lady_3]