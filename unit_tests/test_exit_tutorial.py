"""
This module tests exit_tutorial function from tutorial.py
"""
from tutorial import exit_tutorial
from unittest import TestCase


class TestExitTutorial(TestCase):
    def test_exit_tutorial_start_location(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = exit_tutorial(test_character)
        self.assertTrue(actual)

    def test_exit_tutorial_x_coordinate_1(self):
        test_character = {'X-coordinate': 1, 'Y-coordinate': 0}
        actual = exit_tutorial(test_character)
        self.assertTrue(actual)

    def test_exit_tutorial_x_coordinate_2(self):
        test_character = {'X-coordinate': 2, 'Y-coordinate': 0}
        actual = exit_tutorial(test_character)
        self.assertTrue(actual)

    def test_exit_tutorial_x_coordinate_3(self):
        test_character = {'X-coordinate': 3, 'Y-coordinate': 0}
        actual = exit_tutorial(test_character)
        self.assertTrue(actual)

    def test_exit_tutorial_x_coordinate_4_exit(self):
        test_character = {'X-coordinate': 4, 'Y-coordinate': 0}
        actual = exit_tutorial(test_character)
        self.assertFalse(actual)