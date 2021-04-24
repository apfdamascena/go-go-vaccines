from constants.BackgroundConstants import BackgroundConstants
from images.VirusAssets import VirusAssets
import random

class Virus:

    def __init__(self):
        self.__images = VirusAssets()
        self.__virus_options =[
            self.__images.virus_blue,
            self.__images.virus_green,
            self.__images.virus_red,
            self.__images.virus_yellow
        ]
        self.__random_choice_virus = 0
        self.__axis_x = 1315
        self.__axis_y_options = [
            580,470, 540]
        self.__random_choice_axis_y = 0
        self.__axis_y  = self.__axis_y_options[self.__random_choice_axis_y]

    
    def draw(self, window):
        window.blit(self.__virus_options[self.__random_choice_virus],
                    (self.__axis_x, self.__axis_y_options[self.__random_choice_axis_y], 30, 30)) 
    
    def move(self):
        self.__axis_x -= BackgroundConstants.VELOCITY

        if  self.__axis_x < -200:
            self.__random_choice_virus = random.randint(0, len(self.__virus_options)-1)
            self.__random_choice_axis_y = random.randint(0, len(self.__axis_y_options)-1)
            self.__axis_y  = self.__axis_y_options[self.__random_choice_axis_y]
            self.__axis_x = 1315 + random.randint(100, 200)

    @property
    def axis_x(self):
        return self.__axis_x

    @property
    def axis_y(self):
        return self.__axis_y


        