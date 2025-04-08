"""
This module tests move_character function in character_module.py
"""
from character_module import move_character
from unittest import TestCase


class TestMoveCharacter(TestCase):
    def test_move_character_moves_down_direction_2(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction = 2
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_down_to_edge_direction_2(self):
        character = {"X-coordinate": 0, "Y-coordinate": 3, "Current HP": 5}
        direction = 2
        expected = {"X-coordinate": 0, "Y-coordinate": 4, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_up_direction_1(self):
        character = {"X-coordinate": 0, "Y-coordinate": 4, "Current HP": 5}
        direction = 1
        expected = {"X-coordinate": 0, "Y-coordinate": 3, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_up_to_edge_direction_1(self):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        direction = 1
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_right_direction_3(self):
        character = {"X-coordinate": 0, "Y-coordinate": 3, "Current HP": 5}
        direction = 3
        expected = {"X-coordinate": 1, "Y-coordinate": 3, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_right_to_edge_direction_3(self):
        character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        direction = 3
        expected = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_left_direction_4(self):
        character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5}
        direction = 4
        expected = {"X-coordinate": 1, "Y-coordinate": 3, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)

    def test_move_character_moves_left_to_edge_direction_4(self):
        character = {"X-coordinate": 1, "Y-coordinate": 3, "Current HP": 5}
        direction = 4
        expected = {"X-coordinate": 0, "Y-coordinate": 3, "Current HP": 5}
        move_character(character, direction)
        self.assertEqual(expected, character)