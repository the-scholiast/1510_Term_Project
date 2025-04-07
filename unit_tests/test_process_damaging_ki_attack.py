"""
This module tests process_damaging_ki_attack function from battle.py
"""
from battle import process_damaging_ki_attack
from unittest import TestCase


class TestProcessDamagingKiAttack(TestCase):
    def test_process_damaging_ki_attack_return_message(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        actual = process_damaging_ki_attack('Sunder',
                                            'Slams the ground in front of you creating a wave of Ki.',
                                            35, 1.0, test_character, test_monster)
        expected = 'You used Sunder! Slams the ground in front of you creating a wave of Ki. You dealt 35 Ki damage!'
        self.assertEqual(expected, actual)

    def test_process_damaging_ki_attack_ki_reduction(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}

        process_damaging_ki_attack('Sunder',
                                   'Slams the ground in front of you creating a wave of Ki.',
                                   35, 1.0, test_character, test_monster)
        expected = 40
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_process_damaging_ki_attack_ki_lower_bound_reduction(self):
        test_character = {'Current Ki': 10}
        test_monster = {'Current Health': 100}

        process_damaging_ki_attack('Sunder',
                                   'Slams the ground in front of you creating a wave of Ki.',
                                   35, 1.0, test_character, test_monster)
        expected = 0
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_process_damaging_ki_attack_monster_health_reduction(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        process_damaging_ki_attack('Sunder',
                                   'Slams the ground in front of you creating a wave of Ki.',
                                   35, 1.0, test_character, test_monster)
        expected = 65
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_process_damaging_ki_attack_monster_low_health_reduction(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 10}
        process_damaging_ki_attack('Sunder',
                                   'Slams the ground in front of you creating a wave of Ki.',
                                   35, 1.0, test_character, test_monster)
        expected = -25
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_process_damaging_ki_attack_increased_damage_modifier_return_message(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        actual = process_damaging_ki_attack('Sunder',
                                            'Slams the ground in front of you creating a wave of Ki.',
                                            35, 2.0, test_character, test_monster)
        expected = 'You used Sunder! Slams the ground in front of you creating a wave of Ki. You dealt 70 Ki damage!'
        self.assertEqual(expected, actual)

    def test_process_damaging_ki_attack_increased_damage_modifier_monster_health_reduction(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        actual = process_damaging_ki_attack('Sunder',
                                            'Slams the ground in front of you creating a wave of Ki.',
                                            35, 2.0, test_character, test_monster)
        expected = 30
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)