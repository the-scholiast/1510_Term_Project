"""
This module tests remove_equipment_modifiers function from character_module.py
"""
from character_module import remove_equipment_modifiers
from unittest import TestCase


class TestRemoveEquipmentModifiers(TestCase):
    def test_remove_equipment_modifiers_defense_helmet(self):
        test_character = {'Equipment': {'Helmet': ('Iron Hat', 0.02), 'Armour': '',
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.02, 'Damage Modifier': 1.0}
        remove_equipment_modifiers(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_remove_equipment_modifiers_defense_armour(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': ('Copper Plate', 0.04),
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.04, 'Damage Modifier': 1.0}
        remove_equipment_modifiers(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_remove_equipment_modifiers_damage_ring(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': ('Ruby Ring', 0.04), 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.04}
        remove_equipment_modifiers(test_character)
        actual = test_character['Damage Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_remove_equipment_modifiers_damage_amulet(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': '', 'Amulet': ('Crystal Pendant', 0.04)},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.04}
        remove_equipment_modifiers(test_character)
        actual = test_character['Damage Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_remove_equipment_modifiers_all_defense_equipment(self):
        test_character = {'Equipment': {'Helmet': ('Iron Helmet', 0.04), 'Armour': ('War Plate', 0.08),
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.12, 'Damage Modifier': 1.0}
        remove_equipment_modifiers(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_remove_equipment_modifiers_all_damage_equipment(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': ('Ruby Ring', 0.04), 'Amulet': ('Crystal Pendant', 0.04)},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.08}
        remove_equipment_modifiers(test_character)
        actual = test_character['Damage Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_remove_equipment_modifiers_no_equipment(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '',
                                        'Ring': '', 'Amulet': ''},
                          'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        remove_equipment_modifiers(test_character)
        actual = test_character['Defense Modifier']
        expected = 1.0
        self.assertEqual(expected, actual)