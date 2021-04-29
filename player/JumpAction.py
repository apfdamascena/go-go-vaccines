
from constants.PlayerConstants import PlayerConstants
from constants.JumpConstants import JumpConstants

class JumpAction:

    def __init__(self):
        self.__is_jumping = False
        self.__jump_time = JumpConstants.JUMP_TIME

    def jumping(self, axis_y):
        if not self.__is_jumping:
            return axis_y
        if self.__jump_time >= -JumpConstants.JUMP_TIME:
            jump_size = JumpConstants.ACCELERATION_DIVIDED_BY_TWO * (self.__jump_time ** JumpConstants.SQUARE)
            axis_y -= jump_size * self.__is_going_up_or_down()
            self.__jump_time -= JumpConstants.DECREASE_TIME
        else:
            self.__is_jumping = False
            self.__jump_time = JumpConstants.JUMP_TIME
        return axis_y

    
    def __is_going_up_or_down(self):
        if self.__jump_time <= JumpConstants.ARRIVED_IN_ASCENT_TIME:
            return JumpConstants.GOING_DOWN
        return JumpConstants.GOING_UP

    def player_is_jumping(self):
        self.__is_jumping = True
    
    @property
    def is_jumping(self):
        return self.__is_jumping
        