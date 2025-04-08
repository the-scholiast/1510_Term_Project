"""
This module tests the level_up function from character_module.py
"""
from unittest import TestCase
from character_module import level_up


class TestLevelUp(TestCase):
    def test_level_up_from_level_1_to_2(self):
        character = {
            'Level': 1,
            'Experience': 100,
            'Health': 200,
            'Current Health': 180,
            'Ki': 50,
            'Current Ki': 30,
            'Damage Modifier': 1.0,
            'Stance': ['Bear'],
            'Title': 'the Amateur'
        }
        result = level_up(character)
        expected = (
            True, 2, 250, 250, 65, 65, 1.1,
            ['Bear', 'Turtle'], 0, 'the Novice'
        )
        actual = (
            result,
            character['Level'],
            character['Health'],
            character['Current Health'],
            character['Ki'],
            character['Current Ki'],
            character['Damage Modifier'],
            character['Stance'],
            character['Experience'],
            character['Title']
        )
        self.assertEqual(expected, actual)

    def test_level_up_from_level_2_to_3(self):
        character = {
            'Level': 2,
            'Experience': 100,
            'Health': 250,
            'Current Health': 200,
            'Ki': 65,
            'Current Ki': 40,
            'Damage Modifier': 1.1,
            'Stance': ['Bear', 'Turtle'],
            'Title': 'the Novice'
        }
        result = level_up(character)
        expected = (
            True, 3, 300, 300, 80, 80, 1.2,
            ['Bear', 'Turtle', 'Snake'], 0, 'the Accepted'
        )
        actual = (
            result,
            character['Level'],
            character['Health'],
            character['Current Health'],
            character['Ki'],
            character['Current Ki'],
            character['Damage Modifier'],
            character['Stance'],
            character['Experience'],
            character['Title']
        )
        self.assertEqual(expected, actual)

    def test_level_up_cannot_exceed_level_3(self):
        character = {
            'Level': 3,
            'Experience': 100,
            'Health': 300,
            'Current Health': 250,
            'Ki': 80,
            'Current Ki': 60,
            'Damage Modifier': 1.2,
            'Stance': ['Bear', 'Turtle', 'Snake'],
            'Title': 'the Accepted'
        }
        result = level_up(character)
        expected = (
            False, 3, 300, 250, 80, 60, 1.2,
            ['Bear', 'Turtle', 'Snake'], 100, 'the Accepted'
        )
        actual = (
            result,
            character['Level'],
            character['Health'],
            character['Current Health'],
            character['Ki'],
            character['Current Ki'],
            character['Damage Modifier'],
            character['Stance'],
            character['Experience'],
            character['Title']
        )
        self.assertEqual(expected, actual)

    def test_level_up_insufficient_experience(self):
        character = {
            'Level': 1,
            'Experience': 50,
            'Health': 200,
            'Current Health': 180,
            'Ki': 50,
            'Current Ki': 30,
            'Damage Modifier': 1.0,
            'Stance': ['Bear'],
            'Title': 'the Amateur'
        }
        result = level_up(character)
        expected = (
            False, 1, 200, 180, 50, 30, 1.0,
            ['Bear'], 50, 'the Amateur'
        )
        actual = (
            result,
            character['Level'],
            character['Health'],
            character['Current Health'],
            character['Ki'],
            character['Current Ki'],
            character['Damage Modifier'],
            character['Stance'],
            character['Experience'],
            character['Title']
        )
        self.assertEqual(expected, actual)