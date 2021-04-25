import os
import pygame

class PlayerAssets:

    __MAIN_CHARACTER = os.path.join('assets', 'characters', 'Nurse_right.png')
    __SQUAT_CHARACTER_RIGHT = os.path.join('assets', 'characters', 'nurse_down.png')
    __SQUAT_CHARACTER_LEFT = os.path.join('assets', 'characters', 'Nurse_down_left.png')
    __CHARACTER_RIGHT_RUN = os.path.join('assets', 'characters', 'nurse_right_run.png')
    __CHARACTER_RIGHT_RUN2 = os.path.join('assets', 'characters', 'Nurse_right_run2.png')
    __CHARACTER_LEFT = os.path.join('assets', 'characters', 'Nurse_left.png')
    __CHARACTER_LEFT_RUN = os.path.join('assets', 'characters', 'Nurse_left_run.png')
    __CHARACTER_LEFT_RUN2 = os.path.join('assets', 'characters', 'Nurse_left_run2.png')

    def __init__(self):
        main_character_right = pygame.image.load(self.__MAIN_CHARACTER)
        character_right_run = pygame.image.load(self.__CHARACTER_RIGHT_RUN)
        character_right_run2 = pygame.image.load(self.__CHARACTER_RIGHT_RUN2)
        main_character_left = pygame.image.load(self.__CHARACTER_LEFT)
        character_left_run = pygame.image.load(self.__CHARACTER_LEFT_RUN)
        character_left_run2 = pygame.image.load(self.__CHARACTER_LEFT_RUN2)
        self.__character_images_right = [main_character_right, character_right_run, main_character_right,character_right_run2]
        self.__character_images_left = [main_character_left, character_left_run,  main_character_left, character_left_run2]
        self.__squat_character_right = pygame.image.load(self.__SQUAT_CHARACTER_RIGHT)
        self.__squat_character_left = pygame.image.load(self.__SQUAT_CHARACTER_LEFT)
        # this is here because it was used in obstacles
        self.__character_right_run = pygame.image.load(self.__CHARACTER_RIGHT_RUN)


    @property
    def character_images_right(self):
        return self.__character_images_right

    @property
    def character_images_left(self):
        return self.__character_images_left

    @property
    def squat_character_right(self):
        return self.__squat_character_right

    @property
    def squat_character_left(self):
        return self.__squat_character_left

    @property
    def character_right_run(self):
        return self.__character_right_run
