"""
This module tests get_user_choice_battle_menu function from battle.py
"""
import io
from battle import get_user_choice_battle_menu
from unittest import TestCase
from unittest.mock import patch


class TestGetUserChoiceBattleMenu(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_battle_menu_input_is_one(self, _):
        expected = '1'
        actual = get_user_choice_battle_menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["      1       "])
    def test_get_user_choice_battle_menu_input_is_one_with_whitespace(self, _):
        expected = '1'
        actual = get_user_choice_battle_menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_battle_menu_input_is_two(self, _):
        expected = '2'
        actual = get_user_choice_battle_menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["      2       "])
    def test_get_user_choice_battle_menu_input_is_two_with_whitespace(self, _):
        expected = '2'
        actual = get_user_choice_battle_menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_battle_menu_input_is_three(self, _):
        expected = '3'
        actual = get_user_choice_battle_menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["      3       "])
    def test_get_user_choice_battle_menu_input_is_three_with_whitespace(self, _):
        expected = '3'
        actual = get_user_choice_battle_menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0", '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_battle_menu_invalid_number_input_message(self, mock_output, _):
        expected = "Invalid choice. The option name.\n"
        get_user_choice_battle_menu()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["hello", '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_battle_menu_invalid_non_number_input_message(self, mock_output, _):
        expected = "Invalid choice. The option name.\n"
        get_user_choice_battle_menu()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["  ", '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_battle_menu_invalid_whitespace_input_message(self, mock_output, _):
        expected = "Invalid choice. The option name.\n"
        get_user_choice_battle_menu()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)