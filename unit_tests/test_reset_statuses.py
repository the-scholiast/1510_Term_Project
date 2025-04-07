"""
This module tests reset_statuses function from battle.py
"""
from battle import reset_statuses
from unittest import TestCase


class TestResetStatuses(TestCase):
    def test_reset_statuses_with_non_zero_statuses(self):
        test_character = {'Status': {'Poison': 3, 'Bleed': 2, 'Shell': 1, 'Berserk': 2}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_reset_statuses_already_zero(self):
        test_character = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_reset_statuses_duplicates(self):
        test_character = {'Status': {'Poison': 2, 'Bleed': 2, 'Shell': 2, 'Berserk': 2}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_reset_statuses_mix_zero_with_int(self):
        test_character = {'Status': {'Poison': 2, 'Bleed': 2, 'Shell': 0, 'Berserk': 0}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_reset_statuses_medium_int(self):
        test_character = {'Status': {'Poison': 5, 'Bleed': 5, 'Shell': 5, 'Berserk': 5}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_reset_statuses_int_ones(self):
        test_character = {'Status': {'Poison': 1, 'Bleed': 1, 'Shell': 1, 'Berserk': 1}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_reset_statuses_high_int(self):
        test_character = {'Status': {'Poison': 12, 'Bleed': 12, 'Shell': 12, 'Berserk': 12}}
        reset_statuses(test_character)
        expected = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
        actual = test_character
        self.assertEqual(expected, actual)