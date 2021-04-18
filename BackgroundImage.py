from Constants import Constants


class BackgroundImage:
    def __init__(self, img, mult, axis_begin, axis_end):
        self.__image = img
        self.__mult = mult 
        self.__axis_begin = axis_begin
        self.__axis_end = axis_end

    def move(self):
        self.__axis_begin -= Constants.VELOCITY * self.__mult
        self.__axis_end -= Constants.VELOCITY * self.__mult

        if self.__axis_begin < Constants.WIDTH * Constants.AXIS_ADJUSTMENT:
            self.__axis_begin = Constants.WIDTH
        if self.__axis_end < Constants.WIDTH * Constants.AXIS_ADJUSTMENT:
            self.__axis_end = Constants.WIDTH
        return self.__axis_begin, self.__axis_end
        
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


