import curses
from snap.position import Position


class Screen:

    _red = None
    _green = None
    _grid_start = Position(3, 6)

    def __init__(self, screen, grid, current, flipper):
        self._screen = screen
        self._grid = grid
        self._current = current
        self._flipper = flipper
        self._initialise_colours()

    def draw_grid(self):
        self._add_grid_strings()
        self._reset()

    def draw_modified_grid(self):
        self._draw_strings(Screen._green)
        self._reset()

    def _add_grid_strings(self):
        self._draw_strings()
        self._draw_card(self._current, Screen._red)
        if self._flipper.flipped():
            self._draw_card(self._flipper.flipped(), Screen._red)

    def _draw_strings(self, mod=None):
        for index, string in enumerate(self._grid.strings()):
            self._add_grid_string(0, index, string, mod)

    def _draw_card(self, pos, mod=None):
        for i in range(4):
            x_pos = 4 * pos.x()
            x_pos_end = 4 * (pos.x() + 1)
            y_pos = 4 * pos.y() + i
            card_row = self._grid.strings()[y_pos][x_pos:x_pos_end]
            self._add_grid_string(x_pos, y_pos, card_row, mod)

    def _reset(self):
        self._screen.move(0, 0)
        self._screen.refresh()

    def hide_all(self):
        self._grid.hide_all()
        self._screen.refresh()

    def get_key_pressed(self):
        return self._screen.getch()

    def _add_grid_string(self, x, y, row, mod):
        new_x = x + Screen._grid_start.x()
        new_y = y + Screen._grid_start.y()
        self._add_string(new_x, new_y, row, mod)

    def _add_string(self, x, y, row, mod=None):
        self._screen.addstr(y, x, row, mod) if mod else self._screen.addstr(y, x, row)

    def _initialise_colours(self):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        Screen._red = curses.color_pair(1)
        Screen._green = curses.color_pair(2)

    def draw_logo(self):
        for index, string in enumerate(self._logo_strings()):
            self._add_string(Screen._grid_start.x() - 2, index, string)

    def _logo_strings(self):
        return [
            """  ____                    _ """,
            """ / ___| _ __   __ _ _ __ | |""",
            """ \___ \| '_ \ / _` | '_ \| |""",
            """  ___) | | | | (_| | |_) |_|""",
            """ |____/|_| |_|\__,_| .__/(_)""",
            """                   |_|      """,
        ]