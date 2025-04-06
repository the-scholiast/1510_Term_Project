"""
This module contains functions for the battle mechanic.
"""
import random
from itertools import cycle
from typing import Optional

from __init__ import BATTLE_STANCES


# Create monster with Health and stats as a dictionary
def create_monster(monster: str) -> dict:
    """
    Generate a monster with stats depending on its type.

    :param monster: is a string
    :precondition: monster must be ('Wendigo', 'Djinn', 'Skinwalker', 'Ghoul', 'Shapeshifter', 'Werewolf', 'Vampire')
    :postcondition: generate a monster represented as a dictionary containing its name and stats
    :return: a monster represented as a dictionary containing its name and stats

    >>> actual = create_monster('Ghoul')
    >>> expected = {'Name': 'Ghoul', 'Health': 80, 'Current Health': 80, 'Status': {'Buff': 0, 'Snared': 0},
    ... 'Damage Modifier': 1.0, 'Health Modifier': 1.0}
    >>> actual == expected
    True
    >>> actual = create_monster('Vampire')
    >>> expected = {'Name': 'Vampire', 'Health': 90, 'Current Health': 90, 'Status': {'Buff': 0, 'Snared': 0},
    ... 'Damage Modifier': 1.0, 'Health Modifier': 1.0}
    >>> actual == expected
    True
    """
    # Base health for different monster types
    monster_health = {
        'Wendigo': 100,
        'Djinn': 85,
        'Skinwalker': 90,
        'Ghoul': 80,
        'Shapeshifter': 95,
        'Werewolf': 110,
        'Vampire': 90
    }
    # Create monster dictionary with health and status
    monster_dict = {
        'Name': monster,
        'Health': monster_health.get(monster), 'Current Health': monster_health.get(monster),
        'Status': {'Buff': 0, 'Snared': 0},
        'Damage Modifier': 1.0, 'Health Modifier': 1.0
    }
    return monster_dict


# Obtain attack move from Monster
def get_monster_attack(monster: str) -> list:
    """
    Randomly select an attack move from a monster's available attacks using weighted probability.

    Attacks are selected with weighted probability: 50% for first attack, 35% for second, 15% for third.

    :param monster: a string representing the monster type
    :precondition: monster must be a string of: 'Wendigo', 'Djinn', 'Skinwalker', 'Ghoul',
                   'Shapeshifter', 'Werewolf', 'Vampire'
    :postcondition: select a random attack based on weighted probability
    :postcondition: generate a list containing [attack_name, description, attack_type, damage] as [str, str, str, int]
    :return: list containing [attack_name, description, attack_type, damage] as [str, str, str, int]
    """
    # Stores 3 monster attack moves. Its values are [Description, Move Type, Damage].
    monster_attack_list = {
        'Wendigo': {
            'Swipe': ['A vicious claw attack dealing physical damage.', 'Attack', 10],
            'Insatiable Hunger': ['A frenzied bite that heals the Wendigo.', 'Heal', 8],
            'Poison Bite': ['A venomous bite that inflicts poison damage over time.', 'Poison', 10]
        },
        'Djinn': {
            'Ki blast': ['A blast of magical energy.', 'Attack', 12],
            'Soul Drain': ['Drains the target’s life force to heal the Djinn.', 'Heal', 8],
            'Mind Crush': ['Overwhelms the target’s mind, causing mental damage and confusion.', 'Attack', 20]
        },
        'Skinwalker': {
            'Savage Pounce': ['Leaps at the target with fangs and claws.', 'Attack', 8],
            'Fear Howl': ['Unleashes a terrifying howl.', 'Attack', 12],
            'Vengeful Claws': ['Rakes the target with vicious claws, dealing heavy damage.', 'Bleed', 15]
        },
        'Ghoul': {
            'Claw Slash': ['A basic claw swipe that deals physical damage.', 'Attack', 10],
            'Bite': ['A quick bite that deals damage and has a chance to inflict bleed.', 'Bleed', 10],
            'Frenzied Strike': ['A rapid series of claw strikes that deal moderate damage.', 'Attack', 18]
        },
        'Shapeshifter': {
            'Claw Strike': ['A basic swipe with sharp claws dealing physical damage.', 'Attack', 8],
            'Quick Dash': ['Dashes forward, striking the enemy with a quick slash.', 'Attack', 12],
            'Form Strike': ['Transforms a part of the body into a weapon to strike the enemy.', 'Attack', 18]
        },
        'Werewolf': {
            'Feral Charge': ['Dashes forward, knocking down enemies.', 'Attack', 12],
            'Lunar Frenzy': ['Enters a berserk state, increasing Health and Damage.', 'Buff', 0],
            'Crippling Bite': ['Bites the target causing bleed.', 'Bleed', 16]
        },
        'Vampire': {
            'Blood Drain': ['Drinks the target’s blood to restore health.', 'Heal', 6],
            'Shadow Step': ['Teleports behind the enemy for a surprise attack.', 'Attack', 15],
            'Fang Strike': ['Delivers a powerful bite that deals damage and drains life force.', 'Heal', 16]
        }
    }
    # Get list of attacks
    attack_names = list(monster_attack_list[monster].keys())
    # Weighted list of monster attacks
    monster_attack_weights = [0.5, 0.35, 0.15]
    # Select weighted random attack
    attack_name = random.choices(attack_names, weights=monster_attack_weights, k=1)[0]
    attack_details = monster_attack_list[monster][attack_name]
    # Return list of attack name and its details
    return [attack_name] + attack_details


