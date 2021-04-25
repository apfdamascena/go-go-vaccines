import pygame
from images.PlayerAssets import PlayerAssets
from constants.PlayerConstants import PlayerConstants
from player.JumpAction import JumpAction
from player.SquatAction import SquatAction

class Player:

    def __init__(self):
        self.__images = PlayerAssets()
        self.__jump_action = JumpAction()
        self.__squat_action = SquatAction()
        self.__axis_x = PlayerConstants.INITIAL_X
        self.__axis_y = PlayerConstants.INITIAL_Y
        self.__is_top_box = False
        self.__character_position = 0
        self.__direction_right = True

    def draw(self, window):
        if self.__squat_action.is_squatting:
            if self.__direction_right: 
              self.__squat_action.squatting_right(window, self.__axis_x, self.__axis_y)
            else:
                self.__squat_action.squatting_left(window, self.__axis_x, self.__axis_y)
        elif self.__direction_right: 
            window.blit(self.__images.character_images_right[self.__character_position], (self.__axis_x, self.__axis_y, 100, 100))
        else:
            window.blit(self.__images.character_images_left[self.__character_position], (self.__axis_x, self.__axis_y, 100, 100))
            # pygame.display.update()

    def move(self, hit_top_box, hit_side_box):

        if hit_top_box:
            self.__jump_action.stop_jumping()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.__jump_action.player_is_jumping()
                
                if event.key == pygame.K_DOWN and not self.__jump_action.is_jumping:
                    self.__squat_action.player_is_squatting()

        self.__axis_y = self.__jump_action.jumping(self.__axis_y)


        if not hit_side_box:

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.__axis_x += PlayerConstants.VELOCITY
                self.change_image()
                self.__direction_right = True

            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                self.__axis_x -= PlayerConstants.VELOCITY
                self.change_image()
                self.__direction_right = False

            else:
                self.__character_position = 0

        if pygame.key.get_pressed()[pygame.K_DOWN] and not self.__jump_action.is_jumping:
            self.__squat_action.player_is_squatting()


    def change_axis_y(self, hit_top_box):
        if hit_top_box and not self.__is_top_box:
            self.__axis_y = 450
            self.__is_top_box = True
        if not hit_top_box and self.__is_top_box:
            self.__axis_y = 540
            self.__is_top_box = False

    def change_image(self):
        if self.__character_position >= len(self.__images.character_images_left)-1:
            self.__character_position = 0
        else: 
            self.__character_position +=1

    @property
    def axis_x(self):
        return self.__axis_x

    @property
    def axis_y(self):
        return self.__axis_y

    @property
    def is_top_box(self):
        return self.__is_top_box







