"""
This module contains functions for the battle mechanic.
"""
import random
from itertools import cycle
from typing import Optional
from __init__ import BATTLE_STANCES


# Scale monster damage with player level
def calculate_monster_damage_modifier(character_level: int) -> float:
    """
    Calculate a monster's damage modifier based on the character Level.

    :param character_level: an integer between [1, 3]
    :precondition: character_level must be an integer between [1, 3]
    :postcondition: if character_level == 1, damage_modifier = 1.0
    :postcondition: if character_level == 2, damage_modifier = 1.2
    :postcondition: if character_level == 3, damage_modifier = 1.5
    :return: a float value representing the monster's damage modifier

    >>> calculate_monster_damage_modifier(1)
    1.0
    >>> calculate_monster_damage_modifier(2)
    1.2
    >>> calculate_monster_damage_modifier(3)
    1.5
    """
    # Base damage modifier
    damage_modifier = 1.0
    # Level 1: No change
    if character_level == 1:
        return damage_modifier
    # Level 2: +20% damage
    elif character_level == 2:
        return damage_modifier + 0.2
    # Level 3: +50% damage
    elif character_level == 3:
        return damage_modifier + 0.5


# Scale monster Health with player level
def calculate_monster_health_modifier(character_level: int) -> float:
    """
    Calculate monster health modifier based on character Level.

    :param character_level: an integer between [1, 3]
    :precondition: character_level must be an integer between [1, 3]
    :postcondition: if character_level == 1, health_modifier = 1.0
    :postcondition: if character_level == 2, health_modifier = 1.25
    :postcondition: if character_level == 3, health_modifier = 1.5
    :return: a float value representing the monster's health modifier

    >>> calculate_monster_health_modifier(1)
    1.0
    >>> calculate_monster_health_modifier(2)
    1.25
    >>> calculate_monster_health_modifier(3)
    1.5
    """
    # Base health modifier
    health_modifier = 1.0
    # Level 1: No change
    if character_level == 1:
        return health_modifier
    # Level 2: +25% health
    elif character_level == 2:
        return health_modifier + 0.25
    # Level 3: +50% health
    elif character_level == 3:
        return health_modifier + 0.5


# Apply monster scaling based on character level
def apply_difficulty_scaling(monster: dict, character_level: int) -> dict:
    """
    Apply difficulty scaling to a monster based on character level.
    """
    # Calculate new modifiers
    new_damage_modifier = calculate_monster_damage_modifier(character_level)
    new_health_modifier = calculate_monster_health_modifier(character_level)
    # Store original health before modifications
    original_health = monster['Health']
    # Update monster modifiers
    monster['Damage Modifier'] = new_damage_modifier
    monster['Health Modifier'] = new_health_modifier
    # Calculate health increase
    health_multiplier = new_health_modifier
    new_health = int(original_health * health_multiplier)
    # Update monster health values
    monster['Health'] = new_health
    monster['Current Health'] = new_health
    return monster


# Create monster with Health and stats as a dictionary
def create_monster(monster: str, character_level: int = 1) -> dict:
    """
    Generate a monster with stats depending on its type and character level.

    :param monster: is a string
    :param character_level: an integer representing character level (default=1) between [1, 3]
    :precondition: monster must be ('Wendigo', 'Djinn', 'Skinwalker', 'Ghoul', 'Shapeshifter', 'Werewolf', 'Vampire')
    :precondition: character_level must be an integer between [1, 3]
    :postcondition: generate a monster represented as a dictionary containing its name and stats
    :postcondition: apply difficulty scaling based on character level
    :return: a monster represented as a dictionary containing its name and stats

    >>> actual = create_monster('Ghoul')
    >>> expected = {'Name': 'Ghoul', 'Health': 100, 'Current Health': 100, 'Status': {'Buff': 0, 'Snared': 0},
    ... 'Damage Modifier': 1.0, 'Health Modifier': 1.0}
    >>> actual == expected
    True
    >>> actual = create_monster('Vampire', 2)
    >>> expected = {'Name': 'Vampire', 'Health': 125, 'Current Health': 125, 'Status': {'Buff': 0, 'Snared': 0},
    ... 'Damage Modifier': 1.2, 'Health Modifier': 1.25}
    >>> actual == expected
    True
    >>> actual = create_monster('Vampire', 3)
    >>> expected = {'Name': 'Vampire', 'Health': 150, 'Current Health': 150, 'Status': {'Buff': 0, 'Snared': 0},
    ... 'Damage Modifier': 1.5, 'Health Modifier': 1.5}
    >>> actual == expected
    True
    """
    # Base health for different monster types
    monster_health = {
        'Wendigo': 100,
        'Djinn': 90,
        'Skinwalker': 100,
        'Ghoul': 100,
        'Shapeshifter': 90,
        'Werewolf': 80,
        'Vampire': 100
    }
    # Create monster dictionary with health and status
    monster_dict = {
        'Name': monster,
        'Health': monster_health[monster], 'Current Health': monster_health[monster],
        'Status': {'Buff': 0, 'Snared': 0},
        'Damage Modifier': 1.0, 'Health Modifier': 1.0
    }
    # Apply difficulty scaling if character level > 1
    if character_level > 1:
        monster_dict = apply_difficulty_scaling(monster_dict, character_level)
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
            'Crippling Bite': ['Bites the target causing bleed.', 'Bleed', 16],
            'Lunar Frenzy': ['Enters a berserk state, increasing Health and Damage.', 'Buff', 0]
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
def process_attack(character: dict, monster_modifier: float, defense_modifier: float,
                   damage: int, attack_name: str, description: str) -> str:
    """
    Apply standard monster attack to character Current Health and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0
    :param monster_modifier: a positive float number > 0
    :param defense_modifier: a positive float number >= 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: character must be a dictionary containing character data with
                   a 'Current Health' key with an integer value > 0
    :precondition: monster_modifier must be a positive float number > 0
    :precondition: defense_modifier must be a positive float number >= 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: calculate (damage * monster_modifier * defense_modifier)
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: generate a string message containing attack_name, description, and damage
    :return: a string message containing attack_name, description, and damage

    >>> test_character = {'Current Health': 100}
    >>> test_description = 'A vicious claw attack dealing physical damage.'
    >>> process_attack(test_character, 1.5, 1.0, 10, 'Swipe', test_description)
    'Monster used Swipe! A vicious claw attack dealing physical damage. You took 15 damage!'
    >>> print(test_character)
    {'Current Health': 85}
    >>> test_character = {'Current Health': 9}
    >>> test_description = 'Teleports behind the enemy for a surprise attack.'
    >>> process_attack(test_character, 1.0, 1.0, 15, 'Shadow Step', test_description)
    'Monster used Shadow Step! Teleports behind the enemy for a surprise attack. You took 15 damage!'
    >>> print(test_character)
    {'Current Health': -6}
    >>> test_character = {'Current Health': 100}
    >>> test_description = 'A vicious claw attack dealing physical damage.'
    >>> process_attack(test_character, 1.5, 0.0, 10, 'Swipe', test_description)
    'Monster used Swipe! A vicious claw attack dealing physical damage. You took 0 damage!'
    >>> print(test_character)
    {'Current Health': 100}
    """
    damage = int(damage * monster_modifier * defense_modifier)
    character['Current Health'] -= damage
    return f"Monster used {attack_name}! {description} You took {damage} damage!"


