
from constants.BackgroundConstants import BackgroundConstants
from constants.HumanConstants import HumanConstants

class Human:

    def __init__(self, sprite):
        self.__sprite = sprite
        self.__current_image = 0
        self.__axis_y = 542

    def draw(self, window, axis_x):
        character = self.__sprite[self.__current_image]
        window.blit(character, (axis_x, self.__axis_y, 100, 100))
        self.__current_image += HumanConstants.VELOCITY_CHANGE_HUMAN_IMAGE
        self.__current_image %= HumanConstants.QUANTITY_OF_IMAGE

    def change_axis_y(self, x):
        self.__axis_y = x
        
