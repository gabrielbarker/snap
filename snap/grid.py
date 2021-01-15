from random import shuffle, sample
from snap.card import Card
from snap.hand import Hand


class Grid:
    def __init__(self, height):
        self._height = height
        self._hands = self._get_new_hands()

    def get(self, p):
        return self._hands[p.y()].get(p.x())

    def hide_all(self):
        [hand.hide_all() for hand in self._hands]

    def strings(self):
        strings = []
        for hand in self._hands:
            strings += hand.strings()
        return strings

    def _get_new_hands(self):
        indices = sample(range(52), self._height ** 2) * 2
        shuffle(indices)
        hands = []
        for i in range(self._height):
            row = indices[i * self._height * 2 : (i + 1) * self._height * 2]
            hands.append(Hand([Card(j) for j in row]))
        return hands
