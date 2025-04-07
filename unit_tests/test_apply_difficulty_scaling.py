"""
This module tests apply_difficulty_scaling function from battle.py
"""
from battle import apply_difficulty_scaling
from unittest import TestCase


class TestApplyDifficultyScaling(TestCase):
    def test_apply_difficulty_scaling_level_one_damage_modifier(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 1)
        expected = 1.0
        actual = test_monster['Damage Modifier']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_one_health_modifier(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 1)
        expected = 1.0
        actual = test_monster['Health Modifier']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_one_max_health(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 1)
        expected = 100
        actual = test_monster['Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_one_current_health(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 1)
        expected = 100
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_two_damage_modifier(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 2)
        expected = 1.2
        actual = test_monster['Damage Modifier']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_two_health_modifier(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 2)
        expected = 1.25
        actual = test_monster['Health Modifier']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_two_max_health(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 2)
        expected = 125
        actual = test_monster['Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_two_current_health(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 2)
        expected = 125
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_three_damage_modifier(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 3)
        expected = 1.5
        actual = test_monster['Damage Modifier']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_three_health_modifier(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 3)
        expected = 1.5
        actual = test_monster['Health Modifier']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_three_max_health(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 3)
        expected = 150
        actual = test_monster['Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_level_three_current_health(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 3)
        expected = 150
        actual = test_monster['Current Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_different_health(self):
        test_monster = {'Name': 'Werewolf', 'Health': 80, 'Current Health': 80,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        apply_difficulty_scaling(test_monster, 2)
        expected = 100
        actual = test_monster['Health']
        self.assertEqual(expected, actual)

    def test_apply_difficulty_scaling_return_updated_monster(self):
        test_monster = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100,
                        'Status': {'Buff': 0, 'Snared': 0},
                        'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = apply_difficulty_scaling(test_monster, 2)
        expected = {'Name': 'Ghoul', 'Health': 125, 'Current Health': 125,
                    'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.2, 'Health Modifier': 1.25}
        self.assertEqual(expected, actual)
