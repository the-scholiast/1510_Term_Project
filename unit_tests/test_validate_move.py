"""
This module tests validate_move function from character_module.py
"""
from character_module import validate_move
from unittest import TestCase


class TestValidateMove(TestCase):
    def test_validate_move_character_cannot_move_up_direction_one(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = 1
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_moves_up_direction_one(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 3, "Y-coordinate": 3}
        direction = 1
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_cannot_move_left_direction_four(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = 4
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_moves_left_direction_four(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 3, "Y-coordinate": 3}
        direction = 4
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_cannot_move_right_direction_three(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 4, "Y-coordinate": 0}
        direction = 3
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_moves_right_direction_three(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 3, "Y-coordinate": 3}
        direction = 3
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_cannot_move_down_direction_two(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 3, "Y-coordinate": 4}
        direction = 2
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_moves_down_direction_two(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        character = {"X-coordinate": 4, "Y-coordinate": 3}
        direction = 2
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)