# Process healing attacks
def process_heal_attack(character: dict, monster: dict, damage: int, defense_modifier: float,
                        attack_name: str, description: str) -> str:
    """
    Apply heal monster attack to monster Current Health, character Current Health, and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0
    :param monster: a dictionary containing monster data with a 'Current Health' key with an integer value > 0
                    and 'Damage Modifier' key with a float > 0
    :param damage: a positive integer representing monster damage
    :param defense_modifier: a positive float number >= 0
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: monster must be a dictionary containing character data with
                   a 'Current Health' key with an integer value > 0 and 'Damage Modifier' key with a float > 0
    :precondition: character must be a dictionary containing character data with
                   a 'Current Health' key with an integer value > 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: defense_modifier must be a positive float number >= 0
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: calculate (damage * monster['Damage Modifier'] * defense_modifier)
    :postcondition: increase monster Current Health by heal amount
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: generate a string message containing attack_name, description, damage, and heal_amount
    :return: a string message containing attack_name, description, damage, and heal_amount

    >>> test_character = {'Current Health': 100}
    >>> test_monster = {'Current Health': 100, 'Damage Modifier': 1.0}
    >>> test_description = 'Drinks the target’s blood to restore health.'
    >>> expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
    ...             'You took 6 damage! Monster healed for 3 health!')
    >>> expected == process_heal_attack(test_character, test_monster, 6, 1.0, 'Blood Drain', test_description)
    True
    >>> print(test_character, test_monster)
    {'Current Health': 94} {'Current Health': 103, 'Damage Modifier': 1.0}
    >>> test_character = {'Current Health': 1}
    >>> test_monster = {'Current Health': 1, 'Damage Modifier': 2.0}
    >>> test_description = 'Drinks the target’s blood to restore health.'
    >>> expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
    ...             'You took 12 damage! Monster healed for 6 health!')
    >>> expected == process_heal_attack(test_character, test_monster, 6, 1.0, 'Blood Drain', test_description)
    True
    >>> print(test_character, test_monster)
    {'Current Health': -11} {'Current Health': 7, 'Damage Modifier': 2.0}
    >>> test_character = {'Current Health': 1}
    >>> test_monster = {'Current Health': 1, 'Damage Modifier': 2.0}
    >>> test_description = 'Drinks the target’s blood to restore health.'
    >>> expected = ('Monster used Blood Drain! Drinks the target’s blood to restore health. '
    ...             'You took 0 damage! Monster healed for 0 health!')
    >>> expected == process_heal_attack(test_character, test_monster, 6, 0.0, 'Blood Drain', test_description)
    True
    >>> print(test_character, test_monster)
    {'Current Health': 1} {'Current Health': 1, 'Damage Modifier': 2.0}
    """
    damage = int(damage * monster['Damage Modifier'] * defense_modifier)
    heal_amount = damage // 2
    monster['Current Health'] += heal_amount
    character['Current Health'] -= damage
    message = (f"Monster used {attack_name}! {description} You took {damage} damage! "
               f"Monster healed for {heal_amount} health!")
    return message


# Process poison attacks and add poison status
def process_poison_attack(character: dict, monster_modifier: float, defense_modifier: float, damage: int,
                          attack_name: str, description: str) -> str:
    """
    Apply poison monster attack to character Current Health and Status, and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0 and
                      'Status' key containing a dictionary of Poison:value as (str:int >= 0)
    :param monster_modifier: a positive float number > 0
    :param defense_modifier: a positive float number >= 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: character must be a dictionary containing character data with a 'Current Health' key with
                   an integer value > 0 and 'Status' key containing a dictionary of Poison:value as (str:int >= 0)
    :precondition: monster_modifier must be a positive float number > 0
    :precondition: defense_modifier must be a positive float number >= 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: calculate (damage * monster_modifier * defense_modifier)
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: increase character Poison Status by 4
    :postcondition: generate a string message containing attack_name, description, and damage
    :return: a string message containing attack_name, description, and damage

    >>> test_character = {'Current Health': 100, 'Status': {'Poison': 0}}
    >>> test_description = 'A venomous bite that inflicts poison damage over time.'
    >>> expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
    ...             'You took 15 damage and are poisoned!')
    >>> expected == process_poison_attack(test_character, 1.5, 1.0, 10, 'Poison Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 85, 'Status': {'Poison': 4}}
    >>> test_character = {'Current Health': 10, 'Status': {'Poison': 4}}
    >>> test_description = 'A venomous bite that inflicts poison damage over time.'
    >>> expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
    ...             'You took 10 damage and are poisoned!')
    >>> expected == process_poison_attack(test_character, 1.0, 1.0, 10, 'Poison Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 0, 'Status': {'Poison': 8}}
    >>> test_character = {'Current Health': 10, 'Status': {'Poison': 4}}
    >>> test_description = 'A venomous bite that inflicts poison damage over time.'
    >>> expected = ('Monster used Poison Bite! A venomous bite that inflicts poison damage over time. '
    ...             'You took 0 damage and are poisoned!')
    >>> expected == process_poison_attack(test_character, 1.0, 0.0, 10, 'Poison Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 10, 'Status': {'Poison': 8}}
    """
    damage = int(damage * monster_modifier * defense_modifier)
    character['Current Health'] -= damage
    # Lasts for 4 turns
    character['Status']['Poison'] += 4
    return f"Monster used {attack_name}! {description} You took {damage} damage and are poisoned!"


