"""
This module tests create_monster function from battle.py
"""
from battle import create_monster
from unittest import TestCase


class TestCreateMonster(TestCase):
    def test_create_monster_character_level_1(self):
        expected = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Ghoul')
        self.assertEqual(expected, actual)

    def test_create_monster_character_level_2(self):
        expected = {'Name': 'Ghoul', 'Health': 125, 'Current Health': 125, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.2, 'Health Modifier': 1.25}
        actual = create_monster('Ghoul', 2)
        self.assertEqual(expected, actual)

    def test_create_monster_character_level_3(self):
        expected = {'Name': 'Ghoul', 'Health': 150, 'Current Health': 150, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.5, 'Health Modifier': 1.5}
        actual = create_monster('Ghoul', 3)
        self.assertEqual(expected, actual)

    def test_create_monster_generate_ghoul(self):
        expected = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Ghoul')
        self.assertEqual(expected, actual)

    def test_create_monster_generate_vampire(self):
        expected = {'Name': 'Vampire', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Vampire')
        self.assertEqual(expected, actual)

    def test_create_monster_generate_werewolf(self):
        expected = {'Name': 'Werewolf', 'Health': 80, 'Current Health': 80, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Werewolf')
        self.assertEqual(expected, actual)

    def test_create_monster_generate_skinwalker(self):
        expected = {'Name': 'Skinwalker', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Skinwalker')
        self.assertEqual(expected, actual)

    def test_create_monster_generate_wendigo(self):
        expected = {'Name': 'Wendigo', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Wendigo')
        self.assertEqual(expected, actual)

    def test_create_monster_generate_djinn(self):
        expected = {'Name': 'Djinn', 'Health': 90, 'Current Health': 90, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Djinn')
        self.assertEqual(expected, actual)