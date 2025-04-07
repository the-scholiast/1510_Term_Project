"""
This module tests apply_ki_damage_attack function from battle.py
"""
from battle import apply_ki_damage_attack
from unittest import TestCase


class TestApplyKiDamageAttack(TestCase):
    def test_apply_ki_damage_attack_basic_message(self):
        test_monster = {'Current Health': 100}
        attack_description = 'Slams the ground in front of you creating a wave of Ki.'
        actual = apply_ki_damage_attack('Sunder', attack_description,
                                        35, 1.0, test_monster)
        expected = 'You used Sunder! Slams the ground in front of you creating a wave of Ki. You dealt 35 Ki damage!'
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_basic_health(self):
        test_monster = {'Current Health': 100}
        attack_description = 'Slams the ground in front of you creating a wave of Ki.'
        apply_ki_damage_attack('Sunder', attack_description, 35, 1.0, test_monster)
        expected = 65
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_to_low_health_monster_message(self):
        test_monster = {'Current Health': 10}
        attack_description = "A lion's mouth forms at the center of the shield and shoots a Ki wave."
        actual = apply_ki_damage_attack('Roar', attack_description,
                                        45, 1.0, test_monster)
        expected = ("You used Roar! A lion's mouth forms at the center of the shield and shoots a Ki wave. "
                    "You dealt 45 Ki damage!")
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_to_low_health_monster_health(self):
        test_monster = {'Current Health': 10}
        attack_description = "A lion's mouth forms at the center of the shield and shoots a Ki wave."
        apply_ki_damage_attack('Roar', attack_description, 45, 1.0, test_monster)
        expected = -35
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_with_damage_modifier_message(self):
        test_monster = {'Current Health': 100}
        attack_description = 'Splits into hundreds of smaller whips making its attack unavoidable.'
        actual = apply_ki_damage_attack('Hydra', attack_description,
                                        50, 1.5, test_monster)
        expected = ('You used Hydra! Splits into hundreds of smaller whips making its attack unavoidable. '
                    'You dealt 75 Ki damage!')
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_with_damage_modifier_health(self):
        test_monster = {'Current Health': 100}
        attack_description = 'Splits into hundreds of smaller whips making its attack unavoidable.'
        apply_ki_damage_attack('Hydra', attack_description, 50, 1.5, test_monster)
        expected = 25
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_with_fractional_damage_modifier_message(self):
        test_monster = {'Current Health': 100}
        attack_description = 'Whip entangles its target, paralyzing its victim.'
        actual = apply_ki_damage_attack('Snare', attack_description,
                                        12, 0.25, test_monster)
        expected = 'You used Snare! Whip entangles its target, paralyzing its victim. You dealt 3 Ki damage!'
        self.assertEqual(expected, actual)

    def test_apply_ki_damage_attack_with_fractional_damage_modifier_health(self):
        test_monster = {'Current Health': 100}
        attack_description = 'Whip entangles its target, paralyzing its victim.'
        apply_ki_damage_attack('Snare', attack_description, 12, 0.25, test_monster)
        expected = 97
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)