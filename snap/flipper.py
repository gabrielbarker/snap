from threading import Timer


class Flipper:
    def __init__(self, grid, current_position):
        self._current = current_position
        self._grid = grid
        self._flipped = None
        self._turned = []

    def flip(self):
        self._grid.get(self._current).show()
        if self._is_not_distinct_card():
            return
        if self._flipped:
            self._compare()
        else:
            self._flipped = self._current.clone()

    def flipped(self):
        return self._flipped

    def number_turned(self):
        return len(self._turned)

    def _is_not_distinct_card(self):
        is_turned = self._turned.count(self._current) > 0
        is_in_same_spot = self._flipped and (self._flipped == self._current)
        return is_turned or is_in_same_spot

    def _compare(self):
        if self._flipped_equals_position():
            self._add_to_matched()
        else:
            self._hide_after_interval()
        self._flipped = None

    def _flipped_equals_position(self):
        flipped = self._grid.get(self._flipped)
        current = self._grid.get(self._current)
        return flipped == current

    def _add_to_matched(self):
        self._turned.append(self._flipped)
        self._turned.append(self._current.clone())

    def _hide_after_interval(self):
        flipped = self._grid.get(self._flipped)
        current = self._grid.get(self._current)
        hide_cards = lambda: self._hide_flipped_and_current_card(flipped, current)
        Timer(0.5, hide_cards).start()

    def _hide_flipped_and_current_card(self, flipped, current):
        current.hide()
        flipped.hide()