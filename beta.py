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


def main():
    npc_list = {'Monsters': 14, 'Friendly': 7, 'Environment': 4}
    print(npc_list)


if __name__ == "__main__":
    main()