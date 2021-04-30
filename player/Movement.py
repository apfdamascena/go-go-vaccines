
from images.PlayerAssets import PlayerAssets
from player.JumpAction import JumpAction
from player.SquatAction import SquatAction
from images.PlayerAssets import PlayerAssets

class Movement:

    def __init__(self):
        self.__jump_action = JumpAction()
        self.__squat_action = SquatAction()
        self.__images = PlayerAssets()
        self.__direction_right = True
        self.__character_position = 0

    def drawing(self, window, axis_x, axis_y):
        if self.__squat_action.is_squatting:
            if self.__direction_right: 
                self.__squat_action.squatting_right(window, axis_x, axis_y)
            else:
                self.__squat_action.squatting_left(window, axis_x, axis_y)
        elif self.__direction_right: 
            window.blit(self.__images.character_images_right[self.__character_position], (axis_x, axis_y, 100, 100))
        else:
            window.blit(self.__images.character_images_left[self.__character_position], (axis_x, axis_y, 100, 100))


    def handle_bottom_right_pressed(self):
        self.__change_image()
        self.__direction_right = True
    
    def handle_bottom_left_pressed(self):
        self.__change_image()
        self.__direction_right = False

    def restart_player(self):
        self.__character_position = 0

    def __change_image(self):
        if self.__character_position >= len(self.__images.character_images_left)-1:
            self.__character_position = 0
        else: 
            self.__character_position += 1


    @property
    def jump(self):
        return self.__jump_action
    
    @property
    def squat(self):
        return self.__squat_action
