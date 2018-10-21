'''Author: Brandon Trabucco, Copyright 2019
Helper functoions to display and run a simple game'''


from collections import namedtuple
from tkinter import Tk, Canvas, Frame, BOTH, NW


ROOT = Tk()


#####################################
# lets make some really cool colors #
#####################################


def _color_clip(v):
    return max(0.0, min(1.0, v))


class Color(object):

    def __init__(self, red=0.0, green=0.0, blue=0.0):
        self.red = _color_clip(red)
        self.green = _color_clip(green)
        self.blue = _color_clip(blue)

    def __add__(self, x):
        assert(isinstance(x, Color) or isinstance(x, float))
        if isinstance(x, Color):
            return Color(red=_color_clip(self.red + x.red), 
                        green=_color_clip(self.green + x.green), 
                        blue=_color_clip(self.blue + x.blue))
        else:
            return Color(red=_color_clip(self.red + x), 
                        green=_color_clip(self.green + x), 
                        blue=_color_clip(self.blue + x))

    def __sub__(self, x):
        assert(isinstance(x, Color) or isinstance(x, float))
        if isinstance(x, Color):
            return Color(red=_color_clip(self.red - x.red), 
                        green=_color_clip(self.green - x.green), 
                        blue=_color_clip(self.blue - x.blue))
        else:
            return Color(red=_color_clip(self.red - x), 
                        green=_color_clip(self.green - x), 
                        blue=_color_clip(self.blue - x))

    def __mul__(self, x):
        assert(isinstance(x, Color) or isinstance(x, float))
        if isinstance(x, Color):
            return Color(red=_color_clip(self.red * x.red), 
                        green=_color_clip(self.green * x.green), 
                        blue=_color_clip(self.blue * x.blue))
        else:
            return Color(red=_color_clip(self.red * x), 
                        green=_color_clip(self.green * x), 
                        blue=_color_clip(self.blue * x))

    def __div__(self, x):
        assert(isinstance(x, Color) or isinstance(x, float))
        if isinstance(x, Color):
            return Color(red=_color_clip(self.red / x.red), 
                        green=_color_clip(self.green / x.green), 
                        blue=_color_clip(self.blue / x.blue))
        else:
            return Color(red=_color_clip(self.red / x), 
                        green=_color_clip(self.green /x), 
                        blue=_color_clip(self.blue / x))

    def tohex(self):
        return "#%02x%02x%02x" % (int(self.red * 255), 
            int(self.green * 255), int(self.blue * 255))

    def __eq__(self, x):
        assert(isinstance(x, Color))
        return self.tohex() == x.tohex()


class RedColor(Color):

    def __init__(self):
        super(RedColor, self).__init__(red=1.0, green=0.0, blue=0.0)


class GreenColor(Color):

    def __init__(self):
        super(GreenColor, self).__init__(red=0.0, green=1.0, blue=0.0)


class BlueColor(Color):

    def __init__(self):
        super(BlueColor, self).__init__(red=0.0, green=0.0, blue=1.0)


class BlackColor(Color):

    def __init__(self):
        super(BlackColor, self).__init__(red=0.0, green=0.0, blue=0.0)


class GreyColor(Color):

    def __init__(self):
        super(GreyColor, self).__init__(red=0.5, green=0.5, blue=0.5)


class WhiteColor(Color):

    def __init__(self):
        super(WhiteColor, self).__init__(red=1.0, green=1.0, blue=1.0)


class EerieBlackColor(Color):
    
    def __init__(self):
        super(EerieBlackColor, self).__init__(
            red=25/255, green=23/255, blue=22/255)


class UroblinYellowColor(Color):
    
    def __init__(self):
        super(UroblinYellowColor, self).__init__(
            red=230/255, green=175/255, blue=46/255)


class GainsboroWhiteColor(Color):
    
    def __init__(self):
        super(GainsboroWhiteColor, self).__init__(
            red=224/255, green=226/255, blue=219/255)


class DarkSlateBlueColor(Color):
    
    def __init__(self):
        super(DarkSlateBlueColor, self).__init__(
            red=61/255, green=52/255, blue=139/255)


class BlackShadowsBeigeColor(Color):
    
    def __init__(self):
        super(BlackShadowsBeigeColor, self).__init__(
            red=190/255, green=183/255, blue=164/255)


####################################
# lets make some game tiles to use #
####################################


class Drawable(object):

    def draw(self, canvas):
        pass

    def undraw(self, canvas):
        pass


