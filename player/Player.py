import pygame
import time
from images.PlayerAssets import PlayerAssets
from constants.PlayerConstants import PlayerConstants
from player.JumpAction import JumpAction
from player.SquatAction import SquatAction
from constants.BackgroundConstants import BackgroundConstants
from player.Movement import Movement

class Player:

    def __init__(self):
        self.__movement = Movement()
        self.__axis_x = PlayerConstants.INITIAL_X
        self.__axis_y = PlayerConstants.INITIAL_Y
        self.__is_top_box = False
        self.__invencible = False
        self.__draw_invencible = True
        self.__invencible_time = time.time()

    def draw(self, window):
        if not self.__invencible:
            self.__movement.drawing(window, self.__axis_x, self.__axis_y)
        else:
            if self.__invencible_time+1 > time.time():
                if self.__draw_invencible:
                    self.__movement.drawing(window, self.__axis_x, self.__axis_y)
                    self.__draw_invencible = False
                else:
                    self.__draw_invencible = True
            else:
                self.__invencible = False


    def move(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.__movement.jump.player_is_jumping()

                if event.key == pygame.K_DOWN and not self.__movement.jump.is_jumping:
                    self.__movement.squat.player_is_squatting()

        self.__axis_y = self.__movement.jump.jumping(self.__axis_y)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.axis_x < 900:
                self.__axis_x += PlayerConstants.VELOCITY
                self.__movement.handle_bottom_right_pressed()

        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.__axis_x != 0:
                self.__axis_x -= PlayerConstants.VELOCITY
                self.__movement.handle_bottom_left_pressed()
        else:
            self.__movement.restart_player()

        if pygame.key.get_pressed()[pygame.K_DOWN] and not self.__movement.jump.is_jumping:
            self.__movement.squat.player_is_squatting()

        self.__walk()

    def __walk(self):
        if (self.__axis_x != 0):
            self.__axis_x -= BackgroundConstants.VELOCITY

    @property
    def axis_x(self):
        return self.__axis_x

    @property
    def axis_y(self):
        return self.__axis_y
        
    @property
    def invencible(self):
        return self.__invencible

    def is_invencible(self):
        self.__invencible = True
        self.__invencible_time = time.time()
    