# Process standard attacks
def process_attack(character: dict, monster_modifier: float, damage: int, attack_name: str, description: str) -> str:
    """
    Apply standard monster attack to character Current Health and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0
    :param monster_modifier: a positive float number > 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: character must be a dictionary containing character data with
                   a 'Current Health' key with an integer value > 0
    :precondition: monster_modifier must be a positive float number > 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: multiply damage by monster_modifier
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: generate a string message containing attack_name, description, and damage
    :return: a string message containing attack_name, description, and damage

    >>> test_character = {'Current Health': 100}
    >>> test_description = 'A vicious claw attack dealing physical damage.'
    >>> process_attack(test_character, 1.5, 10, 'Swipe', test_description)
    'Monster used Swipe! A vicious claw attack dealing physical damage. You took 15 damage!'
    >>> print(test_character)
    {'Current Health': 85}
    >>> test_character = {'Current Health': 9}
    >>> test_description = 'Teleports behind the enemy for a surprise attack.'
    >>> process_attack(test_character, 1.0, 15, 'Shadow Step', test_description)
    'Monster used Shadow Step! Teleports behind the enemy for a surprise attack. You took 15 damage!'
    >>> print(test_character)
    {'Current Health': -6}
    """
    damage = int(damage * monster_modifier)
    character['Current Health'] -= damage
    return f"Monster used {attack_name}! {description} You took {damage} damage!"


# Process healing attacks
def process_heal_attack(character: dict, monster: dict, damage: int, attack_name: str, description: str) -> str:
    """
    Apply heal monster attack to monster Current Health, character Current Health, and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0
    :param monster: a dictionary containing monster data with a 'Current Health' key with an integer value > 0
                    and 'Damage Modifier' key with a float > 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: monster must be a dictionary containing character data with
                   a 'Current Health' key with an integer value > 0 and 'Damage Modifier' key with a float > 0
    :precondition: character must be a dictionary containing character data with
                   a 'Current Health' key with an integer value > 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: multiply damage by monster_modifier
    :postcondition: increase monster Current Health by heal amount
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: generate a string message containing attack_name, description, damage, and heal_amount
    :return: a string message containing attack_name, description, damage, and heal_amount

    >>> test_character = {'Current Health': 100}
    >>> test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
    >>> test_description = 'Drinks the target’s blood to restore health.'
    >>> expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
    ...             'You took 6 damage! Monster healed for 3 health!')
    >>> expected == process_heal_attack(test_character, test_monster, 6, 'Blood Drain', test_description)
    True
    >>> print(test_character, test_monster)
    {'Current Health': 94} {'Current Health': 103, 'Damage Modifier': 1.0}
    >>> test_character = {'Current Health': 1}
    >>> test_monster = {'Current Health': 1, 'Damage Modifier': 2.0}
    >>> test_description = 'Drinks the target’s blood to restore health.'
    >>> expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
    ...             'You took 12 damage! Monster healed for 6 health!')
    >>> expected == process_heal_attack(test_character, test_monster, 6, 'Blood Drain', test_description)
    True
    >>> print(test_character, test_monster)
    {'Current Health': -11} {'Current Health': 7, 'Damage Modifier': 2.0}
    """
    damage = int(damage * monster['Damage Modifier'])
    heal_amount = damage // 2
    monster['Current Health'] += heal_amount
    character['Current Health'] -= damage
    message = (f"Monster used {attack_name}! {description} You took {damage} damage! "
               f"Monster healed for {heal_amount} health!")
    return message


