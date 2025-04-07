"""
This module tests process_poison_attack function from battle.py
"""
from battle import process_poison_attack
from unittest import TestCase


class TestProcessPoisonAttack(TestCase):
    def test_process_poison_attack_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        actual = process_poison_attack(test_character, monster_modifier, defense_modifier,
                                       damage, test_attack, test_description)
        expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
                    'You took 10 damage and are poisoned!')
        self.assertEqual(expected, actual)

    def test_process_poison_attack_character_loses_health_and_increase_poison(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 90, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_increased_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 1.5
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        actual = process_poison_attack(test_character, monster_modifier, defense_modifier,
                                       damage, test_attack, test_description)
        expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
                    'You took 15 damage and are poisoned!')
        self.assertEqual(expected, actual)

    def test_process_poison_attack_increased_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 1.5
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 85, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_reduced_defense_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        actual = process_poison_attack(test_character, monster_modifier, defense_modifier,
                                       damage, test_attack, test_description)
        expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
                    'You took 5 damage and are poisoned!')
        self.assertEqual(expected, actual)

    def test_process_poison_attack_reduced_defense_modifier_character_loses_health(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 95, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_different_defense_and_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 2.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        actual = process_poison_attack(test_character, monster_modifier, defense_modifier,
                                       damage, test_attack, test_description)
        expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
                    'You took 10 damage and are poisoned!')
        self.assertEqual(expected, actual)

    def test_process_poison_attack_different_defense_and_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
        monster_modifier = 2.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 90, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_character_loses_health_to_0(self):
        test_character = {'Current Health': 10, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 0, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_character_loses_health_below_0(self):
        test_character = {'Current Health': 5, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': -5, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_poison_is_0(self):
        test_character = {'Current Health': 20, 'Status': {'Poison': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 10, 'Status': {'Poison': 4}}
        self.assertEqual(expected, test_character)

    def test_process_poison_attack_poison_is_not_0(self):
        test_character = {'Current Health': 20, 'Status': {'Poison': 4}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Poison Bite'
        test_description = 'A venomous bite that inflicts poison damage over time.'
        process_poison_attack(test_character, monster_modifier, defense_modifier,
                              damage, test_attack, test_description)
        expected = {'Current Health': 10, 'Status': {'Poison': 8}}
        self.assertEqual(expected, test_character)