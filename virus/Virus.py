from constants.BackgroundConstants import BackgroundConstants
from constants.VirusConstants import VirusConstants
from images.VirusAssets import VirusAssets
import random

class Virus:

    def __init__(self, axis_x, random_virus_choice):
        self.__images = VirusAssets()
        self.__virus_options =[
            self.__images.virus_blue,
            self.__images.virus_green,
            self.__images.virus_red,
            self.__images.virus_yellow
        ]
        self.__random_choice_virus = random_virus_choice
        self.__axis_x, self.__saved_axis_x = axis_x, axis_x
        self.__axis_y_options = [
            VirusConstants.HEIGHT_VIRUS_ONE,
            VirusConstants.HEIGHT_VIRUS_TWO,
            VirusConstants.HEIGHT_VIRUS_THREE]
        self.__random_choice_axis_y = 0
        self.__axis_y  = self.__axis_y_options[self.__random_choice_axis_y]

    
    def draw(self, window):
        window.blit(self.__virus_options[self.__random_choice_virus],
                    (self.__axis_x, self.__axis_y_options[self.__random_choice_axis_y], 30, 30)) 
    
    def move(self):
        self.__axis_x -= BackgroundConstants.VELOCITY

        if  self.__axis_x < -VirusConstants.AXIS_X_TO_CHANGE_VIRUS:
            self.__random_choice_virus = random.randint(0, len(self.__virus_options)-1)
            self.__random_choice_axis_y = random.randint(0, len(self.__axis_y_options)-1)
            self.__axis_y  = self.__axis_y_options[self.__random_choice_axis_y]
            self.__axis_x = self.__saved_axis_x + random.randint(472, 1926)

    @property
    def axis_x(self):
        return self.__axis_x

    @property
    def axis_y(self):
        return self.__axis_y


        