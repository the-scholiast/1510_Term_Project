"""
This module tests get_item function from battle.py
"""
import io
from battle import get_item
from unittest import TestCase
from unittest.mock import patch


class TestGetItem(TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_get_item_input_0_back(self, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
        actual = get_item(test_character)
        self.assertIsNone(actual)

    @patch('builtins.input', side_effect=["1"])
    def test_get_item_input_1_health_pots(self, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
        expected = "Health Pots"
        actual = get_item(test_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_item_input_2_shards(self, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
        expected = "Shards"
        actual = get_item(test_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_invalid_input_then_valid_input(self, mock_output, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
        get_item(test_character)
        expected = "Invalid item. Please select from the available options.\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["abc", "0"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_non_numeric_input(self, mock_output, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
        get_item(test_character)
        expected = "Invalid item. Please select from the available options.\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_get_item_no_items_available(self, _):
        test_character = {'Items': {'Health Pots': 0, 'Shards': 0}}
        actual = get_item(test_character)
        self.assertIsNone(actual)

    @patch('builtins.input', side_effect=["1"])
    def test_get_item_only_health_pots_available(self, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 0}}
        expected = "Health Pots"
        actual = get_item(test_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1"])
    def test_get_item_only_shards_available(self, _):
        test_character = {'Items': {'Health Pots': 0, 'Shards': 3}}
        expected = "Shards"
        actual = get_item(test_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "0"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_out_of_range_input(self, mock_output, _):
        test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
        get_item(test_character)
        expected = "Invalid item. Please select from the available options.\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_get_item_press_enter_to_return_none(self, _):
        test_character = {'Items': {'Health Pots': 0, 'Shards': 0}}
        actual = get_item(test_character)
        self.assertIsNone(actual)