# Process poison attacks and add poison status
def process_poison_attack(character: dict, monster_modifier: float, damage: int,
                          attack_name: str, description: str) -> str:
    """
    Apply poison monster attack to character Current Health and Status, and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0 and
                      'Status' key containing a dictionary of Poison:value as (str:int >= 0)
    :param monster_modifier: a positive float number > 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: character must be a dictionary containing character data with a 'Current Health' key with
                   an integer value > 0 and 'Status' key containing a dictionary of Poison:value as (str:int >= 0)
    :precondition: monster_modifier must be a positive float number > 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: multiply damage by monster_modifier
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: increase character Poison Status by 4
    :postcondition: generate a string message containing attack_name, description, and damage
    :return: a string message containing attack_name, description, and damage

    >>> test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
    >>> test_description = 'A venomous bite that inflicts poison damage over time.'
    >>> expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
    ...             'You took 15 damage and are poisoned!')
    >>> expected == process_poison_attack(test_character, 1.5, 10, 'Poison Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 85, 'Status': {'Poison': 4}}
    >>> test_character = {'Current Health': 10, 'Status': {'Poison': 4}}
    >>> test_description = 'A venomous bite that inflicts poison damage over time.'
    >>> expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
    ...             'You took 10 damage and are poisoned!')
    >>> expected == process_poison_attack(test_character, 1.0, 10, 'Poison Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 0, 'Status': {'Poison': 8}}
    """
    damage = int(damage * monster_modifier)
    character['Current Health'] -= damage
    # Lasts for 4 turns
    character['Status']['Poison'] += 4
    return f"Monster used {attack_name}! {description} You took {damage} damage and are poisoned!"


# Process bleed attacks and add bleed status
def process_bleed_attack(character: dict, monster_modifier: float, damage: int,
                         attack_name: str, description: str) -> str:
    """
    Apply bleed monster attack to character Current Health and Status, and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0 and
                      'Status' key containing a dictionary of Bleed:value as (str:int >= 0)
    :param monster_modifier: a positive float number > 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: character must be a dictionary containing character data with a 'Current Health' key with
                   an integer value > 0 and 'Status' key containing a dictionary of Bleed:value as (str:int >= 0)
    :precondition: monster_modifier must be a positive float number > 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: multiply damage by monster_modifier
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: increase character Bleed Status by 2
    :postcondition: generate a string message containing attack_name, description, and damage
    :return: a string message containing attack_name, description, and damage

    >>> test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
    >>> test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
    >>> expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
    ...             'You took 15 damage and are bleeding!')
    >>> expected == process_bleed_attack(test_character, 1.5, 10, 'Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 85, 'Status': {'Bleed': 2}}
    >>> test_character = {'Current Health': 10, 'Status': {'Bleed': 2}}
    >>> test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
    >>> expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
    ...             'You took 10 damage and are bleeding!')
    >>> expected == process_bleed_attack(test_character, 1.0, 10, 'Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 0, 'Status': {'Bleed': 4}}
    """
    damage = int(damage * monster_modifier)
    character['Current Health'] -= damage
    # Lasts for 2 turns
    character['Status']['Bleed'] += 2
    return f"Monster used {attack_name}! {description} You took {damage} damage and are bleeding!"


# Process buff attacks
def process_buff_attack(monster: dict, attack_name: str, description: str) -> str:
    """
    Increase Damage Modifier, Health Modifier, Current Health values, and return message of the attack description.

    :param monster: a dictionary containing monster data with: a 'Current Health' key with an integer value > 0,
                    'Damage Modifier' key with a float > 0, 'Health Modifier' key with a float > 0
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: monster must be a dictionary containing monster data with: a 'Current Health' key with
                   an integer value > 0, 'Damage Modifier' key with a float > 0, 'Health Modifier' key with a float > 0
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: increase 'Damage Modifier' value by 0.2
    :postcondition: increase 'Health Modifier' value by 0.5
    :postcondition: increase 'Current Health' value by multiple of 'Health Modifier'
    :postcondition: generate a string message containing attack_name and description
    :return: a string message containing attack_name and description

    >>> test_monster = {'Damage Modifier': 1.0, 'Health Modifier': 1.0, 'Current Health': 100}
    >>> test_description = 'Enters a berserk state, increasing Health and Damage.'
    >>> expected_message = ("Monster used Lunar Frenzy! Enters a berserk state, increasing Health and Damage. "
    ...                     "Monster's damage and Health is increased!")
    >>> expected_message == process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
    True
    >>> print(test_monster)
    {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 150}
    >>> test_monster = {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 50}
    >>> test_description = 'Enters a berserk state, increasing Health and Damage.'
    >>> expected_message = ("Monster used Lunar Frenzy! Enters a berserk state, increasing Health and Damage. "
    ...                     "Monster's damage and Health is increased!")
    >>> expected_message == process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
    True
    >>> print(test_monster)
    {'Damage Modifier': 1.4, 'Health Modifier': 2.0, 'Current Health': 100}
    """
    monster['Damage Modifier'] += 0.2
    monster['Health Modifier'] += 0.5
    monster['Current Health'] = int(monster['Current Health'] * monster['Health Modifier'])
    return f"Monster used {attack_name}! {description} Monster's damage and Health is increased!"