class Tile(Drawable):

    width = 30
    height = 40

    def __init__(self, letter, text_color, background_color):
        assert(isinstance(text_color, Color) and 
            isinstance(background_color, Color) and 
            isinstance(letter, str) and len(letter) == 1)
        self.letter = letter
        self.text_color = text_color
        self.background_color = background_color
        self.box_handle = None
        self.letter_handle = None

    def __eq__(self, x):
        assert(isinstance(x, Tile))
        return (self.letter == x.letter and 
            self.text_color == x.text_color and 
            self.background_color == x.background_color)

    def draw(self, canvas, x, y):

        self.box_handle = canvas.create_rectangle(
            x * Tile.width, y * Tile.height, (x + 1) * Tile.width, (y + 1) * Tile.height, 
            fill=self.background_color.tohex())
        self.letter_handle = canvas.create_text(
            (x + .5) * Tile.width, (y + .5) * Tile.height, text=self.letter, 
            font=('Courier', 16), fill=self.text_color.tohex())

    def undraw(self, canvas):

        if self.box_handle is not None:
            canvas.delete(self.box_handle)
            self.box_handle = None
        if self.letter_handle is not None:
            canvas.delete(self.letter_handle)
            self.letter_handle = None


class BackgroundTile(Tile):

    def __init__(self):
        super(BackgroundTile, self).__init__(
            letter='.', text_color=GreyColor(), background_color=BlackColor())


class WallTile(Tile):

    def __init__(self):
        super(WallTile, self).__init__(
            letter='#', text_color=BlackColor(), background_color=GreyColor())


class FloorTile(Tile):

    def __init__(self):
        super(FloorTile, self).__init__(
            letter='.', text_color=GreyColor(), background_color=WhiteColor())


class PlayerTile(Tile):

    def __init__(self):
        super(PlayerTile, self).__init__(
            letter='P', text_color=DarkSlateBlueColor(), background_color=UroblinYellowColor())


class StackableTile(Tile):

    def __init__(self, bottom_tile):
        assert(isinstance(bottom_tile, Tile))
        self.queue = [bottom_tile]

    def push(self, tile):
        assert(isinstance(tile, Tile))
        self.queue = self.queue + [tile]

    def peek(self):
        return self.queue[-1]

    def pop(self):
        assert(len(self.queue) > 1)
        x = self.queue[-1]
        self.queue = self.queue[:-1]
        return x

    def __len__(self):
        return len(self.queue)

    @property
    def letter(self):
        return self.peek().letter

    @property
    def text_color(self):
        return self.peek().text_color

    @property
    def background_color(self):
        return self.peek().background_color

    @letter.setter
    def letter(self, x):
        self.peek().letter = x

    @text_color.setter
    def text_color(self, x):
        self.peek().text_color = x

    @background_color.setter
    def background_color(self, x):
        self.peek().background_color = x

    def draw(self, canvas, x, y):
        self.peek().draw(canvas, x, y)

    def undraw(self, canvas):
        self.peek().undraw(canvas)


#####################################
# lets make a game board to play on #
#####################################


class Board(Drawable):

    def __init__(self, name, tiles):
        self.name = name
        self.height = len(tiles)
        self.width = len(tiles[0])
        assert(all([len(x) == self.width for x in tiles]))
        self.tiles = tiles

    def draw(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x].draw(canvas, x, y)

    def undraw(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x].undraw(canvas)

    def place_tile(self, tile, x, y):
        self.tiles[y][x].push(tile)

    def remove_tile(self, x, y):
        return self.tiles[y][x].pop()


class RoomBoard(Board):

    def __init__(self, name, height, width, offset):
        tiles = [[None for x in range(width + 2 * offset)] for y in range(height + 2 * offset)]
        for x in range(width + 2 * offset):
            for y in range(height + 2 * offset):
                if x < offset or x >= width + offset or y < offset or y >= height + offset:
                    tiles[y][x] = StackableTile(BackgroundTile())
                elif x == offset or x == width + offset - 1 or y == offset or y == height + offset - 1:
                    tiles[y][x] = StackableTile(WallTile())
                else:
                    tiles[y][x] = StackableTile(FloorTile())
        super(RoomBoard, self).__init__(name, tiles)

                
######################################
# lets make a user interface to show #
######################################


