"""
This module tests apply_equipment function from character_module.py
"""
from character_module import apply_equipment
from unittest import TestCase


class TestApplyEquipment(TestCase):
    def test_apply_equipment_defense_helmet(self):
        test_character = {'Equipment': {'Helmet': ('Iron Hat', 0.02), 'Armour': '',
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.02
        self.assertEqual(expected, actual)

    def test_apply_equipment_defense_armour(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': ('Copper Plate', 0.04),
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.04
        self.assertEqual(expected, actual)

    def test_apply_equipment_damage_ring(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': ('Ruby Ring', 0.04), 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Damage Modifier']
        expected = 1.04
        self.assertEqual(expected, actual)

    def test_apply_equipment_damage_amulet(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': '', 'Amulet': ('Crystal Pendant', 0.04)},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Damage Modifier']
        expected = 1.04
        self.assertEqual(expected, actual)

    def test_apply_equipment_all_defense_equipment(self):
        test_character = {'Equipment': {'Helmet': ('Iron Helmet', 0.04), 'Armour': ('War Plate', 0.08),
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.12
        self.assertEqual(expected, actual)

    def test_apply_equipment_all_damage_equipment(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': ('Ruby Ring', 0.04), 'Amulet': ('Crystal Pendant', 0.04)},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Damage Modifier']
        expected = 1.08
        self.assertEqual(expected, actual)

    def test_apply_equipment_no_equipment(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        apply_equipment(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)