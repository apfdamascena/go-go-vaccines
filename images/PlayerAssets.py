import os
import pygame

class PlayerAssets:

    __MAIN_CHARACTER = os.path.join('assets', 'characters', 'Nurse_right.png')
    __SQUAT_CHARACTER = os.path.join('assets', 'characters', 'nurse_down.png')
    __CHARACTER_RIGHT_RUN = os.path.join('assets', 'characters', 'nurse_right_run.png')
    __CHARACTER_RIGHT_RUN2 = os.path.join('assets', 'characters', 'Nurse_right_run2.png')
    __CHARACTER_LEFT = os.path.join('assets', 'characters', 'Nurse_left.png')
    __CHARACTER_LEFT_RUN = os.path.join('assets', 'characters', 'Nurse_left_run.png')
    __CHARACTER_LEFT_RUN2 = os.path.join('assets', 'characters', 'Nurse_left_run2.png')

    def __init__(self):
        self.__main_character = pygame.image.load(self.__MAIN_CHARACTER)
        self.__squat_character = pygame.image.load(self.__SQUAT_CHARACTER)
        self.__character_right_run = pygame.image.load(self.__CHARACTER_RIGHT_RUN)
        self.__character_right_run2 = pygame.image.load(self.__CHARACTER_RIGHT_RUN2)
        self.__main_character2 = pygame.image.load(self.__CHARACTER_LEFT)
        self.__character_left_run = pygame.image.load(self.__CHARACTER_LEFT_RUN)
        self.__character_left_run2 = pygame.image.load(self.__CHARACTER_LEFT_RUN2)
        self.__charater_images = [self.__main_character,self.__character_right_run,self.__main_character,self.__character_right_run2,self.__main_character2,self.__character_left_run, self.__main_character2,self.__character_left_run2]

    @property
    def main_character(self):
        return self.__main_character

    @property
    def charater_images(self):
        return self.__charater_images

    @property
    def squat_character(self):
        return self.__squat_character

    @property
    def character_right_run(self):
        return self.__character_right_run