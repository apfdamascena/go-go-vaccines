
from images.PlayerAssets import PlayerAssets
from player.JumpAction import JumpAction
from player.SquatAction import SquatAction

class Movement:

    def __init__(self):
        self.__jump_action = JumpAction()
        self.__squat_action = SquatAction()
        self.__direction_right = True
        self.__character_position = 0

    def drawing(self, window):
        if self.__squat_action.is_squatting:
            if self.__direction_right: 
              self.__squat_action.squatting_right(window, self.__axis_x, self.__axis_y)
            else:
                self.__squat_action.squatting_left(window, self.__axis_x, self.__axis_y)
        elif self.__direction_right: 
            window.blit(self.__images.character_images_right[self.__character_position], (self.__axis_x, self.__axis_y, 100, 100))
        else:
            window.blit(self.__images.character_images_left[self.__character_position], (self.__axis_x, self.__axis_y, 100, 100))

    @property
    def jumping(self):
        return self.__jump_action
    
    @property
    def squatting(self):
        return self.__squat_action

