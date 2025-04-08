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
            print(f"Thank you! Enjoy your time {player_name}!\n")
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
        'Health': 250, 'Current Health': 250, 'Ki': 60, 'Current Ki': 60,
        'Defense Modifier': 1.0, 'Damage Modifier': 1.2, 'Active Defense Modifier': 1.0,
        'X-coordinate': 0, 'Y-coordinate': 0,
        'Crystals': 0,
        'Items': {'Health Pots': 0, 'Shards': 0},
        'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""},
        'Status': {"Poison": 0, "Bleed": 0, 'Shell': 0, 'Berserk': 0},
        'Stance': ['Bear'], 'Active Stance': 'Bear'
    }
    return character


# Update the title of the character into it's name, depending on level
def update_title(character: dict) -> dict:
    """
    Update the character's title based on their current level.

    :param character: a dictionary containing character data with a 'Level' and 'Title' key
    :precondition: character must be a non-empty dictionary
    :precondition: character must have a 'Level' key with an integer value between [1, 3]
    :precondition: character must have a 'Title' key with a string value
    :postcondition: update the character's 'Title' to match their current level
    :return: character dictionary with updated title

    >>> test_character = {'Name': 'Alex', 'Level': 1, 'Title': ''}
    >>> updated_character = update_title(test_character)
    >>> updated_character['Title']
    'the Amateur'
    >>> test_character = {'Name': 'Sam', 'Level': 2, 'Title': 'the Amateur'}
    >>> updated_character = update_title(test_character)
    >>> updated_character['Title']
    'the Novice'
    >>> test_character = {'Name': 'Morgan', 'Level': 3, 'Title': 'the Novice'}
    >>> updated_character = update_title(test_character)
    >>> updated_character['Title']
    'the Accepted'
    """
    current_level = character['Level']
    # Name for each level
    level_name = {1: 'Amateur', 2: 'Novice', 3: 'Accepted'}
    # Edit character title depending on level
    character['Title'] = f'the {level_name[current_level]}'
    return character


# Character equipments item
def obtain_and_equip(equipment_choice: tuple, character: dict) -> None:
    """
    Equip a piece of equipment to the character's equipment slot.

    :param equipment_choice: a tuple containing (item type, item name, modifier)
    :param character: a dictionary containing character data with 'Equipment' key and
                      equipment slot keys as value
    :precondition: equipment_choice must be a tuple with 3 elements
    :precondition: equipment_choice must contain (item type, item name, modifier) as (str, str, float)
    :precondition: character must have an 'Equipment' key with a dictionary of equipment slots
    :precondition: character['Equipment'] must contain ('Helmet', 'Armour', 'Ring', 'Amulet') as keys
    :precondition: character['Equipment'] keys value must contain either empty strings or
                   tuples of (item name, modifier) values as (str, float > 0)
    :precondition: item type must be a valid equipment slot
    :postcondition: update the character's equipment with the new item
    :postcondition: print a message confirming equipment acquisition

    >>> test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
    >>> test_equipment = ('Helmet', 'Iron Hat', 0.02)
    >>> obtain_and_equip(test_equipment, test_character)
    You have equipped Iron Hat!
    >>> test_character['Equipment']['Helmet']
    ('Iron Hat', 0.02)
    >>> test_character = {'Equipment': {'Helmet': '', 'Armour': '', 'Ring': '', 'Amulet': ''}}
    >>> test_equipment = ('Ring', 'Ruby Ring', 0.04)
    >>> obtain_and_equip(test_equipment, test_character)
    You have equipped Ruby Ring!
    >>> test_character['Equipment']['Ring']
    ('Ruby Ring', 0.04)
    """
    item_type, item_name, price = equipment_choice
    character_equipment = character['Equipment']
    character_equipment[item_type] = (item_name, price)
    print(f"You have equipped {item_name}!")


