"""
This module tests merchant_offers function from encounters.py
"""
from encounters import merchant_offers
from unittest import TestCase


class TestMerchantOffers(TestCase):
    def test_merchant_offers_level_1(self):
        test_character = {"Level": 1}
        expected = {'Helmet': ('Iron Hat', 0.05), 'Armour': ('Copper Plate', 0.05),
                    'Ring': ('Copper Ring', 0.05), 'Amulet': ('Wooden Charm', 0.05)}
        actual = merchant_offers(test_character)
        self.assertEqual(expected, actual)

    def test_merchant_offers_level_2(self):
        test_character = {"Level": 2}
        expected = {'Helmet': ('Iron Helmet', 0.1), 'Armour': ('War Plate', 0.1),
                    'Ring': ('Ruby Ring', 0.1), 'Amulet': ('Crystal Pendant', 0.1)}
        actual = merchant_offers(test_character)
        self.assertEqual(expected, actual)

    def test_merchant_offers_level_3(self):
        test_character = {"Level": 3}
        expected = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
                    'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
        actual = merchant_offers(test_character)
        self.assertEqual(expected, actual)
