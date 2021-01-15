import curses
from snap.position import Position
from snap.screen import Screen


class Display:

    _red = None
    _green = None
    _grid_start = Position(3, 6)
    _logo_start = Position(1, 0)

    def __init__(self, screen, grid, current, flipper):
        self._screen = Screen(screen)
        self._grid = grid
        self._current = current
        self._flipper = flipper
        self._initialise_colours()

    def draw_grid(self):
        self._draw_grid()
        self._draw_card(self._current, Display._red)
        if self._flipper.flipped():
            self._draw_card(self._flipper.flipped(), Display._red)
        self._screen.refresh()

    def draw_modified_grid(self):
        self._draw_grid(Display._green)
        self._screen.refresh()

    def _draw_grid(self, mod=None):
        self._screen.draw_strings(self._grid.strings(), Display._grid_start, mod)

    def _draw_card(self, pos, mod=None):
        card_position = pos.clone().times(4).add(Display._grid_start)
        self._screen.draw_strings(self._grid.get(pos).strings(), card_position, mod)

    def hide_all(self):
        self._grid.hide_all()

    def get_key_pressed(self):
        return self._screen.get_key_pressed()

    def _initialise_colours(self):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        Display._red = curses.color_pair(1)
        Display._green = curses.color_pair(2)

    def draw_logo(self):
        self._screen.draw_strings(self._logo_strings(), Display._logo_start)

    def _logo_strings(self):
        return [
            """  ____                    _ """,
            """ / ___| _ __   __ _ _ __ | |""",
            """ \___ \| '_ \ / _` | '_ \| |""",
            """  ___) | | | | (_| | |_) |_|""",
            """ |____/|_| |_|\__,_| .__/(_)""",
            """                   |_|      """,
        ]