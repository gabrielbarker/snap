import unittest
import io
import sys
from snap.position import Position


class TestPosition(unittest.TestCase):
    def test__equality__two_equal_points__returns_true(self):
        a = Position(3, 7)
        b = Position(3, 7)
        self.assertEqual(a, b)

    def test__equality__two_unequal_points__returns_false(self):
        a = Position(7, 3)
        b = Position(3, 7)
        self.assertNotEqual(a, b)

    def test__x__origin__returns_zero(self):
        self.assertEqual(0, Position(0, 0).x())

    def test__y__origin__returns_zero(self):
        self.assertEqual(0, Position(0, 0).y())

    def test__x__point__returns_x_coordinate(self):
        self.assertEqual(3, Position(3, 7).x())

    def test__y__point__returns_y_coordinate(self):
        self.assertEqual(7, Position(3, 7).y())

    def test__equality__two_equal_points__returns_true(self):
        a = Position(3, 7)
        b = Position(3, 7)
        self.assertEqual(a, b)

    def test__equality__two_unequal_points__returns_false(self):
        a = Position(7, 3)
        b = Position(3, 7)
        self.assertNotEqual(a, b)

    def test__add__two_points__returns_sum(self):
        a = Position(3, 7)
        b = Position(-4, 5)
        expected_sum = Position(3 - 4, 7 + 5)
        self.assertEqual(expected_sum, a.add(b))
        self.assertEqual(expected_sum, a)

    def test__mod_two_points__returns_sum(self):
        a = Position(12, 15)
        modulus = Position(5, 7)
        expected_result = Position(12 % 5, 15 % 7)
        self.assertEqual(expected_result, a.mod(modulus))
        self.assertEqual(expected_result, a)

    def test__times__number_and_position__returns_scalar_product(self):
        a = Position(3, 7)
        k = 3
        expected_product = Position(3 * k, 7 * k)
        self.assertEqual(expected_product, a.times(k))
        self.assertEqual(expected_product, a)