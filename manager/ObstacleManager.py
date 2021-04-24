import random
from obstacle.Box import Box
from manager.Manager import Manager


class ObstacleManager(Manager):

    def __init__(self):
        first = random.randint(900, 1800)
        second = random.randint(1800, 3600)

        self.__boxes = [
            Box(first),
            Box(second)
        ]
        super().__init__(self.__boxes)

    @property
    def boxes(self):
        return self.__boxes
