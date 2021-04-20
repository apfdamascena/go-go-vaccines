from background.Images import Images

class SquatAction:

    def __init__(self):
        self.__is_squatting = False
        self.__images = Images()


    def squatting(self,window, axis_x, axis_y):
        window.blit(self.__images.squat_character, (axis_x, axis_y, 100, 100))
        self.__is_squatting = False

    def player_is_squatting(self):
        self.__is_squatting = True
    
    @property
    def is_squatting(self):
        return self.__is_squatting
