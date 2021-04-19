
from constants.PlayerConstants import PlayerConstants

class JumpAction:

    def __init__(self):
        self.__isJumping = False
        self.__jump_time = PlayerConstants.JUMP_TIME

    def jumping(self, axis_y):
        if not self.__isJumping:
            return axis_y
        if self.__jump_time >= -PlayerConstants.JUMP_TIME:
            going_up_or_down = self.__is_going_up_or_down()
            axis_y -= PlayerConstants.ACCELERATION_DIVIDED_BY_TWO * (self.__jump_time ** 2)  * going_up_or_down
            self.__jump_time -= 1
        else:
            self.__isJumping = False
            self.__jump_time = PlayerConstants.JUMP_TIME
        return axis_y

    
    def __is_going_up_or_down(self):
        if self.__jump_time <= 0:
            return -1
        return 1

    def i_am_jumping(self):
        self.__isJumping = True

    @property
    def isJumping(self):
        return self.__isJumping
        