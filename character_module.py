"""
This module contains functions that make and edit the character.
"""
from encounters import user_input_hot_spring


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
    character = {
        'Name': f'{player_name}', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Current Health': 100,
        'Ki': 50, 'Current Ki': 50, 'Experience': 0, 'Defense Modifier': 1, 'Damage Modifier': 1,
        'Crystals': 0, 'X-coordinate': 0, 'Y-coordinate': 0, 'Items': {'Health Pots': 0, 'Shards': 0},
        'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""}, 'Stance': ['Bear'],
        'Status': {"Poison": 0, "Bleed": 0, 'Shell': 0, 'Berserk': 0}, 'Active Stance': 'Bear',
        'Active Defense Modifier': 1
    }
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
    character_items = character['Equipment']
    for equipment, item in items.items():
        character_items[equipment] = item


# Apply equipment stats
def apply_equipment(character: dict):
    defense_equipment = {"Helmet", "Armour"}
    damage_equipment = {"Ring", "Amulet"}
    character_equipment = character.get("Equipment")
    # Apply equipment modifier to character
    for equipment in character_equipment:
        if equipment[0] in defense_equipment:
            character["Defense Modifier"] += equipment[1]
        elif equipment[0] in damage_equipment:
            character["Damage Modifier"] += equipment[1]


def validate_move(board, character, direction):
    """
    Return True if the character's coordinates after moving are in the board else return False.

    :param board: a dictionary of length rows * columns where (row, column) tuples containing integers of every possible
                  combination are the dictionary keys, and their values are descriptions of the locations as strings
    :param character: a dictionary containing "X-coordinate":value and "Y-coordinate":value
                      (as string:int within range [0, 4]), and "Current HP":value (as string:int of range [1, 5])
    :param direction: an integer between [1, 4]
    :precondition: board and character must be non-empty dictionaries
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate", and "Current HP" as strings
    :precondition: board must contain all possible combinations of (X-coordinate, Y-coordinate) keys as tuples
                   of ints within range [0, 4] and random location descriptions as values of strings
    :precondition: character (X-coordinate value, Y-coordinate value) must be in board
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :precondition: Current HP value must be an integer within range [1, 5]
    :precondition: direction must be an integer between [1, 4] representing ('Up', 'Down', 'Left', Right')
    :postcondition: leave board and character unmodified
    :postcondition: check if the character's coordinates after moving are in the board
    :return: True if the character's coordinates after moving are in the board else return False

    >>> small_board = {(0, 0): "Empty room", (0, 1): "Corridor", (0, 2): "Colonnade", (0, 3): "Empty room"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(small_board, test_character, 1)
    False
    >>> small_board = {(0, 0): "Empty room", (1, 0): "Corridor", (2, 0): "Colonnade", (3, 0): "Empty room"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(small_board, test_character, 2)
    True
    >>> small_board = {(4, 4): "Empty room", (4, 3): "Corridor", (4, 2): "Colonnade", (4, 1): "Empty room"}
    >>> test_character = {"Y-coordinate": 4, "X-coordinate": 3, "Current HP": 5}
    >>> validate_move(small_board, test_character, 3)
    True
    """
    # Leave character unmodified
    new_x_coordinate = character["X-coordinate"]
    new_y_coordinate = character["Y-coordinate"]
    # Update the coordinate depending on direction
    if direction == 1:
        new_y_coordinate -= 1
    elif direction == 2:
        new_y_coordinate += 1
    elif direction == 3:
        new_x_coordinate += 1
    elif direction == 4:
        new_x_coordinate -= 1
    # Return True if coordinates in board else False
    return (new_y_coordinate, new_x_coordinate) in board


def move_character(character, direction):
    """
    Increment or decrement the character's X- or Y-coordinate depending on the direction.

    :param character: a dictionary containing "X-coordinate":value and "Y-coordinate":value
                      (as string:int within range [0, 4]), and "Current HP":value (as string:int of range [1, 5])
    :param direction: an integer between [1, 4]
    :precondition: character must be a non-empty dictionary
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate", and "Current HP" as strings
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :precondition: Current HP value must be an integer within range [1, 5]
    :precondition: direction must be an integer between [1, 4] representing ('Up', 'Down', 'Left', Right')
    :postcondition: X- and Y-coordinates values are integers within range [0, 4]
    :postcondition: increment or decrement character's X- or Y-coordinate depending on the direction

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> move_character(test_character, 2)
    >>> test_character == {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
    True
    >>> test_character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5}
    >>> move_character(test_character, 3)
    >>> test_character == {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5}
    True
    >>> test_character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5}
    >>> move_character(test_character, 1)
    >>> test_character == {"Y-coordinate": 3, "Current HP": 5, "X-coordinate": 3}
    True
    """
    # Modify the original character dictionary coordinates
    if direction == 1:
        character["Y-coordinate"] -= 1
    elif direction == 2:
        character["Y-coordinate"] += 1
    elif direction == 3:
        character["X-coordinate"] += 1
    elif direction == 4:
        character["X-coordinate"] -= 1


# EDIT TO INPUT 1 CHARACTER
def get_user_choice():
    """
    Return the direction ("Up", "Down", "Left", "Right") the user inputs.

    :postcondition: obtain a direction ("Up", "Down", "Left", "Right") as a string from the user
    :return: the direction ("Up", "Down", "Left", "Right") as a string based on the user input
    """
    directions = list(enumerate(("Up", "Down", "Right", "Left"), 1))
    for direction in directions:
        print(f"{direction[0]}. {direction[1]}")
    while True:
        valid_moves = {1, 2, 3, 4}
        user_direction = input("Please enter 1, 2, 3, or 4 to move: ").strip()
        if user_direction.isdigit() and int(user_direction) in valid_moves:
            return int(user_direction)