# Remove current equipment modifiers
def remove_equipment_modifiers(character: dict) -> None:
    """
    Remove modifiers from all equipped items from the character's stats.

    :param character: a dictionary containing character data with 'Equipment',
                      'Defense Modifier', and 'Damage Modifier' keys
    :precondition: character must be a dictionary containing 'Equipment' key with equipment slots,
                   'Defense Modifier' key with float value, and 'Damage Modifier' key with float value
    :precondition: character['Equipment'] must contain ('Helmet', 'Armour', 'Ring', 'Amulet') as keys
    :precondition: character['Equipment'] keys value must contain either empty strings or
                   tuples of (item name, modifier) values as (str, float > 0)
    :postcondition: subtract equipment modifiers from character's stats based on equipment type

    >>> test_character = {'Equipment': {'Helmet': ('Iron Hat', 0.02), 'Armour': ('Copper Plate', 0.04),
    ...                                 'Ring': ('Copper Ring', 0.02), 'Amulet': ''},
    ...                   'Defense Modifier': 1.06, 'Damage Modifier': 1.02}
    >>> remove_equipment_modifiers(test_character)
    >>> expected_defense, expected_damage = 1.0, 1.0
    >>> actual_defense, actual_damage = test_character['Defense Modifier'], test_character['Damage Modifier']
    >>> (expected_defense, expected_damage) == (actual_defense, actual_damage)
    True
    >>> test_character = {'Equipment': {'Helmet': '', 'Armour': ('War Plate', 0.08),
    ...                                 'Ring': ('Ruby Ring', 0.04), 'Amulet': ('Crystal Pendant', 0.04)},
    ...                   'Defense Modifier': 1.08, 'Damage Modifier': 1.08}
    >>> remove_equipment_modifiers(test_character)
    >>> expected_defense, expected_damage = 1.0, 1.0
    >>> actual_defense, actual_damage = test_character['Defense Modifier'], test_character['Damage Modifier']
    >>> (expected_defense, expected_damage) == (actual_defense, actual_damage)
    True
    >>> test_character = {'Equipment': {'Helmet': '', 'Armour': '',
    ...                                 'Ring': '', 'Amulet': ''},
    ...                   'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
    >>> remove_equipment_modifiers(test_character)
    >>> expected_defense, expected_damage = 1.0, 1.0
    >>> actual_defense, actual_damage = test_character['Defense Modifier'], test_character['Damage Modifier']
    >>> (expected_defense, expected_damage) == (actual_defense, actual_damage)
    True
    """
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
def apply_equipment(character: dict) -> None:
    """
    Apply modifiers from equipped items to the character's stats.

    :param character: a dictionary containing character data with 'Equipment',
                      'Defense Modifier', and 'Damage Modifier' keys
    :precondition: character must be a dictionary containing 'Equipment' key with equipment slots,
                  'Defense Modifier' key with float value, and 'Damage Modifier' key with float value
    :precondition: character['Equipment'] must contain ('Helmet', 'Armour', 'Ring', 'Amulet') as keys
    :precondition: character['Equipment'] keys value must contain either empty strings or
                   tuples of (item name, modifier) values as (str, float > 0)
    :postcondition: add equipment modifiers to character's stats based on equipment type

    >>> test_character = {'Equipment': {'Helmet': ('Iron Hat', 0.02), 'Armour': ('Copper Plate', 0.04),
    ...                                 'Ring': ('Copper Ring', 0.02), 'Amulet': ''},
    ...                   'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
    >>> apply_equipment(test_character)
    >>> expected_defense, expected_damage = 1.06, 1.02
    >>> actual_defense, actual_damage = test_character['Defense Modifier'], test_character['Damage Modifier']
    >>> (expected_defense, expected_damage) == (actual_defense, actual_damage)
    True
    >>> test_character = {'Equipment': {'Helmet': '', 'Armour': ('War Plate', 0.08),
    ...                                 'Ring': ('Ruby Ring', 0.04), 'Amulet': ('Crystal Pendant', 0.04)},
    ...                   'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
    >>> apply_equipment(test_character)
    >>> expected_defense, expected_damage = 1.08, 1.08
    >>> actual_defense, actual_damage = test_character['Defense Modifier'], test_character['Damage Modifier']
    >>> (expected_defense, expected_damage) == (actual_defense, actual_damage)
    True
    >>> test_character = {'Equipment': {'Helmet': '', 'Armour': '',
    ...                                 'Ring': '', 'Amulet': ''},
    ...                   'Defense Modifier': 1.0, 'Damage Modifier': 1.0}
    >>> apply_equipment(test_character)
    >>> expected_defense, expected_damage = 1.00, 1.00
    >>> actual_defense, actual_damage = test_character['Defense Modifier'], test_character['Damage Modifier']
    >>> (expected_defense, expected_damage) == (actual_defense, actual_damage)
    True
    """
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
def print_apply_equipment(equipment: tuple, character: dict) -> None:
    """
    Print a message about increased character stats based on the item type.

    :param equipment: a tuple containing (item type, item name, modifier) as (str, str, float)
    :param character: a dictionary containing character data with 'Defense Modifier' and 'Damage Modifier' keys
                      with float values
    :precondition: equipment must be a tuple with 3 elements (item type, item name, modifier) as (str, str, float)
    :precondition: equipment[0] must be a string representing the item type
    :precondition: character must be a dictionary containing 'Defense Modifier' and 'Damage Modifier' keys
    :precondition: character['Defense Modifier'] and character['Damage Modifier'] values must be floats
    :postcondition: print a message about the increased stat based on item type

    >>> test_character = {'Defense Modifier': 1.06, 'Damage Modifier': 1.0}
    >>> test_equipment = ('Helmet', 'Iron Hat', 0.02)
    >>> print_apply_equipment(test_equipment, test_character)
    Your Defense Modifier increased to 1.06!
    >>> test_character = {'Defense Modifier': 1.0, 'Damage Modifier': 1.04}
    >>> test_equipment = ('Ring', 'Ruby Ring', 0.04)
    >>> print_apply_equipment(test_equipment, test_character)
    Your Damage Modifier increased to 1.04!
    >>> test_character = {'Defense Modifier': 1.12, 'Damage Modifier': 1.0}
    >>> test_equipment = ('Armour', 'War Plate', 0.08)
    >>> print_apply_equipment(test_equipment, test_character)
    Your Defense Modifier increased to 1.12!
    """
    defense_equipment = {"Helmet", "Armour"}
    damage_equipment = {"Ring", "Amulet"}
    if equipment[0] in defense_equipment:
        print(f"Your Defense Modifier increased to {character['Defense Modifier']}!")
    elif equipment[0] in damage_equipment:
        print(f"Your Damage Modifier increased to {character['Damage Modifier']}!")


