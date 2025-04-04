"""
This module contains functions that make and edit the character.
"""


# Ask user for proper player name
def proper_name() -> str:
    """
    Prompt the user for a valid character name containing only letters.

    Continually prompts the user until they provide a valid name.

    :postcondition: user is prompted for input until a valid name is provided
    :return: a string containing only alphabetic characters representing the character name
    """
    # Keep asking user for valid name
    while True:
        player_name = input("Please enter a valid character name (letters only): ").strip()
        if player_name.isalpha():
            print(f"Thank you! Enjoy your time {player_name}!")
            return player_name
        else:
            print("Not a valid character name. Try again.")


# Make character including the player's name
def make_character(player_name: str) -> dict:
    """
    Create a new character dictionary with default starting attributes.

    Character contains starting stats, empty inventory, default stance,
    and base modifiers. The character starts at position (0, 0) with full Health and Ki.

    :param player_name: a string containing only alphabetic characters representing the character name
    :precondition: player_name must be a non-empty string
    :precondition: player_name must be only alphabetic characters
    :postcondition: creates a character dictionary with default starting values
    :return: a dictionary containing all character attributes including name, stats,
             position, inventory, equipment, and status effects
    """
    character = {
        'Name': f'{player_name}', 'Title': 'the Amateur',
        'Level': 1, 'Experience': 0,
        'Health': 150, 'Current Health': 150, 'Ki': 50, 'Current Ki': 50,
        'Defense Modifier': 1.0, 'Damage Modifier': 1.0, 'Active Defense Modifier': 1.0,
        'X-coordinate': 0, 'Y-coordinate': 0,
        'Crystals': 0,
        'Items': {'Health Pots': 0, 'Shards': 0},
        'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""},
        'Status': {"Poison": 0, "Bleed": 0, 'Shell': 0, 'Berserk': 0},
        'Stance': ['Bear'], 'Active Stance': 'Bear'
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


# Character equipments item
def obtain_and_equip(equipment_choice: tuple, character: dict):
    item_type, item_name, price = equipment_choice
    character_equipment = character['Equipment']
    character_equipment[item_type] = (item_name, price)
    print(f"You have equipped {item_name}!")


# Remove current equipment modifiers
def remove_equipment_modifiers(character: dict):
    defense_equipment = {"Helmet", "Armour"}
    damage_equipment = {"Ring", "Amulet"}
    # Get the dictionary storing equipment
    character_equipment = character.get("Equipment")
    # Remove equipment modifier to character
    for equipment_type, equipment_data in character_equipment.items():
        # Skip if no equipment in this slot
        if not equipment_data:
            continue
        # Equipment data is stored as a tuple (name, modifier)
        item_name, modifier = equipment_data
        # Remove modifier based on equipment type
        if equipment_type in defense_equipment:
            character["Defense Modifier"] -= modifier
        elif equipment_type in damage_equipment:
            character["Damage Modifier"] -= modifier

# Apply equipment stats
def apply_equipment(character: dict):
    defense_equipment = {"Helmet", "Armour"}
    damage_equipment = {"Ring", "Amulet"}
    # Get the dictionary storing equipment
    character_equipment = character.get("Equipment")
    # Apply equipment modifier to character
    for equipment_type, equipment_data in character_equipment.items():
        # Skip if no equipment in this slot
        if not equipment_data:
            continue
        # Equipment data is stored as a tuple (name, modifier)
        item_name, modifier = equipment_data
        # Apply modifier based on equipment type
        if equipment_type in defense_equipment:
            character["Defense Modifier"] += modifier
        elif equipment_type in damage_equipment:
            character["Damage Modifier"] += modifier


# Print increase in stats from equipment
def print_apply_equipment(equipment: tuple, character: dict):
    defense_equipment = {"Helmet", "Armour"}
    damage_equipment = {"Ring", "Amulet"}
    if equipment[0] in defense_equipment:
        print(f"Your Defense Modifier increased to {character['Defense Modifier']}!")
    elif equipment[0] in damage_equipment:
        print(f"Your Damage Modifier increased to {character['Damage Modifier']}!")


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
    :precondition: direction must be an integer between [1, 4] representing ('Up', 'Down', 'Left', 'Right')
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
    :precondition: direction must be an integer between [1, 4] representing ('Up', 'Down', 'Left', 'Right')
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


# Get direction represent as an integer between 1 and 4 ('Up', 'Down', 'Left', 'Right')
def get_user_choice():
    """
    Return the direction as an integer between [1, 4] representing ('Up', 'Down', 'Left', 'Right').

    :postcondition: obtain a direction as an integer between [1, 4] representing ('Up', 'Down', 'Left', 'Right')
                    from user input
    :return: the direction as an integer between [1, 4] representing ('Up', 'Down', 'Left', 'Right')
    """
    directions = list(enumerate(("Up", "Down", "Right", "Left"), 1))
    for direction in directions:
        print(f"{direction[0]}. {direction[1]}")
    while True:
        valid_moves = {1, 2, 3, 4}
        user_direction = input("Please enter 1, 2, 3, or 4 to move: ").strip()
        if user_direction.isdigit() and int(user_direction) in valid_moves:
            return int(user_direction)


# Character level up boost
def level_up(character: dict):
    """
    Update character Health, Ki, Damage Modifier, and Stance after leveling up.

    :param character: a dictionary containing character name, stats, items,
                      coordinates, equipment, status, level, and stance
    :precondition: character must be a dictionary containing all character attributes including name, stats,
                   position, inventory, equipment, and status effects
    """
    current_level = character['Level']
    current_exp = character['Experience']
    # Experience needed for each level
    exp_requirements = 150
    # Check if character can level up
    if current_level < 3 and current_exp >= exp_requirements:
        # Level up
        character['Level'] += 1
        # Update title
        update_title(character)
        # Update stats
        character['Health'] += 50
        character['Current Health'] = character['Health']
        character['Ki'] += 15
        character['Current Ki'] = character['Ki']
        character['Damage Modifier'] += 0.1
        # Add new stance at level 2
        if character['Level'] == 2:
            character['Stance'].append('Turtle')
        # Add another stance at level 3
        elif character['Level'] == 3:
            character['Stance'].append('Snake')
        # Reset character experience
        character['Experience'] = 0
        return True
    return False


# Print character leveling up
def print_level_up(character: dict):
    # Print the obtained stats
    print(f"Level Up! You are now level {character['Level']}!")
    print(f"New title: {character['Title']}")
    print(f"Health increased to {character['Health']}")
    print(f"Ki increased to {character['Ki']}")
    # Print the new unlocked stance
    if character['Level'] > 1:
        print(f"New stance unlocked: {character['Stance'][-1]}")


# Uses item from character inventory
def use_item(character: dict, item_choice: str):
    if item_choice == 'Health Pots':
        # Use health potion if available
        if character['Items']['Health Pots'] > 0:
            heal_amount = 50
            character['Current Health'] = min(character['Health'], character['Current Health'] + heal_amount)
            character['Items']['Health Pots'] -= 1
            print(f"You used a Health Potion and restored {heal_amount} health!")
    elif item_choice == 'Shards':
        # Use Ki shard if available
        if character['Items']['Shards'] > 0:
            ki_amount = 20
            character['Current Ki'] = min(character['Ki'], character['Current Ki'] + ki_amount)
            character['Items']['Shards'] -= 1
            print(f"You used a Shard and restored {ki_amount} Ki!")