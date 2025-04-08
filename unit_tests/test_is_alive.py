"""
This module tests is_alive function from game.py
"""
from game import is_alive
from unittest import TestCase


class TestIsAlive(TestCase):
    def test_is_alive_health_greater_than_0(self):
        test_character = {"Current Health": 100}
        actual = is_alive(test_character)
        self.assertTrue(actual)

    def test_is_alive_health_1(self):
        test_character = {"Current Health": 1}
        actual = is_alive(test_character)
        self.assertTrue(actual)

    def test_is_alive_health_0(self):
        test_character = {"Current Health": 0}
        actual = is_alive(test_character)
        self.assertFalse(actual)

    def test_is_alive_health_negative(self):
        test_character = {"Current Health": -10}
        actual = is_alive(test_character)
        self.assertFalse(actual)