"""
This module tests update_status_effects function from battle.py
"""
from battle import update_status_effects
from unittest import TestCase


class TestUpdateStatusEffects(TestCase):
    def test_update_status_effects_decrement_character_active_effects(self):
        test_character = {'Status': {'Shell': 2, 'Berserk': 3, 'Poison': 1, 'Bleed': 5},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.5}
        test_monster = {'Status': {'Buff': 2, 'Snared': 1}}
        update_status_effects(test_character, test_monster)
        expected = {'Status': {'Shell': 1, 'Berserk': 2, 'Poison': 0, 'Bleed': 4},
                    'Defense Modifier': 1.0, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.5}
        self.assertEqual(expected, test_character)

    def test_update_status_effects_decrement_monster_active_effects(self):
        test_character = {'Status': {'Shell': 2, 'Berserk': 3, 'Poison': 1, 'Bleed': 4},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.5}
        test_monster = {'Status': {'Buff': 2, 'Snared': 1}}
        update_status_effects(test_character, test_monster)
        expected = {'Status': {'Buff': 1, 'Snared': 0}}
        self.assertEqual(expected, test_monster)

    def test_update_status_effects_shell_expires_resets_defense_modifier(self):
        test_character = {'Status': {'Shell': 1, 'Berserk': 0, 'Poison': 0, 'Bleed': 0},
                          'Defense Modifier': 1.2, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 1.2
        self.assertEqual(expected, test_character['Active Defense Modifier'])

    def test_update_status_effects_shell_effect_decrements_to_zero(self):
        test_character = {'Status': {'Shell': 1, 'Berserk': 0, 'Poison': 1, 'Bleed': 0},
                          'Defense Modifier': 1.2, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 0
        self.assertEqual(expected, test_character['Status']['Shell'])

    def test_update_status_effects_berserk_expires_reduces_damage_modifier(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 1, 'Poison': 0, 'Bleed': 0},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.5}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 1.0
        self.assertEqual(expected, test_character['Damage Modifier'])

    def test_update_status_effects_berserk_effect_decrements_to_zero(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 1, 'Poison': 0, 'Bleed': 1},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.5}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 0
        self.assertEqual(expected, test_character['Status']['Berserk'])

    def test_update_status_effects_shell_reset_defense_with_custom_value(self):
        test_character = {'Status': {'Shell': 1, 'Berserk': 0, 'Poison': 0, 'Bleed': 0},
                          'Defense Modifier': 1.5, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 1.5
        self.assertEqual(expected, test_character['Active Defense Modifier'])

    def test_update_status_effects_poison_effect_decrements(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 3, 'Bleed': 0},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 2
        self.assertEqual(expected, test_character['Status']['Poison'])

    def test_update_status_effects_bleed_effect_decrements(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 0, 'Bleed': 3},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 2
        self.assertEqual(expected, test_character['Status']['Bleed'])

    def test_update_status_effects_monster_buff_decrements(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 0, 'Bleed': 0},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 2, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = 1
        self.assertEqual(expected, test_monster['Status']['Buff'])

    def test_update_status_effects_monster_snared_decrements(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 0, 'Bleed': 0},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 2}}
        update_status_effects(test_character, test_monster)
        expected = 1
        self.assertEqual(expected, test_monster['Status']['Snared'])

    def test_update_status_effects_inactive_effects_remain_zero(self):
        test_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 0, 'Bleed': 0},
                          'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
        test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
        update_status_effects(test_character, test_monster)
        expected = {'Shell': 0, 'Berserk': 0, 'Poison': 0, 'Bleed': 0}
        self.assertEqual(expected, test_character['Status'])