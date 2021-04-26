import math


class WaveMovement:

    def moving(self, axis_x, axis_y):
        return axis_y + 100 * math.sin(math.radians(axis_x) * 0.9)