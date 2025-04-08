"""
This module tests the get_npc_dialogue function from tutorial.py
"""
from tutorial import get_npc_dialogue
from unittest import TestCase


class TestGetNPCDialogue(TestCase):
    def test_get_npc_dialogue_length(self):
        dialogue = get_npc_dialogue('Self', 'Alice')
        actual = len(dialogue)
        expected = 3
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_first_line(self):
        dialogue = get_npc_dialogue('Self', 'Alice')
        actual = dialogue[0][0]
        expected = "Today's the day! I'm going to become an official member of the Reaper's Guild!"
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_input_boolean_is_false(self):
        dialogue = get_npc_dialogue('Self', 'Alice')
        self.assertFalse(dialogue[0][1])

    def test_get_npc_dialogue_character_name_used(self):
        dialogue = get_npc_dialogue('Self', 'Alice')
        actual = dialogue[2][0]
        expected = "Alice enters the main room of the Guild."
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_darrow_dialogue_length(self):
        dialogue = get_npc_dialogue('Darrow', 'Alice')
        actual = len(dialogue)
        expected = 8
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_darrow_dialogue_first_line_input_boolean_is_True(self):
        dialogue = get_npc_dialogue('Darrow', 'Alice')
        self.assertTrue(dialogue[0][1])

    def test_get_npc_dialogue_darrow_dialogue_first_line_content(self):
        dialogue = get_npc_dialogue('Darrow', 'Alice')
        actual = dialogue[0][0]
        expected = 'Finally awake eh Alice? So how about it. Do you need to prep or are you ready to go?'
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_misaki_dialogue_length(self):
        dialogue = get_npc_dialogue('Misaki', 'Alice')
        actual = len(dialogue)
        expected = 7
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_misaki_dialogue_first_line_input_boolean_is_false(self):
        dialogue = get_npc_dialogue('Misaki', 'Alice')
        self.assertFalse(dialogue[0][1])

    def test_get_npc_dialogue_misaki_dialogue_last_line_content(self):
        dialogue = get_npc_dialogue('Misaki', 'Alice')
        actual = dialogue[6][0]
        expected = "Don't get yourself killed, okay? I bet Ragnar has some combat tips for you."
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_ragnar_dialogue_length(self):
        dialogue = get_npc_dialogue('Ragnar', 'Alice')
        actual = len(dialogue)
        expected = 12
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_ragnar_dialogue_first_line_input_boolean_is_false(self):
        dialogue = get_npc_dialogue('Ragnar', 'Alice')
        self.assertFalse(dialogue[0][1])

    def test_get_npc_dialogue_ragnar_dialogue_first_line_content(self):
        dialogue = get_npc_dialogue('Ragnar', 'Alice')
        actual = dialogue[0][0]
        expected = "Lo, Alice! I can't let you leave without you knowing how to defend yourself."
        self.assertEqual(actual, expected)

    def test_get_npc_dialogue_ragnar_dialogue_last_line_content(self):
        dialogue = get_npc_dialogue('Ragnar', 'Alice')
        actual = dialogue[11][0]
        expected = "We'll that's pretty much the basics. Now come back with that Crystal!."
        self.assertEqual(actual, expected)