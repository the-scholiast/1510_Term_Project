"""
This module tests turn_order from battle.py
"""
from battle import turn_order
from unittest import TestCase
from unittest.mock import patch


class TestTurnOrder(TestCase):
    @patch('random.randint', return_value=1)
    def test_turn_order_character_first_strike_message(self, _):
        monster_name = "Werewolf"
        turns, actual = turn_order(monster_name)
        expected = "You strike first!"
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_turn_order_monster_first_strike_message(self, _):
        monster_name = "Werewolf"
        turns, actual = turn_order(monster_name)
        expected = f"The {monster_name} strikes first!"
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    def test_turn_order_character_first_strike_verify_turn_order(self, _):
        monster_name = "Werewolf"
        turns, actual = turn_order(monster_name)
        expected = ['character', 'monster']
        actual = [next(turns), next(turns)]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_turn_order_monster_first_strike_verify_turn_order(self, _):
        monster_name = "Werewolf"
        turns, actual = turn_order(monster_name)
        expected = ['monster', 'character']
        actual = [next(turns), next(turns)]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    def test_turn_order_character_first_strike_next_cycle(self, _):
        monster_name = "Werewolf"
        turns, actual = turn_order(monster_name)
        next(turns)
        expected = ['monster', 'character']
        actual = [next(turns), next(turns)]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_turn_order_monster_first_strike_next_cycle(self, _):
        monster_name = "Werewolf"
        turns, actual = turn_order(monster_name)
        next(turns)
        expected = ['character', 'monster']
        actual = [next(turns), next(turns)]
        self.assertEqual(actual, expected)