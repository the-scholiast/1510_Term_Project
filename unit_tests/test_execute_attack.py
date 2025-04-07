"""
This module tests execute_attack function from battle.py
"""
from battle import execute_attack
from unittest import TestCase


class TestExecuteAttack(TestCase):
    def test_execute_attack_physical_attack_returns_true(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        success, _ = execute_attack('Physical', 'Heavy Strike',
                                    'A powerful blow with massive physical damage.',
                                    20, 1.0, test_character, test_monster)
        expected = True
        actual = success
        self.assertEqual(expected, actual)

    def test_execute_attack_physical_attack_returns_message_with_damage(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        _, message = execute_attack('Physical', 'Heavy Strike',
                                    'A powerful blow with massive physical damage.',
                                    20, 1.0, test_character, test_monster)
        expected = True
        actual = 'You dealt 20 damage' in message
        self.assertEqual(expected, actual)

    def test_execute_attack_physical_attack_returns_message_with_attack_move(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        _, message = execute_attack('Physical', 'Heavy Strike',
                                    'A powerful blow with massive physical damage.',
                                    20, 1.0, test_character, test_monster)
        expected = True
        actual = 'You used Heavy Strike!' in message
        self.assertEqual(expected, actual)

    def test_execute_attack_physical_attack_reduces_monster_health(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        execute_attack('Physical', 'Heavy Strike',
                       'A powerful blow with massive physical damage.',
                       20, 1.0, test_character, test_monster)
        expected = 80
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_execute_attack_ki_attack_with_damage_returns_true(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        success, _ = execute_attack('Ki', 'Sunder',
                                    'Slams the ground in front of you creating a wave of Ki.',
                                    35, 1.0, test_character, test_monster)
        expected = True
        actual = success
        self.assertEqual(expected, actual)

    def test_execute_attack_ki_attack_message_contains_attack_name(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        _, message = execute_attack('Ki', 'Sunder',
                                    'Slams the ground in front of you creating a wave of Ki.',
                                    35, 1.0, test_character, test_monster)
        expected = True
        actual = 'You used Sunder!' in message
        self.assertEqual(expected, actual)

    def test_execute_attack_ki_attack_reduces_character_ki(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        execute_attack('Ki', 'Sunder',
                       'Slams the ground in front of you creating a wave of Ki.',
                       35, 1.0, test_character, test_monster)
        expected = 40
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_execute_attack_ki_attack_reduces_monster_health(self):
        test_character = {'Current Ki': 50}
        test_monster = {'Current Health': 100}
        execute_attack('Ki', 'Sunder',
                       'Slams the ground in front of you creating a wave of Ki.',
                       35, 1.0, test_character, test_monster)
        expected = 65
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_execute_attack_snare_returns_true(self):
        test_character = {'Current Ki': 50, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Current Health': 100, 'Status': {'Snared': 0}}
        success, _ = execute_attack('Ki', 'Snare',
                                    'Whip entangles its target, paralyzing its victim.',
                                    12, 1.0, test_character, test_monster)
        expected = True
        actual = success
        self.assertEqual(expected, actual)

    def test_execute_attack_snare_message_contains_damage(self):
        test_character = {'Current Ki': 50, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Current Health': 100, 'Status': {'Snared': 0}}
        _, message = execute_attack('Ki', 'Snare',
                                    'Whip entangles its target, paralyzing its victim.',
                                    12, 1.0, test_character, test_monster)
        expected = True
        actual = 'You dealt 12 Ki damage' in message
        self.assertEqual(expected, actual)

    def test_execute_attack_snare_message_contains_effect(self):
        test_character = {'Current Ki': 50, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Current Health': 100, 'Status': {'Snared': 0}}
        _, message = execute_attack('Ki', 'Snare',
                                    'Whip entangles its target, paralyzing its victim.',
                                    12, 1.0, test_character, test_monster)
        expected = True
        actual = 'monster is snared' in message
        self.assertEqual(expected, actual)

    def test_execute_attack_snare_applies_snared_status(self):
        test_character = {'Current Ki': 50, 'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Current Health': 100, 'Status': {'Snared': 0}}
        execute_attack('Ki', 'Snare',
                       'Whip entangles its target, paralyzing its victim.',
                       12, 1.0, test_character, test_monster)
        expected = 2
        actual = test_monster['Status']['Snared']
        self.assertEqual(expected, actual)

    def test_execute_attack_special_ki_berserk_returns_true(self):
        test_character = {'Current Ki': 50, 'Damage Modifier': 1.0,
                          'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        success, _ = execute_attack('Ki', 'Berserk',
                                    'Enters a state of rage, increasing both physical damage and Ki attacks.',
                                    0, 1.0, test_character, test_monster)
        expected = True
        actual = success
        self.assertEqual(expected, actual)

    def test_execute_attack_berserk_message_damage_increase(self):
        test_character = {'Current Ki': 50, 'Damage Modifier': 1.0,
                          'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        _, message = execute_attack('Ki', 'Berserk',
                                    'Enters a state of rage, increasing both physical damage and Ki attacks.',
                                    0, 1.0, test_character, test_monster)
        expected = True
        actual = 'damage is increased' in message
        self.assertEqual(expected, actual)

    def test_execute_attack_berserk_increases_damage_modifier(self):
        test_character = {'Current Ki': 50, 'Damage Modifier': 1.0,
                          'Status': {'Berserk': 0, 'Shell': 0}}
        test_monster = {'Status': {'Snared': 0}}
        execute_attack('Ki', 'Berserk',
                       'Enters a state of rage, increasing both physical damage and Ki attacks.',
                       0, 1.0, test_character, test_monster)
        expected = 1.5
        actual = test_character['Damage Modifier']
        self.assertEqual(expected, actual)

    def test_execute_attack_insufficient_ki_returns_false(self):
        test_character = {'Current Ki': 5}
        test_monster = {'Current Health': 100}
        success, _ = execute_attack('Ki', 'Sunder',
                                    'Slams the ground in front of you creating a wave of Ki.',
                                    35, 1.0, test_character, test_monster)
        expected = False
        actual = success
        self.assertEqual(expected, actual)

    def test_execute_attack_insufficient_ki_returns_empty_string(self):
        test_character = {'Current Ki': 5}
        test_monster = {'Current Health': 100}
        _, message = execute_attack('Ki', 'Sunder',
                                    'Slams the ground in front of you creating a wave of Ki.',
                                    35, 1.0, test_character, test_monster)
        expected = ""
        actual = message
        self.assertEqual(expected, actual)

    def test_execute_attack_insufficient_ki_doesnt_reduce_ki(self):
        test_character = {'Current Ki': 5}
        test_monster = {'Current Health': 100}
        execute_attack('Ki', 'Sunder',
                       'Slams the ground in front of you creating a wave of Ki.',
                       35, 1.0, test_character, test_monster)
        expected = 5
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)