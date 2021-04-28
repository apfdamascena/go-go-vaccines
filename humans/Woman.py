from humans.Human import Human
from images.WomanAssets import WomanAssets


class Woman(Human):

    def __init__(self):
        self.__images = WomanAssets()
        self.__sprites = self.__images.woman
        super().__init__(self.__sprites)