# Process bleed attacks and add bleed status
def process_bleed_attack(character: dict, monster_modifier: float, defense_modifier: float, damage: int,
                         attack_name: str, description: str) -> str:
    """
    Apply bleed monster attack to character Current Health and Status, and return damage description.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value > 0 and
                      'Status' key containing a dictionary of Bleed:value as (str:int >= 0)
    :param monster_modifier: a positive float number > 0
    :param defense_modifier: a positive float number >= 0
    :param damage: a positive integer representing monster damage
    :param attack_name: a string representing monster attack name
    :param description: a string representing monster attack description
    :precondition: character must be a dictionary containing character data with a 'Current Health' key with
                   an integer value > 0 and 'Status' key containing a dictionary of Bleed:value as (str:int >= 0)
    :precondition: monster_modifier must be a positive float number > 0
    :precondition: defense_modifier must be a positive float number >= 0
    :precondition: damage must be positive integer representing monster damage
    :precondition: attack_name must be a non-empty string representing monster attack name
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: calculate (damage * monster_modifier * defense_modifier)
    :postcondition: reduce character Current Health by monster damage amount
    :postcondition: increase character Bleed Status by 2
    :postcondition: generate a string message containing attack_name, description, and damage
    :return: a string message containing attack_name, description, and damage

    >>> test_character = {'Current Health': 100, 'Status': {'Bleed': 0}}
    >>> test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
    >>> expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
    ...             'You took 15 damage and are bleeding!')
    >>> expected == process_bleed_attack(test_character, 1.5, 1.0, 10, 'Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 85, 'Status': {'Bleed': 2}}
    >>> test_character = {'Current Health': 10, 'Status': {'Bleed': 2}}
    >>> test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
    >>> expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
    ...             'You took 10 damage and are bleeding!')
    >>> expected == process_bleed_attack(test_character, 1.0, 1.0, 10, 'Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 0, 'Status': {'Bleed': 4}}
    >>> test_character = {'Current Health': 10, 'Status': {'Bleed': 2}}
    >>> test_description = 'A quick bite that deals damage and has a chance to inflict bleed.'
    >>> expected = ('Monster used Bite! A quick bite that deals damage and has a chance to inflict bleed. '
    ...             'You took 0 damage and are bleeding!')
    >>> expected == process_bleed_attack(test_character, 1.0, 0.0, 10, 'Bite', test_description)
    True
    >>> print(test_character)
    {'Current Health': 10, 'Status': {'Bleed': 4}}
    """
    damage = int(damage * monster_modifier * defense_modifier)
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
    :precondition: attack_name must be a non-empty string 'Lunar Frenzy'
    :precondition: description must be a non-empty string representing monster attack description
    :postcondition: increase 'Damage Modifier' value by 0.2
    :postcondition: increase 'Health Modifier' value by 0.5
    :postcondition: increase 'Current Health' value by multiple of 'Health Modifier'
    :postcondition: generate a string message containing attack_name and description
    :return: a string message containing attack_name and description

    >>> test_monster = {'Damage Modifier': 1.0, 'Health Modifier': 1.0, 'Current Health': 100}
    >>> test_description = 'Enters a berserk state, increasing Health and Damage.'
    >>> expected_message = ("Monster used Lunar Frenzy! Enters a berserk state, increasing Health and Damage. "
    ...                     "Monster's damage and Health are increased!")
    >>> expected_message == process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
    True
    >>> print(test_monster)
    {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 150}
    >>> test_monster = {'Damage Modifier': 1.2, 'Health Modifier': 1.5, 'Current Health': 50}
    >>> test_description = 'Enters a berserk state, increasing Health and Damage.'
    >>> expected_message = ("Monster used Lunar Frenzy! Enters a berserk state, increasing Health and Damage. "
    ...                     "Monster's damage and Health are increased!")
    >>> expected_message == process_buff_attack(test_monster, 'Lunar Frenzy', test_description)
    True
    >>> print(test_monster)
    {'Damage Modifier': 1.4, 'Health Modifier': 2.0, 'Current Health': 100}
    """
    monster['Damage Modifier'] += 0.2
    monster['Health Modifier'] += 0.5
    monster['Current Health'] = int(monster['Current Health'] * monster['Health Modifier'])
    return f"Monster used {attack_name}! {description} Monster's damage and Health are increased!"


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
    :precondition: character['Stance'] must be a non-empty list of strings
                   representing stance names ['Bear', 'Turtle', 'Snake']
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
def display_attack_options(stance: str, attacks_moves: dict) -> None:
    """
    Print all available attack moves for the character's current stance.

    :param stance: a string representing the character's current stance ('Bear', 'Turtle', 'Snake')
    :param attacks_moves: a dictionary where keys are attack names and values are lists containing
                         [description, attack_type, damage] as (str, str, int >= 0)
    :precondition: stance must be a non-empty string representing one of the character's available stances
    :precondition: attacks_moves must be a non-empty dictionary containing attack moves for the stance
    :precondition: each attack in attacks_moves must have a list with exactly 3 elements:
                   [description, attack_type, damage] as (str, str, int >= 0)
    :postcondition: print the current stance name
    :postcondition: print available attacks:
    :postcondition: print each attack with its number, name, type, description, and damage or effect
    :postcondition: for attacks with damage > 0, show the damage value
    :postcondition: for attacks with damage == 0, show "Special Effect" instead of damage

    >>> test_stance = 'Bear'
    >>> test_attack_moves = {
    ... 'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 20],
    ... 'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 35],
    ... 'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]}
    >>> display_attack_options(test_stance, test_attack_moves)
    Your stance: Bear
    Available attacks:
    1. Heavy Strike (Physical) - A powerful blow with massive physical damage. - Damage: 20
    2. Sunder (Ki) - Slams the ground in front of you creating a wave of Ki. - Damage: 35
    3. Berserk (Ki) - Enters a state of rage, increasing both physical damage and Ki attacks. - Special Effect
    >>> test_stance = 'Turtle'
    >>> test_attack_moves = {
    ... 'Bash': ['Coats the outer shield with spikes, then bashes into the enemy.', 'Physical', 15],
    ... 'Shell': ['Take no damage next two turns.', 'Ki', 0],
    ... 'Roar': ["A lion's mouth forms at the center of the shield and shoots a Ki wave.", 'Ki', 45]}
    >>> display_attack_options(test_stance, test_attack_moves)
    Your stance: Turtle
    Available attacks:
    1. Bash (Physical) - Coats the outer shield with spikes, then bashes into the enemy. - Damage: 15
    2. Shell (Ki) - Take no damage next two turns. - Special Effect
    3. Roar (Ki) - A lion's mouth forms at the center of the shield and shoots a Ki wave. - Damage: 45
    >>> test_stance = 'Snake'
    >>> test_attack_moves = {
    ... 'Lash': ['Whip extends to lash its target.', 'Physical', 20],
    ... 'Snare': ['Whip entangles its target, paralyzing its victim.', 'Ki', 12],
    ... 'Hydra': ['Splits into hundreds of smaller whips making its attack unavoidable.', 'Ki', 50]}
    >>> display_attack_options(test_stance, test_attack_moves)
    Your stance: Snake
    Available attacks:
    1. Lash (Physical) - Whip extends to lash its target. - Damage: 20
    2. Snare (Ki) - Whip entangles its target, paralyzing its victim. - Damage: 12
    3. Hydra (Ki) - Splits into hundreds of smaller whips making its attack unavoidable. - Damage: 50
    """
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
def get_attack_choice(attacks_dict: dict) -> Optional[tuple]:
    """
    Obtain the user's attack choice from the available attack moves.

    Prompt the user to select an attack by number from the displayed attack options,
    or allow user to return to the battle menu. Validate the input to ensure it corresponds to an available attack.

    :param attacks_dict: a dictionary where keys are attack names and values are lists containing
                         [description, attack_type, damage] as (str, str, int >= 0)
    :precondition: attacks_dict must be a non-empty dictionary containing exactly three attack moves
    :postcondition: validate user input to ensure it corresponds to an available attack or back option
    :postcondition: convert user's numeric choice to the corresponding attack move
    :postcondition: if a valid attack is selected, obtain a tuple containing
                    (attack_name, [description, attack_type, damage])
    :postcondition: if user input == '0', obtain None value
    :return: a tuple containing (attack_name, [description, attack_type, damage]) if a valid attack is selected,
             or None if the user chooses to go back to the battle menu
    """
    # Keep asking for valid number
    while True:
        user_input = input("Choose your attack. Enter a number between 1 and 3, or 0 to go back: ").strip()
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

    >>> test_monster = {'Current Health': 100}
    >>> apply_physical_attack('Heavy Strike', 'A powerful blow with massive physical damage.', 20, 1.0, test_monster)
    'You used Heavy Strike! A powerful blow with massive physical damage. You dealt 20 damage!'
    >>> test_monster
    {'Current Health': 80}
    >>> test_monster = {'Current Health': 100}
    >>> apply_physical_attack('Lash', 'Whip extends to lash its target.', 20, 1.5, test_monster)
    'You used Lash! Whip extends to lash its target. You dealt 30 damage!'
    >>> test_monster
    {'Current Health': 70}
    >>> test_monster = {'Current Health': 10}
    >>> apply_physical_attack('Heavy Strike', 'A powerful blow with massive physical damage.', 20, 1.0, test_monster)
    'You used Heavy Strike! A powerful blow with massive physical damage. You dealt 20 damage!'
    >>> test_monster
    {'Current Health': -10}
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

    >>> test_monster = {'Current Health': 100}
    >>> attack_description = 'Slams the ground in front of you creating a wave of Ki.'
    >>> apply_ki_damage_attack('Sunder', attack_description, 35, 1.0, test_monster)
    'You used Sunder! Slams the ground in front of you creating a wave of Ki. You dealt 35 Ki damage!'
    >>> test_monster
    {'Current Health': 65}
    >>> test_monster = {'Current Health': 10}
    >>> attack_description = "A lion's mouth forms at the center of the shield and shoots a Ki wave."
    >>> apply_ki_damage_attack('Roar', attack_description, 45, 1.0, test_monster)
    "You used Roar! A lion's mouth forms at the center of the shield and shoots a Ki wave. You dealt 45 Ki damage!"
    >>> test_monster
    {'Current Health': -35}
    >>> test_monster = {'Current Health': 100}
    >>> attack_description = 'Splits into hundreds of smaller whips making its attack unavoidable.'
    >>> apply_ki_damage_attack('Hydra', attack_description, 50, 1.5, test_monster)
    'You used Hydra! Splits into hundreds of smaller whips making its attack unavoidable. You dealt 75 Ki damage!'
    >>> test_monster
    {'Current Health': 25}
    """
    damage = int(damage * damage_modifier)
    # Apply damage to monster
    monster['Current Health'] -= damage
    return f"You used {attack_name}! {description} You dealt {damage} Ki damage!"


# Apply Berserk buff to character
def apply_berserk_buff(attack_name: str, description: str, character: dict) -> str:
    """
    Apply Berserk buff to character and return result message.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param character: a dictionary containing character data with: 'Damage Modifier' key with float value > 0,
                      'Status' key containing 'Berserk':value as (str:int >= 0)
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: character must be a dictionary containing character data with 'Damage Modifier' and 'Status' keys
    :precondition: character['Damage Modifier'] value must be a float > 0
    :precondition: character['Status'] value must contain 'Berserk' key
    :precondition: character['Status']['Berserk'] value must be a positive integer >= 0
    :postcondition: increase 'Damage Modifier' value by 0.5
    :postcondition: increase 'Berserk' value by 3
    :postcondition: generate a string message describing the buff results
    :return: a string message describing the buff results

    >>> test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
    >>> test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
    >>> actual_message = apply_berserk_buff('Berserk', test_description, test_character)
    >>> expected_message = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks.'
    ... ' Your damage is increased by 50% for 3 turns!')
    >>> expected_character = {'Damage Modifier': 1.5, 'Status': {'Berserk': 6}}
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    >>> test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 2}}
    >>> test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
    >>> actual_message = apply_berserk_buff('Berserk', test_description, test_character)
    >>> expected_message = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks.'
    ... ' Your damage is increased by 50% for 3 turns!')
    >>> expected_character = {'Damage Modifier': 1.5, 'Status': {'Berserk': 8}}
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    >>> test_character = {'Damage Modifier': 1.5, 'Status': {'Berserk': 6}}
    >>> test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
    >>> actual_message = apply_berserk_buff('Berserk', test_description, test_character)
    >>> expected_message = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks.'
    ... ' Your damage is increased by 50% for 3 turns!')
    >>> expected_character = {'Damage Modifier': 2.0, 'Status': {'Berserk': 12}}
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    """
    character['Damage Modifier'] += 0.5
    # Add duration tracking for Berserk. Lasts for 3 turns
    character['Status']['Berserk'] += 6
    return f"You used {attack_name}! {description} Your damage is increased by 50% for 3 turns!"


# Apply Shell buff to character
def apply_shell_buff(attack_name: str, description: str, character: dict) -> str:
    """
    Apply Shell buff to character and return result message.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param character: a dictionary containing character data with:
                      'Status' key containing dict of different status effects
                      'Active Defense Modifier' key with float value >= 0
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: character must be a dictionary containing character data
                   with 'Active Defense Modifier' and 'Status' keys
    :precondition: character['Active Defense Modifier'] value must be a float >= 0
    :precondition: character['Status'] value must contain 'Shell' key
    :precondition: character['Status']['Shell'] value must be a positive integer >= 0
    :postcondition: set 'Active Defense Modifier' value to 0.0
    :postcondition: increase 'Shell' value by 2
    :postcondition: generate a string message describing the buff results
    :return: a string message describing the buff results

    >>> test_description = 'Take no damage next two turns.'
    >>> test_character = {'Active Defense Modifier': 1.0, 'Status': {'Shell': 0}}
    >>> actual_message = apply_shell_buff('Shell', test_description, test_character)
    >>> expected_message = "You used Shell! Take no damage next two turns."
    >>> expected_character = {'Active Defense Modifier': 0.0, 'Status': {'Shell': 4}}
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    >>> test_description = 'Take no damage next two turns.'
    >>> test_character = {'Active Defense Modifier': 0.0, 'Status': {'Shell': 3}}
    >>> actual_message = apply_shell_buff('Shell', test_description, test_character)
    >>> expected_message = "You used Shell! Take no damage next two turns."
    >>> expected_character = {'Active Defense Modifier': 0.0, 'Status': {'Shell': 7}}
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    >>> test_description = 'Take no damage next two turns.'
    >>> test_character = {'Active Defense Modifier': 0.5, 'Status': {'Shell': 10}}
    >>> actual_message = apply_shell_buff('Shell', test_description, test_character)
    >>> expected_message = "You used Shell! Take no damage next two turns."
    >>> expected_character = {'Active Defense Modifier': 0.0, 'Status': {'Shell': 14}}
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    """
    # Add Shell status with duration. Lasts for 2 turns
    character['Status']['Shell'] += 4
    character['Active Defense Modifier'] = 0.0
    return f"You used {attack_name}! {description}"


# Apply snare effect to monster
def apply_snare_effect(monster: dict) -> str:
    """
    Apply Snared status to monster and return result message.

    :param monster: a dictionary containing monster data with
                    'Status' key containing 'Snared':value as (str, int >= 0)
    :precondition: monster must be a dictionary containing monster data with
                   'Status' key containing 'Snared':value as (str, int >= 0)
    :precondition: monster must be a dictionary containing monster data
    :precondition: monster['Status'] value must contain 'Snared' key
    :precondition: monster['Status']['Snared'] value must be a positive integer >= 0
    :postcondition: increase 'Snared' value by 1
    :postcondition: generate a string message describing the attack results
    :return: a string message describing the attack results

    >>> test_monster = {'Status': {'Snared': 0}}
    >>> expected_message = "The monster is snared and will miss its next turn!"
    >>> expected_monster = {'Status': {'Snared': 2}}
    >>> actual_message = apply_snare_effect(test_monster)
    >>> (expected_message, expected_monster) == (actual_message, test_monster)
    True
    >>> test_monster = {'Status': {'Snared': 1}}
    >>> expected_message = "The monster is snared and will miss its next turn!"
    >>> expected_monster = {'Status': {'Snared': 3}}
    >>> actual_message = apply_snare_effect(test_monster)
    >>> (expected_message, expected_monster) == (actual_message, test_monster)
    True
    >>> test_monster = {'Status': {'Snared': 9}}
    >>> expected_message = "The monster is snared and will miss its next turn!"
    >>> expected_monster = {'Status': {'Snared': 11}}
    >>> actual_message = apply_snare_effect(test_monster)
    >>> (expected_message, expected_monster) == (actual_message, test_monster)
    True
    """
    # Monster loses a turn
    monster['Status']['Snared'] += 2
    return "The monster is snared and will miss its next turn!"


# Process special Ki attack based on name
def process_special_ki_attack(attack_name: str, description: str, character: dict, monster: dict) -> str:
    """
    Process special Ki attack based on attack name.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param character: a dictionary containing character data with
                      'Status' key containing 'Berserk' and 'Shell' as keys with integer >= 0 as values
    :param monster: a dictionary containing monster data with
                    'Status' key containing 'Snared':value as (str, int >= 0)
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: character must be a dictionary containing character data
    :precondition: character['Status'] value must contain 'Shell' and 'Berserk' keys
    :precondition: character['Status']['Shell'] value must be integer >= 0
    :precondition: character['Status']['Berserk'] value must be integer >= 0
    :precondition: monster must be a dictionary containing monster data
    :precondition: monster['Status'] value must contain 'Snared' key
    :precondition: monster['Status']['Snared'] value must be integer >= 0
    :postcondition: increase value of the attack_name 'Status' of the character
    :postcondition: if attack_name == 'Snare', increase value of monster['Status']['Snared'] by 1
    :postcondition: obtain the message describing the attack results of the attack_name
    :return: a string message describing the attack results

    >>> test_character = {'Damage Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> test_description = 'Enters a state of rage, increasing both physical damage and Ki attacks.'
    >>> expected_message = ('You used Berserk! Enters a state of rage, increasing both physical damage and Ki attacks. '
    ...                     'Your damage is increased by 50% for 3 turns!')
    >>> expected_character = {'Damage Modifier': 1.5, 'Status': {'Berserk': 6, 'Shell': 0}}
    >>> actual_message = process_special_ki_attack('Berserk', test_description, test_character, test_monster)
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    >>> test_character = {'Active Defense Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> test_description = 'Take no damage next two turns.'
    >>> expected_message = 'You used Shell! Take no damage next two turns.'
    >>> expected_character = {'Active Defense Modifier': 0.0, 'Status': {'Berserk': 0, 'Shell': 4}}
    >>> actual_message = process_special_ki_attack('Shell', test_description, test_character, test_monster)
    >>> (expected_message, expected_character) == (actual_message, test_character)
    True
    >>> test_character = {'Status': {'Berserk': 0, 'Shell': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> expected_message = 'The monster is snared and will miss its next turn!'
    >>> expected_monster = {'Status': {'Snared': 2}}
    >>> actual_message = process_special_ki_attack('Snare', test_description, test_character, test_monster)
    >>> (expected_message, expected_monster) == (actual_message, test_monster)
    True
    """
    if attack_name == 'Berserk':
        return apply_berserk_buff(attack_name, description, character)
    elif attack_name == 'Shell':
        return apply_shell_buff(attack_name, description, character)
    elif attack_name == 'Snare':
        return apply_snare_effect(monster)


# Apply ki attack cost
def apply_ki_cost(character: dict) -> None:
    """
    Deduct the Ki cost from the character.

    :param character: a dictionary containing character data with 'Current Ki':value as (str:int >= 10)
    :precondition: character must be a dictionary containing character data with 'Current Ki':value as (str:int >= 10)
    :postcondition: reduce 'Current Ki' value by 10

    >>> test_character = {'Current Ki': 50}
    >>> expected = {'Current Ki': 40}
    >>> apply_ki_cost(test_character)
    >>> expected == test_character
    True
    >>> test_character = {'Current Ki': 10}
    >>> expected = {'Current Ki': 0}
    >>> apply_ki_cost(test_character)
    >>> expected == test_character
    True
    """
    character['Current Ki'] -= 10


# Process damaging Ki attack
def process_damaging_ki_attack(attack_name: str, description: str, damage: int,
                               damage_modifier: float, character: dict, monster: dict) -> str:
    """
    Process a Ki attack that deals damage.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param damage: a positive integer > 0
    :param damage_modifier: a float > 0
    :param character: a dictionary containing character data
    :param monster: a dictionary containing monster data
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: damage must be a positive integer > 0
    :precondition: damage_modifier must be a float > 0
    :precondition: character must be a dictionary containing character data
    :precondition: monster must be a dictionary containing monster data
    :postcondition: reduce character Current Ki by 10
    :postcondition: reduce monster Current Health by damage * damage_modifier
    :postcondition: generate a message string describing the attack results
    :return: a string message describing the attack results

    >>> test_character = {'Current Ki': 50}
    >>> test_monster = {'Current Health': 100}
    >>> process_damaging_ki_attack('Sunder', 'Slams the ground in front of you creating a wave of Ki.', 35, 1.0,
    ...                            test_character, test_monster)
    'You used Sunder! Slams the ground in front of you creating a wave of Ki. You dealt 35 Ki damage!'
    >>> test_character['Current Ki']
    40
    >>> test_monster['Current Health']
    65
    >>> test_character = {'Current Ki': 20}
    >>> test_monster = {'Current Health': 50}
    >>> process_damaging_ki_attack('Roar', "A lion's mouth forms at the center of the shield and shoots a Ki wave.", 45,
    ...                            1.5, test_character, test_monster)
    "You used Roar! A lion's mouth forms at the center of the shield and shoots a Ki wave. You dealt 67 Ki damage!"
    >>> test_character['Current Ki']
    10
    >>> test_monster['Current Health']
    -17
    >>> test_character = {'Current Ki': 10}
    >>> test_monster = {'Current Health': 100}
    >>> process_damaging_ki_attack('Snare', 'Whip entangles its target, paralyzing its victim.', 12, 1.0,
    ...                            test_character, test_monster)
    'You used Snare! Whip entangles its target, paralyzing its victim. You dealt 12 Ki damage!'
    >>> test_character['Current Ki']
    0
    >>> test_monster['Current Health']
    88
    """
    # Apply Ki cost
    apply_ki_cost(character)
    # Apply damage and get message
    return apply_ki_damage_attack(attack_name, description, damage, damage_modifier, monster)


# Process special Ki attack with ki cost
def process_special_ki_attack_with_cost(attack_name: str, description: str,
                                        character: dict, monster: dict) -> str:
    """
    Process a special Ki attack and apply its cost.

    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param character: a dictionary containing character data
    :param monster: a dictionary containing monster data
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: character must be a dictionary containing character data
    :precondition: monster must be a dictionary containing monster data
    :postcondition: reduce character Current Ki by 10
    :postcondition: if attack_name == 'Shell' or 'Berserk' increase value of the
                    attack_name 'Status' of the character by 2 or 3
    :postcondition: if attack_name == 'Snare', increase value of monster['Status']['Snared'] by 1
    :postcondition: obtain the message describing the attack results of the attack_name
    :return: a string message describing the attack results

    >>> test_character = {'Current Ki': 50, 'Damage Modifier': 1.0, 'Status': {'Berserk': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> process_special_ki_attack_with_cost('Berserk', 'Battle description.', test_character, test_monster)
    'You used Berserk! Battle description. Your damage is increased by 50% for 3 turns!'
    >>> test_character['Current Ki']
    40
    >>> test_character['Damage Modifier']
    1.5
    >>> test_character = {'Current Ki': 30, 'Active Defense Modifier': 1.0, 'Status': {'Shell': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> process_special_ki_attack_with_cost('Shell', 'Battle description.', test_character, test_monster)
    'You used Shell! Battle description.'
    >>> test_character['Current Ki']
    20
    >>> test_character['Status']['Shell'] > 0
    True
    >>> test_character = {'Current Ki': 15, 'Status': {'Berserk': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> process_special_ki_attack_with_cost('Snare', 'Not used.', test_character, test_monster)
    'The monster is snared and will miss its next turn!'
    >>> test_character['Current Ki']
    5
    >>> test_monster['Status']['Snared']
    2
    """
    # Apply Ki cost
    apply_ki_cost(character)
    # Apply special effect and get message
    return process_special_ki_attack(attack_name, description, character, monster)


# Print attack message if valid
def print_attack_result(attack_type: str, success: bool, message: str) -> None:
    """
    Print the result of an attack attempt.

    :param attack_type: a string representing the type of attack ('Physical' or 'Ki')
    :param success: a boolean indicating whether the attack was successful
    :param message: a string describing the attack result
    :precondition: attack_type must be a string ('Physical' or 'Ki')
    :precondition: success must be a boolean indicating if the attack succeeded
    :precondition: message must be a string containing attack result description
    :postcondition: if success is True, print the message
    :postcondition: if success is False and attack_type is 'Ki', print not enough Ki message
    :postcondition: if success is False and attack_type is not 'Ki', do nothing

    >>> print_attack_result('Physical', True, 'You hit the monster for 20 damage!')
    You hit the monster for 20 damage!
    >>> print_attack_result('Ki', False, 'This message should not be printed')
    You don't have enough Ki to use this attack! Choose another action.
    >>> print_attack_result('Physical', False, 'This message should not be printed')
    """
    # Print attack message if attack is valid
    if success:
        print(message)
    # Print not enough Ki message
    elif attack_type == 'Ki':
        print("You don't have enough Ki to use this attack! Choose another action.")


# Execute attack
def execute_attack(attack_type: str, attack_name: str, description: str,
                   damage: int, damage_modifier: float, character: dict, monster: dict) -> tuple:
    """
    Execute an attack against a monster based on the attack type and return the result.

    For Physical attacks, it applies the damage to the monster.
    For Ki attacks, it first checks if the character has enough Ki (10),
    then processes the attack based on whether it deals damage and/or has special effects.

    :param attack_type: a string indicating the type of attack ('Physical' or 'Ki')
    :param attack_name: a string representing the name of the attack
    :param description: a string describing the attack
    :param damage: a positive integer representing the base damage of the attack (0 for non-damaging abilities)
    :param damage_modifier: a float > 0
    :param character: a dictionary containing character data including 'Current Ki' with an integer value >= 0
    :param monster: a dictionary containing monster data with 'Current Health' key with an integer value > 0
    :precondition: attack_type must be either 'Physical' or 'Ki'
    :precondition: attack_name must be a string representing the name of the attack
    :precondition: description must be a string describing the attack
    :precondition: damage must be a positive integer >= 0
    :precondition: damage_modifier must be a float > 0
    :precondition: character must be a dictionary containing 'Current Ki' key with an integer value >= 0
    :precondition: monster must be a dictionary containing 'Current Health' key with an integer value > 0
    :postcondition: if attack_type is 'Physical', call apply_physical_attack
    :postcondition: if attack_type is 'Ki' and character has enough Ki, process the Ki attack based on its type
    :postcondition: if attack_type is 'Ki' and character doesn't have enough Ki, return False with an empty message
    :postcondition: for 'Snare' apply both damage and special effects
    :return: a tuple containing (success_boolean, result_message) where:
             success_boolean is True if the attack was executed successfully else False
             result_message is a string describing the attack result, or an empty string if the attack failed

    >>> test_character = {'Current Ki': 50}
    >>> test_monster = {'Current Health': 100}
    >>> test_description = 'Slams the ground in front of you creating a wave of Ki.'
    >>> success, result = execute_attack('Ki', 'Sunder', test_description, 35, 1.0, test_character, test_monster)
    >>> success
    True
    >>> 'You used Sunder!' in result and 'You dealt 35 Ki damage!' in result
    True
    >>> test_character['Current Ki']
    40
    >>> test_monster['Current Health']
    65
    >>> test_character = {'Current Ki': 50, 'Damage Modifier': 1.0, 'Status': {'Berserk': 0, 'Shell': 0}}
    >>> test_monster = {'Status': {'Snared': 0}}
    >>> test_description = 'Enters a state of rage, increasing damage.'
    >>> success, result = execute_attack('Ki', 'Berserk', test_description, 0, 1.0, test_character, test_monster)
    >>> success
    True
    >>> 'Your damage is increased' in result
    True
    >>> test_character['Current Ki']
    40
    >>> test_character = {'Current Ki': 5}
    >>> test_monster = {'Current Health': 100}
    >>> test_description = 'Slams the ground in front of you creating a wave of Ki.'
    >>> success, result = execute_attack('Ki', 'Sunder', test_description, 35, 1.0, test_character, test_monster)
    >>> success
    False
    >>> result
    ''
    >>> test_character['Current Ki']
    5
    >>> test_monster['Current Health']
    100
    """
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


# Update status effects for both character and monster
def update_status_effects(character: dict, monster: dict) -> None:
    """
    Update and decrement status effect durations for both character and monster.

    Reduce all active status effect durations by 1 and reset relevant modifiers when effects expire.

    :param character: a dictionary containing character data with 'Status' dictionary and relevant modifiers
    :param monster: a dictionary containing monster data with 'Status' dictionary
    :precondition: character must be a dictionary containing 'Status' key with
                   a dictionary of effect:duration as (str:int >=0)
    :precondition: character must have 'Defense Modifier' key with float value > 0
    :precondition: character must have 'Active Defense Modifier' key with float values >= 0
    :precondition: character must have 'Damage Modifier' key with float value > 0
    :precondition: monster must be a dictionary containing 'Status' key with
                   a dictionary of effect:duration as (str:int >=0)
    :postcondition: decrement durations of all active status effects by 1
    :postcondition: reset character 'Active Defense Modifier' when 'Shell' effect duration reaches 0
    :postcondition: reduce character 'Damage Modifier' by 0.5 when 'Berserk' effect duration reaches 0

    >>> test_character = {'Status': {'Shell': 1, 'Berserk': 0, 'Poison': 2},
    ...                   'Defense Modifier': 1.0, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.0}
    >>> test_monster = {'Status': {'Buff': 1, 'Snared': 2}}
    >>> update_status_effects(test_character, test_monster)
    >>> expected_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 1},
    ...                       'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
    >>> test_character == expected_character
    True
    >>> test_monster
    {'Status': {'Buff': 0, 'Snared': 1}}
    >>> test_character = {'Status': {'Shell': 0, 'Berserk': 1, 'Poison': 0},
    ...                   'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.5}
    >>> test_monster = {'Status': {'Buff': 0, 'Snared': 0}}
    >>> update_status_effects(test_character, test_monster)
    >>> expected_character = {'Status': {'Shell': 0, 'Berserk': 0, 'Poison': 0},
    ...                       'Defense Modifier': 1.0, 'Active Defense Modifier': 1.0, 'Damage Modifier': 1.0}
    >>> test_character == expected_character
    True
    >>> test_monster
    {'Status': {'Buff': 0, 'Snared': 0}}
    >>> test_character = {'Status': {'Shell': 2, 'Berserk': 2, 'Poison': 3},
    ...                   'Defense Modifier': 1.0, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.5}
    >>> test_monster = {'Status': {'Buff': 3, 'Snared': 3}}
    >>> update_status_effects(test_character, test_monster)
    >>> expected_character = {'Status': {'Shell': 1, 'Berserk': 1, 'Poison': 2},
    ...                       'Defense Modifier': 1.0, 'Active Defense Modifier': 0.0, 'Damage Modifier': 1.5}
    >>> test_character == expected_character
    True
    >>> test_monster
    {'Status': {'Buff': 2, 'Snared': 2}}
    """
    # Update character status effects
    for effect, duration in list(character['Status'].items()):
        if duration > 0:
            character['Status'][effect] -= 1
            if character['Status'][effect] == 0:
                # Reset effect when duration expires
                if effect == 'Shell':
                    character['Active Defense Modifier'] = character['Defense Modifier']
                elif effect == 'Berserk':
                    character['Damage Modifier'] -= .5
    # Update monster status effects
    for effect, duration in list(monster['Status'].items()):
        if duration > 0:
            monster['Status'][effect] -= 1


# Apply damaging status effects to character
def apply_status_damage(character: dict) -> str:
    """
    Apply damage from active status effects like Poison and Bleed to the character.

    :param character: a dictionary containing character data with:
                      'Current Health':value as (str:int value > 0),
                      'Status' key with a dictionary containing 'Poison' and 'Bleed':duration as (str:int value >= 0)
    :precondition: character must be a dictionary containing character data with:
                   'Current Health':value as (str:int value > 0),
                   'Status' key with a dictionary containing 'Poison' and 'Bleed':duration as (str:int value >= 0)
    :postcondition: if Poison, reduce character Current Health by 5
    :postcondition: if Bleed, reduce character Current Health by 15
    :postcondition: generate a message describing the status effect damage
    :return: a string message describing the status effect damage applied, or empty string if no effects

    >>> test_character = {'Current Health': 100, 'Status': {'Poison': 3, 'Bleed': 0}}
    >>> apply_status_damage(test_character)
    'You take 5 damage from Poison!'
    >>> test_character
    {'Current Health': 95, 'Status': {'Poison': 3, 'Bleed': 0}}
    >>> test_character = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 2}}
    >>> apply_status_damage(test_character)
    'You take 15 damage from Bleed!'
    >>> test_character
    {'Current Health': 85, 'Status': {'Poison': 0, 'Bleed': 2}}
    >>> test_character = {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 0}}
    >>> apply_status_damage(test_character)
    ''
    >>> test_character
    {'Current Health': 100, 'Status': {'Poison': 0, 'Bleed': 0}}
    """
    # Apply poison damage (5 damage per turn)
    if character['Status']['Poison'] > 0:
        poison_damage = 5
        character['Current Health'] -= poison_damage
        return f"You take {poison_damage} damage from Poison!"
    # Apply bleed damage (15 damage per turn)
    elif character['Status']['Bleed'] > 0:
        bleed_damage = 15
        character['Current Health'] -= bleed_damage
        return f"You take {bleed_damage} damage from Bleed!"
    # No active status effects
    return ""


# Reset character Statuses to 0 after battle ends
def reset_statuses(character: dict) -> None:
    """
    Reset all character status effects to 0 after battle ends.

    :param character: a dictionary containing character data with a 'Status' key
                      that contains a dictionary of status effect name:duration as (str:int >= 0)
    :precondition: character must be a dictionary containing a 'Status' key
    :precondition: character['Status'] must be a dictionary with status effects as keys
                   and integer values >= 0
    :postcondition: set all status effect durations to 0

    >>> test_character = {'Status': {'Poison': 3, 'Bleed': 2, 'Shell': 1, 'Berserk': 0}}
    >>> reset_statuses(test_character)
    >>> test_character
    {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
    >>> test_character = {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
    >>> reset_statuses(test_character)
    >>> test_character
    {'Status': {'Poison': 0, 'Bleed': 0, 'Shell': 0, 'Berserk': 0}}
    """
    character_statuses = character['Status']
    for status in character_statuses.keys():
        character_statuses[status] = 0


# Check if monster health is <= 0
def monster_defeat(monster: dict) -> bool:
    """
    Return True if monster Current Health is <= 0 else False

    :param monster: a dictionary containing monster data with a 'Current Health' key with an integer value
    :precondition: monster must be a dictionary containing 'Current Health' key with an integer value
    :postcondition: leave monster unmodified
    :postcondition: determine if monster is defeated (Current Health <= 0)
    :return: True if monster Current Health is <= 0 else False

    >>> test_monster = {'Current Health': 0}
    >>> monster_defeat(test_monster)
    True
    >>> test_monster = {'Current Health': -5}
    >>> monster_defeat(test_monster)
    True
    >>> test_monster = {'Current Health': 10}
    >>> monster_defeat(test_monster)
    False
    """
    # Default get 0 to avoid crashes
    monster_health = monster.get("Current Health", 0)
    return monster_health <= 0


# Get rewards after defeating monster, gain 8 Crystals, and 35 experience. Gain 25 to Health if level 3.
def monster_rewards(character: dict) -> None:
    """
    Award rewards to character after defeating a monster.

    Always awards 8 Crystals. For level 3 characters, increases max Health by
    25 and Damage Modifier by 0.04. For characters below level 3, awards 35 experience.

    :param character: a dictionary containing character data with 'Crystals', 'Level', 'Experience',
                     'Health', 'Current Health', and 'Damage Modifier' keys
    :precondition: character must be a dictionary containing 'Crystals', 'Level', 'Experience',
                   'Health', 'Current Health', and 'Damage Modifier' keys
    :precondition: character['Level'] must be an integer between [1, 3]
    :precondition: character['Crystals'] must be an integer between [0, 99]
    :precondition: character['Experience'] must be an integer >= 0
    :precondition: character['Health'] and character['Current Health'] must be integers > 0
    :precondition: character['Damage Modifier'] must be a float > 0
    :postcondition: increase character['Crystals'] by 8
    :postcondition: if character['Level'] == 3, increase character['Health'] and character['Current Health'] by 25
                    and increase character['Damage Modifier'] by 0.04
    :postcondition: if character['Level'] < 3, increase character['Experience'] by 35
    :postcondition: print slain foe message and character stats increases

    >>> test_character = {'Crystals': 10, 'Level': 1, 'Experience': 0, 'Health': 200,
    ... 'Current Health': 150, 'Damage Modifier': 1.0}
    >>> expected_character = {'Crystals': 18, 'Level': 1, 'Experience': 35, 'Health': 200,
    ... 'Current Health': 150, 'Damage Modifier': 1.0}
    >>> monster_rewards(test_character)
    You have slain your foe!
    You gained 8 Crystals!
    Total Crystals: 18
    You gained 35 experience!
    >>> test_character == expected_character
    True
    >>> test_character = {'Crystals': 92, 'Level': 3, 'Experience': 50, 'Health': 300,
    ... 'Current Health': 200, 'Damage Modifier': 1.2}
    >>> expected_character = {'Crystals': 100, 'Level': 3, 'Experience': 50, 'Health': 325,
    ... 'Current Health': 225, 'Damage Modifier': 1.24}
    >>> monster_rewards(test_character)
    You have slain your foe!
    You gained 8 Crystals!
    Total Crystals: 100
    Your maximum Health has increased by 25 and Damage by 4%!
    >>> test_character == expected_character
    True
    """
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