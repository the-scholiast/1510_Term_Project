"""
This module tests get_attack_choice from battle.py
"""
import io
from battle import get_attack_choice
from unittest import TestCase
from unittest.mock import patch


class TestGetAttackChoice(TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_get_attack_choice_input_0_return_none(self, _):
        expected = None
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        actual = get_attack_choice(attacks)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["    0    "])
    def test_get_attack_choice_input_with_whitespace(self, _):
        expected = None
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        actual = get_attack_choice(attacks)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1"])
    def test_get_attack_choice_input_1_return_attack_move(self, _):
        expected = ('Heavy Strike', ['A powerful blow with massive physical damage.', 'Physical', 20])
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        actual = get_attack_choice(attacks)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_attack_choice_input_2_return_attack_move(self, _):
        expected = ('Sunder', ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35])
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        actual = get_attack_choice(attacks)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_attack_choice_input_3_return_attack_move(self, _):
        expected = ('Berserk', ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0])
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        actual = get_attack_choice(attacks)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["hi", '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_attack_choice_input_not_number_ValueError_continue_loop(self, mock_output, _):
        expected = "Please enter a valid number.\n"
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        get_attack_choice(attacks)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_attack_choice_input_number_invalid_continue_loop(self, mock_output, _):
        expected = "Invalid choice. Please enter a number between 0 and 3\n"
        attacks = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        get_attack_choice(attacks)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)