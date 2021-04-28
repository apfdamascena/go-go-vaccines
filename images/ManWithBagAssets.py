
import os
import pygame

class ManWithBagAssets:

    MAN_WITH_BAG_1 = os.path.join('assets', 'humans', 'man_with_bag_1.png')
    MAN_WITH_BAG_2 = os.path.join('assets', 'humans', 'man_with_bag_2.png')
    MAN_WITH_BAG_3 = os.path.join('assets', 'humans', 'man_with_bag_2.png')

    def __init__(self):
        self.__man_with_bag_1 = pygame.image.load(self.MAN_WITH_BAG_1)
        self.__man_with_bag_2 = pygame.image.load(self.MAN_WITH_BAG_2)
        self.__man_with_bag_3 = pygame.image.load(self.MAN_WITH_BAG_3)


    @property
    def man_with_bag(self):
        return [self.__man_with_bag_1, self.__man_with_bag_2, self.__man_with_bag_1, self.__man_with_bag_3]