"""
This module tests the print_level_up function from character_module.py
"""
import io
from unittest import TestCase
from unittest.mock import patch
from character_module import print_level_up


class TestPrintLevelUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_up_level_2(self, mock_output):
        character = {'Level': 2, 'Title': 'the Novice', 'Health': 250, 'Ki': 65, 'Stance': ['Bear', 'Turtle']}
        print_level_up(character)
        actual = mock_output.getvalue()
        expected = (
            "Level Up! You are now level 2!\n"
            "New title: the Novice\n"
            "Health increased to 250\n"
            "Ki increased to 65\n"
            "New stance unlocked: Turtle\n"
        )
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_up_level_3(self, mock_output):
        character = {'Level': 3, 'Title': 'the Accepted', 'Health': 300, 'Ki': 80,
                     'Stance': ['Bear', 'Turtle', 'Snake']}
        print_level_up(character)
        actual = mock_output.getvalue()
        expected = (
            "Level Up! You are now level 3!\n"
            "New title: the Accepted\n"
            "Health increased to 300\n"
            "Ki increased to 80\n"
            "New stance unlocked: Snake\n"
        )
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_up_level_1_no_stance(self, mock_output):
        character = {'Level': 1, 'Title': 'the Amateur', 'Health': 200, 'Ki': 50, 'Stance': ['Bear']}
        print_level_up(character)
        actual = mock_output.getvalue()
        expected = (
            "Level Up! You are now level 1!\n"
            "New title: the Amateur\n"
            "Health increased to 200\n"
            "Ki increased to 50\n"
        )
        self.assertEqual(expected, actual)