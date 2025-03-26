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
    npc_list = {'Friendly': ['Civilian', 'Merchant', 'Guard', 'Fairy'],
                'Monsters': ['Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'],
                'Environment': ['Hot Spring']
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