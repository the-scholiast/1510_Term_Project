"""
This module tests process_bleed_attack function from battle.py
"""
from battle import process_bleed_attack
from unittest import TestCase


class TestProcessBleedAttack(TestCase):
    def test_process_bleed_attack_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        actual = process_bleed_attack(test_character, monster_modifier, defense_modifier,
                                      damage, test_attack, test_description)
        expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
                    'You took 10 damage and are bleeding!')
        self.assertEqual(expected, actual)

    def test_process_bleed_attack_character_loses_health_and_increase_bleed(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 90, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_increased_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 1.5
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        actual = process_bleed_attack(test_character, monster_modifier, defense_modifier,
                                      damage, test_attack, test_description)
        expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
                    'You took 15 damage and are bleeding!')
        self.assertEqual(expected, actual)

    def test_process_bleed_attack_increased_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 1.5
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 85, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_reduced_defense_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        actual = process_bleed_attack(test_character, monster_modifier, defense_modifier,
                                      damage, test_attack, test_description)
        expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
                    'You took 5 damage and are bleeding!')
        self.assertEqual(expected, actual)

    def test_process_bleed_attack_reduced_defense_modifier_character_loses_health(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 95, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_different_defense_and_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 2.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        actual = process_bleed_attack(test_character, monster_modifier, defense_modifier,
                                      damage, test_attack, test_description)
        expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
                    'You took 10 damage and are bleeding!')
        self.assertEqual(expected, actual)

    def test_process_bleed_attack_different_defense_and_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
        monster_modifier = 2.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 90, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_character_loses_health_to_0(self):
        test_character = {'Current Health': 10, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 0, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_character_loses_health_below_0(self):
        test_character = {'Current Health': 5, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': -5, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_Bleed_is_0(self):
        test_character = {'Current Health': 20, 'Status': {'Bleed': 0}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 10, 'Status': {'Bleed': 2}}
        self.assertEqual(expected, test_character)

    def test_process_bleed_attack_Bleed_is_not_0(self):
        test_character = {'Current Health': 20, 'Status': {'Bleed': 2}}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Bite'
        test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
        process_bleed_attack(test_character, monster_modifier, defense_modifier,
                             damage, test_attack, test_description)
        expected = {'Current Health': 10, 'Status': {'Bleed': 4}}
        self.assertEqual(expected, test_character)
