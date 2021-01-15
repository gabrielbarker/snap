import unittest
from snap.value import Value


class TestValue(unittest.TestCase):
    def test__string__index_0_returns_A(self):
        self.assertEqual("A ", Value.string(0))

    def test__string__index_1_returns_2(self):
        self.assertEqual("2 ", Value.string(1))

    def test__string__index_9_returns_10(self):
        self.assertEqual("10", Value.string(9))

    def test__string__index_10_returns_J(self):
        self.assertEqual("J ", Value.string(10))

    def test__string__index_11_returns_Q(self):
        self.assertEqual("Q ", Value.string(11))

    def test__string__index_12_returns_K(self):
        self.assertEqual("K ", Value.string(12))

    def test__name__index_0_returns_ace(self):
        self.assertEqual("ace", Value.name(0))

    def test__name__index_1_returns_2(self):
        self.assertEqual("2", Value.name(1))

    def test__name__index_9_returns_10(self):
        self.assertEqual("10", Value.name(9))

    def test__name__index_10_returns_jack(self):
        self.assertEqual("jack", Value.name(10))

    def test__name__index_11_returns_queen(self):
        self.assertEqual("queen", Value.name(11))

    def test__name__index_12_returns_king(self):
        self.assertEqual("king", Value.name(12))
