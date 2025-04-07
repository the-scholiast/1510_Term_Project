"""
This module tests process_heal_attack function from battle.py
"""
from battle import process_heal_attack
from unittest import TestCase


class TestProcessHealAttack(TestCase):
    def test_process_heal_attack_retrieve_proper_message(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        actual = process_heal_attack(test_character, test_monster, damage, defense_modifier,
                                     test_attack, test_description)
        expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
                    'You took 6 damage! Monster healed for 3 health!')
        self.assertEqual(expected, actual)

    def test_process_heal_attack_character_loses_health(self):
        test_character = {'Current Health': 120}
        test_monster = {'Current Health': 110, 'Damage Modifier': 1.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 114}
        self.assertEqual(expected, test_character)

    def test_process_heal_attack_character_loses_health_with_fractional_damage(self):
        test_character = {'Current Health': 120}
        test_monster = {'Current Health': 110, 'Damage Modifier': 1.25}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 113}
        self.assertEqual(expected, test_character)

    def test_process_heal_attack_monster_gains_health(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 103, 'Damage Modifier': 1.0}
        self.assertEqual(expected, test_monster)

    def test_process_heal_attack_increased_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 50}
        test_monster = {'Current Health': 100, 'Damage Modifier': 2.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        actual = process_heal_attack(test_character, test_monster, damage, defense_modifier,
                                     test_attack, test_description)
        expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
                    'You took 12 damage! Monster healed for 6 health!')
        self.assertEqual(expected, actual)

    def test_process_heal_attack_increased_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 2.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 88}
        self.assertEqual(expected, test_character)

    def test_process_heal_attack_increased_monster_modifier_monster_gains_health(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 2.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 106, 'Damage Modifier': 2.0}
        self.assertEqual(expected, test_monster)

    def test_process_heal_attack_reduced_defense_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
        defense_modifier = 0.5
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        actual = process_heal_attack(test_character, test_monster, damage, defense_modifier,
                                     test_attack, test_description)
        expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
                    'You took 3 damage! Monster healed for 1 health!')
        self.assertEqual(expected, actual)

    def test_process_heal_attack_reduced_defense_modifier_character_loses_health(self):
        test_character = {'Current Health': 200}
        test_monster = {'Current Health': 200, 'Damage Modifier': 1.0}
        defense_modifier = 0.5
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 197}
        self.assertEqual(expected, test_character)

    def test_process_heal_attack_reduced_defense_modifier_monster_gains_health(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
        defense_modifier = 0.5
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 101, 'Damage Modifier': 1.0}
        self.assertEqual(expected, test_monster)

    def test_process_heal_attack_different_defense_and_monster_modifier_retrieve_proper_message(self):
        test_character = {'Current Health': 200}
        test_monster = {'Current Health': 200, 'Damage Modifier': 2.0}
        defense_modifier = 0.5
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        actual = process_heal_attack(test_character, test_monster, damage, defense_modifier,
                                     test_attack, test_description)
        expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
                    'You took 6 damage! Monster healed for 3 health!')
        self.assertEqual(expected, actual)

    def test_process_heal_attack_different_defense_and_monster_modifier_character_loses_health(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 2.0}
        defense_modifier = 0.5
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 94}
        self.assertEqual(expected, test_character)

    def test_process_heal_different_defense_and_monster_modifier_gains_health(self):
        test_character = {'Current Health': 100}
        test_monster = {'Current Health': 100, 'Damage Modifier': 2.0}
        defense_modifier = 0.5
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 103, 'Damage Modifier': 2.0}
        self.assertEqual(expected, test_monster)

    def test_process_heal_attack_character_loses_health_to_0(self):
        test_character = {'Current Health': 6}
        test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': 0}
        self.assertEqual(expected, test_character)

    def test_process_heal_attack_character_loses_health_below_0(self):
        test_character = {'Current Health': 3}
        test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
        defense_modifier = 1.0
        damage = 6
        test_attack = 'Blood Drain'
        test_description = 'Drinks the target’s blood to restore health.'
        process_heal_attack(test_character, test_monster, damage, defense_modifier,
                            test_attack, test_description)
        expected = {'Current Health': -3}
        self.assertEqual(expected, test_character)