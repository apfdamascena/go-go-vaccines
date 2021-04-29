import pygame
import time
import os
from constants.BackgroundConstants import BackgroundConstants
from constants.CollectablesConstants import CollectableConstants
from constants.PontuationConstants import PontuationConstants

class Pontuation:

    def __init__(self):
        self.__initial_time = time.time()
        self.__added_point = time.time() - 2
    def draw(self, window):
        black =  (0, 0, 0)
        grey =  (50, 50, 50)
        current_time = time.time()
        pinscher_font = os.path.join('font', 'SHPinscher-Regular.otf')
        font = pygame.font.Font(pinscher_font, 40, bold=True)
        text_a = str("{:.2f}".format((current_time - self.__initial_time)*PontuationConstants.MULTIPLIER)).zfill(2)
        text = font.render(text_a, True, black)
        window.blit(text,  (460, CollectableConstants.Y_HEART, 100, 100))
        if self.__added_point + 1 > current_time:
            text = font.render(('+ '+str(PontuationConstants.PLUS_TRANFORM_HUMAN)), True, grey)
            window.blit(text,  (460, CollectableConstants.Y_HEART+40, 100, 100))

    def add_point(self):
        self.__initial_time -= PontuationConstants.PLUS_TRANFORM_HUMAN/PontuationConstants.MULTIPLIER
        self.__added_point = time.time()

