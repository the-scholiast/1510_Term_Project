"""
This module tests get_stance function from battle.py
"""
import io
from battle import get_stance
from unittest import TestCase
from unittest.mock import patch


class TestGetStance(TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_get_stance_input_0_back(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        actual = get_stance(test_character)
        self.assertIsNone(actual)

    @patch('builtins.input', side_effect=["0"])
    def test_get_stance_input_0_back_no_change(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        self.assertEqual(expected, test_character)

    @patch('builtins.input', side_effect=["1"])
    def test_user_input_1_bear_stance(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        self.assertEqual(expected, test_character)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_1_bear_stance_print_message(self, mock_output, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = ("You adopt the Bear stance!\n"
                    "Clavem transforms into a giant greatsword. "
                    "The edges aren't very sharp but it packs a huge punch.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_user_input_2_turtle_stance(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Turtle'}
        self.assertEqual(expected, test_character)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_2_turtle_stance_print_message(self, mock_output, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = ("You adopt the Turtle stance!\n"
                    "Clavem transforms into a shield. "
                    "The outer shield can be imbued with ki.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_user_input_3_snake_stance(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Snake'}
        self.assertEqual(expected, test_character)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_3_snake_stance_print_message(self, mock_output, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = ("You adopt the Snake stance!\n"
                    "Clavem transforms into a whip. "
                    "It can extend to great lengths or split into hundreds of smaller whips.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "0"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_invalid_input_message(self, mock_output, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = "Invalid stance. Please select from the available options.\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["5", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_input_invalid_input_then_valid_input_message(self, mock_output, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = ("Invalid stance. Please select from the available options.\n"
                    "You adopt the Bear stance!\n"
                    "Clavem transforms into a giant greatsword. "
                    "The edges aren't very sharp but it packs a huge punch.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1"])
    def test_user_input_same_as_active_stance(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        get_stance(test_character)
        expected = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        self.assertEqual(expected, test_character)

    @patch('builtins.input', side_effect=["5", "0"])
    def test_user_input_invalid_input_then_valid_input(self, _):
        test_character = {'Stance': ['Bear', 'Turtle', 'Snake'], 'Active Stance': 'Bear'}
        expected = None
        actual = get_stance(test_character)
        self.assertEqual(expected, actual)