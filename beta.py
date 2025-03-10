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
    character = {'Name': f'{player_name}', 'Level': 1, 'Health': 100, 'Strength': 15, 'Speed': 10, 'Luck': 5,
                 'Honour': 0, 'Ki': 50, 'Spirit': 10, 'Experience': 0, 'Crystals': 0, 'Shards': 10,
                 'Current Health': 100, 'X-coordinate': 0, 'Y-coordinate': 0}
    return character


# Update the title of the character into it's name, depending on level
def update_title(character):
    current_level = character['Level']

    # Name for each level
    level_name = {1: 'Amateur', 2: 'Novice', 3: 'Accepted'}

    character['Name'] += f' the {level_name[current_level]}'

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
    Berserk: Perform Heavy Strike imbued with Ki the next 3 turns. Huge boost to Strength and Ki during affect. (Physical, Ki)
Turtle: Clavem transforms into a shield. Its shape and size can be manipulated. The outer shield can be imbued with ki.
    Shell: Basic move. 95% reduced Physical damage taken and 85% reduced Ki damage taken.
    Bash: Coats the outer shield with spikes then bash into the enemy. (Physical)
    Roar: Can be used after absorbing damage with Shell. A lion's mouth forms and shoots a Ki wave based on 
          damage taken. (Ki)
    
Snake: Clavem transforms into a whip. It can extend to great lengths or split into hundreds of smaller whips.
"""
battle_stances = ['Bear', 'Turtle', 'Snake']
character_attacks = {'Bear': ['Heavy Strike', 'Sunder', 'Berserk'],
                     'Turtle': ['Shell', 'Bash', 'Roar'],
                     'Snake': []}

# Store NPC genre:type
"""
Meadows Monsters:
    Djinn: A spirit that lives in magic lamps. They are capable of possessing humans and animals.
           They are believed to be made of smokeless fire.
Woods Monsters:
    Wendigo: A cannibalistic monster. They are tall, thin, and emaciated, with pale skin.
             They posses humanoid and deer features.
"""
npc_list = {'Friendly': {'Civilian', 'Merchant', 'Guard', 'Fairy'},
            'Monsters': {'Meadows': {'Djinn', 'Skinwalker', 'Ghoul'},
                         'Woods': {'Wendigo', 'Shapeshifter', 'Werewolf'},
                         'Mountain': {'Vampire', }
                         }
            }

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
def obtain_random_npc(group_type):
    """

    :param group_type:
    :return:
    >>> obtain_random_npc('[!]')
    Werewolf
    >>> obtain_random_npc('[!]')
    Civilian
    >>> obtain_random_npc('[!]')
    Merchant
    """
    # Store how many of each encounter in a zone
    npc_count = {'Monsters': 10, 'Friendly': 5}
    # Store the types of encounters (manually adjust how many types will be within the grid)
    encounters = []
    [encounters.extend([npc] * npc_count[npc]) for npc in npc_list]
    random_type = random.choice(encounters)
    # Randomly obtain the exact NPC given the random_type (random count?)
    print(random_type)


def main():
    obtain_random_npc('')


if __name__ == "__main__":
    main()