# Check if character is defeated and append defeat message if True
def check_character_defeat(character: dict, message: str) -> str:
    """
    Append a defeat message to the original message if character's Current Health is 0 or less.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value
    :param message: a string representing the current battle message
    :precondition: character must be a dictionary containing character data with a 'Current Health' key
                   with an integer value
    :precondition: message must be a non-empty string
    :postcondition: leave character unmodified
    :postcondition: append defeat message to original message if character's Current Health is <= 0
    :return: the original message or original message with defeat message appended

    >>> test_character = {'Current Health': 10}
    >>> test_message = "Monster used Swipe! You took 5 damage!"
    >>> check_character_defeat(test_character, test_message)
    'Monster used Swipe! You took 5 damage!'
    >>> test_character = {'Current Health': 0}
    >>> test_message = "Monster used Swipe! You took 10 damage!"
    >>> check_character_defeat(test_character, test_message)
    'Monster used Swipe! You took 10 damage!\\nYou have been defeated!'
    >>> test_character = {'Current Health': -5}
    >>> test_message = "Monster used Soul Drain! You took 15 damage!"
    >>> check_character_defeat(test_character, test_message)
    'Monster used Soul Drain! You took 15 damage!\\nYou have been defeated!'
    """
    if character['Current Health'] <= 0:
        message += "\nYou have been defeated!"
    return message


# Apply monster attack and its effect to character -->> move to game()?
def apply_monster_attack(attack: list, character: dict, monster: dict):
    # Unpack attack list
    attack_name, description, attack_type, damage = attack
    # Obtain 'Damage Modifier' value from monster
    monster_modifier = monster['Damage Modifier']
    # Process attack based on type
    if attack_type == 'Attack':
        message = process_attack(character, monster_modifier, damage, attack_name, description)
    elif attack_type == 'Heal':
        message = process_heal_attack(character, monster, damage, attack_name, description)
    elif attack_type == 'Poison':
        message = process_poison_attack(character, monster_modifier, damage, attack_name, description)
    elif attack_type == 'Bleed':
        message = process_bleed_attack(character, monster_modifier, damage, attack_name, description)
    # Buff type
    else:
        message = process_buff_attack(monster, attack_name, description)
    # Check if character is defeated
    message = check_character_defeat(character, message)
    # Display the message
    print(message)


# Use itertools.cycle to obtain cycling turn order for character and monster
def turn_order(monster: str) -> tuple:
    """
    Determine the turn order between the character and monster with a 50% chance for either to go first.

    Create an infinite cycle of turns using itertools.cycle and returns a message indicating who strikes first.

    :param monster: a string representing the monster's name
    :precondition: monster must be a non-empty string representing the monster's name
    :postcondition: determine if character or monster goes first with 50% probability
    :postcondition: create an infinite cycle iterator for alternating turns
    :return: a tuple containing (turns_iterator, first_strike_message) where turns_iterator is an
             itertools.cycle object alternating between 'character' and 'monster', and first_strike_message
             is a string indicating who strikes first
    """
    # 50% chance to go first
    if random.randint(1, 2) == 1:
        first_strike_message = "You strike first!"
        turns = cycle(['character', 'monster'])
    else:
        first_strike_message = f"The {monster} strikes first!"
        turns = cycle(['monster', 'character'])
    return turns, first_strike_message


# Skip monster turn if snared
def skip_turn(monster: dict) -> bool:
    """
    Check if the monster is snared and should skip its turn.

    Print a message if the monster is snared and cannot move this turn.

    :param monster: a dictionary containing monster data with a 'Name' key with a string value
                    and a 'Status' key with a dictionary containing a 'Snared' key with an integer value >= 0
    :precondition: monster must be a dictionary containing monster data with a 'Name' key with a string value
                   and a 'Status' key with a dictionary containing a 'Snared' key with an integer value >= 0
    :postcondition: leave monster unmodified
    :postcondition: print message if monster is snared
    :return: True if Snared value > 0 else False

    >>> test_monster = {'Name': 'Werewolf', 'Status': {'Snared': 0}}
    >>> skip_turn(test_monster)
    False
    >>> test_monster = {'Name': 'Vampire', 'Status': {'Snared': 1}}
    >>> skip_turn(test_monster)
    Vampire is snared and cannot move this turn!
    True
    >>> test_monster = {'Name': 'Wendigo', 'Status': {'Snared': 2}}
    >>> skip_turn(test_monster)
    Wendigo is snared and cannot move this turn!
    True
    """
    # Check if monster is snared
    if monster['Status']['Snared'] > 0:
        print(f"{monster['Name']} is snared and cannot move this turn!")
        return True
    return False


# Display battle menu with options in Pokemon-style format
def display_battle_menu():
    """
    Display the main battle menu option in Pokemon-style.

    Print a visual menu with three options: STANCE, ITEM, and FIGHT, each enclosed in a box
    drawn with Unicode box drawing characters.

    :postcondition: print a blank line followed by a formatted battle menu to the console
    :postcondition: menu displays three numbered options: 1.STANCE, 2.ITEM, and 3.FIGHT
    :postcondition: options are enclosed in Unicode box drawing characters to create a visual menu

    >>> display_battle_menu()
    <BLANKLINE>
    ┌────────────┐  ┌────────────┐
    │  1.STANCE  │  │   2.ITEM   │
    └────────────┘  └────────────┘
    ┌────────────┐
    │  3.FIGHT   │
    └────────────┘
    """
    # Display main battle menu
    print()
    print("┌────────────┐  ┌────────────┐")
    print("│  1.STANCE  │  │   2.ITEM   │")
    print("└────────────┘  └────────────┘")
    print("┌────────────┐")
    print("│  3.FIGHT   │")
    print("└────────────┘")


