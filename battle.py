"""
This module contains functions for the battle mechanic.
"""
import random
from itertools import cycle

# Stores 3 monster attack moves. Its values are [Description, Move Type, Damage].
MONSTER_ATTACK_LIST = {
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

# Store character's attack moves
CHARACTER_ATTACKS = {
    'Bear': {
        'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 15],
        'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 25],
        'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
    },
    'Turtle': {
        'Bash': ['Coats the outer shield with spikes, then bashes into the enemy.', 'Physical', 10],
        'Shell': ['Take no damage next two turns.', 'Ki', 0],
        'Roar': ["A lion's mouth forms at the center of the shield and shoots a Ki wave.", 'Ki', 40]
    },
    'Snake': {
        'Lash': ['Whip extends to lash its target.', 'Physical', 12],
        'Snare': ['Whip entangles its target, paralyzing its victim.', 'Ki', 8],
        'Hydra': ['Splits into hundreds of smaller whips making its attack unavoidable.', 'Ki', 50]
    }
}
# Create monster with Health
def create_monster(monster):
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
        'Health': monster_health.get(monster),
        'Current Health': monster_health.get(monster),
        'Status Effects': {'Buff': 0},
        'Damage Modifier': 1.0,
        'Health Modifier': 1.0
    }
    return monster_dict


# Obtain attack move from Monster
def get_monster_attack(monster: str) -> list:
    # Get list of attacks
    attack_names = list(MONSTER_ATTACK_LIST[monster].keys())
    # Weighted list of monster attacks
    monster_attack_weights = [0.5, 0.35, 0.15]
    # Select weighted random attack
    attack_name = random.choices(attack_names, weights=monster_attack_weights, k=1)[0]
    attack_details = MONSTER_ATTACK_LIST[monster][attack_name]
    # Return list of attack name and its details
    return [attack_name] + attack_details


# Apply monster attack and its affect to character
def apply_monster_attack(attack: list, character: dict) -> str:
    # Unpack attack list
    attack_name, description, attack_type, damage = attack
    # Check if character has Shell active -> Figure out how to apply #######################################

    # Apply monster attack based on type
    if attack_type == 'Attack':
        character['Current Health'] -= damage
        message = f"Monster used {attack_name}! {description} You took {damage} damage!"
    elif attack_type == 'Heal':
        # Monster heals itself 50% of the damage dealt
        heal_amount = damage // 2
        message = f"Monster used {attack_name}! {description} Monster healed for {heal_amount} health!"
    elif attack_type == 'Poison':
        character['Current Health'] -= damage
        # Add poison status effect
        character['Status']['Poison'] = 4  # Lasts for 4 turns
        message = f"Monster used {attack_name}! {description} You took {damage} damage and are poisoned!"
    elif attack_type == 'Bleed':
        character['Current Health'] -= damage
        # Add bleed status effect
        character['Status']['Bleed'] = 2  # Lasts for 2 turns
        message = f"Monster used {attack_name}! {description} You took {damage} damage and are bleeding!"
    else:
        # Monster buffs itself
        message = f"Monster used {attack_name}! {description} Monster's damage is increased!"
    # Check if character is defeated
    if character['Current Health'] <= 0:
        message += "\nYou have been defeated!"
    return message


# Figure out turn order depending on who got "First Strike" -> use itertools.cycle?
def turn_order(monster, character):
    # 50% chance to go first
    if random.random() < 0.5:
        first_strike_message = "You strike first!"
        turns = cycle(['character', 'monster'])
    else:
        first_strike_message = f"The {monster} strikes first!"
        turns = cycle(['monster', 'character'])
    return turns, first_strike_message


# Obtain user input for attack move. Max value = 3 (number of attack moves).
def get_user_choice():
    # Keep asking for valid number
    while True:
        try:
            user_input = input("Choose your attack. Enter a number between 1 and 3: ")
            attack_choice = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
        else:
            if 1 <= attack_choice <= 3:
                return attack_choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3")


def display_attack_options(stance, attacks_list):
    print(f"Your stance: {stance}")
    print("Available attacks:")

    attack_names = list(attacks_list.keys())
    for order, attack_name in enumerate(attack_names, 1):
        description = attacks_list[attack_name][0]
        attack_type = attacks_list[attack_name][1]
        damage = attacks_list[attack_name][2]

        # Show damage or effect based on attack type
        effect = f"Damage: {damage}" if damage > 0 else "Special Effect"
        print(f"{order}. {attack_name} ({attack_type}) - {description} - {effect}")

    return attack_names
# TESTING DELETE ######################################
# print(display_attack_options('Bear', {
#         'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 15],
#         'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 25],
#         'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
#     }))

# Display available stances when clicking from display_battle_menu
def display_stances(character):
    pass


# Get user input for stances or back to display_battle_menu
def get_stance(character):
    pass


# Display items when clicking from display_battle_menu
def display_items(character):
    pass


# Get user input for items or back to display_battle_menu
def get_item(character):
    pass


# Display attack list depending on stance
def display_attack_moves(character):
    pass


# Obtain character attack move or back to display_battle_menu
def get_attack_move(character: dict) -> list:
    character_stance = character['Stance']
    user_input = input()
    pass


# Apply character attack to monster
def apply_attack_move(attack: list, turn):
    pass


# Monster gives loot once defeated
def monster_defeat():
    pass


# Display battle menu with options in Pokemon-style format
def display_battle_menu():
    """
    Display the main battle menu options in Pokemon-style.

    :return: The user's choice as a string ('STANCE', 'ITEM', 'FIGHT')
    """
    # Display main battle menu
    print()
    print("┌────────────┐  ┌────────────┐")
    print("│   STANCE   │  │    ITEM    │")
    print("└────────────┘  └────────────┘")
    print("┌────────────┐")
    print("│   FIGHT    │")
    print("└────────────┘")

    # Get user choice
    valid_choices = {'STANCE': 'STANCE', 'ITEM': 'ITEM', 'FIGHT': 'FIGHT'}

    while True:
        choice = input("\nWhat will you do? Enter option name: ").upper()
        if choice in valid_choices:
            return valid_choices[choice]
        else:
            print("Invalid choice. The option name.")
# TESTING DELETE ######################################
display_battle_menu()