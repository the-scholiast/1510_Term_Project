"""
This module tests user_picks_equipment function from encounters.py
"""
import io
from encounters import user_picks_equipment
from unittest import TestCase
from unittest.mock import patch


class TestUserPicksEquipment(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_user_picks_equipment_first_option(self, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = ('Helmet', 'Steel Helmet', 0.15)
        actual = user_picks_equipment(test_equipment)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_user_picks_equipment_second_option(self, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = ('Armour', 'Sun Plate', 0.15)
        actual = user_picks_equipment(test_equipment)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_user_picks_equipment_third_option(self, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = ('Ring', 'Warrior Ring', 0.15)
        actual = user_picks_equipment(test_equipment)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_user_picks_equipment_fourth_option(self, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = ('Amulet', 'Focused Amulet', 0.15)
        actual = user_picks_equipment(test_equipment)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_picks_equipment_invalid_print_message(self, mock_output, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = "Invalid choice. Please enter a number between 1 and 4.\n"
        user_picks_equipment(test_equipment)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "2"])
    def test_user_picks_equipment_invalid_then_valid_input(self, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = ('Armour', 'Sun Plate', 0.15)
        actual = user_picks_equipment(test_equipment)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["abc", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_picks_equipment_non_numeric_input_print_message(self, mock_output, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = "Invalid choice. Please enter a number between 1 and 4.\n"
        user_picks_equipment(test_equipment)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["    1     "])
    def test_user_picks_equipment_valid_option_with_whitespace(self, _):
        test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                          'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        expected = ('Helmet', 'Steel Helmet', 0.15)
        actual = user_picks_equipment(test_equipment)
        self.assertEqual(expected, actual)