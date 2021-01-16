import unittest
import io
import sys
from unittest.mock import Mock, MagicMock
from snap.screen import Screen


class TestScreen(unittest.TestCase):
    def test__draw_strings__calls_addstr_on_screen(self):
        mock_screen = self.get_mock_screen()
        strings = self.get_strings()
        position = self.get_mock_position(2, 3)
        Screen(mock_screen).draw_strings(strings, position)
        expected_call_args = self.get_expected_call_args(strings, position)
        self.assertEqual(expected_call_args, mock_screen.addstr.call_args_list)

    def test__draw_strings__with_mod__calls_addstr_on_screen(self):
        mock_screen = self.get_mock_screen()
        strings = self.get_strings()
        pos = self.get_mock_position(2, 3)
        mod = 1
        Screen(mock_screen).draw_strings(strings, pos, mod)
        expected_call_args = self.get_expected_call_args_with_mod(strings, pos, mod)
        self.assertEqual(expected_call_args, mock_screen.addstr.call_args_list)

    def test__refresh__calls_refresh_on_screen(self):
        mock_screen = self.get_mock_screen()
        Screen(mock_screen).refresh()
        mock_screen.refresh.assert_called_once()

    def test__get_key_pressed__calls_getch_on_screen(self):
        mock_screen = self.get_mock_screen()
        Screen(mock_screen).get_key_pressed()
        mock_screen.getch.assert_called_once()

    def get_mock_screen(self):
        screen = Mock()
        screen.refresh.return_value = MagicMock()
        screen.getch.return_value = MagicMock()
        screen.addstr.return_value = MagicMock()
        return screen

    def get_mock_position(self, x, y):
        pos = Mock()
        pos.x.return_value = x
        pos.y.return_value = y
        return pos

    def get_strings(self):
        return ["123", "456", "789"]

    def get_expected_call_args(self, strings, pos):
        return [((pos.y() + i, pos.x(), strings[i]),) for i in range(len(strings))]

    def get_expected_call_args_with_mod(self, strings, pos, mod):
        return [((pos.y() + i, pos.x(), strings[i], mod),) for i in range(len(strings))]
