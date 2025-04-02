"""
This module contains functions for the battle mechanic.
"""
import random
from itertools import cycle
from __init__ import BATTLE_STANCES

# TEST CHARACTER DELETE #####################################################
test_character = {
    'Name': 'Tester', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Current Health': 100,
    'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Experience': 0, 'Defense Modifier': 1, 'Damage Modifier': 1,
    'Crystals': 0, 'X-coordinate': 0, 'Y-coordinate': 0, 'Items': {'Health Pots': 1, 'Shards': 3},
    'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""}, 'Stance': ['Bear'],
    'Status': {"Poison": 0, "Bleed": 0, 'Shell': 0, 'Berserk': 0}, 'Active Stance': 'Bear',
    'Active Defense Modifier': 1
}
test_monster = {
    'Name': 'Vampire',
    'Health': 95,
    'Current Health': 95,
    'Status Effects': {'Buff': 0, 'Snared': 0},
    'Damage Modifier': 1.0,
    'Health Modifier': 1.0
}
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
        'Status Effects': {'Buff': 0, 'Snared': 0},
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
def apply_monster_attack(attack: list, character: dict):
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
    print(message)


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

# Skip monster turn if snared
def skip_turn(monster):
    # Check if monster is snared
    if monster['Status Effects'].get('Snared') > 0:
        print(f"{monster['Name']} is snared and cannot move this turn!")
        return True
    return False


# Display battle menu with options in Pokemon-style format
def display_battle_menu():
    """
    Display the main battle menu options in Pokemon-style.
    """
    # Display main battle menu
    print()
    print("┌────────────┐  ┌────────────┐")
    print("│   STANCE   │  │    ITEM    │")
    print("└────────────┘  └────────────┘")
    print("┌────────────┐")
    print("│   FIGHT    │")
    print("└────────────┘")


# TESTING DELETE ######################################
# display_battle_menu()

def get_user_choice_battle_menu() -> str:
    # Get user choice from battle menu
    valid_choices = {'STANCE': 'STANCE', 'ITEM': 'ITEM', 'FIGHT': 'FIGHT'}

    while True:
        choice = input("What will you do? Enter option name: ").upper().strip()
        if choice in valid_choices:
            return valid_choices[choice]
        else:
            print("Invalid choice. The option name.")


# Display available stances when clicking from display_battle_menu
def display_stances(character):
    available_stances = character['Stance']
    print("Available Stances:")
    print("┌" + "─" * 22 + "┐")
    # Display each available stance
    for stance_name in available_stances:
        # Find the stance BATTLE_STANCES
        for stance_tuple in BATTLE_STANCES:
            if stance_tuple[0] == stance_name:
                break
        print(f"│ {stance_name:<20} │")
    print("├" + "─" * 22 + "┤")
    print(f"│ {"Back":<20} │")
    print("└" + "─" * 22 + "┘")


# print(display_stances({
#         'Name': 'Tester', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Current Health': 100,
#         'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Experience': 0, 'Defense Modifier': 0, 'Damage Modifier': 1,
#         'Crystals': 0, 'X-coordinate': 0, 'Y-coordinate': 0, 'Items': {'Health Pots': 0, 'Shards': 0},
#         'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""}, 'Stance': ['Bear'],
#         'Status': {"Poison": 0, "Bleed": 0}
#     }))

# Get user input for stances or back to display_battle_menu
def get_stance(character):
    available_stances = character['Stance']
    # Ask user for stance or back to display_battle_menu
    while True:
        user_choice = input("Select a stance or type 'Back' to return: ").strip().title()
        if user_choice in available_stances:
            # Update character's active stance
            character['Active Stance'] = user_choice
            print(f"You adopt the {user_choice} stance!")
            # Obtain the stance_description
            stance_descriptions = {stance[0]: stance[1] for stance in BATTLE_STANCES}
            description = stance_descriptions.get(user_choice)
            print(f"{description}")
            # Return the stance
            return user_choice
        # Back to display_battle_menu
        elif user_choice == 'Back':
            return
        else:
            print("Invalid stance. Please select from the available options.")


# TESTING DELETE ############################################################
# print(get_stance(test_character))


# Display items when clicking from display_battle_menu
def display_items(character):
    items = character['Items']
    print("Available Items:")
    print("┌" + "─" * 22 + "┐")
    # Display each item and its quantity
    for item_name, quantity in items.items():
        if quantity > 0:
            print(f"│ {item_name:<12} x{quantity:<6} │")
    # If no items available
    if all(quantity == 0 for quantity in items.values()):
        print(f"│ {'No items available':<20} │")
    print("├" + "─" * 22 + "┤")
    print(f"│ {"Back":<20} │")
    print("└" + "─" * 22 + "┘")
# TESTING DELETE ######################################
# display_items(test_character)


