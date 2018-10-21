'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


from game_engine.colors import *
from game_engine.tiles import *
from game_engine.stacks import *
from game_engine.drawable import Drawable


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

        assert(x >= 0 and x < self.width and y >= 0 and y < self.height)
        self.tiles[y][x].place_tile(tile)


    def remove_tile(self, x, y):

        assert(x >= 0 and x < self.width and y >= 0 and y < self.height)
        return self.tiles[y][x].remove_tile()


    def add_entity(self, e):

        assert(isinstance(e, Entity))
        self.entities.append(e)

        assert(e.x >= 0 and e.x < self.width and e.y >= 0 and e.y < self.height)
        self.tiles[e.y][e.x].place_tile(e)


    def shift_entity(self, which_entity, dx, dy):

        e = self.entities[which_entity]

        if isinstance(self.tiles[e.y][e.x].first_tile, Entity):
            assert(e.x >= 0 and e.x < self.width and e.y >= 0 and e.y < self.height)
            self.tiles[e.y][e.x].remove_tile()
            
            e.move(dx, dy)
            assert(e.x >= 0 and e.x < self.width and e.y >= 0 and e.y < self.height)
            self.tiles[e.y][e.x].place_tile(e)


    def shift_destination(self, which_entity, dx, dy):

        e = self.entities[which_entity]
        x, y = e.x + dx, e.y + dy
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


class Room(Board):

    def __init__(self, name, height, width, offset):

        tiles = [[None for x in range(width + 2 * offset)] 
            for y in range(height + 2 * offset)]

        for x in range(width + 2 * offset):

            for y in range(height + 2 * offset):

                next_tile = Stack(Floor())

                if (x < offset or x >= width  + offset or 
                    y < offset or y >= height + offset ):
                    next_tile = Stack(Background())

                elif (x == offset or x == width  + offset - 1 or 
                      y == offset or y == height + offset - 1 ):
                    next_tile = Stack(Wall())

                tiles[y][x] = next_tile

        super(Room, self).__init__(name, tiles)