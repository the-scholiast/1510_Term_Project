"""
This module tests check_character_defeat function from battle.py
"""
from battle import check_character_defeat
from unittest import TestCase


class TestCheckCharacterDefeat(TestCase):
    def test_check_character_defeat_positive_health_unchanged_message(self):
        test_character = {'Current Health': 10}
        test_message = "Monster used Swipe! You took 5 damage!"
        result = check_character_defeat(test_character, test_message)
        expected = "Monster used Swipe! You took 5 damage!"
        self.assertEqual(expected, result)

    def test_check_character_defeat_zero_health_append_defeat_message(self):
        test_character = {'Current Health': 0}
        test_message = "Monster used Swipe! You took 10 damage!"
        result = check_character_defeat(test_character, test_message)
        expected = "Monster used Swipe! You took 10 damage!\nYou have been defeated!"
        self.assertEqual(expected, result)

    def test_check_character_defeat_negative_health_append_defeat_message(self):
        test_character = {'Current Health': -5}
        test_message = "Monster used Soul Drain! You took 15 damage!"
        result = check_character_defeat(test_character, test_message)
        expected = "Monster used Soul Drain! You took 15 damage!\nYou have been defeated!"
        self.assertEqual(expected, result)