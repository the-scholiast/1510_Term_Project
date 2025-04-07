"""
This module tests calculate_monster_damage_modifier function from battle.py
"""
from battle import calculate_monster_damage_modifier
from unittest import TestCase


class TestCalculateMonsterDamageModifier(TestCase):
    def test_calculate_monster_damage_modifier_level_one(self):
        expected = 1.0
        actual = calculate_monster_damage_modifier(1)
        self.assertEqual(expected, actual)

    def test_calculate_monster_damage_modifier_level_two(self):
        expected = 1.2
        actual = calculate_monster_damage_modifier(2)
        self.assertEqual(expected, actual)

    def test_calculate_monster_damage_modifier_level_three(self):
        expected = 1.5
        actual = calculate_monster_damage_modifier(3)
        self.assertEqual(expected, actual)
