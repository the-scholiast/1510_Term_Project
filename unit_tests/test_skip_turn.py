"""
This module tests skip_turn function from battle.py
"""
import io
from battle import skip_turn
from unittest import TestCase
from unittest.mock import patch


class TestSkipTurn(TestCase):
    def test_skip_turn_snared_is_zero_return_false(self):
        test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 0}}
        self.assertFalse(skip_turn(test_monster))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_skip_turn_snared_is_greater_than_zero_print_message(self, mock_output):
        test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 3}}
        skip_turn(test_monster)
        actual = mock_output.getvalue()
        expected = "Werewolf is snared and cannot move this turn!\n"
        self.assertEqual(expected, actual)

    def test_skip_turn_snared_is_one_return_true(self):
        test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 1}}
        self.assertTrue(skip_turn(test_monster))

    def test_skip_turn_snared_is_two_return_true(self):
        test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 2}}
        self.assertTrue(skip_turn(test_monster))

    def test_skip_turn_snared_is_medium_return_true(self):
        test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 5}}
        self.assertTrue(skip_turn(test_monster))

    def test_skip_turn_snared_is_high_return_true(self):
        test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 11}}
        self.assertTrue(skip_turn(test_monster))