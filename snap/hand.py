from snap.card import Card


class Hand:
    def __init__(self, cards=[]):
        self._cards = cards

    def get(self, index):
        return self._cards[index]

    def count(self):
        return len(self._cards)

    def hide_all(self):
        [card.hide() for card in self._cards]

    def strings(self):
        strings = ["", "", "", ""]
        for card in self._cards:
            for index, string in enumerate(card.strings()):
                strings[index] += string
        return strings