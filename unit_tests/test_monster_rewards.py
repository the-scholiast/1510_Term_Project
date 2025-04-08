"""
This module tests monster_rewards function from battle.py
"""
import io
from battle import monster_rewards
from unittest import TestCase
from unittest.mock import patch


class TestMonsterRewards(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_rewards_level_1_character_print(self, mock_output):
        test_character = {'Crystals': 10, 'Level': 1, 'Experience': 0, 'Health': 200,
                          'Current Health': 150, 'Damage Modifier': 1.0}
        monster_rewards(test_character)
        expected = (
            "You have slain your foe!\n"
            "You gained 8 Crystals!\n"
            "Total Crystals: 18\n"
            "You gained 35 experience!\n"
        )
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_monster_rewards_level_1_character_gain_exp(self):
        test_character = {'Crystals': 10, 'Level': 1, 'Experience': 0, 'Health': 200,
                          'Current Health': 150, 'Damage Modifier': 1.0}
        monster_rewards(test_character)
        expected = {'Crystals': 18, 'Level': 1, 'Experience': 35, 'Health': 200,
                    'Current Health': 150, 'Damage Modifier': 1.0}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_rewards_level_3_character_print(self, mock_output):
        test_character = {'Crystals': 10, 'Level': 3, 'Experience': 0, 'Health': 200,
                          'Current Health': 150, 'Damage Modifier': 1.0}
        monster_rewards(test_character)
        expected = (
            "You have slain your foe!\n"
            "You gained 8 Crystals!\n"
            "Total Crystals: 18\n"
            "Your maximum Health has increased by 25 and Damage by 4%!\n"
        )
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_monster_rewards_level_3_character_gain_stats_and_no_exp(self):
        test_character = {'Crystals': 10, 'Level': 3, 'Experience': 0, 'Health': 150,
                          'Current Health': 150, 'Damage Modifier': 1.0}
        monster_rewards(test_character)
        expected = {'Crystals': 18, 'Level': 3, 'Experience': 0, 'Health': 175,
                    'Current Health': 175, 'Damage Modifier': 1.04}
        actual = test_character
        self.assertEqual(expected, actual)