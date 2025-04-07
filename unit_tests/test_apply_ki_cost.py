"""
This module tests apply_ki_cost function from battle.py
"""
from battle import apply_ki_cost
from unittest import TestCase


class TestApplyKiCost(TestCase):
    def test_apply_ki_cost_reduce_ki(self):
        test_character = {'Current Ki': 50}
        apply_ki_cost(test_character)
        expected = {'Current Ki': 40}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_apply_ki_cost_reduce_to_zero_ki(self):
        test_character = {'Current Ki': 10}
        apply_ki_cost(test_character)
        expected = {'Current Ki': 0}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_apply_ki_cost_high_current_ki_reduce_ki(self):
        test_character = {'Current Ki': 100}
        apply_ki_cost(test_character)
        expected = {'Current Ki': 90}
        actual = test_character
        self.assertEqual(expected, actual)