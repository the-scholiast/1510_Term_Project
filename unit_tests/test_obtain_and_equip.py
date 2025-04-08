"""
This module tests obtain_and_equip function from character_module.py
"""
import io
from character_module import obtain_and_equip
from unittest import TestCase
from unittest.mock import patch


class TestObtainAndEquip(TestCase):
    def test_obtain_and_equip_helmet(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
        equipment_choice = ('Helmet', 'Iron Hat', 0.02)
        obtain_and_equip(equipment_choice, test_character)
        actual = test_character['Equipment']['Helmet']
        expected = ('Iron Hat', 0.02)
        self.assertEqual(expected, actual)

    def test_obtain_and_equip_armour(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
        equipment_choice = ('Armour', 'Steel Plate', 0.08)
        obtain_and_equip(equipment_choice, test_character)
        actual = test_character['Equipment']['Armour']
        expected = ('Steel Plate', 0.08)
        self.assertEqual(expected, actual)

    def test_obtain_and_equip_ring(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
        equipment_choice = ('Ring', 'Ruby Ring', 0.04)
        obtain_and_equip(equipment_choice, test_character)
        actual = test_character['Equipment']['Ring']
        expected = ('Ruby Ring', 0.04)
        self.assertEqual(expected, actual)

    def test_obtain_and_equip_amulet(self):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
        equipment_choice = ('Amulet', 'Crystal Pendant', 0.04)
        obtain_and_equip(equipment_choice, test_character)
        actual = test_character['Equipment']['Amulet']
        expected = ('Crystal Pendant', 0.04)
        self.assertEqual(expected, actual)

    def test_obtain_and_equip_replace_existing(self):
        test_character = {'Equipment': {'Helmet': ('Iron Hat', 0.02), 'Armour': '', 'Ring': '', 'Amulet': ''}}
        equipment_choice = ('Helmet', 'Steel Helmet', 0.06)
        obtain_and_equip(equipment_choice, test_character)
        actual = test_character['Equipment']['Helmet']
        expected = ('Steel Helmet', 0.06)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_obtain_and_equip_print_message(self, mock_stdout):
        test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
        equipment_choice = ('Helmet', 'Iron Hat', 0.02)
        obtain_and_equip(equipment_choice, test_character)
        expected = "You have equipped Iron Hat!\n"
        self.assertEqual(expected, mock_stdout.getvalue())