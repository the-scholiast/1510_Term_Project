"""
This module tests apply_status_damage function from battle.py
"""
from battle import apply_status_damage
from unittest import TestCase


class TestApplyStatusDamage(TestCase):
    def test_apply_status_damage_poison_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 3, 'Bleed': 0}}
        actual = apply_status_damage(test_character)
        expected = 'You take 5 damage from Poison!'
        self.assertEqual(expected, actual)

    def test_apply_status_damage_poison_health_reduction(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 3, 'Bleed': 0}}
        apply_status_damage(test_character)
        expected = {'Current Health': 95, 'Status': {'Poison': 3, 'Bleed': 0}}
        self.assertEqual(expected, test_character)

    def test_apply_status_damage_bleed_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 2}}
        actual = apply_status_damage(test_character)
        expected = 'You take 15 damage from Bleed!'
        self.assertEqual(expected, actual)

    def test_apply_status_damage_bleed_health_reduction(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 2}}
        apply_status_damage(test_character)
        expected = {'Current Health': 85, 'Status': {'Poison': 0, 'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_apply_status_damage_no_status_effects_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 0}}
        actual = apply_status_damage(test_character)
        expected = ''
        self.assertEqual(expected, actual)

    def test_apply_status_damage_no_status_effects_no_health_change(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 0}}
        apply_status_damage(test_character)
        expected = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 0}}
        self.assertEqual(expected, test_character)

    def test_apply_status_damage_poison_low_health(self):
        test_character = {'Current Health': 5, 'Status': {'Poison': 2, 'Bleed': 0}}
        apply_status_damage(test_character)
        expected = {'Current Health': 0, 'Status': {'Poison': 2, 'Bleed': 0}}
        self.assertEqual(expected, test_character)

    def test_apply_status_damage_bleed_low_health(self):
        test_character = {'Current Health': 10, 'Status': {'Poison': 0, 'Bleed': 1}}
        apply_status_damage(test_character)
        expected = {'Current Health': -5, 'Status': {'Poison': 0, 'Bleed': 1}}
        self.assertEqual(expected, test_character)