
from obstacle.Box import Box

class ShapedObstacle:

    def __init__(self, matrix):
        self.__matrix = matrix
        self.__obstacles = []
        self.__create()

    def __create(self):
        for x in range(3):
            line_obstacles = []
            for y in range(3):
                if self.__matrix[y][x] == 1:
                    line_obstacles.append(
                        Box(900+90*x, 580-90*y))
                else:
                    line_obstacles.append(None)
            self.__obstacles.append(line_obstacles)

    def draw(self, window):
        for x in range(3):
            for y in range(3):
                if self.__obstacles[x][y] != None:
                    self.__obstacles[x][y].draw(window)

    def move(self):
        for x in range(3):
            for y in range(3):
                if self.__obstacles[x][y] != None:
                    self.__obstacles[x][y].move()
    
    @property
    def boxes(self):
        self.__obstacles