"""
This module tests update_title function from character_module.py
"""
from character_module import update_title
from unittest import TestCase


class TestUpdateTitle(TestCase):
    def test_update_title_level_1(self):
        test_character = {'Name': 'Alex', 'Level': 1, 'Title': ''}
        updated_character = update_title(test_character)
        actual = updated_character['Title']
        expected = 'the Amateur'
        self.assertEqual(expected, actual)

    def test_update_title_level_2(self):
        test_character = {'Name': 'Alex', 'Level': 2, 'Title': 'the Amateur'}
        updated_character = update_title(test_character)
        actual = updated_character['Title']
        expected = 'the Novice'
        self.assertEqual(expected, actual)

    def test_update_title_level_3(self):
        test_character = {'Name': 'Alex', 'Level': 3, 'Title': 'the Novice'}
        updated_character = update_title(test_character)
        actual = updated_character['Title']
        expected = 'the Accepted'
        self.assertEqual(expected, actual)