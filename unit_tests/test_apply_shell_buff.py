"""
This module tests apply_shell_buff function from battle.py
"""
from battle import apply_shell_buff
from unittest import TestCase


class TestApplyShellBuff(TestCase):
    def test_apply_shell_buff_return_message(self):
        test_character = {'Active Defense Modifier': 1.0, 'Status': {'Shell': 0}}
        actual = apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = "You used Shell! Take no damage next two turns."
        self.assertEqual(expected, actual)

    def test_apply_shell_buff_shell_status_zero(self):
        test_character = {'Active Defense Modifier': 1.0, 'Status': {'Shell': 0}}
        apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = 4
        actual = test_character['Status']['Shell']
        self.assertEqual(expected, actual)

    def test_apply_shell_buff_active_defense_modifier_non_zero(self):
        test_character = {'Active Defense Modifier': 1.0, 'Status': {'Shell': 0}}
        apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = 0.0
        actual = test_character['Active Defense Modifier']
        self.assertEqual(expected, actual)

    def test_apply_shell_buff_shell_status_existing(self):
        test_character = {'Active Defense Modifier': 0.0, 'Status': {'Shell': 3}}
        apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = 7
        actual = test_character['Status']['Shell']
        self.assertEqual(expected, actual)

    def test_apply_shell_buff_active_defense_modifier_already_zero(self):
        test_character = {'Active Defense Modifier': 0.0, 'Status': {'Shell': 3}}
        apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = 0.0
        actual = test_character['Active Defense Modifier']
        self.assertEqual(expected, actual)

    def test_apply_shell_buff_shell_status_high(self):
        test_character = {'Active Defense Modifier': 0.5, 'Status': {'Shell': 10}}
        apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = 14
        actual = test_character['Status']['Shell']
        self.assertEqual(expected, actual)

    def test_apply_shell_buff_active_defense_modifier_non_zero_float(self):
        test_character = {'Active Defense Modifier': 0.5, 'Status': {'Shell': 10}}
        apply_shell_buff('Shell', 'Take no damage next two turns.', test_character)
        expected = 0.0
        actual = test_character['Active Defense Modifier']
        self.assertEqual(expected, actual)