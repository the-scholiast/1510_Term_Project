"""
This module tests print_attack_result function from battle.py
"""
import io
from battle import print_attack_result
from unittest import TestCase
from unittest.mock import patch


class TestPrintAttackResult(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_attack_result_successful_physical_attack(self, mock_output):
        print_attack_result('Physical', True, 'You hit the monster for 20 damage!')
        expected = 'You hit the monster for 20 damage!\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_attack_result_successful_ki_attack(self, mock_output):
        print_attack_result('Ki', True, 'You unleash a powerful Ki wave!')
        expected = 'You unleash a powerful Ki wave!\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_attack_result_failed_ki_attack(self, mock_output):
        print_attack_result('Ki', False, 'Some message')
        expected = "You don't have enough Ki to use this attack! Choose another action.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_attack_result_failed_physical_attack_no_output(self, mock_output):
        print_attack_result('Physical', False, 'Some message')
        expected = ''
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)