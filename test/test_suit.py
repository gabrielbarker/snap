import unittest
from snap.suit import Suit


class TestSuit(unittest.TestCase):
    def test__char__index_0_returns_heart(self):
        self.assertEqual("♡", Suit.char(0))

    def test__char__index_1_returns_diamond(self):
        self.assertEqual("♢", Suit.char(1))

    def test__char__index_2_returns_club(self):
        self.assertEqual("♣", Suit.char(2))

    def test__char__index_3_returns_spade(self):
        self.assertEqual("♠", Suit.char(3))

    def test__name__index_0_returns_heart(self):
        self.assertEqual("heart", Suit.name(0))

    def test__name__index_1_returns_diamond(self):
        self.assertEqual("diamond", Suit.name(1))

    def test__name__index_2_returns_club(self):
        self.assertEqual("club", Suit.name(2))

    def test__name__index_3_returns_spade(self):
        self.assertEqual("spade", Suit.name(3))
