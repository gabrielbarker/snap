import unittest
import io
import sys
from unittest.mock import Mock, patch
from snap.hand import Hand
from snap.card import Card


class TestHand(unittest.TestCase):
    def test__count__mock_cards__returns_correct_number(self):
        expected_count = 5
        hand = Hand([self.mock_card() for _ in range(expected_count)])
        self.assertEqual(expected_count, hand.count())

    def test__count__empty_hand__returns_zero(self):
        hand = Hand()
        self.assertEqual(0, hand.count())

    def test__get__valid_index__returns_correct_card(self):
        expected_values = self.expected_values(5)
        hand = Hand([self.mock_card(val) for val in expected_values])
        for i in range(5):
            card = hand.get(i)
            self.assertEqual(expected_values[i], card.value())

    def test__strings__mock_cards__returns_correct_strings(self):
        hand = Hand([self.mock_card() for _ in range(5)])
        self.assertEqual(TestHand.FIVE_ACE_OF_HEARTS, hand.strings())

    def expected_values(self, number):
        return ["value-" + str(i + 1) for i in range(number)]

    def mock_card(self, value="0"):
        card = Mock()
        card.value.return_value = value
        card.strings.return_value = TestHand.ACE_OF_HEARTS
        return card

    ACE_OF_HEARTS = [
        " __ ",
        "|A |",
        "| ♡|",
        " ‾‾ ",
    ]

    FIVE_ACE_OF_HEARTS = [
        " __  __  __  __  __ ",
        "|A ||A ||A ||A ||A |",
        "| ♡|| ♡|| ♡|| ♡|| ♡|",
        " ‾‾  ‾‾  ‾‾  ‾‾  ‾‾ ",
    ]