# Get user input for battle menu interaction
def get_user_choice_battle_menu() -> str:
    """
    Prompt the user to select an option from the battle menu and validate their input.

    Continuously prompts the user until they provide a valid choice (1, 2, 3),
    which corresponds to STANCE, ITEM, or FIGHT from the battle menu.

    :postcondition: prompt user for input until a valid choice is provided
    :postcondition: validate that user input is one of the valid choices ('1', '2', '3')
    :return: a string containing the user's validated choice ('1', '2', '3')
    """
    # Get user choice from battle menu
    valid_choices = {'1', '2', '3'}
    while True:
        choice = input("What will you do? Enter option [1, 3]: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. The option name.")


# Display available stances when clicking from display_battle_menu
def display_stances(character: dict):
    """
    Display all available stances for the character in a box with numbered options.

    :param character: a dictionary containing character data with a 'Stance' key that contains a list of stance names
    :precondition: character must be a dictionary containing character data with a 'Stance' key
    :precondition: character['Stance'] must be a non-empty list of strings representing stance names
    :postcondition: print a formatted box of available stances with numbered options
    :postcondition: print a back option as the last option in the menu

    >>> test_character = {'Stance': ['Bear', 'Turtle']}
    >>> display_stances(test_character)
    Available Stances:
    ┌──────────────────────┐
    │ 1. Bear              │
    │ 2. Turtle            │
    ├──────────────────────┤
    │ 0. Back              │
    └──────────────────────┘
    >>> test_character = {'Stance': ['Bear']}
    >>> display_stances(test_character)
    Available Stances:
    ┌──────────────────────┐
    │ 1. Bear              │
    ├──────────────────────┤
    │ 0. Back              │
    └──────────────────────┘
    >>> test_character = {'Stance': ['Bear', 'Turtle', 'Snake']}
    >>> display_stances(test_character)
    Available Stances:
    ┌──────────────────────┐
    │ 1. Bear              │
    │ 2. Turtle            │
    │ 3. Snake             │
    ├──────────────────────┤
    │ 0. Back              │
    └──────────────────────┘
    """
    available_stances = character['Stance']
    print("Available Stances:")
    print("┌" + "─" * 22 + "┐")
    # Display each available stance
    for index, stance_name in enumerate(available_stances, 1):
        print(f"│ {index}. {stance_name:<17} │")
    print("├" + "─" * 22 + "┤")
    print(f"│ {"0. Back":<20} │")
    print("└" + "─" * 22 + "┘")


# Get user input for stances or back to display_battle_menu
def get_stance(character: dict) -> Optional[str]:
    """
    Prompt the user to select a stance from available options or return to the main battle menu.

    Update the character's active stance based on user selection and display the stance description.
    Return the selected stance name or None if the user chooses to go back.

    :param character: a dictionary containing character data with 'Stance' and 'Active Stance' keys
    :precondition: character must be a dictionary containing 'Stance' (list of available stances)
                   and 'Active Stance' (current stance) keys
    :precondition: character['Stance'] must be a non-empty list of strings representing stance names
    :precondition: BATTLE_STANCES must contain tuples of (stance_name, description)
    :postcondition: if user selects a valid stance, update character 'Active Stance' and print the description
    :postcondition: if user selects '0' return to main menu without changes
    :return: the selected stance name as a string if a valid stance is selected or None if user selects to go back
    """
    available_stances = character['Stance']
    available_stances_index = [str(index) for index, stance in enumerate(character['Stance'], 1)]
    # Ask user for stance or back to display_battle_menu
    while True:
        user_choice = input("Select a stance by index number or type 0 to return: ").strip()
        # Back to display_battle_menu
        if user_choice == '0':
            return
        elif user_choice in available_stances_index:
            # Update character's active stance
            character['Active Stance'] = available_stances[int(user_choice) - 1]
            print(f"You adopt the {character['Active Stance']} stance!")
            # Obtain the stance_description
            stance_descriptions = {stance[0]: stance[1] for stance in BATTLE_STANCES}
            description = stance_descriptions[character['Active Stance']]
            print(f"{description}")
            # Return the stance
            return character['Active Stance']
        else:
            print("Invalid stance. Please select from the available options.")


