"""
This module tests process_buff_attack function from battle.py
"""
from battle import process_buff_attack
from unittest import TestCase


class TestProcessBuffAttack(TestCase):
    def test_process_buff_attack_retrieve_proper_message(self):
        test_monster = {'Damage Modifier': 1.0, 'Health Modifier': 1.0, 'Current Health': 100}
        test_description = 'Enters a berserk state, increasing Health and Damage.'
        expected = ("Monster used Lunar Frenzy! Enters a berserk state, increasing Health and Damage. "
                    "Monster's damage and Health are increased!")
        actual = process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
        self.assertEqual(expected, actual)

    def test_process_buff_attack_increase_health_damage_modifier_and_health_from_base_stats(self):
        test_monster = {'Damage Modifier': 1.0, 'Health Modifier': 1.0, 'Current Health': 100}
        test_description = 'Enters a berserk state, increasing Health and Damage.'
        expected = {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 150}
        process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
        self.assertEqual(expected, test_monster)

    def test_process_buff_attack_current_health_lower_bound(self):
        test_monster = {'Damage Modifier': 1.0, 'Health Modifier': 1.0, 'Current Health': 1}
        test_description = 'Enters a berserk state, increasing Health and Damage.'
        expected = {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 1}
        process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
        self.assertEqual(expected, test_monster)

    def test_process_buff_attack_increase_health_damage_modifier_and_health_from_non_base_stats(self):
        test_monster = {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 200}
        test_description = 'Enters a berserk state, increasing Health and Damage.'
        expected = {'Damage Modifier': 1.4, 'Health Modifier': 2.0, 'Current Health': 400}
        process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
        self.assertEqual(expected, test_monster)

    def test_process_buff_attack_retrieve_proper_message_from_non_base_stats(self):
        test_monster = {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 200}
        test_description = 'Enters a berserk state, increasing Health and Damage.'
        expected = ("Monster used Lunar Frenzy! Enters a berserk state, increasing Health and Damage. "
                    "Monster's damage and Health are increased!")
        actual = process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
        self.assertEqual(expected, actual)