# Get user input for items or back to display_battle_menu
def get_item(character):
    items = character.get('Items')
    available_items = [item for item, quantity in items.items() if quantity > 0]
    # If no items available, return to battle menu
    if not available_items:
        input("Press Enter to return to battle menu...")
        return None
    while True:
        user_choice = input("Select an item or type 'Back' to return: ").strip().title()
        if user_choice in available_items:
            return user_choice
        elif user_choice == 'Back':
            return None
        else:
            print("Invalid item. Please select from the available options.")
# TESTING DELETE ######################################
# print(get_item(test_character))


# Obtain character attack moves by stance
def get_attack_moves(character: dict, attacks_dict: dict) -> dict:
    character_stance = character.get('Active Stance')
    attack_moves = attacks_dict.get(character_stance)
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


# TESTING DELETE ######################################
# display_attack_options('Bear', {
#     'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 15],
#     'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 25],
#     'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
# })


# Obtain user input for attack move. Max value = 3 (number of attack moves). 0 to go back to display_battle_menu
def get_attack_choice(character: dict, attacks_dict: dict) -> tuple:
    # Keep asking for valid number
    while True:
        try:
            user_input = input("Choose your attack. Enter a number between 1 and 3, or 0 to go back: ")
            attack_choice = int(user_input) - 1
        except ValueError:
            print("Please enter a valid number.")
        else:
            if 0 <= attack_choice <= 3:
                attack_moves = tuple(attacks_dict.items())
                return attack_moves[attack_choice]
            else:
                print("Invalid choice. Please enter a number between 0 and 3")
            # Condition to exit when input is 0

# TESTING DELETE ######################################
# print(get_attack_choice({
#     'Name': 'Tester', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Current Health': 100,
#     'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Experience': 0, 'Defense Modifier': 0, 'Damage Modifier': 1,
#     'Crystals': 0, 'X-coordinate': 0, 'Y-coordinate': 0, 'Items': {'Health Pots': 0, 'Shards': 0},
#     'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""}, 'Stance': ['Bear'],
#     'Status': {"Poison": 0, "Bleed": 0, "Shell": 0}, 'Active Stance': ['Bear']
# }, {
#     'Heavy Strike': ['A powerful blow with massive physical damage.', 'Physical', 15],
#     'Sunder': ['Slams the ground in front of you creating a wave of Ki.', 'Ki', 25],
#     'Berserk': ['Enters a state of rage, increasing both physical damage and Ki attacks.', 'Ki', 0]
# }))


# Apply character attack to monster ### DECOMPOSE
def apply_attack_move(attack_move: tuple, character: dict, monster: dict):
    attack_name, attack_details = attack_move
    description, attack_type, base_damage = attack_details
    # Apply damage modifier from character
    damage_modifier = character.get('Damage Modifier')
    actual_damage = int(base_damage * damage_modifier)
    message = ""
    # Apply attack based on type
    if attack_type == 'Physical':
        monster['Current Health'] -= actual_damage
        message = f"You used {attack_name}! {description} You dealt {actual_damage} damage!"
    elif attack_type == 'Ki':
        # Check if character has enough Ki
        if character['Current Ki'] >= 10:
            # Ki attacks cost 10 Ki points
            character['Current Ki'] -= 10
            # Damaging Ki attack
            if base_damage > 0:
                monster['Current Health'] -= actual_damage
                message = f"You used {attack_name}! {description} You dealt {actual_damage} Ki damage!"
            # Buff/special Ki attack
            else:
                if attack_name == 'Berserk':
                    character['Damage Modifier'] += 0.5
                    # Add duration tracking for Berserk. Lasts for 3 turns
                    character['Status']['Berserk'] = 3
                    message = f"You used {attack_name}! {description} Your damage is increased by 50% for 3 turns!"
                elif attack_name == 'Shell':
                    # Add Shell status with duration. # Lasts for 2 turns
                    character['Status']['Shell'] = 2
                    character['Active Defense Modifier'] = 0
                    message = f"You used {attack_name}! {description} You take no damage for the next two turns!"
                elif attack_name == 'Snare':
                    # Monster loses a turn
                    monster['Status Effects']['Snared'] = 1
                    message = (f"You used {attack_name}! {description} "
                               f"The monster is snared and will miss its next turn!")
        else:
            message = "You don't have enough Ki to use this attack!"
    print(message)

print(f"before: {test_monster['Current Health']}")
apply_attack_move(('Heavy Strike', ['A powerful blow with massive physical damage.', 'Physical', 15]),
                  test_character, test_monster)
print(f"after: {test_monster['Current Health']}")


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
    for effect, duration in list(monster['Status Effects'].items()):
        if duration > 0:
            monster['Status Effects'][effect] -= 1


# Check if monster health is <= 0
def monster_defeat(monster: dict) -> bool:
    monster_health = monster.get("Health")
    return monster_health <= 0
