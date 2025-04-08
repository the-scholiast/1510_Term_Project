"""
This module tests check_crystals from game.py
"""
from game import check_crystals
from unittest import TestCase


class TestCheckCrystals(TestCase):
    def test_check_crystals_100(self):
        test_character = {'Crystals': 100}
        actual = check_crystals(test_character)
        self.assertTrue(actual)

    def test_check_crystals_0(self):
        test_character = {'Crystals': 0}
        actual = check_crystals(test_character)
        self.assertFalse(actual)

    def test_check_crystals_low(self):
        test_character = {'Crystals': 10}
        actual = check_crystals(test_character)
        self.assertFalse(actual)

    def test_check_crystals_medium(self):
        test_character = {'Crystals': 50}
        actual = check_crystals(test_character)
        self.assertFalse(actual)

    def test_check_crystals_99(self):
        test_character = {'Crystals': 99}
        actual = check_crystals(test_character)
        self.assertFalse(actual)