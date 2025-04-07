"""
This module tests user_input_hot_spring function from encounters.py
"""
import io
from encounters import user_input_hot_spring
from unittest import TestCase
from unittest.mock import patch


class TestUserInputHotSpring(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_user_input_hot_spring_choice_one(self, _):
        expected = 1
        actual = user_input_hot_spring()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_user_input_hot_spring_choice_two(self, _):
        expected = 2
        actual = user_input_hot_spring()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["  1  "])
    def test_user_input_hot_spring_with_whitespace(self, _):
        expected = 1
        actual = user_input_hot_spring()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_hot_spring_invalid_input_message(self, mock_output, _):
        expected = "Invalid choice. Please enter 1 or 2.\n"
        user_input_hot_spring()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3", "1"])
    def test_user_input_hot_spring_invalid_then_valid_input(self, _):
        expected = 1
        actual = user_input_hot_spring()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["abc", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_hot_spring_non_numeric_input_message(self, mock_output, _):
        expected = "Invalid choice. Please enter 1 or 2.\n"
        user_input_hot_spring()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["abc", "2"])
    def test_user_input_hot_spring_non_numeric_input_then_valid_input(self, _):
        expected = 2
        actual = user_input_hot_spring()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_hot_spring_empty_input(self, mock_output, _):
        expected = "Invalid choice. Please enter 1 or 2.\n"
        user_input_hot_spring()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