# Display items when clicking from display_battle_menu
def display_items(character: dict):
    """
    Display the character's available items in a menu box.

    Show each item with its quantity for items that have a quantity greater than 0.
    If no items are available, displays a message indicating this. Always include a "Back" option as option 0.

    :param character: a dictionary containing character data with an 'Items' key
                      that contains a dictionary of item name:quantity pairs (as str: int >= 0)
    :precondition: character must be a dictionary containing an 'Items' key
    :precondition: character['Items'] must be a dictionary with 'Health Pots' and 'Shards' string keys
                   and integer values >= 0
    :postcondition: print a menu of available items with quantities and a back option

    >>> test_character = {'Items': {'Health Pots': 2, 'Shards': 0}}
    >>> display_items(test_character)
    Available Items:
    ┌──────────────────────┐
    │ 1. Health Pots  x2   │
    ├──────────────────────┤
    │ 0. Back              │
    └──────────────────────┘
    >>> test_character = {'Items': {'Health Pots': 0, 'Shards': 0}}
    >>> display_items(test_character)
    Available Items:
    ┌──────────────────────┐
    │ No items available   │
    ├──────────────────────┤
    │ 0. Back              │
    └──────────────────────┘
    >>> test_character = {'Items': {'Health Pots': 2, 'Shards': 1}}
    >>> display_items(test_character)
    Available Items:
    ┌──────────────────────┐
    │ 1. Health Pots  x2   │
    │ 2. Shards       x1   │
    ├──────────────────────┤
    │ 0. Back              │
    └──────────────────────┘
    """
    items = character['Items']
    print("Available Items:")
    print("┌" + "─" * 22 + "┐")
    # Display each item and its quantity
    index = 1
    for item_name, quantity in items.items():
        if quantity > 0:
            print(f"│ {index}. {item_name:<12} x{quantity:<3} │")
            index += 1
    # If no items available
    if all(quantity == 0 for quantity in items.values()):
        print(f"│ {'No items available':<20} │")
    print("├" + "─" * 22 + "┤")
    print(f"│ 0. {"Back":<17} │")
    print("└" + "─" * 22 + "┘")


# Get user input for items or back to display_battle_menu
def get_item(character: dict) -> Optional[str]:
    """
    Obtain the user's item selection from the available items in the character's inventory.

    Prompt the user to select an item by index number from their available items,
    or allows user to return to the battle menu. Only items with quantity > 0 are available.

    :param character: a dictionary containing character data with an 'Items' key
                      that contains a dictionary of item name:quantity pairs (as str: int >= 0)
    :precondition: character must be a dictionary containing an 'Items' key
    :precondition: character['Items'] must be a dictionary with
                   'Health Pots' and 'Shards' string keys and integer values >= 0
    :postcondition: validate user input to ensure it corresponds to an available item or back option
    :postcondition: obtain the selected item name as a string, or None if the user chooses to go back or has no items
    :return: the selected item name as a string, or None if the user chooses to go back or has no items
    """
    items = character['Items']
    available_items = [item for item, quantity in items.items() if quantity > 0]
    # If no items available, return to battle menu
    if not available_items:
        input("Press Enter to return to battle menu...")
        return None
    while True:
        user_choice = input("Select an item by index number or type 0 to return: ").strip()
        # Make sure user choice is a digit between 0 and length of available items
        if user_choice.isdigit() and len(available_items) >= int(user_choice) >= 0:
            return available_items[int(user_choice) - 1]
        elif user_choice == '0':
            return None
        else:
            print("Invalid item. Please select from the available options.")


# Obtain character attack moves by stance
def get_attack_moves(character: dict) -> dict:
    """
    Obtain the attack moves available to a character based on their active stance.

    Each stance (Bear, Turtle, Snake) has three unique attack moves.
    Attack moves are returned as a dictionary where keys are attack names and values are lists
    containing [description, attack_type, damage] as (str, str, int > 0).

    :param character: a dictionary containing character data with an 'Active Stance' key
                      that specifies which stance the character is currently using
    :precondition: character must be a dictionary containing an 'Active Stance' key
    :precondition: character['Active Stance'] must be one of: 'Bear', 'Turtle', 'Snake'
    :postcondition: obtain a dictionary of attack moves where keys are attack names and values are lists
                    containing [description, attack_type, damage] as (str, str, int > 0)
    :postcondition: leave character unmodified
    :return: a dictionary of attack moves where keys are attack names and values are lists
             containing [description, attack_type, damage] as (str, str, int > 0)

    >>> test_character = {'Active Stance': 'Bear'}
    >>> actual = get_attack_moves(test_character)
    >>> expected = {'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
    ...             'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
    ...             'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]}
    >>> actual == expected
    True
    >>> test_character = {'Active Stance': 'Turtle'}
    >>> actual = get_attack_moves(test_character)
    >>> expected = {'Bash': ['Coats the outer shield with spikes, then bashes into the enemy.', 'Physical', 15],
    ...             'Shell': ['Take no damage next two turns.', 'Ki', 0],
    ...             'Roar': ["A lion's mouth forms at the center of the shield and shoots a Ki wave.", 'Ki', 45]}
    >>> actual == expected
    True
    >>> test_character = {'Active Stance': 'Snake'}
    >>> actual = get_attack_moves(test_character)
    >>> expected = {'Lash': ['Whip extends to lash its target.', 'Physical', 20],
    ...             'Snare': ['Whip entangles its target, paralyzing its victim.', 'Ki', 12],
    ...             'Hydra': ['Splits into hundreds of smaller whips making its attack unavoidable.', 'Ki', 50]}
    >>> actual == expected
    True
    """
    # Store character's attack moves
    character_attacks = {
        'Bear': {
            'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
            'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
            'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
        },
        'Turtle': {
            'Bash': ['Coats the outer shield with spikes, then bashes into the enemy.', 'Physical', 15],
            'Shell': ['Take no damage next two turns.', 'Ki', 0],
            'Roar': ["A lion's mouth forms at the center of the shield and shoots a Ki wave.", 'Ki', 45]
        },
        'Snake': {
            'Lash': ['Whip extends to lash its target.', 'Physical', 20],
            'Snare': ['Whip entangles its target, paralyzing its victim.', 'Ki', 12],
            'Hydra': ['Splits into hundreds of smaller whips making its attack unavoidable.', 'Ki', 50]
        }
    }
    # Retrieve current character stance
    character_stance = character['Active Stance']
    # Obtain stance attack moves as a dictionary
    attack_moves = character_attacks[character_stance]
    return attack_moves


