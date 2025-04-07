"""
This module tests check_encounter from encounters.py
"""
from grid import check_encounter
from unittest import TestCase



class TestCheckEncounters(TestCase):
    def test_check_encounter_has_encounter(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 0, 'X-coordinate': 0}
        self.assertTrue(check_encounter(test_character, board))

    def test_check_encounter_no_encounter(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 1, 'X-coordinate': 0}
        self.assertFalse(check_encounter(test_character, board))

    def test_check_encounter_character_bottom_left(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 4, 'X-coordinate': 0}
        self.assertTrue(check_encounter(test_character, board))

    def test_check_encounter_character_bottom_right(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 4, 'X-coordinate': 4}
        self.assertTrue(check_encounter(test_character, board))

    def test_check_encounter_character_top_right(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 0, 'X-coordinate': 4}
        self.assertTrue(check_encounter(test_character, board))

    def test_check_encounter_character_top_left(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 0, 'X-coordinate': 0}
        self.assertTrue(check_encounter(test_character, board))

    def test_check_encounter_character_middle(self):
        board = {
            (0, 0): '[!]', (0, 1): '   ', (0, 2): '[!]', (0, 3): '   ', (0, 4): '[!]',
            (1, 0): '   ', (1, 1): '[!]', (1, 2): '   ', (1, 3): '[!]', (1, 4): '   ',
            (2, 0): '[!]', (2, 1): '   ', (2, 2): '[!]', (2, 3): '   ', (2, 4): '[!]',
            (3, 0): '   ', (3, 1): '[!]', (3, 2): '   ', (3, 3): '[!]', (3, 4): '   ',
            (4, 0): '[!]', (4, 1): '   ', (4, 2): '[!]', (4, 3): '   ', (4, 4): '[!]'
        }
        test_character = {'Y-coordinate': 2, 'X-coordinate': 2}
        self.assertTrue(check_encounter(test_character, board))