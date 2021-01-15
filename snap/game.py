import time
import curses
from snap.position import Position
from snap.grid import Grid
from snap.flipper import Flipper
from threading import Timer


class Game:
    _key_map = {
        curses.KEY_RIGHT: (1, 0),
        curses.KEY_LEFT: (-1, 0),
        curses.KEY_UP: (0, -1),
        curses.KEY_DOWN: (0, 1),
    }

    def __init__(self, screen):
        self._screen = screen
        self._height = 3
        self._grid = Grid(self._height)
        self._current = Position(0, 0)
        self._flipper = Flipper(self._grid, self._current)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def play(self):
        self._draw_grid()
        time.sleep(3)
        self._grid.hide_all()
        while self._all_matched():
            self._draw_grid()
            self._get_movement()
        while True:
            self._draw_modified_grid(curses.color_pair(2))
            self._screen.refresh()

    def _all_matched(self):
        return self._flipper.number_turned() < 2 * (self._height ** 2)

    def _draw_grid(self):
        self._add_grid_strings()
        self._screen.move(0, 0)
        self._screen.refresh()

    def _add_grid_strings(self):
        self._draw_standard_grid()
        self._modify_card_at_position(self._current, curses.color_pair(1))
        if self._flipper.flipped():
            self._modify_card_at_position(self._flipper.flipped(), curses.color_pair(1))

    def _draw_standard_grid(self):
        for i in range(self._height * 4):
            self._screen.addstr(i, 0, self._grid.strings()[i])

    def _draw_modified_grid(self, mod):
        for i in range(self._height * 4):
            self._screen.addstr(i, 0, self._grid.strings()[i], mod)

    def _modify_card_at_position(self, pos, mod):
        for i in range(4):
            x_pos = 4 * pos.x()
            x_pos_end = 4 * (pos.x() + 1)
            y_pos = 4 * pos.y() + i
            card_row = self._grid.strings()[y_pos][x_pos:x_pos_end]
            self._screen.addstr(y_pos, x_pos, card_row, mod)

    def _get_movement(self):
        character_pressed = self._screen.getch()
        self._update_current_position(character_pressed)
        self._update_flipped(character_pressed)

    def _update_current_position(self, character_pressed):
        if character_pressed in Game._key_map:
            self._handle_move(character_pressed)

    def _handle_move(self, character_pressed):
        self._current.add(Game._key_map[character_pressed])
        width_height = (2 * self._height, self._height)
        self._current.add(width_height).mod(width_height)

    def _update_flipped(self, character_pressed):
        if character_pressed == curses.ascii.SP:
            self._flipper.flip()
