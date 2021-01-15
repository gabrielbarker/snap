import time
import curses
from threading import Timer

from snap.position import Position
from snap.grid import Grid
from snap.flipper import Flipper
from snap.screen import Screen


class Game:
    _key_map = {
        curses.KEY_RIGHT: (1, 0),
        curses.KEY_LEFT: (-1, 0),
        curses.KEY_UP: (0, -1),
        curses.KEY_DOWN: (0, 1),
    }

    def __init__(self, screen):
        self._height = 3
        self._current = Position(0, 0)
        grid = Grid(self._height)
        self._flipper = Flipper(grid, self._current)
        self._screen = Screen(screen, grid, self._current, self._flipper)

    def play(self):
        self._screen.draw_logo()
        self._screen.draw_grid()
        time.sleep(3)
        self._screen.hide_all()
        while self._not_all_matched():
            self._screen.draw_grid()
            self._get_movement()
        while True:
            self._screen.draw_modified_grid()

    def _not_all_matched(self):
        total_cards = 2 * (self._height ** 2)
        return self._flipper.number_turned() < total_cards

    def _get_movement(self):
        character_pressed = self._screen.get_key_pressed()
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