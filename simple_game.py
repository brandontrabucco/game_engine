'''Author: Brandon Trabucco, Copyright 2019
A simple game using python where the user solves a maze'''


import game_engine as game
import tkinter as tk


if __name__ == '__main__':

    px = 5
    py = 5

    board = game.RoomBoard("My Game", 10, 15, 3)
    board.place_tile(game.PlayerTile(), px, py)

    ui = game.UI(board)
    ui.make(board)

    def update(c):

        global px
        global py

        dx, dy = 0, 0

        if c == 'w':
            dy = -1
        elif c == 'a':
            dx = -1
        elif c == 's':
            dy = 1
        elif c == 'd':
            dx = 1

        if isinstance(board.tiles[py + dy][px + dx].peek(), game.FloorTile):

            p = board.tiles[py][px].pop()
            board.tiles[py + dy][px + dx].push(p)
            px, py = px + dx, py + dy

        ui.make(board)

    ui.addKeyPressListener(update)

    ui.show()