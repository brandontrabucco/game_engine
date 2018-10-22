'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


from game_engine.colors import *
from game_engine.tiles import *
from game_engine.stacks import *
from game_engine.drawable import Drawable


import random
random.seed(12345)


#####################################
# lets make a game board to play on #
#####################################


class Board(Drawable):

    def __init__(self, name, tiles):

        super(Board, self).__init__(len(tiles), len(tiles[0]))
        assert(all([len(t) == self.width for t in tiles]))

        self.name =  name
        self.tiles = tiles
        self.entities = []


    def place_tile(self, tile, x, y):

        if not (x >= 0 and x < self.width and y >= 0 and y < self.height):
            return False
        self.tiles[y][x].place_tile(tile)
        return True


    def remove_tile(self, x, y):

        if not (x >= 0 and x < self.width and y >= 0 and y < self.height):
            return Null()
        return self.tiles[y][x].remove_tile()


    def add_entity(self, e):

        if not (isinstance(e, Entity)):
            return -1
        self.entities.append(e)

        if not (e.x >= 0 and e.x < self.width and e.y >= 0 and e.y < self.height):
            return -1
        self.tiles[e.y][e.x].place_tile(e)
        return len(self.entities) - 1


    def in_front_of(self, which_entity):

        e = self.entities[which_entity]
        dx, dy = [(0, -1), (1, 0), (0, 1), (-1, 0)][e.z]

        if not (e.x + dx >= 0 and e.x + dx < self.width and e.y + dy >= 0 and e.y + dy < self.height):
            return Null()
        return self.tiles[e.y + dy][e.x + dx].first_tile


    def break_in_front_of(self, which_entity):

        e = self.entities[which_entity]
        dx, dy = [(0, -1), (1, 0), (0, 1), (-1, 0)][e.z]
        return self.remove_tile(e.x + dx, e.y + dy)


    def face_entity(self, which_entity, dx, dy):

        e = self.entities[which_entity]
        e.face(dx, dy)


    def shift_entity(self, which_entity, dx, dy):

        e = self.entities[which_entity]

        if isinstance(self.tiles[e.y][e.x].first_tile, Entity):
            if not (e.x >= 0 and e.x < self.width and e.y >= 0 and e.y < self.height):
                return False
            self.tiles[e.y][e.x].remove_tile()
            
            e.move(dx, dy)
            if not (e.x >= 0 and e.x < self.width and e.y >= 0 and e.y < self.height):
                return False
            self.tiles[e.y][e.x].place_tile(e)

        return True


    def shift_destination(self, which_entity, dx, dy):

        e = self.entities[which_entity]
        x, y = e.x + dx, e.y + dy
        if not (x >= 0 and x < self.width and y >= 0 and y < self.height):
            return Null()
        return self.tiles[y][x].first_tile


    def move_entity(self, which_entity, x, y):

        e = self.entities[which_entity]
        dx, dy = x - e.x, y - e.y
        self.shift_entity(which_entity, dx, dy)


    def move_destination(self, which_entity, x, y):

        e = self.entities[which_entity]
        dx, dy = x - e.x, y - e.y
        return self.shift_destination(which_entity, dx, dy)


    def draw(self, canvas):

        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x].draw(canvas, x, y)


    def undraw(self, canvas):

        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x].undraw(canvas)


class House(Board):

    def __init__(self, name, height, width, offset):

        tiles = [[None for x in range(width + 2 * offset)] 
            for y in range(height + 2 * offset)]

        for x in range(width + 2 * offset):

            for y in range(height + 2 * offset):

                next_stack = Indoor()

                if (x < offset or x >= width  + offset or 
                    y < offset or y >= height + offset ):

                    next_stack = Forest()
                    if random.random() > 0.6:
                        next_stack.remove_tile()

                elif (x == offset or x == width  + offset - 1 or 
                      y == offset or y == height + offset - 1 ):
                    next_stack = Building()

                tiles[y][x] = next_stack

        super(House, self).__init__(name, tiles)