class UI(Frame):
  
    def __init__(self, board):
        super(UI, self).__init__(ROOT, 
            width=board.width * Tile.width, 
            height=board.height * Tile.height)
        self.pack()
        self.master.title(board.name)
        self.canvas = Canvas(self, 
            width=board.width * Tile.width, 
            height=board.height * Tile.height)
        self.canvas.pack()
        self.setup_mouse()
        self.setup_type()
        self.setup_move()

    def show(self):
        ROOT.mainloop()

    def make(self, drawable):
        assert(isinstance(drawable, Drawable))
        drawable.undraw(self.canvas)
        drawable.draw(self.canvas)

    def setup_mouse(self):
        self.onMouseMoveCallback = lambda x, y: None
        self.onMouseClickCallback = lambda x, y: None
        self.onMouseUnclickCallback = lambda x, y: None

    def setup_type(self):
        self.onKeyPressCallback = lambda k: None
        self.onReturnKeyPressCallback = lambda: None
        self.onDeleteKeyPressCallback = lambda: None
        self.onBackspaceKeyPressCallback = lambda: None

    def setup_move(self):
        self.onUpKeyPressCallback = lambda: None
        self.onDownKeyPressCallback = lambda: None
        self.onLeftKeyPressCallback = lambda: None
        self.onRightKeyPressCallback = lambda: None

    def addMouseMoveListener(self, onMouseMoveCallback):
        self.onMouseMoveCallback = onMouseMoveCallback
        ROOT.bind('<Motion>', self.onMouseMove)

    def addMouseClickListener(self, onMouseClickCallback):
        self.onMouseClickCallback = onMouseClickCallback
        ROOT.bind('<Button-1>', self.onMouseClick)

    def addMouseUnclickListener(self, onMouseUnclickCallback):
        self.onMouseUnclickCallback = onMouseUnclickCallback
        ROOT.bind('<ButtonRelease-1>', self.onMouseUnclick)

    def addKeyPressListener(self, onKeyPressCallback):
        self.onKeyPressCallback = onKeyPressCallback
        ROOT.bind('<Key>', self.onKeyPress)

    def addReturnKeyPressListener(self, onReturnKeyPressCallback):
        self.onReturnKeyPressCallback = onReturnKeyPressCallback
        ROOT.bind('<Return>', self.onReturnKeyPress)

    def addDeleteKeyPressListener(self, onDeleteKeyPressCallback):
        self.onDeleteKeyPressCallback = onDeleteKeyPressCallback
        ROOT.bind('<Delete>', self.onDeleteKeyPress)

    def addBackspaceKeyPressListener(self, onBackspaceKeyPressCallback):
        self.onBackspaceKeyPressCallback = onBackspaceKeyPressCallback
        ROOT.bind('<Backspace>', self.onBackspaceKeyPress)

    def addUpKeyPressListener(self, onUpKeyPressCallback):
        self.onUpKeyPressCallback = onUpKeyPressCallback
        ROOT.bind('<Up>', self.onUpKeyPress)

    def addDownKeyPressListener(self, onDownKeyPressCallback):
        self.onDownKeyPressCallback = onDownKeyPressCallback
        ROOT.bind('<Down>', self.onDownKeyPress)

    def addLeftKeyPressListener(self, onLeftKeyPressCallback):
        self.onLeftKeyPressCallback = onLeftKeyPressCallback
        ROOT.bind('<Left>', self.onLeftKeyPress)

    def addRightKeyPressListener(self, onRightKeyPressCallback):
        self.onRightKeyPressCallback = onRightKeyPressCallback
        ROOT.bind('<Right>', self.onRightKeyPress)

    def onMouseMove(self, event):
        x, y = event.x, event.y
        self.onMouseMoveCallback(x, y)

    def onMouseClick(self, event):
        x, y = event.x, event.y
        self.onMouseClickCallback(x, y)

    def onMouseUnclick(self, event):
        x, y = event.x, event.y
        self.onMouseUnclickCallback(x, y)

    def onKeyPress(self, event):
        k = event.char
        self.onKeyPressCallback(k)

    def onReturnKeyPress(self, event):
        self.onReturnKeyPressCallback()

    def onDeleteKeyPress(self, event):
        self.onDeleteKeyPressCallback()

    def onBackspaceKeyPress(self, event):
        self.onBackspaceKeyPressCallback()

    def onUpKeyPress(self, event):
        self.onUpKeyPressCallback()

    def onDownKeyPress(self, event):
        self.onDownKeyPressCallback()

    def onLeftKeyPress(self, event):
        self.onLeftKeyPressCallback()

    def onRightKeyPress(self, event):
        self.onRightKeyPressCallback()
