'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


from game_engine.colors import *
from game_engine.drawable import Drawable
from game_engine.entity import Entity


####################################
# lets make some game tiles to use #
####################################


class Tile(Drawable):

    def __init__(self, letter, text_color, background_color):

        super(Tile, self).__init__(40, 30)
        assert(isinstance(letter, str) and len(letter) == 1 and
               isinstance(text_color, Color) and isinstance(background_color, Color))

        self.letter = letter
        self.text_color = text_color
        self.background_color = background_color

        self.handle_to_background = None
        self.handle_to_text = None


    def __eq__(self, x):

        assert(isinstance(x, Tile))
        return (self.letter == x.letter and 
                self.text_color == x.text_color and 
                self.background_color == x.background_color)
            

    def draw(self, canvas, x, y):

        super(Tile, self).draw(canvas)
        self.handle_to_background = canvas.create_rectangle(
            (x    ) * self.width, (y    ) * self.height, 
            (x + 1) * self.width, (y + 1) * self.height, 
            fill=self.background_color.hex())

        self.handle_to_text = canvas.create_text(
            (x +.5) * self.width, (y +.5) * self.height, 
            text=self.letter,      font=('Courier', 16), 
            fill=self.text_color.hex())


    def undraw(self, canvas):

        super(Tile, self).undraw(canvas)
        if self.handle_to_background is not None:
            canvas.delete(self.handle_to_background)
            self.handle_to_background = None

        if self.handle_to_text is not None:
            canvas.delete(self.handle_to_text)
            self.handle_to_text = None


class Null(Tile):

    def __init__(self):

        super(Null, self).__init__(
            letter=' ', text_color=Black(), background_color=Black())


class Background(Tile):

    def __init__(self):

        super(Background, self).__init__(
            letter='.', text_color=Grey(), background_color=Black())


class Wall(Tile):

    def __init__(self):

        super(Wall, self).__init__(
            letter='#', text_color=Black(), background_color=Grey())


class Floor(Tile):

    def __init__(self):

        super(Floor, self).__init__(
            letter='.', text_color=Grey(), background_color=White())


class Water(Tile):

    def __init__(self):

        super(Water, self).__init__(
            letter='~', text_color=White(), background_color=Cyan())


class Forest(Tile):

    def __init__(self):

        super(Forest, self).__init__(
            letter='&', text_color=Green(), background_color=Brown())


class Grass(Tile):

    def __init__(self):

        super(Grass, self).__init__(
            letter='=', text_color=Green(), background_color=Brown())


class Dirt(Tile):

    def __init__(self):

        super(Dirt, self).__init__(
            letter='.', text_color=Grey(), background_color=Brown())


class Mountain(Tile):

    def __init__(self):

        super(Mountain, self).__init__(
            letter='A', text_color=Red(), background_color=Brown())


class Player(Tile, Entity):

    def __init__(self, x, y):

        Tile.__init__(self,
            letter='P', text_color=Blue(), background_color=Yellow())
        Entity.__init__(self, x, y)


class Enemy(Tile, Entity):

    def __init__(self, x, y):

        Tile.__init__(self,
            letter='E', text_color=Blue(), background_color=Magenta())
        Entity.__init__(self, x, y)