# Check if character movement is valid and within the board boundaries
def validate_move(board: dict, character: dict, direction: int) -> bool:
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

    >>> small_board = {(0, 0): "[!]", (0, 1): "[!]", (0, 2): "[!]", (0, 3): "[!]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(small_board, test_character, 1)
    False
    >>> small_board = {(0, 0): "[!]", (1, 0): "[!]", (2, 0): "[!]", (3, 0): "[!]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(small_board, test_character, 2)
    True
    >>> small_board = {(4, 4): "[!]", (4, 3): "[!]", (4, 2): "[!]", (4, 1): "[!]"}
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


def move_character(character: dict, direction: int) -> None:
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
def get_user_choice() -> int:
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
def level_up(character: dict) -> bool:
    """
    Update character Health, Ki, Damage Modifier, and Stance after leveling up.

    :param character: a dictionary containing character name, stats, items,
                      coordinates, equipment, status, level, and stance
    :precondition: character must be a dictionary containing all character attributes including name, stats,
                   position, inventory, equipment, and status effects
    :postcondition: if character can level up, increase stats and generate True
    :postcondition: if character cannot level up, generate False
    :return: True if character leveled up else False

    >>> test_character = {'Level': 1, 'Experience': 100, 'Health': 200, 'Current Health': 180,
    ...                   'Ki': 50, 'Current Ki': 30, 'Damage Modifier': 1.0,
    ...                   'Stance': ['Bear'], 'Title': 'the Amateur'}
    >>> result = level_up(test_character)
    >>> (True, 2, 250, 250, 65, 65, 1.1, ['Bear', 'Turtle'], 0, 'the Novice') == (
    ...     result, test_character['Level'], test_character['Health'],
    ...     test_character['Current Health'], test_character['Ki'],
    ...     test_character['Current Ki'], test_character['Damage Modifier'],
    ...     test_character['Stance'], test_character['Experience'], test_character['Title']
    ... )
    True
    >>> test_character = {'Level': 2, 'Experience': 100, 'Health': 250, 'Current Health': 200,
    ...                   'Ki': 65, 'Current Ki': 40, 'Damage Modifier': 1.1,
    ...                   'Stance': ['Bear', 'Turtle'], 'Title': 'the Accepted'}
    >>> result = level_up(test_character)
    >>> (True, 3, 300, 300, 80, 80, 1.2, ['Bear', 'Turtle', 'Snake'], 0, 'the Accepted') == (
    ...     result, test_character['Level'], test_character['Health'],
    ...     test_character['Current Health'], test_character['Ki'],
    ...     test_character['Current Ki'], test_character['Damage Modifier'],
    ...     test_character['Stance'], test_character['Experience'], test_character['Title']
    ... )
    True
    """
    current_level = character['Level']
    current_exp = character['Experience']
    # Experience needed for each level
    exp_requirements = 100
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
        character['Current Ki'] = character['Ki']  # Fully restore ki on level up
        # Increase damage modifier and round to 2 decimal places to avoid floating-point precision issues
        character['Damage Modifier'] += 0.1
        character['Damage Modifier'] = round(character['Damage Modifier'], 2)
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


# Print character leveling up details
def print_level_up(character: dict) -> None:
    """
    Print detailed information about the character's level up progression.

    Displays the new level, title, increased health and ki,
    and newly unlocked stance if applicable.

    :param character: a dictionary containing character data
    :precondition: character must be a dictionary with 'Level', 'Title',
                   'Health', 'Ki', and 'Stance' keys
    :precondition: charater['Level'] value must be an integer between [1, 3]
    :precondition: charater['Title'] value must be a non-empty string
    :precondition: charater['Health'] value must be a positive integer > 0
    :precondition: charater['Ki'] value must be a positive integer > 0
    :precondition: charater['Stance'] value must be a list containing available stance as strings
    :postcondition: print the detailed information about the character's level up progression

    >>> test_character = {'Level': 2, 'Title': 'the Novice', 'Health': 250, 'Ki': 65, 'Stance': ['Bear', 'Turtle']}
    >>> print_level_up(test_character)
    Level Up! You are now level 2!
    New title: the Novice
    Health increased to 250
    Ki increased to 65
    New stance unlocked: Turtle
    >>> test_character = {'Level': 3, 'Title': 'the Accepted', 'Health': 300,
    ...                   'Ki': 80, 'Stance': ['Bear', 'Turtle', 'Snake']}
    >>> print_level_up(test_character)
    Level Up! You are now level 3!
    New title: the Accepted
    Health increased to 300
    Ki increased to 80
    New stance unlocked: Snake
    """
    # Print the obtained stats
    print(f"Level Up! You are now level {character['Level']}!")
    print(f"New title: {character['Title']}")
    print(f"Health increased to {character['Health']}")
    print(f"Ki increased to {character['Ki']}")
    # Print the new unlocked stance
    if character['Level'] > 1:
        print(f"New stance unlocked: {character['Stance'][-1]}")


# Uses item from character inventory
def use_item(character: dict, item_choice: str) -> None:
    """
    Use an item from the character's inventory to restore Health or Ki.

    :param character: A dictionary containing character's inventory and stats
    :param item_choice: A string specifying the item to use ('Health Pots' or 'Shards')
    :precondition: character must be a dictionary with 'Items', 'Health', 'Current Health',
                   'Ki', and 'Current Ki' keys
    :precondition: charater['Health'] value must be an integer > 0
    :precondition: charater['Current Health'] value be an integer between [1, charater['Health']]
    :precondition: charater['Ki'] value must be an integer >= 0
    :precondition: charater['Current Ki'] value be an integer between [0, charater['Ki']]
    :precondition: charater['Items'] contain 'Health Pots' and 'Shards' keys with integer values >= 0
    :postcondition: reduce the item count and increases health or ki if item is available
    :postcondition: print the restored amount from using an item

    >>> test_character = {'Health': 200, 'Current Health': 150, 'Ki': 50, 'Current Ki': 30,
    ...                   'Items': {'Health Pots': 2, 'Shards': 1}}
    >>> use_item(test_character, 'Health Pots')
    You used a Health Potion and restored 70 health!
    >>> test_character['Current Health']
    200
    >>> test_character['Items']['Health Pots']
    1
    >>> test_character = {'Health': 200, 'Current Health': 180, 'Ki': 50, 'Current Ki': 30,
    ...                   'Items': {'Health Pots': 1, 'Shards': 2}}
    >>> use_item(test_character, 'Shards')
    You used a Shard and restored 30 Ki!
    >>> test_character['Current Ki']
    50
    >>> test_character['Items']['Shards']
    1
    >>> test_character = {'Health': 200, 'Current Health': 180, 'Ki': 50, 'Current Ki': 30,
    ...                   'Items': {'Health Pots': 0, 'Shards': 0}}
    >>> use_item(test_character, 'Health Pots')
    >>> test_character['Current Health']
    180
    """
    if item_choice == 'Health Pots':
        # Use health potion if available
        if character['Items']['Health Pots'] > 0:
            heal_amount = 70
            # Make sure not to restore past Health
            character['Current Health'] = min(character['Health'], character['Current Health'] + heal_amount)
            character['Items']['Health Pots'] -= 1
            print(f"You used a Health Potion and restored {heal_amount} health!")
    elif item_choice == 'Shards':
        # Use Ki shard if available
        if character['Items']['Shards'] > 0:
            ki_amount = 30
            # Make sure not to restore past Ki
            character['Current Ki'] = min(character['Ki'], character['Current Ki'] + ki_amount)
            character['Items']['Shards'] -= 1
            print(f"You used a Shard and restored {ki_amount} Ki!")