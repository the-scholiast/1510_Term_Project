"""
This module contains all possible encounters with NPCs and monsters.
"""
import random

# TEST CHARACTER DELETE #####################################################
test_character = {
    'Name': 'Tester', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Current Health': 100,
    'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Experience': 0, 'Defense Modifier': 1, 'Damage Modifier': 1,
    'Crystals': 0, 'X-coordinate': 0, 'Y-coordinate': 0, 'Items': {'Health Pots': 1, 'Shards': 3},
    'Equipment': {'Helmet': "", 'Armour': "", 'Ring': "", 'Amulet': ""}, 'Stance': ['Bear'],
    'Status': {"Poison": 0, "Bleed": 0, 'Shell': 0, 'Berserk': 0}, 'Active Stance': 'Bear',
    'Active Defense Modifier': 1
}


def check_encounter(character: dict, board: dict) -> bool:
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    return board[character_location] == '[!]'


def obtain_random_npc(npc_count: dict) -> str:
    """
    Obtain a random encounter depending on the weights.

    :param:
    :return:
    """
    npc_list = {'Friendly': 'Merchant',
                'Monsters': ('Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'),
                'Environment': 'Hot Spring'
                }
    # Store how many of each encounter in a zone

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
    character_level = character.get("Level")
    # Equipment offerings based on character level
    equipment_by_level = {
        1: {'Helmet': ('Iron Hat', 0.02), 'Armour': ('Copper Plate', 0.04),
            'Ring': ('Copper Ring', 0.02), 'Amulet': ('Wooden Charm', 0.02)},
        2: {'Helmet': ('Iron Helmet', 0.04), 'Armour': ('War Plate', 0.08),
            'Ring': ('Ruby Ring', 0.04), 'Amulet': ('Crystal Pendant', 0.04)},
        3: {'Helmet': ('Steel Helmet', 0.06), 'Armour': ('Sun Plate', 0.12),
            'Ring': ('Warrior Ring', 0.06), 'Amulet': ('Focused Amulet', 0.06)}
    }
    return equipment_by_level.get(character_level)


# Print merchant offers
def print_merchant_offers(equipment: dict):
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
    print("│ 0. Leave                                         │")
    print("└" + "─" * 50 + "┘")
# TESTING DELETE
test_equipment = {'Helmet': ('Iron Hat', 0.02), 'Armour': ('Copper Plate', 0.04),
                  'Ring': ('Copper Ring', 0.02), 'Amulet': ('Wooden Charm', 0.02)}
# print_merchant_offers(test_equipment)

# Get user equipment choice
def user_picks_equipment(equipment) -> tuple:
    # Create mapping of numbers to item types
    equipment_types = list(equipment.keys())
    equipment_choice = {str(index): item_type for index, item_type in enumerate(equipment_types, 1)}
    while True:
        user_input = input("Enter the number of the item you wish to purchase: ").strip()
        if user_input in equipment_choice:
            item_type = equipment_choice[user_input]
            item_name, price = equipment[item_type]
            return item_type, item_name, price
        else:
            print(f"Invalid choice. Please enter a number between 1 and 3.")
# TESTING DELETE
# print(user_picks_equipment(test_equipment))

# Merchant gives equipment and character equips it
def obtain_and_equip(equipment_choice: tuple, character: dict):
    item_type, item_name, price = equipment_choice
    character_equipment = character['Equipment']
    character_equipment[item_type] = (item_name, price)
    print(f"You have equipped {item_name}!")
# TESTING DELETE
# obtain_and_equip(('Helmet', 'Iron Hat', 0.02), test_character)

# Hot spring encounter options
def hot_spring_encounter():
    print("You've discovered a steaming hot spring nestled between large rocks!")
    print("The water has a slight blue hue and smells faintly of minerals.")
    print("┌" + "─" * 50 + "┐")
    print("│ What would you like to do?                       │")
    print("├" + "─" * 50 + "┤")
    print("│ 1. Bathe in the spring (fully restore Health/Ki) │")
    print("│ 2. Collect minerals (gain Health pots and shards)│")
    print("└" + "─" * 50 + "┘")
# TEST DELETE
# hot_spring_encounter()

# Get user choice for hot spring
def user_input_hot_spring() -> int:
    valid_choices = {"1", "2"}
    while True:
        user_choice = input("Enter your choice [1-2]: ").strip()
        if user_choice in valid_choices:
            return int(user_choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")


# Heals to full for Health and Ki or can receive items instead
def hot_spring_reward(character: dict, user_choice: int):
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
# TEST DELETE
hot_spring_reward(test_character, 2)