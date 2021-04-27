import os
import pygame

class RedHeadWomanAssets:


    RED_HEAD_WOMAN_1 = os.path.join('assets', 'humans', 'redhead_woman_1.png')
    RED_HEAD_WOMAN_2 = os.path.join('assets', 'humans', 'redhead_woman_2.png')
    RED_HEAD_WOMAN_3 = os.path.join('assets', 'humans', 'redhead_woman_3.png')


    def __init__(self):
        self.__red_head_woman_1 = pygame.image.load(self.RED_HEAD_WOMAN_1)
        self.__red_head_woman_2 = pygame.image.load(self.RED_HEAD_WOMAN_2)
        self.__red_head_woman_3 = pygame.image.load(self.RED_HEAD_WOMAN_3)

    @property
    def red_head_woman(self):
        return [self.__red_head_woman_1, self.__red_head_woman_2, self.__red_head_woman_1, self.__red_head_woman_3]