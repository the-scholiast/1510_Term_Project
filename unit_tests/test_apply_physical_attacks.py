"""
This module tests apply_physical_attack function from battle.py
"""
from battle import apply_physical_attack
from unittest import TestCase


class TestApplyPhysicalAttack(TestCase):
    def test_apply_physical_attack_basic_message(self):
        test_monster = {'Current Health': 100}
        description = 'A powerful blow with massive physical damage.'
        actual = apply_physical_attack('Heavy Strike',
                                       description, 20, 1.0, test_monster)
        expected = 'You used Heavy Strike! A powerful blow with massive physical damage. You dealt 20 damage!'
        self.assertEqual(expected, actual)

    def test_apply_physical_attack_basic_health(self):
        test_monster = {'Current Health': 100}
        description = 'A powerful blow with massive physical damage.'
        apply_physical_attack('Heavy Strike', description, 20, 1.0, test_monster)
        expected = 80
        self.assertEqual(expected, test_monster['Current Health'])

    def test_apply_physical_attack_with_damage_modifier_message(self):
        test_monster = {'Current Health': 100}
        description = 'Whip extends to lash its target.'
        actual = apply_physical_attack('Lash', description, 20, 1.5, test_monster)
        expected = 'You used Lash! Whip extends to lash its target. You dealt 30 damage!'
        self.assertEqual(expected, actual)

    def test_apply_physical_attack_with_damage_modifier_health(self):
        test_monster = {'Current Health': 100}
        description = 'Whip extends to lash its target.'
        apply_physical_attack('Lash', description, 20, 1.5, test_monster)
        expected = 70
        self.assertEqual(expected, test_monster['Current Health'])

    def test_apply_physical_attack_to_low_health_monster_message(self):
        test_monster = {'Current Health': 10}
        description = 'A powerful blow with massive physical damage.'
        actual = apply_physical_attack('Heavy Strike', description,
                                       20, 1.0, test_monster)
        expected = 'You used Heavy Strike! A powerful blow with massive physical damage. You dealt 20 damage!'
        self.assertEqual(expected, actual)

    def test_apply_physical_attack_to_low_health_monster_health(self):
        test_monster = {'Current Health': 10}
        description = 'A powerful blow with massive physical damage.'
        apply_physical_attack('Heavy Strike', description, 20, 1.0, test_monster)
        expected = -10
        self.assertEqual(expected, test_monster['Current Health'])

    def test_apply_physical_attack_with_zero_damage_modifier_message(self):
        test_monster = {'Current Health': 100}
        description = 'A feeble attempt at an attack.'
        actual = apply_physical_attack('Weak Strike', description,
                                       20, 0.0, test_monster)
        expected = 'You used Weak Strike! A feeble attempt at an attack. You dealt 0 damage!'
        self.assertEqual(expected, actual)

    def test_apply_physical_attack_with_zero_damage_modifier_health(self):
        test_monster = {'Current Health': 100}
        description = 'A feeble attempt at an attack.'
        apply_physical_attack('Weak Strike', description, 20, 0.0, test_monster)
        expected = 100
        self.assertEqual(expected, test_monster['Current Health'])

    def test_apply_physical_attack_with_fractional_damage_modifier_message(self):
        test_monster = {'Current Health': 100}
        description = 'A glancing hit that does minimal damage.'
        actual = apply_physical_attack('Glancing Blow', description,
                                       20, 0.25, test_monster)
        expected = 'You used Glancing Blow! A glancing hit that does minimal damage. You dealt 5 damage!'
        self.assertEqual(expected, actual)

    def test_apply_physical_attack_with_fractional_damage_modifier_health(self):
        test_monster = {'Current Health': 100}
        description = 'A glancing hit that does minimal damage.'
        apply_physical_attack('Glancing Blow', description, 20, 0.25, test_monster)
        expected_health = 95
        self.assertEqual(expected_health, test_monster['Current Health'])