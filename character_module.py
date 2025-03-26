"""
This module contains functions that make and edit the character.
"""

# Ask user for proper player name
def proper_name():
    # Keep asking user for valid name
    while True:
        player_name = input("Please enter a valid character name (letters only): ").strip()
        if player_name.isalpha():
            print(f"Thank you! Enjoy your time {player_name}!")
            return player_name
        else:
            print("Not a valid character name. Try again.")


# Make character including the player's name
def make_character(player_name):
    character = {'Name': f'{player_name}', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Strength': 15,
                 'Speed': 10, 'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Spirit': 10, 'Experience': 0,
                 'Crystals': 0, 'Current Health': 100, 'X-coordinate': 0, 'Y-coordinate': 0,
                 'Items': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""}}
    return character


# Update the title of the character into it's name, depending on level
def update_title(character):
    current_level = character['Level']
    # Name for each level
    level_name = {1: 'Amateur', 2: 'Novice', 3: 'Accepted'}
    # Edit character title depending on level
    character['Title'] = f'the {level_name[current_level]}'
    return character


def equip_items(character: dict, items: dict):
    """
    Equip items onto character.

    :param character:
    :param items:
    """
    character_items = character['Items']
    for equipment, item in items.items():
        character_items[equipment] = item