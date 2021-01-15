import curses
from snap.position import Position


class Screen:
    def __init__(self, screen):
        self._screen = screen

    def draw_strings(self, strings, position, mod=None):
        for index, string in enumerate(strings):
            self._add_string(position.x(), position.y() + index, string, mod)
        self._screen.move(0, 0)

    def refresh(self):
        self._screen.refresh()

    def get_key_pressed(self):
        return self._screen.getch()

    def _add_string(self, x, y, row, mod=None):
        self._screen.addstr(y, x, row, mod) if mod else self._screen.addstr(y, x, row)