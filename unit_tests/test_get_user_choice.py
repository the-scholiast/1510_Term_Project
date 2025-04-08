"""
This module tests get_user_choice function from character_module.py
"""
from character_module import get_user_choice
from unittest import TestCase
from unittest.mock import patch


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value="1")
    def test_get_user_choice_input_1(self, _):
        actual = get_user_choice()
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    def test_get_user_choice_input_2(self, _):
        actual = get_user_choice()
        expected = 2
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    def test_get_user_choice_input_3(self, _):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="4")
    def test_get_user_choice_input_4(self, _):
        actual = get_user_choice()
        expected = 4
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0", "1"])
    def test_get_user_choice_invalid_then_valid(self, _):
        actual = get_user_choice()
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "3"])
    def test_get_user_choice_out_of_range_then_valid(self, _):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["abc", "2"])
    def test_get_user_choice_non_digit_then_valid(self, _):
        actual = get_user_choice()
        expected = 2
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["  4  "])
    def test_get_user_choice_with_whitespace(self, _):
        actual = get_user_choice()
        expected = 4
        self.assertEqual(expected, actual)