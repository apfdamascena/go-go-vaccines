import pygame
import time
from constants.BackgroundConstants import BackgroundConstants
from constants.CollectablesConstants import CollectableConstants
class Pontuation:

    def __init__(self):
        self.__initial_time = time.time()

    def draw(self, window):
        black = (0,0,0)
        current_time = time.time()
        font = pygame.font.SysFont('comicsansms', 55)
        text_a = str(current_time - self.__initial_time).zfill(2)
        text = font.render(text_a, True, black)
        window.blit(text,  (BackgroundConstants.WIDTH/2, CollectableConstants.Y_HEART, 100, 100))
