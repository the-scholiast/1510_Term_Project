"""
This module tests make_character function from character_module.py
"""
from character_module import make_character
from unittest import TestCase


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        test_name = "TestHero"
        actual = make_character(test_name)
        expected = {
            'Name': 'TestHero', 'Title': 'the Amateur',
            'Level': 1, 'Experience': 0,
            'Health': 200, 'Current Health': 200, 'Ki': 60, 'Current Ki': 60,
            'Defense Modifier': 1.0, 'Damage Modifier': 1.0, 'Active Defense Modifier': 1.0,
            'X-coordinate': 0, 'Y-coordinate': 0,
            'Crystals': 0,
            'Items': {'Health Pots': 0, 'Shards': 0},
            'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""},
            'Status': {"Poison": 0, "Bleed": 0, 'Shell': 0, 'Berserk': 0},
            'Stance': ['Bear'], 'Active Stance': 'Bear'
        }
        self.assertEqual(expected, actual)
