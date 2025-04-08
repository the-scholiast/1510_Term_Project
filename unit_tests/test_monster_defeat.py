"""
This module tests monster_defeat function from battle.py
"""
from battle import monster_defeat
from unittest import TestCase


class TestMonsterDefeat(TestCase):
    def test_monster_defeat_health_zero(self):
        test_monster = {'Current Health': 0}
        actual = monster_defeat(test_monster)
        self.assertTrue(actual)

    def test_monster_defeat_health_negative(self):
        test_monster = {'Current Health': -5}
        actual = monster_defeat(test_monster)
        self.assertTrue(actual)

    def test_monster_defeat_health_positive(self):
        test_monster = {'Current Health': 10}
        actual = monster_defeat(test_monster)
        self.assertFalse(actual)