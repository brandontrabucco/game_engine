'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


#####################################
# lets make some really cool colors #
#####################################


def _color_clip(v):

    return max(0.0, min(1.0, v))


class Color(object):

    def __init__(self, red=0.0, green=0.0, blue=0.0):

        self.red =   _color_clip(red)
        self.green = _color_clip(green)
        self.blue =  _color_clip(blue)


    def __add__(self, x):

        assert(isinstance(x, Color) or isinstance(x, float))

        if isinstance(x, Color):

            return Color(red=  _color_clip(self.red + x.red), 
                         green=_color_clip(self.green + x.green), 
                         blue= _color_clip(self.blue + x.blue))

        return Color(red=  _color_clip(self.red + x), 
                     green=_color_clip(self.green + x), 
                     blue= _color_clip(self.blue + x))


    def __sub__(self, x):

        assert(isinstance(x, Color) or isinstance(x, float))

        if isinstance(x, Color):

            return Color(red=  _color_clip(self.red - x.red), 
                         green=_color_clip(self.green - x.green), 
                         blue= _color_clip(self.blue - x.blue))

        return Color(red=  _color_clip(self.red - x), 
                     green=_color_clip(self.green - x), 
                     blue= _color_clip(self.blue - x))


    def __mul__(self, x):

        assert(isinstance(x, Color) or isinstance(x, float))

        if isinstance(x, Color):

            return Color(red=  _color_clip(self.red * x.red), 
                         green=_color_clip(self.green * x.green), 
                         blue= _color_clip(self.blue * x.blue))

        return Color(red=  _color_clip(self.red * x), 
                     green=_color_clip(self.green * x), 
                     blue= _color_clip(self.blue * x))


    def __div__(self, x):

        assert(isinstance(x, Color) or isinstance(x, float))

        if isinstance(x, Color):
            
            return Color(red=  _color_clip(self.red / x.red), 
                         green=_color_clip(self.green / x.green), 
                         blue= _color_clip(self.blue / x.blue))

        return Color(red=  _color_clip(self.red / x), 
                     green=_color_clip(self.green /x), 
                     blue= _color_clip(self.blue / x))
 

    def hex(self):

        return "#%02x%02x%02x" % (
            int(self.red * 255.0), int(self.green * 255.0), int(self.blue * 255.0))


    def __eq__(self, x):

        assert(isinstance(x, Color))
        return self.hex() == x.hex()


class Red(Color):

    def __init__(self):

        super(Red, self).__init__(red=1.0, green=0.0, blue=0.0)


class Green(Color):

    def __init__(self):

        super(Green, self).__init__(red=0.0, green=1.0, blue=0.0)


class Blue(Color):

    def __init__(self):

        super(Blue, self).__init__(red=0.0, green=0.0, blue=1.0)


class Cyan(Color):

    def __init__(self):

        super(Cyan, self).__init__(red=0.0, green=1.0, blue=1.0)


class Yellow(Color):

    def __init__(self):

        super(Yellow, self).__init__(red=1.0, green=1.0, blue=0.0)


class Magenta(Color):

    def __init__(self):

        super(Magenta, self).__init__(red=1.0, green=0.0, blue=1.0)


class Black(Color):

    def __init__(self):

        super(Black, self).__init__(red=0.0, green=0.0, blue=0.0)


class Grey(Color):

    def __init__(self):

        super(Grey, self).__init__(red=0.5, green=0.5, blue=0.5)


class White(Color):

    def __init__(self):

        super(White, self).__init__(red=1.0, green=1.0, blue=1.0)


class Brown(Color):

    def __init__(self):

        super(Brown, self).__init__(red=0.5, green=0.35, blue=0.25)