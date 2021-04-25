import os
import pygame


class CollectablesAssets:

    HEART = os.path.join('assets', 'collectables', 'heart.png')
    GREY_HEART = os.path.join('assets', 'collectables', 'heart-grey.png')
    VACCINE = os.path.join('assets', 'collectables', 'vaccine.png')

    def __init__(self):
        self.__heart = pygame.image.load(self.HEART)
        self.__grey_heart = pygame.image.load(self.GREY_HEART)
        self.__vaccine = pygame.image.load(self.VACCINE)

    @property
    def heart(self):
        return self.__heart

    @property
    def grey_heart(self):
        return self.__grey_heart

    @property
    def vaccine(self):
        return self.__vaccine
