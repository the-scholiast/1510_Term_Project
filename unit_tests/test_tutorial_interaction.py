"""
This module tests tutorial_interaction function from tutorial.py
"""
import io
from tutorial import tutorial_interaction
from unittest import TestCase
from unittest.mock import patch


class TestTutorialInteraction(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_tutorial_interaction_darrow_continue_tutorial(self, _):
        character = {'Name': 'Hero', 'X-coordinate': 1, 'Y-coordinate': 0}
        actual = tutorial_interaction('Darrow', character)
        expected = False
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_tutorial_interaction_darrow_skip_tutorial(self, _):
        character = {'Name': 'Hero', 'X-coordinate': 0, 'Y-coordinate': 0}
        actual = tutorial_interaction('Darrow', character)
        expected = True
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tutorial_interaction_darrow_skip_message(self, mock_output, _):
        character = {'Name': 'Hero', 'X-coordinate': 1, 'Y-coordinate': 0}
        tutorial_interaction('Darrow', character)
        actual = mock_output.getvalue()
        expected = ("Darrow: Finally awake eh Hero? So how about it. Do you need to prep or are you ready to go?\n"
                    "Darrow: ZEHAHAHAHAHAHA! That's the spirit! Go bring me the head of a worthy beast!\n")
        self.assertEqual(actual, expected)