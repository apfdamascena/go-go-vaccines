from constants.BackgroundConstants import BackgroundConstants


class BackgroundImage:
    def __init__(self, image, mult):
        self.__image = image
        self.__mult = mult 
        self.__axis_begin = BackgroundConstants.ZERO
        self.__axis_end = BackgroundConstants.WIDTH

    def move(self):
        self.__axis_begin -= BackgroundConstants.VELOCITY * self.__mult
        self.__axis_end -= BackgroundConstants.VELOCITY * self.__mult

        if self.__axis_begin < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            self.__axis_begin = BackgroundConstants.WIDTH
        if self.__axis_end < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            self.__axis_end = BackgroundConstants.WIDTH
                
    @property
    def image(self):
        return self.__image

    @property
    def mult(self):
        return self.__mult

    @property
    def axis_begin(self):
        return self.__axis_begin

    @property
    def axis_end(self):
        return self.__axis_end


