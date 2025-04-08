"""
This module tests make_board from grid.py
"""
from grid import make_board
from unittest import TestCase


class TestMakeBoard(TestCase):
    def test_make_board_dimensions(self):
        board = make_board(5, 5)
        actual = len(board)
        expected = 25
        self.assertEqual(expected, actual)

    def test_make_board_correct_tuple_keys_and_encounter_marker(self):
        actual = make_board(5, 5)
        expected = {
            (0, 0): '[!]', (1, 0): '[!]', (2, 0): '[!]', (3, 0): '[!]', (4, 0): '[!]', (0, 1): '[!]',
            (1, 1): '[!]', (2, 1): '[!]', (3, 1): '[!]', (4, 1): '[!]', (0, 2): '[!]', (1, 2): '[!]', (2, 2): '[!]',
            (3, 2): '[!]', (4, 2): '[!]', (0, 3): '[!]', (1, 3): '[!]', (2, 3): '[!]', (3, 3): '[!]', (4, 3): '[!]',
            (0, 4): '[!]', (1, 4): '[!]', (2, 4): '[!]', (3, 4): '[!]', (4, 4): '[!]'
        }
        self.assertEqual(actual, expected)