"""
This module contains functions for the battle mechanic.
"""
import random
from itertools import cycle

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

# Store character's attack moves
character_attacks = {
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
    pass


# Apply monster attack and its affect to character
def apply_monster_attack(attack: list, turn):
    pass


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


# Obtain character attack move
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


#