from snap.suit import Suit
from snap.value import Value


class Card:
    _top_row = " __ "
    _bottom_row = " ‾‾ "
    _value_row = "|{}|"
    _suit_row = "| {}|"
    _hidden_row = "|++|"
    _hidden_strings = [_top_row, _hidden_row, _hidden_row, _bottom_row]

    def __init__(self, index):
        self._index = index
        self._hidden = False
        self._value = Value.string(index % 13)
        self._suit = Suit.char(index // 13)

    def suit(self):
        return self._suit

    def value(self):
        return self._value

    def hide(self):
        self._hidden = True
        return self

    def show(self):
        self._hidden = False
        return self

    def __eq__(self, other):
        return self._index == other._index

    def strings(self):
        if self._hidden:
            return Card._hidden_strings
        return [
            Card._top_row,
            Card._value_row.format(self._value),
            Card._suit_row.format(self._suit),
            Card._bottom_row,
        ]
