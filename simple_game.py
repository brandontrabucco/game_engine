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

    board = game.House("My Game", 10, 15, 3)
    player_id = board.add_entity(game.Player(7, 8))

    ui = game.UI(board)
    ui.update_drawable(board)

    def key_listener(key):

        if key == 'e':

            if isinstance(board.in_front_of(player_id), game.Breakable):
                board.break_in_front_of(player_id)

        else:

            dx, dy = _key_to_direction(key)
            board.face_entity(player_id, dx, dy)

            if isinstance(board.shift_destination(player_id, dx, dy), game.Walkable):
                board.shift_entity(player_id, dx, dy)

        ui.update_drawable(board)

    ui.addKeyPressListener(key_listener)
    ui.show_window()