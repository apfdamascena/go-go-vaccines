from constants.BackgroundConstants import BackgroundConstants


class MovingBackground:

    def move(self, axis_begin, axis_end):

        axis_begin -= BackgroundConstants.VELOCITY
        axis_end -= BackgroundConstants.VELOCITY

        if axis_begin < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            axis_begin = BackgroundConstants.WIDTH
        if axis_end < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            axis_end = BackgroundConstants.WIDTH
        return axis_begin, axis_end
