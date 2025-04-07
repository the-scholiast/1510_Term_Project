"""
This module tests process_special_ki_attack function from battle.py
"""
from battle import process_special_ki_attack
from unittest import TestCase


class TestProcessSpecialKiAttack(TestCase):
    def test_process_special_ki_attack_berserk_return_message(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        actual = process_special_ki_attack(
            'Berserk',
            'Enters a state of rage, increasing both physical damage and Ki attacks.',
            test_character, test_monster)
        expected = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks. '
                    'Your damage is increased by 50% for 3 turns!')
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_berserk_damage_modifier(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}

        process_special_ki_attack('Berserk',
                                  'Enters a state of rage, increasing both physical damage and Ki attacks.',
                                  test_character, test_monster)
        expected = 1.5
        actual = test_character['Damage Modifier']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_berserk_status(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack('Berserk',
                                  'Enters a state of rage, increasing both physical damage and Ki attacks.',
                                  test_character, test_monster)
        expected = 6
        actual = test_character['Status']['Berserk']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_shell_return_message(self):
        test_character = {'Active Defense Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        actual = process_special_ki_attack('Shell',
                                           'Take no damage next two turns.',
                                           test_character, test_monster)
        expected = 'You used Shell! Take no damage next two turns.'
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_shell_active_defense_modifier(self):
        test_character = {'Active Defense Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack('Shell',
                                  'Take no damage next two turns.',
                                  test_character, test_monster)
        expected = 0.0
        actual = test_character['Active Defense Modifier']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_shell_status(self):
        test_character = {'Active Defense Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack('Shell',
                                  'Take no damage next two turns.',
                                  test_character, test_monster)
        expected = 4
        actual = test_character['Status']['Shell']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_snare_return_message(self):
        test_character = {'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        actual = process_special_ki_attack('Snare',
                                           'Whip entangles its target, paralyzing its victim.',
                                           test_character, test_monster)
        expected = 'The monster is snared and will miss its next turn!'
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_snare_monster_status(self):
        test_character = {'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack('Snare',
                                  'Whip entangles its target, paralyzing its victim.',
                                  test_character, test_monster)
        expected = 2
        actual = test_monster['Status']['Snared']
        self.assertEqual(expected, actual)