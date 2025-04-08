"""
This module tests print_apply_equipment function from character_module.py
"""
import io
from character_module import print_apply_equipment
from unittest import TestCase
from unittest.mock import patch


class TestPrintApplyEquipment(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_apply_equipment_helmet(self, mock_output):
        test_character = {'Defense Modifier': 1.02, 'Damage Modifier': 1.0}
        test_equipment = ('Helmet', 'Iron Hat', 0.02)
        print_apply_equipment(test_equipment, test_character)
        actual = mock_output.getvalue()
        expected = "Your Defense Modifier increased to 1.02!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_apply_equipment_armour(self, mock_output):
        test_character = {'Defense Modifier': 1.04, 'Damage Modifier': 1.0}
        test_equipment = ('Armour', 'Copper Plate', 0.04)
        print_apply_equipment(test_equipment, test_character)
        actual = mock_output.getvalue()
        expected = "Your Defense Modifier increased to 1.04!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_apply_equipment_ring(self, mock_output):
        test_character = {'Defense Modifier': 1.0, 'Damage Modifier': 1.04}
        test_equipment = ('Ring', 'Ruby Ring', 0.04)
        print_apply_equipment(test_equipment, test_character)
        actual = mock_output.getvalue()
        expected = "Your Damage Modifier increased to 1.04!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_apply_equipment_amulet(self, mock_output):
        test_character = {'Defense Modifier': 1.0, 'Damage Modifier': 1.02}
        test_equipment = ('Amulet', 'Crystal Pendant', 0.02)
        print_apply_equipment(test_equipment, test_character)
        actual = mock_output.getvalue()
        expected = "Your Damage Modifier increased to 1.02!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_apply_equipment_high_defense(self, mock_output):
        test_character = {'Defense Modifier': 1.5, 'Damage Modifier': 1.0}
        test_equipment = ('Helmet', 'Steel Helmet', 0.06)
        print_apply_equipment(test_equipment, test_character)
        actual = mock_output.getvalue()
        expected = "Your Defense Modifier increased to 1.5!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_apply_equipment_high_damage(self, mock_output):
        test_character = {'Defense Modifier': 1.0, 'Damage Modifier': 1.5}
        test_equipment = ('Ring', 'Warrior Ring', 0.06)
        print_apply_equipment(test_equipment, test_character)
        actual = mock_output.getvalue()
        expected = "Your Damage Modifier increased to 1.5!\n"
        self.assertEqual(expected, actual)