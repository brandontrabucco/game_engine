'''Author: Brandon Trabucco, Copyright 2019
A simple game using python where the user solves a maze'''


import game_engine as game


def _key_to_direction(key):

    dx, dy = 0, 0

    if key == 'w':
        dy = -1
    elif key == 'a':
        dx = -1
    elif key == 's':
        dy = 1
    elif key == 'd':
        dx = 1

    return dx, dy


if __name__ == '__main__':

    board = game.Room("My Game", 10, 15, 3)
    board.add_entity(game.Player(7, 8))

    ui = game.UI(board)
    ui.update_drawable(board)

    def key_listener(key):

        dx, dy = _key_to_direction(key)
        if isinstance(board.shift_destination(0, dx, dy), game.Floor):
            board.shift_entity(0, dx, dy)

        ui.update_drawable(board)

    ui.addKeyPressListener(key_listener)
    ui.show_window()