# Display attack list depending on stance
def display_attack_options(stance, attacks_moves):
    print(f"Your stance: {stance}")
    print("Available attacks:")
    attack_names = list(attacks_moves.keys())
    for order, attack_name in enumerate(attack_names, 1):
        description = attacks_moves[attack_name][0]
        attack_type = attacks_moves[attack_name][1]
        damage = attacks_moves[attack_name][2]
        # Show damage or effect based on attack type
        effect = f"Damage: {damage}" if damage > 0 else "Special Effect"
        print(f"{order}. {attack_name} ({attack_type}) - {description} - {effect}")


# Obtain user input for attack move. Max value = 3 (number of attack moves). 0 to go back to display_battle_menu
def get_attack_choice(attacks_dict: dict):
    # Keep asking for valid number
    while True:
        user_input = input("Choose your attack. Enter a number between 1 and 3, or 0 to go back: ")
        if user_input == '0':
            return None
        try:
            attack_choice = int(user_input) - 1
        except ValueError:
            print("Please enter a valid number.")
        else:
            if 0 <= attack_choice <= 2:
                attack_moves = tuple(attacks_dict.items())
                return attack_moves[attack_choice]
            else:
                print("Invalid choice. Please enter a number between 0 and 3")


# Apply physical attack to monster
def apply_physical_attack(attack_name: str, description: str, damage: int,
                          damage_modifier: float, monster: dict) -> str:
    """
    Apply physical attack damage to monster and return result message.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param damage: a positive integer > 0
    :param damage_modifier: a float > 0
    :param monster: a dictionary containing monster data with 'Current Health' key with an integer value > 0
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: damage must be a positive integer > 0
    :precondition: damage_modifier must be a float > 0
    :precondition: monster must be a dictionary containing monster data
                   with 'Current Health' key with an integer value > 0
    :postcondition: multiply damage by damage_modifier and round to integer
    :postcondition: reduce monster 'Current Health' value by damage amount
    :postcondition: generate a string message describing the attack results
    :return: a string message describing the attack results
    """
    damage = int(damage * damage_modifier)
    monster['Current Health'] -= damage
    return f"You used {attack_name}! {description} You dealt {damage} damage!"


# Apply damaging Ki attack to monster
def apply_ki_damage_attack(attack_name: str, description: str, damage: int,
                           damage_modifier: float, monster: dict) -> str:
    """
    Apply Ki attack damage to monster and return result message.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param damage: a positive integer > 0
    :param damage_modifier: a float > 0
    :param monster: a dictionary containing monster data with 'Current Health' key with an integer value > 0
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: damage must be a positive integer > 0
    :precondition: damage_modifier must be a float > 0
    :precondition: monster must be a dictionary containing monster data
                   with 'Current Health' key with an integer value > 0
    :postcondition: multiply damage by damage_modifier and round to integer
    :postcondition: reduce monster 'Current Health' value by damage amount
    :postcondition: generate a string message describing the attack results
    :return: a string message describing the attack results
    """
    damage = int(damage * damage_modifier)
    # Apply damage to monster
    monster['Current Health'] -= damage
    return f"You used {attack_name}! {description} You dealt {damage} Ki damage!"


# Apply Berserk buff to character
def apply_berserk_buff(attack_name: str, description: str, character: dict) -> str:
    character['Damage Modifier'] += 0.5
    # Add duration tracking for Berserk. Lasts for 3 turns
    character['Status']['Berserk'] += 3
    return f"You used {attack_name}! {description} Your damage is increased by 50% for 3 turns!"


