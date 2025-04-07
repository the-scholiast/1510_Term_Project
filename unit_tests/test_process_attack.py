"""
This module tests process_attack function from battle.py
"""
from battle import process_attack
from unittest import TestCase


class TestProcessAttack(TestCase):
    def test_process_attack_retrieve_proper_message(self):
        test_character = {'Current Health': 100}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        actual = process_attack(test_character, monster_modifier, defense_modifier,
                                damage, test_attack, test_description)
        expected = 'Monster used Swipe! A vicious claw attack dealing physical damage. You took 10 damage!'
        self.assertEqual(expected, actual)

    def test_process_attack_character_loses_health(self):
        test_character = {'Current Health': 100}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': 90}
        self.assertEqual(expected, test_character)

    def test_process_attack_character_loses_health_with_fractional_damage(self):
        test_character = {'Current Health': 100}
        monster_modifier = 1.25
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': 88}
        self.assertEqual(expected, test_character)

    def test_process_attack_increased_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 120}
        monster_modifier = 1.5
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        actual = process_attack(test_character, monster_modifier, defense_modifier,
                                damage, test_attack, test_description)
        expected = 'Monster used Swipe! A vicious claw attack dealing physical damage. You took 15 damage!'
        self.assertEqual(expected, actual)

    def test_process_attack_increased_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 120}
        monster_modifier = 1.5
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': 105}
        self.assertEqual(expected, test_character)

    def test_process_attack_reduced_defense_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100}
        monster_modifier = 1.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        actual = process_attack(test_character, monster_modifier, defense_modifier,
                                damage, test_attack, test_description)
        expected = 'Monster used Swipe! A vicious claw attack dealing physical damage. You took 5 damage!'
        self.assertEqual(expected, actual)

    def test_process_attack_reduced_defense_modifier_character_loses_health(self):
        test_character = {'Current Health': 100}
        monster_modifier = 1.0
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': 95}
        self.assertEqual(expected, test_character)

    def test_process_attack_different_defense_and_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 50}
        monster_modifier = 1.5
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        actual = process_attack(test_character, monster_modifier, defense_modifier,
                                damage, test_attack, test_description)
        expected = 'Monster used Swipe! A vicious claw attack dealing physical damage. You took 7 damage!'
        self.assertEqual(expected, actual)

    def test_process_attack_different_defense_and_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 50}
        monster_modifier = 1.5
        defense_modifier = 0.5
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': 43}
        self.assertEqual(expected, test_character)

    def test_process_attack_character_loses_health_to_0(self):
        test_character = {'Current Health': 10}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': 0}
        self.assertEqual(expected, test_character)

    def test_process_attack_character_loses_health_below_0(self):
        test_character = {'Current Health': 5}
        monster_modifier = 1.0
        defense_modifier = 1.0
        damage = 10
        test_attack = 'Swipe'
        test_description = 'A vicious claw attack dealing physical damage.'
        process_attack(test_character, monster_modifier, defense_modifier,
                       damage, test_attack, test_description)
        expected = {'Current Health': -5}
        self.assertEqual(expected, test_character)