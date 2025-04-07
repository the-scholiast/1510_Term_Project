"""
This module tests get_monster_attack function from battle.py
"""
from battle import get_monster_attack
from unittest import TestCase
from unittest.mock import patch


class TestGetMonsterAttack(TestCase):
    @patch('random.choices', return_value=['Feral Charge'])
    def test_get_monster_attack_get_first_attack(self, _):
        expected = ['Feral Charge', 'Dashes forward, knocking down enemies.', 'Attack', 12]
        actual = get_monster_attack('Werewolf')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Crippling Bite'])
    def test_get_monster_attack_get_second_attack(self, _):
        expected = ['Crippling Bite', 'Bites the target causing bleed.', 'Bleed', 16]
        actual = get_monster_attack('Werewolf')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Lunar Frenzy'])
    def test_get_monster_attack_get_third_attack(self, _):
        expected = ['Lunar Frenzy', 'Enters a berserk state, increasing Health and Damage.', 'Buff', 0]
        actual = get_monster_attack('Werewolf')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Feral Charge'])
    def test_get_monster_attack_get_werewolf_attack(self, _):
        expected = ['Feral Charge', 'Dashes forward, knocking down enemies.', 'Attack', 12]
        actual = get_monster_attack('Werewolf')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Shadow Step'])
    def test_get_monster_attack_get_vampire_attack(self, _):
        expected = ['Shadow Step', 'Teleports behind the enemy for a surprise attack.', 'Attack', 15]
        actual = get_monster_attack('Vampire')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Claw Strike'])
    def test_get_monster_attack_get_shapeshifter_attack(self, _):
        expected = ['Claw Strike', 'A basic swipe with sharp claws dealing physical damage.', 'Attack', 8]
        actual = get_monster_attack('Shapeshifter')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Claw Slash'])
    def test_get_monster_attack_get_ghoul_attack(self, _):
        expected = ['Claw Slash', 'A basic claw swipe that deals physical damage.', 'Attack', 10]
        actual = get_monster_attack('Ghoul')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Savage Pounce'])
    def test_get_monster_attack_get_skinwalker_attack(self, _):
        expected = ['Savage Pounce', 'Leaps at the target with fangs and claws.', 'Attack', 8]
        actual = get_monster_attack('Skinwalker')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Poison Bite'])
    def test_get_monster_attack_get_wendigo_attack(self, _):
        expected = ['Poison Bite', 'A venomous bite that inflicts poison damage over time.', 'Poison', 10]
        actual = get_monster_attack('Wendigo')
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Ki blast'])
    def test_get_monster_attack_get_djinn_attack(self, _):
        expected = ['Ki blast', 'A blast of magical energy.', 'Attack', 12]
        actual = get_monster_attack('Djinn')
        self.assertEqual(expected, actual)