'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


from game_engine.tiles import Tile
from game_engine.drawable import Drawable


####################################
# lets make some game tiles to use #
####################################


class Stack(Tile):

    def __init__(self, bottom_tile):

        Drawable.__init__(self, 40, 30)
        assert(isinstance(bottom_tile, Tile))
        self.stack_of_tiles = [bottom_tile]


    def place_tile(self, tile):

        assert(isinstance(tile, Tile))
        self.stack_of_tiles = self.stack_of_tiles + [tile]


    def remove_tile(self):

        assert(len(self.stack_of_tiles) > 1)
        return self.stack_of_tiles.pop(-1)


    def look_at(self, i):

        return self.stack_of_tiles[i]


    def __len__(self):

        return len(self.stack_of_tiles)


    @property
    def first_tile(self):

        return self.look_at(-1)


    @property
    def second_tile(self):

        return self.look_at(-2)


    @property
    def letter(self):

        return self.first_tile.letter


    @property
    def text_color(self):

        return self.first_tile.text_color


    @property
    def background_color(self):
        
        return self.first_tile.background_color


    @letter.setter
    def letter(self, x):

        self.first_tile.letter = x


    @text_color.setter
    def text_color(self, x):

        self.first_tile.text_color = x


    @background_color.setter
    def background_color(self, x):

        self.first_tile.background_color = x


    def draw(self, canvas, x, y):

        Drawable.draw(self, canvas)
        self.first_tile.draw(canvas, x, y)


    def undraw(self, canvas):

        Drawable.undraw(self, canvas)
        for tile in self.stack_of_tiles:
            tile.undraw(canvas)