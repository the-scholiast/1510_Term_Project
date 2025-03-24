# File for idea and testing
import random

# Dictionary storing Character's stats
# character_stats = {'name': 'tester', 'level': 1, 'Health': 100, 'Strength': 15, 'Speed': 10, 'Luck': 5,
#                   'Honour': 0, 'Ki': 50, 'Spirit': 10, 'Experience': 0, 'Crystals': 0, 'Shards': 10,
#                   'Current Health': 100, 'X-coordinate': 0, 'Y-coordinate': 0}
"""
Health: Life pool. You lose the game if it goes to zero.
Ki: Resource pool for special abilities.
Strength: Determines how much physical damage you do. Reduces physical based attacks taken.
Spirit: Determines how much Ki based damage you do. Reduces ki based attacks taken.
Speed: Determines how often it is your turn.
Luck: Determines your dodge and critical hit chance. Also determines the chance of rare items from merchants.
Honour: Determines how NPCs interact with you. High honour = favourable options.
        Negative honour = arrest chance and weaker options.
Experience: 100 exp needed to level up. Resets back to zero.
Crystals: Collectable resource needed to battle zone boss.
Shards: Tradable resource. For upgrading stats and buying items.
X-coordinate and Y-coordinate: Current character location on the grid.
"""


# Make character including the player's name
def make_character(player_name):
    character = {'Name': f'{player_name}', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Strength': 15,
                 'Speed': 10, 'Luck': 5, 'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Spirit': 10, 'Experience': 0,
                 'Crystals': 0, 'Shards': 10, 'Current Health': 100, 'X-coordinate': 0, 'Y-coordinate': 0,
                 'Items': set()}
    return character


# Update the title of the character into it's name, depending on level
def update_title(character):
    current_level = character['Level']

    # Name for each level
    level_name = {1: 'Amateur', 2: 'Novice', 3: 'Accepted'}
    # Edit character title depending on level
    character['Title'] = f'the {level_name[current_level]}'
    return character


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


# Character Battle Stances with Clavem and its attack list
"""
Bear: Clavem transforms into a giant greatsword. The edges aren't very sharp but it packs a huge punch.
    Heavy Strike: Basic attack. (Physical)
    Sunder: Slams the ground in front of you creating a wave of ki. (Ki)
    Berserk: Perform Heavy Strike imbued with Ki the next 3 turns. Huge boost to Strength and Ki during affect. (Physical Ki)
Turtle: Clavem transforms into a shield. Its shape and size can be manipulated. The outer shield can be imbued with ki.
    Shell: Basic move. Reduced Physical and Ki damage taken depending on Strength and Spirit (Physical Ki).
    Bash: Coats the outer shield with spikes then bash into the enemy. (Physical)
    Roar: Can be used after absorbing damage with Shell. A lion's mouth forms and shoots a Ki wave based on 
          damage taken. (Ki)
Snake: Clavem transforms into a whip. It can extend to great lengths or split into hundreds of smaller whips.
    Lash: Basic attack. Whip extends to lash its target (Physical).
    Snare: Whip entangles its target, paralyzing its victim and inflicting poison (Physical Ki).
    Hydra: Splits into hundreds of smaller whips making its attack unavoidable (Physical Ki).
"""
battle_stances = ['Bear', 'Turtle', 'Snake']
character_attacks = {'Bear': [('Heavy Strike', 'Physical'), ('Sunder', 'Ki'), ('Berserk', 'Physical Ki')],
                     'Turtle': [('Shell', 'Physical Ki'), ('Bash', 'Physical'), ('Roar', 'Ki')],
                     'Snake': [('Lash', 'Physical'), ('Snare', 'Physical Ki'), ('Hydra', 'Physical Ki')]}

# Store NPC genre:type
"""
Meadows Monsters:
    Djinn: A spirit that lives in magic lamps. They are capable of possessing humans and animals.
           They are believed to be made of smokeless fire.
Woods Monsters:
    Wendigo: A cannibalistic monster. They are tall, thin, and emaciated, with pale skin.
             They posses humanoid and deer features.
"""
# NPC list for multiple zones
# npc_list = {'Friendly': {'Civilian', 'Merchant', 'Guard', 'Fairy'},
#             'Monsters': {'Meadows': {'Djinn', 'Skinwalker', 'Ghoul'},
#                          'Woods': {'Wendigo', 'Shapeshifter', 'Werewolf'},
#                          'Mountain': {'Vampire', }},
#             'Environment': {'Hot Spring'}
#             }
# NPC list for single zone (simple)
# npc_list = {'Friendly': ['Civilian', 'Merchant', 'Guard', 'Fairy'],
#             'Monsters': ['Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'],
#             'Environment': ['Hot Spring']
#             }

# Store Monster's list of attacks (Ordered from most likely attack to least likely)
"""
Wendigo:
    Swipe: Basic attack. Swipes with its claws.
    Insatiable Hunger: Increases its appetite, boosting its stats.
    Poison Bite: Its saliva is toxic causing its bite to apply poison.
"""
monster_attack_list = {'Wendigo': ['Swipe', 'Insatiable Hunger', 'Poison Bite'],
                       'Djinn': ['Paralyze', 'Soul Drain', 'Possess']}

# Store list of potential boss to fight
"""
Zodd

"""


# Given the grid character, randomly choose from an element from within its group type.
# Weighted system to guarantee certain numbers of NPCs/Monsters
def obtain_random_npc():
    """

    :param:
    :return:
    >>> obtain_random_npc('[!]')
    Werewolf
    >>> obtain_random_npc('[!]')
    Civilian
    >>> obtain_random_npc('[!]')
    Merchant
    """
    npc_list = {'Friendly': ['Civilian', 'Merchant', 'Guard', 'Fairy'],
                'Monsters': ['Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'],
                'Environment': ['Hot Spring']
                }
    # Store how many of each encounter in a zone
    npc_count = {'Monsters': 14, 'Friendly': 7, 'Environment': 4}

    # Sort NPC list by its keys
    npc_list_keys = sorted(list(npc_list.keys()))

    # Create weighted NPC list
    weighted_list = [npc_count[npc_type] for npc_type in sorted(npc_list)]

    # Get a weighted random selection of encounter type
    random_type = random.choices(population=npc_list_keys,
                                 weights=weighted_list,
                                 k=1)[0]

    # Get random NPC from that type
    random_npc = random.choice(npc_list[random_type])

    return random_npc


def main():
    print(obtain_random_npc())


if __name__ == "__main__":
    main()