"""
This module tests the use_item function from character_module.py
"""
import io
from character_module import use_item
from unittest import TestCase
from unittest.mock import patch


class TestUseItem(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_item_health_pot_message(self, mock_output):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 2, 'Shards': 1}}
        use_item(character, 'Health Pots')
        actual = mock_output.getvalue()
        expected = "You used a Health Potion and restored 70 health!\n"
        self.assertEqual(expected, actual)

    def test_use_item_health_pot_current_health(self):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 2, 'Shards': 1}}
        use_item(character, 'Health Pots')
        actual = character['Current Health']
        expected = 200
        self.assertEqual(actual, expected)

    def test_use_item_health_pot_item_count(self):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 2, 'Shards': 1}}
        use_item(character, 'Health Pots')
        actual = character['Items']['Health Pots']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_item_shard_message(self, mock_output):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 1, 'Shards': 2}}
        use_item(character, 'Shards')
        actual = mock_output.getvalue()
        expected = "You used a Shard and restored 30 Ki!\n"
        self.assertEqual(expected, actual)

    def test_use_item_shard_current_ki(self):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 1, 'Shards': 2}}
        use_item(character, 'Shards')
        actual = character['Current Ki']
        expected = 50
        self.assertEqual(actual, expected)

    def test_use_item_shard_item_count(self):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 1, 'Shards': 2}}
        use_item(character, 'Shards')
        actual = character['Items']['Shards']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_item_no_items_message(self, mock_output):
        character = {'Health': 200, 'Current Health': 150, 'Ki': 50,
                     'Current Ki': 30, 'Items': {'Health Pots': 0, 'Shards': 0}}
        use_item(character, 'Health Pots')
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)