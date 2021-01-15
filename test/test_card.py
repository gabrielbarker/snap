import unittest
import io
import sys
from snap.card import Card


class TestCard(unittest.TestCase):
    def test__suit__index_0__hearts(self):
        self.assertEqual(TestCard.HEARTS, Card(0).suit())

    def test__suit__index_51__spades(self):
        self.assertEqual(TestCard.SPADES, Card(51).suit())

    def test__suit__index_22__diamonds(self):
        self.assertEqual(TestCard.DIAMONDS, Card(22).suit())

    def test__suit__index_28__clubs(self):
        self.assertEqual(TestCard.CLUBS, Card(28).suit())

    def test__value__index_0__ace(self):
        self.assertEqual(TestCard.ACE, Card(0).value())

    def test__value__index_51__king(self):
        self.assertEqual(TestCard.KING, Card(51).value())

    def test__value__index_22__ten(self):
        self.assertEqual(TestCard.TEN, Card(22).value())

    def test__value__index_28__three(self):
        self.assertEqual(TestCard.THREE, Card(28).value())

    def test__strings__index_0__correct_strings_for_ace_of_hearts(self):
        self.assertEqual(TestCard.ACE_OF_HEARTS, Card(0).strings())

    def test__strings__index_51__correct_strings_for_king_of_spades(self):
        self.assertEqual(TestCard.KING_OF_SPADES, Card(51).strings())

    def test__strings__index_22__correct_strings_for_ten_of_diamonds(self):
        self.assertEqual(TestCard.TEN_OF_DIAMONDS, Card(22).strings())

    def test__strings__index_28__correct_strings_for_ten_of_diamonds(self):
        self.assertEqual(TestCard.THREE_OF_CLUBS, Card(28).strings())

    def test__strings__hide__correct_strings_for_blank_card(self):
        self.assertEqual(TestCard.BLANK, Card(28).hide().strings())

    HEARTS = "♡"
    DIAMONDS = "♢"
    CLUBS = "♣"
    SPADES = "♠"

    ACE = "A "
    KING = "K "
    TEN = "10"
    THREE = "3 "

    ACE_OF_HEARTS = [
        " __ ",
        "|A |",
        "| ♡|",
        " ‾‾ ",
    ]

    KING_OF_SPADES = [
        " __ ",
        "|K |",
        "| ♠|",
        " ‾‾ ",
    ]

    TEN_OF_DIAMONDS = [
        " __ ",
        "|10|",
        "| ♢|",
        " ‾‾ ",
    ]

    THREE_OF_CLUBS = [
        " __ ",
        "|3 |",
        "| ♣|",
        " ‾‾ ",
    ]

    BLANK = [
        " __ ",
        "|++|",
        "|++|",
        " ‾‾ ",
    ]
