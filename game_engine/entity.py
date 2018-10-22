'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


#####################################
# An interface representing movable #
#####################################


class Entity(object):
    
    def __init__(self, x, y, z=0):

        self._x = x
        self._y = y
        self._z = z


    @property
    def x(self):

        return self._x


    @property
    def y(self):

        return self._y


    @property
    def z(self):

        return self._z


    @x.setter
    def x(self, x):

        self._x = x


    @y.setter
    def y(self, y):

        self._y = y


    @z.setter
    def z(self, z):

        self._z = z


    def zero(self):

        self.x = 0
        self.y = 0
        self.z = 0


    def move(self, dx, dy):

        self.x = self.x + dx
        self.y = self.y + dy

    
    def face(self, dx, dy):

        if abs(dx) > abs(dy):

            if dx < 0:
                self.z = 3
            else:
                self.z = 1
                
        else:
            
            if dy < 0:
                self.z = 0
            else:
                self.z = 2

    
    def __add__(self, e):

        assert(isinstance(e, Entity))
        return Entity(self.x + e.x, self.y + e.y)

    
    def __sub__(self, e):

        assert(isinstance(e, Entity))
        return Entity(self.x - e.x, self.y - e.y)

    
    def __mul__(self, e):

        assert(isinstance(e, Entity))
        return Entity(self.x * e.x, self.y * e.y)

    
    def __div__(self, e):

        assert(isinstance(e, Entity))
        return Entity(self.x / e.x, self.y / e.y)
