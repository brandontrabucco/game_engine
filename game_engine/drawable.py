'''Author: Brandon Trabucco, Copyright 2019
Helper functions to display and run a simple game'''


from tkinter import Canvas


####################################
# An interface drawn to the screen #
####################################


class Drawable(object):
    
    def __init__(self, height, width):

        self.height = height
        self.width = width


    def draw(self, canvas):

        assert(isinstance(canvas, Canvas))


    def undraw(self, canvas):

        assert(isinstance(canvas, Canvas))