# Apply Shell buff to character
def apply_shell_buff(attack_name: str, description: str, character: dict) -> str:
    # Add Shell status with duration. Lasts for 2 turns
    character['Status']['Shell'] += 2
    character['Active Defense Modifier'] = 0.0
    return f"You used {attack_name}! {description} You take no damage for the next two turns!"


# Apply snare effect to monster
def apply_snare_effect(monster: dict) -> str:
    # Monster loses a turn
    monster['Status']['Snared'] += 1
    return "The monster is snared and will miss its next turn!"


# Process special Ki attack based on name
def process_special_ki_attack(attack_name: str, description: str, character: dict, monster: dict) -> str:
    if attack_name == 'Berserk':
        return apply_berserk_buff(attack_name, description, character)
    elif attack_name == 'Shell':
        return apply_shell_buff(attack_name, description, character)
    elif attack_name == 'Snare':
        return apply_snare_effect(monster)


# Apply ki attack cost
def apply_ki_cost(character: dict) -> None:
    character['Current Ki'] -= 10


# Process damaging Ki attack
def process_damaging_ki_attack(attack_name: str, description: str, damage: int,
                               damage_modifier: float, character: dict, monster: dict) -> str:
    # Apply Ki cost
    apply_ki_cost(character)
    # Apply damage and get message
    return apply_ki_damage_attack(attack_name, description, damage, damage_modifier, monster)


# Process special Ki attack with ki cost
def process_special_ki_attack_with_cost(attack_name: str, description: str,
                                        character: dict, monster: dict) -> str:
    # Apply Ki cost
    apply_ki_cost(character)
    # Apply special effect and get message
    return process_special_ki_attack(attack_name, description, character, monster)


# Print attack message if valid
def print_attack_result(attack_type: str, success: bool, message: str) -> None:
    # Print attack message if attack is valid
    if success:
        print(message)
    # Print not enough Ki message
    elif attack_type == 'Ki':
        print("You don't have enough Ki to use this attack! Choose another action.")


# Execute attack
def execute_attack(attack_type: str, attack_name: str, description: str,
                   damage: int, damage_modifier: float, character: dict, monster: dict) -> tuple:
    # Apply physical attack. Return True and result message
    if attack_type == 'Physical':
        message = apply_physical_attack(attack_name, description, damage, damage_modifier, monster)
        return True, message
    else:
        # Apply Ki attack. Return True if character has enough Ki with result message. Else return False with "".
        if character['Current Ki'] >= 10:
            if damage > 0 and attack_name != 'Snare':
                message = process_damaging_ki_attack(attack_name, description, damage,
                                                     damage_modifier, character, monster)
                return True, message
            # Snare has special effect and does damage
            elif attack_name == 'Snare':
                message = process_damaging_ki_attack(attack_name, description, damage,
                                                     damage_modifier, character, monster)
                message += "\n" + process_special_ki_attack_with_cost(attack_name, description, character, monster)
                return True, message
            else:
                message = process_special_ki_attack_with_cost(attack_name, description, character, monster)
                return True, message
        return False, ""


# Manager function to apply attack move
def apply_attack_move(attack_move: tuple, character: dict, monster: dict) -> None:
    # Unpack attack details
    attack_name, attack_details = attack_move
    description, attack_type, damage = attack_details
    # Get damage modifier from character
    damage_modifier = character['Damage Modifier']
    # Check if the attack is valid and execute it
    success, message = execute_attack(attack_type, attack_name, description,
                                      damage, damage_modifier, character, monster)
    # Print the result
    print_attack_result(attack_type, success, message)


# Update status effects for both character and monster
def update_status_effects(character, monster):
    # Update character status effects
    for effect, duration in list(character['Status'].items()):
        if duration > 0:
            character['Status'][effect] -= 1
            if character['Status'][effect] == 0:
                # Reset effect when duration expires
                if effect == 'Shell':
                    character['Active Defense Modifier'] = character.get('Defense Modifier')
                elif effect == 'Berserk':
                    character['Damage Modifier'] -= .5
    # Update monster status effects
    for effect, duration in list(monster['Status'].items()):
        if duration > 0:
            monster['Status'][effect] -= 1


# Check if monster health is <= 0
def monster_defeat(monster: dict) -> bool:
    monster_health = monster.get("Current Health")
    return monster_health <= 0


# Get rewards after defeating monster, gain 8 Crystals, and 35 experience. Gain 25 to Health if level 3.
def monster_rewards(character: dict):
    print("You have slain your foe!")
    # Award Crystals
    character['Crystals'] += 8
    print(f"You gained 8 Crystals!")
    print(f"Total Crystals: {character['Crystals']}")
    # Provide special reward for level 3 characters
    if character['Level'] == 3:
        character['Health'] += 25
        character['Current Health'] += 25
        character['Damage Modifier'] += 0.04
        print(f"Your maximum Health has increased by 25 and Damage by 4%!")
        return
    # Award experience
    character['Experience'] += 35
    print(f"You gained 35 experience!")