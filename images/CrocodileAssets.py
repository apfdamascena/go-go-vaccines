
import os
import pygame

class CrocodileAssets:

    CROCODILE_ONE = os.path.join('assets', 'crocodile', 'crocodile1_3.png')
    CROCODILE_TWO = os.path.join('assets', 'crocodile', 'crocodile2.png')
    CROCODILE_THREE = os.path.join('assets', 'crocodile', 'crocodile2.png')


    def __init__(self):
        self.__crocodile_one = pygame.image.load(self.CROCODILE_ONE)
        self.__crocodile_two = pygame.image.load(self.CROCODILE_TWO)
        self.__crocodile_three = pygame.image.load(self.CROCODILE_THREE)

    
    @property
    def crocodile_one(self):
        return self.__crocodile_one
    
    @property
    def crocodile_two(self):
        return self.__crocodile_two
    
    @property
    def crocodile_three(self):
        return self.__crocodile_three

    