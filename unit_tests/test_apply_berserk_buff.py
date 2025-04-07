"""
This module tests apply_berserk_buff function from battle.py
"""
from battle import apply_berserk_buff
from unittest import TestCase


class TestApplyBerserkBuff(TestCase):
    def test_apply_berserk_buff_status_zero_message(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
        test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
        actual = apply_berserk_buff('Berserk', test_description, test_character)
        expected = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks.'
                    ' Your damage is increased by 50% for 3 turns!')
        self.assertEqual(expected, actual)

    def test_apply_berserk_buff_status_zero_increase(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
        test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
        apply_berserk_buff('Berserk', test_description, test_character)
        expected = {'Damage Modifier': 1.5, 'Status': {'Berserk': 6}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_apply_berserk_buff_existing_berserk_status_return_message(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 2}}
        test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
        actual = apply_berserk_buff('Berserk', test_description, test_character)
        expected = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks.'
                    ' Your damage is increased by 50% for 3 turns!')
        self.assertEqual(expected, actual)

    def test_apply_berserk_buff_character_state_existing_status(self):
        test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 2}}
        test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
        apply_berserk_buff('Berserk', test_description, test_character)
        expected = {'Damage Modifier': 1.5, 'Status': {'Berserk': 8}}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_apply_berserk_buff_multiple_increases_return_message(self):
        test_character = {'Damage Modifier': 1.5, 'Status': {'Berserk': 6}}
        test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
        actual = apply_berserk_buff('Berserk', test_description, test_character)
        expected = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks.'
                    ' Your damage is increased by 50% for 3 turns!')
        self.assertEqual(expected, actual)

    def test_apply_berserk_buff_character_state_multiple_increases(self):
        test_character = {'Damage Modifier': 1.5, 'Status': {'Berserk': 6}}
        test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
        apply_berserk_buff('Berserk', test_description, test_character)
        expected = {'Damage Modifier': 2.0, 'Status': {'Berserk': 12}}
        actual = test_character
        self.assertEqual(expected, actual)