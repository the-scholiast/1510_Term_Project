"""
This module tests the tutorial_npcs function from tutorial.py
"""
from tutorial import tutorial_npcs
from unittest import TestCase


class TestTutorialNPCs(TestCase):
    def test_tutorial_npcs_self(self):
        actual = tutorial_npcs((0, 0))
        expected = 'Self'
        self.assertEqual(actual, expected)

    def test_tutorial_npcs_darrow(self):
        actual = tutorial_npcs((1, 0))
        expected = 'Darrow'
        self.assertEqual(actual, expected)

    def test_tutorial_npcs_misaki(self):
        actual = tutorial_npcs((2, 0))
        expected = 'Misaki'
        self.assertEqual(actual, expected)

    def test_tutorial_npcs_ragnar(self):
        actual = tutorial_npcs((3, 0))
        expected = 'Ragnar'
        self.assertEqual(actual, expected)