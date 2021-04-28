from humans.Human import Human
from images.OldLadyAssets import OldLadyAssets


class OldLady(Human):

    def __init__(self):
        self.__images = OldLadyAssets()
        self.__sprites = self.__images.old_lady
        super().__init__(self.__sprites)        
        self.change_axis_y(563)
