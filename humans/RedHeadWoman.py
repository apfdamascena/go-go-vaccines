from humans.Human import Human
from images.RedHeadWomanAssets import RedHeadWomanAssets


class RedHeadWoman(Human):

    def __init__(self):
        self.__images = RedHeadWomanAssets()
        self.__sprites = self.__images.red_head_woman
        super().__init__(self.__sprites)