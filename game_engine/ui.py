'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


from tkinter import Tk, Canvas, Frame, BOTH, NW
from game_engine.tiles import *

                
######################################
# lets make a user interface to show #
######################################


ROOT = Tk()
NULL = Null()


class UI(Frame):
  
    def __init__(self, board):

        super(UI, self).__init__(ROOT, 
            width=board.width * NULL.width, 
            height=board.height * NULL.height)
        self.pack()
        self.master.title(board.name)

        self.canvas = Canvas(self, 
            width=board.width * NULL.width, 
            height=board.height * NULL.height)
        self.canvas.pack()

        self.setup_mouse()
        self.setup_type()
        self.setup_move()


    def show_window(self):

        ROOT.mainloop()


    def update_drawable(self, drawable):

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
