"""
This module tests hot_spring_reward function from encounters.py
"""
import io
from encounters import hot_spring_reward
from unittest import TestCase
from unittest.mock import patch


class TestHotSpringReward(TestCase):
    def test_hot_spring_reward_choice_one_heal_health(self):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 1)
        expected = 100
        actual = test_character['Current Health']
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_one_restore_ki(self):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 1)
        expected = 50
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hot_spring_reward_choice_one_output_message(self, mock_output):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 1)
        expected = ("You relax in the warm spring. Your wounds heal and your ki is restored!\n"
                    "Health: 100/100\n"
                    "Ki: 50/50\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_one_already_full_health(self):
        test_character = {'Health': 100, 'Current Health': 100, 'Ki': 50, 'Current Ki': 50,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 1)
        expected = 100
        actual = test_character['Current Health']
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_one_already_full_ki(self):
        test_character = {'Health': 100, 'Current Health': 100, 'Ki': 50, 'Current Ki': 50,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        expected = 50
        actual = test_character['Current Ki']
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_obtain_two_health_pots(self):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 1, 'Shards': 3}}
        hot_spring_reward(test_character, 2)
        expected = 3
        actual = test_character['Items']['Health Pots']
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_obtain_two_shards(self):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 1, 'Shards': 3}}
        hot_spring_reward(test_character, 2)
        expected = 5
        actual = test_character['Items']['Shards']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hot_spring_reward_choice_two_output_message(self, mock_output):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 2)
        expected = ("You collected minerals from around the spring!\n"
                    "Gained: 2 Health Potion(s) and 2 Shard(s)\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_two_zero_health_pots(self):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 2)
        expected = 2
        actual = test_character['Items']['Health Pots']
        self.assertEqual(expected, actual)

    def test_hot_spring_reward_choice_two_zero_shards(self):
        test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
                          'Items': {'Health Pots': 0, 'Shards': 0}}
        hot_spring_reward(test_character, 2)
        expected = 2
        actual = test_character['Items']['Shards']
        self.assertEqual(expected, actual)
