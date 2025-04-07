"""
This module tests process_special_ki_attack_with_cost function from battle.py
"""
from battle import process_special_ki_attack_with_cost
from unittest import TestCase


class TestProcessSpecialKiAttackWithCost(TestCase):
    def test_process_special_ki_attack_with_cost_berserk_attack_return_message(self):
        test_character = {'Current Ki': 50, 'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
        test_monster = {'Status': {'Snared': 0}}
        actual = process_special_ki_attack_with_cost('Berserk', 'Battle description.',
                                                     test_character, test_monster)
        expected = ('You used Berserk! Battle description. '
                    'Your damage is increased by 50% for 3 turns!')
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_berserk_attack_ki_reduction(self):
        test_character = {'Current Ki': 50, 'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
        test_monster = {'Status': {'Snared': 0}}

        process_special_ki_attack_with_cost('Berserk', 'Battle description.',
                                            test_character, test_monster)
        expected = 40
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_berserk_attack_damage_modifier(self):
        test_character = {'Current Ki': 50, 'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
        test_monster = {'Status': {'Snared': 0}}

        process_special_ki_attack_with_cost('Berserk', 'Battle description.',
                                            test_character, test_monster)
        expected = 1.5
        actual = test_character['Damage Modifier']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_shell_attack_return_message(self):
        test_character = {'Current Ki': 30, 'Active Defense Modifier': 1.0,
                          'Status': {'Shell': 0}, 'Defense Modifier': 1.0}
        test_monster = {'Status': {'Snared': 0}}
        actual = process_special_ki_attack_with_cost('Shell', 'Battle description.',
                                                     test_character, test_monster)
        expected = 'You used Shell! Battle description.'
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_shell_attack_ki_reduction(self):
        test_character = {'Current Ki': 30, 'Active Defense Modifier': 1.0,
                          'Status': {'Shell': 0}, 'Defense Modifier': 1.0}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack_with_cost('Shell', 'Battle description.',
                                            test_character, test_monster)
        expected = 20
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_shell_attack_active_defense_modifier(self):
        test_character = {'Current Ki': 30, 'Active Defense Modifier': 1.0,
                          'Status': {'Shell': 0}, 'Defense Modifier': 1.0}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack_with_cost('Shell', 'Battle description.',
                                            test_character, test_monster)
        expected = 0.0
        actual = test_character['Active Defense Modifier']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_snare_attack_return_message(self):
        test_character = {'Current Ki': 15, 'Status': {'Berserk': 0}}
        test_monster = {'Status': {'Snared': 0}}
        actual = process_special_ki_attack_with_cost('Snare', 'Not used.',
                                                     test_character, test_monster)
        expected = 'The monster is snared and will miss its next turn!'
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_snare_attack_ki_reduction(self):
        test_character = {'Current Ki': 15, 'Status': {'Berserk': 0}}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack_with_cost('Snare', 'Not used.',
                                            test_character, test_monster)
        expected = 5
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_process_special_ki_attack_with_cost_snare_attack_ki_monster_snared(self):
        test_character = {'Current Ki': 15, 'Status': {'Berserk': 0}}
        test_monster = {'Status': {'Snared': 0}}
        process_special_ki_attack_with_cost('Snare', 'Not used.',
                                            test_character, test_monster)
        expected = 2
        actual = test_monster['Status']['Snared']
        self.assertEqual(expected, actual)