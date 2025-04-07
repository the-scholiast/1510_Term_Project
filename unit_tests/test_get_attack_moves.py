"""
This module tests get_attack_moves function from battle.py
"""
from battle import get_attack_moves
from unittest import TestCase


class TestGetAttackMoves(TestCase):
    def test_get_attack_moves_bear_stance(self):
        test_character = {'Active Stance': 'Bear'}
        expected = {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        }
        actual = get_attack_moves(test_character)
        self.assertEqual(expected, actual)

    def test_get_attack_moves_turtle_stance(self):
        test_character = {'Active Stance': 'Turtle'}
        expected = {
            'Bash': ['Coats the outer shield with spikes, then bashes into the enemy.', 'Physical', 15],
            'Shell': ['Take no damage next two turns.', 'Ki', 0],
            'Roar': ["A lion's mouth forms at the center of the shield and shoots a Ki wave.", 'Ki', 45]
        }
        actual = get_attack_moves(test_character)
        self.assertEqual(expected, actual)

    def test_get_attack_moves_snake_stance(self):
        test_character = {'Active Stance': 'Snake'}
        expected = {
            'Lash': ['Whip extends to lash its target.', 'Physical', 20],
            'Snare': ['Whip entangles its target, paralyzing its victim.', 'Ki', 12],
            'Hydra': ['Splits into hundreds of smaller whips making its attack unavoidable.', 'Ki', 50]
        }
        actual = get_attack_moves(test_character)
        self.assertEqual(expected, actual)