from battle import create_monster
from unittest import TestCase


class TestCreateMonster(TestCase):
    def test_create_monster_create_wendigo(self):
        expected = {'Name': 'Wendigo', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Wendigo')
        self.assertEqual(expected, actual)

    def test_create_monster_create_djinn(self):
        expected = {'Name': 'Djinn', 'Health': 90, 'Current Health': 90, 'Status': {'Buff': 0, 'Snared': 0},
                    'Damage Modifier': 1.0, 'Health Modifier': 1.0}
        actual = create_monster('Djinn')
        self.assertEqual(expected, actual)