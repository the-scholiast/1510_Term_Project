"""
This module contains all possible encounters with NPCs and monsters.
"""
import random


def check_encounter(character: dict, board: dict) -> bool:
    """
    Return True if an encounter '[!]' is present at the character's location else False.

    :param character: a dictionary containing character coordinates with 'X-coordinate' and 'Y-coordinate' keys
    :param board: a dictionary representing the game board with (row, column) tuple keys and location markers
    :precondition: character must contain 'X-coordinate' and 'Y-coordinate' integer keys between [0, 4]
    :precondition: board must be a dictionary with (row, column) tuple keys (as ints == 5)
    :precondition: board must contain '[!]' or '   ' as values
    :postcondition: determine if the character's current location has an encounter
    :postcondition: leave character and board unmodified
    :return: True if an encounter '[!]' is present at the character's location else False

    >>> test_board = {(0, 0): '[!]', (0, 1): '[!]', (0, 2): '[!]', (0, 3): '[!]'}
    >>> test_character = {'Y-coordinate': 0, 'X-coordinate': 0}
    >>> check_encounter(test_character, test_board)
    True
    >>> test_board = {(0, 0): '[!]', (0, 1): '[!]', (0, 2): '[!]', (0, 3): '   '}
    >>> test_character = {'Y-coordinate': 0, 'X-coordinate': 3}
    >>> check_encounter(test_character, test_board)
    False
    >>> test_board = {(0, 0): '[!]', (0, 1): '[!]', (0, 2): '[!]', (0, 3): '[!]'}
    >>> test_character = {'Y-coordinate': 0, 'X-coordinate': 1}
    >>> check_encounter(test_character, test_board)
    True
    """
    character_location = (character['Y-coordinate'], character['X-coordinate'])
    return board[character_location] == '[!]'


