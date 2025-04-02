"""
This module contains all possible encounters with NPCs and monsters.
"""
import random


def check_encounter(character: dict, board: dict) -> bool:
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    return board[character_location] == '[!]'


def obtain_random_npc(npc_count: dict) -> str:
    """
    Obtain a random encounter depending on the weights.

    :param:
    :return:
    >>> obtain_random_npc({'Monsters': 14, 'Friendly': 7, 'Environment': 4})
    Werewolf
    >>> obtain_random_npc({'Monsters': 14, 'Friendly': 7, 'Environment': 4})
    Civilian
    >>> obtain_random_npc({'Monsters': 14, 'Friendly': 7, 'Environment': 4})
    Merchant
    """
    npc_list = {'Friendly': 'Merchant',
                'Monsters': ('Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'),
                'Environment': 'Hot Spring'
                }
    # Store how many of each encounter in a zone

    # Sort NPC list by its keys
    npc_list_keys = sorted(list(npc_list.keys()))

    # Create weighted NPC list
    weighted_list = [npc_count[npc_type] for npc_type in sorted(npc_list)]

    # Get a weighted random selection of encounter type
    random_type = random.choices(population=npc_list_keys,
                                 weights=weighted_list,
                                 k=1)[0]
    # Reduce weight of obtained NPC type
    npc_count[random_type] -= 1
    # Get random NPC from that type
    random_npc = random.choice(npc_list[random_type])
    return random_npc


# Merchant offers equipment depending on level
def merchant_offers(character: dict) -> dict:
    character_level = character.get("Level")
    # Equipment offerings based on character level
    equipment_by_level = {
        1: {'Helmet': ('Iron Hat', 0.02), 'Armour': ('Copper Plate', 0.04),
            'Ring': ('Copper Ring', 0.02), 'Amulet': ('Wooden Charm', 0.02)},
        2: {'Helmet': ('Iron Helmet', 0.04), 'Armour': ('War Plate', 0.08),
            'Ring': ('Ruby Ring', 0.04), 'Amulet': ('Crystal Pendant', 0.04)},
        3: {'Helmet': ('Steel Helmet', 0.06), 'Armour': ('Sun Plate', 0.12),
            'Ring': ('Warrior Ring', 0.06), 'Amulet': ('Focused Amulet', 0.06)}
    }
    return equipment_by_level.get(character_level, equipment_by_level[1])


# Print merchant offers
def print_merchant_offers():
    pass


# Get user equipment choice
def user_picks_equipment():
    pass


# Merchant gives equipment and character equips it
def obtain_and_equip():
    pass


# Hot spring encounter options
def hot_spring_encounter():
    pass


# Get user choice for hot spring
def user_input_hot_spring():
    pass


# Heals to full for Health and Ki or can receive items instead
def hot_spring_reward(character: dict):
    pass