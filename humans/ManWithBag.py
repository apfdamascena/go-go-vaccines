from humans.Human import Human
from images.ManWithBagAssets import ManWithBagAssets


class ManWithBag(Human):

    def __init__(self):
        self.__images = ManWithBagAssets()
        self.__sprites = self.__images.man_with_bag
        super().__init__(self.__sprites)
