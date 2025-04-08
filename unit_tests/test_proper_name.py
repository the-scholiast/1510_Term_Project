"""
This module tests proper_name function from character_module.py
"""
import io
from character_module import proper_name
from unittest import TestCase
from unittest.mock import patch


class TestProperName(TestCase):
    @patch('builtins.input', side_effect=['John'])
    def test_proper_name_valid_input(self, _):
        actual = proper_name()
        expected = 'John'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['    John   '])
    def test_proper_name_valid_input_with_whitespace(self, _):
        actual = proper_name()
        expected = 'John'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['John123', 'Sarah'])
    def test_proper_name_invalid_then_valid_input(self, _):
        actual = proper_name()
        expected = 'Sarah'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['John123', 'Mike'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_proper_name_invalid_input_message(self, mock_output, _):
        proper_name()
        actual = mock_output.getvalue()
        expected = "Not a valid character name. Try again.\n"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['', 'Mike'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_proper_name_empty_input_message(self, mock_output, _):
        proper_name()
        actual = mock_output.getvalue()
        expected = "Not a valid character name. Try again.\n"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['John'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_proper_name_output_message(self, mock_output, _):
        proper_name()
        expected = "Thank you! Enjoy your time John!\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)