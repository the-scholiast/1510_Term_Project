"""
This module tests obtain_random_npc function in encounters.py
"""
from encounters import obtain_random_npc
from unittest import TestCase
from unittest.mock import patch


class TestObtainRandomNpc(TestCase):
    @patch('random.choices', return_value=['Monsters'])
    @patch('random.choice', return_value=['Dijnn'])
    def test_obtain_random_npc_obtain_random_monster(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = 'Dijnn'
        actual = obtain_random_npc(npc_count)[0]
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Monsters'])
    @patch('random.choice', return_value=['Wendigo'])
    def test_obtain_random_npc_obtain_different_random_monster(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = 'Wendigo'
        actual = obtain_random_npc(npc_count)[0]
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Monsters'])
    @patch('random.choice', return_value=['Dijnn'])
    def test_obtain_random_npc_obtain_random_monster_decrement_npc_count(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = {'Monsters': 13, 'Friendly': 6, 'Environment': 4}
        obtain_random_npc(npc_count)
        actual = npc_count
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Friendly'])
    @patch('random.choice', return_value=['Merchant'])
    def test_obtain_random_npc_obtain_merchant(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = 'Merchant'
        actual = obtain_random_npc(npc_count)[0]
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Friendly'])
    @patch('random.choice', return_value=['Merchant'])
    def test_obtain_random_npc_obtain_merchant_decrement_npc_count(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = {'Monsters': 14, 'Friendly': 5, 'Environment': 4}
        obtain_random_npc(npc_count)
        actual = npc_count
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Environment'])
    @patch('random.choice', return_value=['Hot Spring'])
    def test_obtain_random_npc_obtain_hot_spring(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = 'Hot Spring'
        actual = obtain_random_npc(npc_count)[0]
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Environment'])
    @patch('random.choice', return_value=['Hot Spring'])
    def test_obtain_random_npc_obtain_hot_spring_decrement_npc_count(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
        expected = {'Monsters': 14, 'Friendly': 6, 'Environment': 3}
        obtain_random_npc(npc_count)
        actual = npc_count
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Monsters'])
    @patch('random.choice', return_value=['Dijnn'])
    def test_obtain_random_npc_only_one_count_non_zero(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 0, 'Environment': 0}
        expected = 'Dijnn'
        actual = obtain_random_npc(npc_count)[0]
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Monsters'])
    @patch('random.choice', return_value=['Dijnn'])
    def test_obtain_random_npc_one_count_non_zero(self, _, __):
        npc_count = {'Monsters': 14, 'Friendly': 3, 'Environment': 0}
        expected = 'Dijnn'
        actual = obtain_random_npc(npc_count)[0]
        self.assertEqual(expected, actual)