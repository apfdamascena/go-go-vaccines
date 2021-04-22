import os
import pygame

class PlayerAssets:

    __MAIN_CHARACTER = os.path.join('assets', 'characters', 'main-character.png')
    __SQUAT_CHARACTER = os.path.join('assets', 'characters', 'nurse_down.png')
    __CHARACTER_RIGHT_RUN = os.path.join('assets', 'characters', 'nurse_right_run.png')

    def __init__(self):
        self.__main_character = pygame.image.load(self.__MAIN_CHARACTER)
        self.__squat_character = pygame.image.load(self.__SQUAT_CHARACTER)
        self.__character_right_run = pygame.image.load(self.__CHARACTER_RIGHT_RUN)

    @property
    def main_character(self):
        return self.__main_character

    @property
    def squat_character(self):
        return self.__squat_character

    @property
    def character_right_run(self):
        return self.__character_right_run