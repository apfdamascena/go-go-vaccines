from images.PlayerAssets import PlayerAssets

class SquatAction:

    def __init__(self):
        self.__is_squatting = False
        self.__images = PlayerAssets()


    def squatting_right(self,window, axis_x, axis_y):
        window.blit(self.__images.squat_character_right, (axis_x, axis_y+6, 100, 100))
        self.__is_squatting = False

    def squatting_left(self,window, axis_x, axis_y):
        window.blit(self.__images.squat_character_left, (axis_x-40, axis_y+6, 100, 100))
        self.__is_squatting = False
    
    def player_is_squatting(self):
        self.__is_squatting = True
    
    @property
    def is_squatting(self):
        return self.__is_squatting
