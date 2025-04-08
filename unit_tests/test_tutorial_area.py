"""
This module tests tutorial_area function from tutorial.py
"""
from tutorial import tutorial_area
from unittest import TestCase


class TestTutorialArea(TestCase):
    def test_tutorial_area_dimensions(self):
        board = tutorial_area()
        actual = len(board)
        expected = 5
        self.assertEqual(expected, actual)

    def test_tutorial_area_correct_tuple_keys_and_encounter_marker(self):
        actual = tutorial_area()
        expected = {(0, 0): '[?]', (0, 1): '[?]', (0, 2): '[?]', (0, 3): '[?]', (0, 4): '[?]'}
        self.assertEqual(actual, expected)