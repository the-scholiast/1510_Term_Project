"""
This module tests handle_input from tutorial.py
"""
from tutorial import handle_input
from unittest import TestCase
from unittest.mock import patch


class TestHandleInput(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_handle_input_darrow_skip_tutorial(self, _):
        actual = handle_input('Darrow', 0)
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[' '])
    def test_handle_input_darrow_skip_tutorial_whitespace(self, _):
        actual = handle_input('Darrow', 0)
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['asdf'])
    def test_handle_input_darrow_skip_tutorial_non_numeric(self, _):
        actual = handle_input('Darrow', 0)
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1'])
    def test_handle_input_darrow_do_tutorial(self, _):
        actual = handle_input('Darrow', 0)
        expected = 2
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[' '])
    def test_handle_input_darrow_whitespace_next_dialogue(self, _):
        actual = handle_input('Darrow', 1)
        expected = 2
        self.assertEqual(actual, expected)

    def test_handle_input_other_npc(self):
        actual = handle_input('Misaki', 1)
        expected = 2
        self.assertEqual(actual, expected)