def obtain_random_npc(npc_count: dict) -> str:
    """
    Obtain a random NPC encounter based on weighted probabilities.

    :param npc_count: a dictionary containing the counts of each NPC type (Friendly, Monsters, Environment)
    :precondition: npc_count must be a dictionary with keys 'Friendly', 'Monsters', 'Environment'
                   and integer values >= 0 representing the count of each NPC type
    :postcondition: select a random NPC type based on the weighted counts in npc_count
    :postcondition: decrement the count of the selected NPC type in npc_count by 1
    :postcondition: obtain a random NPC as a string from the list of NPCs for the chosen type
    :return: a string representing the randomly selected NPC
    """
    npc_list = {'Friendly': ['Merchant'],
                'Monsters': ['Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'],
                'Environment': ['Hot Spring']
                }
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
    """
    Return a dictionary of equipment offers based on the character level.

    :param character: a dictionary containing character data including 'Level' key with an integer value between [1, 3]
    :precondition: character must be a dictionary containing 'Level' key with an integer value between [1, 3]
    :postcondition: select the correct equipment dictionary based on character level
    :return: a dictionary containing equipment types ('Helmet', 'Armour', 'Ring', 'Amulet') as string keys and
             tuples of (item name, modifier) as values as (str:float)

    >>> test_character = {"Level": 1}
    >>> expected = {'Helmet': ('Iron Hat', 0.05), 'Armour': ('Copper Plate', 0.05),
    ...             'Ring': ('Copper Ring', 0.05), 'Amulet': ('Wooden Charm', 0.05)}
    >>> actual = merchant_offers(test_character)
    >>> expected == actual
    True
    >>> test_character = {"Level": 2}
    >>> expected = {'Helmet': ('Iron Helmet', 0.1), 'Armour': ('War Plate', 0.1),
    ...             'Ring': ('Ruby Ring', 0.1), 'Amulet': ('Crystal Pendant', 0.1)}
    >>> actual = merchant_offers(test_character)
    >>> expected == actual
    True
        >>> test_character = {"Level": 3}
    >>> expected = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
    ...             'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
    >>> actual = merchant_offers(test_character)
    >>> expected == actual
    True
    """
    character_level = character["Level"]
    # Equipment offerings based on character level
    equipment_by_level = {
        1: {'Helmet': ('Iron Hat', 0.05), 'Armour': ('Copper Plate', 0.05),
            'Ring': ('Copper Ring', 0.05), 'Amulet': ('Wooden Charm', 0.05)},
        2: {'Helmet': ('Iron Helmet', 0.1), 'Armour': ('War Plate', 0.1),
            'Ring': ('Ruby Ring', 0.1), 'Amulet': ('Crystal Pendant', 0.1)},
        3: {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
            'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
    }
    return equipment_by_level[character_level]


# Print merchant offers
def print_merchant_offers(equipment: dict) -> None:
    """
       Display the merchant's equipment offerings as a table.

       A table showing each equipment item with its type, name, and modifier value.

       :param equipment: a dictionary where keys are item types ('Helmet', 'Armour', 'Ring', 'Amulet')
                         and values are tuples of (item name, modifier) as (str, float)
       :precondition: equipment must be a non-empty dictionary with item types ('Helmet', 'Armour', 'Ring', 'Amulet')
                      as keys and tuples of (item name, modifier) as values
       :postcondition: print a table of merchant offerings

       >>> test_equipment = {'Helmet': ('Steel Helmet', 0.15), 'Armour': ('Sun Plate', 0.15),
       ...                   'Ring': ('Warrior Ring', 0.15), 'Amulet': ('Focused Amulet', 0.15)}
       >>> print_merchant_offers(test_equipment)
       Merchant: 'I have some fine wares for an adventurer like yourself!'
       ┌──────────────────────────────────────────────────┐
       │ #  ITEM TYPE     ITEM NAME           MODIFIER    │
       ├──────────────────────────────────────────────────┤
       │ 1. Helmet       Steel Helmet       +0.15 DEF     │
       │ 2. Armour       Sun Plate          +0.15 DEF     │
       │ 3. Ring         Warrior Ring       +0.15 DMG     │
       │ 4. Amulet       Focused Amulet     +0.15 DMG     │
       ├──────────────────────────────────────────────────┤
       """
    print("Merchant: 'I have some fine wares for an adventurer like yourself!'")
    # Print the top row
    print("┌" + "─" * 50 + "┐")
    print("│ #  ITEM TYPE     ITEM NAME           MODIFIER    │")
    print("├" + "─" * 50 + "┤")
    # Print each item
    for index, (item_type, (item_name, modifier)) in enumerate(equipment.items(), 1):
        # Determine modifier type based on item type
        mod_type = "DEF" if item_type in ["Helmet", "Armour"] else "DMG"
        print(f"│ {index}. {item_type:<12} {item_name:<18} +{modifier:.2f} {mod_type}     │")
    # Print bottom row
    print("├" + "─" * 50 + "┤")


# Get user equipment choice
def user_picks_equipment(equipment: dict) -> tuple:
    """
    Prompt the user to select equipment to obtain and return the selected item details.

    :param equipment: a dictionary where keys are item types and values are tuples of
                      (item name, modifier) as (str, float)
    :precondition: equipment must be a non-empty dictionary with item types ('Helmet', 'Armour', 'Ring', 'Amulet')
                   as keys and tuples of (item name, modifier) as values
    :postcondition: obtain a valid user selection from the available equipment options
    :return: a tuple containing (item type, item_name, modifier) as (str, str, float)
    """
    # Create mapping of numbers to item types
    equipment_types = list(equipment.keys())
    equipment_choice = {str(index): item_type for index, item_type in enumerate(equipment_types, 1)}
    while True:
        user_input = input("Enter the number of the item you wish to obtain: ").strip()
        if user_input in equipment_choice:
            item_type = equipment_choice[user_input]
            item_name, price = equipment[item_type]
            return item_type, item_name, price
        else:
            print(f"Invalid choice. Please enter a number between 1 and 4.")


# Hot spring encounter options
def hot_spring_encounter() -> None:
    """
    Print the hot spring encounter options to the user.

    :postcondition: print the hot spring description and available options
    """
    print("You've discovered a steaming hot spring nestled between large rocks!")
    print("The water has a slight blue hue and smells faintly of minerals.")
    print("┌" + "─" * 50 + "┐")
    print("│ What would you like to do?                       │")
    print("├" + "─" * 50 + "┤")
    print("│ 1. Bathe in the spring (fully restore Health/Ki) │")
    print("│ 2. Collect minerals (gain Health pots and shards)│")
    print("└" + "─" * 50 + "┘")


# Get user choice for hot spring
def user_input_hot_spring() -> int:
    """
    Return the user input (1 or 2) for hot spring encounter.

    Continuously prompt the user until they provide a valid choice (1 or 2).

    :postcondition: prompt user for input until a valid choice (1 or 2) is provided
    :postcondition: validate that user input is one of the valid choices ('1' or '2')
    :return: an integer (1 or 2) representing the user's validated choice
    """
    valid_choices = {"1", "2"}
    while True:
        user_choice = input("Enter your choice [1, 2]: ").strip()
        if user_choice in valid_choices:
            return int(user_choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Heals to full for Health and Ki or can receive items instead
def hot_spring_reward(character: dict, user_choice: int) -> None:
    """
    Apply rewards to the character based on their hot spring choice.

    :param character: a dictionary containing character data with 'Health', 'Current Health',
                      'Ki', 'Current Ki', and 'Items' keys
    :param user_choice: an integer (1 or 2)
    :precondition: character must contain 'Health', 'Current Health', 'Ki', 'Current Ki' keys with integer values >= 0
    :precondition: character must contain 'Items' key with a dictionary containing
                   'Health Pots' and 'Shards' keys with integer values >= 0
    :precondition: user_choice must be either 1 or 2
    :postcondition: if user_choice is 1, update character's 'Current Health' and 'Current Ki' to their maximum values
    :postcondition: if user_choice is 2, increase character's 'Health Pots' and 'Shards' values by 2 each
    :postcondition: print the correct message depennding on user_choice

    >>> test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
    ...                   'Items': {'Health Pots': 0, 'Shards': 0}}
    >>> hot_spring_reward(test_character, 1)
    You relax in the warm spring. Your wounds heal and your ki is restored!
    Health: 100/100
    Ki: 50/50
    >>> test_character
    {'Health': 100, 'Current Health': 100, 'Ki': 50, 'Current Ki': 50, 'Items': {'Health Pots': 0, 'Shards': 0}}
    >>> test_character = {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25,
    ...                   'Items': {'Health Pots': 1, 'Shards': 1}}
    >>> hot_spring_reward(test_character, 2)
    You collected minerals from around the spring!
    Gained: 2 Health Potion(s) and 2 Shard(s)
    >>> test_character
    {'Health': 100, 'Current Health': 50, 'Ki': 50, 'Current Ki': 25, 'Items': {'Health Pots': 3, 'Shards': 3}}
    """
    # Character uses hot spring. Restore Health and Ki to full
    if user_choice == 1:
        character["Current Health"] = character["Health"]
        character["Current Ki"] = character["Ki"]
        print("You relax in the warm spring. Your wounds heal and your ki is restored!")
        print(f"Health: {character['Current Health']}/{character['Health']}")
        print(f"Ki: {character['Current Ki']}/{character['Ki']}")
    # Collect items - health pots and shards
    else:
        health_pots = 2
        shards = 2
        character["Items"]["Health Pots"] += health_pots
        character["Items"]["Shards"] += shards
        print(f"You collected minerals from around the spring!")
        print(f"Gained: {health_pots} Health Potion(s) and {shards} Shard(s)")