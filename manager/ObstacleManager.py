from obstacle.Box import Box
from manager.Manager import Manager

class ObstacleManager(Manager):

    def __init__(self):
        self.__boxes = [
            Box(900),
            Box(1419),
            Box(2100),
            Box(2762),
            Box(3200)
        ]
        super().__init__(self.__boxes)

    @property
    def boxes(self):
        return self.__boxes