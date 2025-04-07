"""
This module tests apply_snare_effect function from battle.py
"""
from battle import apply_snare_effect
from unittest import TestCase


class TestApplySnareEffect(TestCase):
    def test_apply_snare_effect_zero_snare_return_message(self):
        test_monster = {'Status': {'Snared': 0}}
        actual = apply_snare_effect(test_monster)
        expected = "The monster is snared and will miss its next turn!"
        self.assertEqual(expected, actual)

    def test_apply_snare_effect_zero_snare_status(self):
        test_monster = {'Status': {'Snared': 0}}
        apply_snare_effect(test_monster)
        expected = 2
        actual = test_monster['Status']['Snared']
        self.assertEqual(expected, actual)

    def test_apply_snare_effect_existing_snare_return_message(self):
        test_monster = {'Status': {'Snared': 1}}
        actual = apply_snare_effect(test_monster)
        expected = "The monster is snared and will miss its next turn!"
        self.assertEqual(expected, actual)

    def test_apply_snare_effect_existing_snare_status(self):
        test_monster = {'Status': {'Snared': 1}}
        apply_snare_effect(test_monster)
        expected = 3
        actual = test_monster['Status']['Snared']
        self.assertEqual(expected, actual)

    def test_apply_snare_effect_high_snare_return_message(self):
        test_monster = {'Status': {'Snared': 9}}
        actual = apply_snare_effect(test_monster)
        expected = "The monster is snared and will miss its next turn!"
        self.assertEqual(expected, actual)

    def test_apply_snare_effect_high_snare_status(self):
        test_monster = {'Status': {'Snared': 9}}
        apply_snare_effect(test_monster)
        expected = 11
        actual = test_monster['Status']['Snared']
        self.assertEqual(expected, actual)