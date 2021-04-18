from Constants import Constants


class MovingBackground:

    def move(self, axis_begin, axis_end):

        axis_begin -= Constants.VELOCITY
        axis_end -= Constants.VELOCITY

        if axis_begin < Constants.WIDTH * Constants.AXIS_ADJUSTMENT:
            axis_begin = Constants.WIDTH
        if axis_end < Constants.WIDTH * Constants.AXIS_ADJUSTMENT:
            axis_end = Constants.WIDTH
        return axis_begin, axis_end

