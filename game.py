# Future import files below
import battle
import character_module
import encounters
import grid
import sys
import tutorial
from __init__ import NPC_DICT


def check_crystals(character):
    """
    Return True if character has 100 Crystals or else return False.

    :param character:
    :return:
    """
    # Obtain Crystals value from character
    crystals = character['Crystals']
    return crystals >= 100


def is_alive(character) -> bool:
    """
    Return True if character's Current Health is greater than 0 else return False.

    :param character:
    :return:
    """
    current_health = character['Current Health']
    return current_health > 0


def game_lost(alive):
    print("Your quest to become Accepted has ended.")
    print("So much blood spills from your guts.")
    print("You let go of your family heirloom.")
    print("There is only regret as you close your eyes for the final time.")
    sys.exit(0)


def game():
    # Ask user for proper character name @DONE
    name = character_module.proper_name()
    # Create new character @DONE
    character = character_module.make_character(name)
    # Make tutorial zone @STARTED
    tutorial_zone = grid.tutorial_area()
    in_tutorial = tutorial.exit_tutorial(character)
    # Character spawns in
    # Character goes through NPC interactions. Can skip to main zone. @DONE
    while in_tutorial:
        # Dialogue with Darrow explaining the goal @DONE
        # Dialogue with Misaki explaining stats and monsters @STARTED
        # Dialogue with Ragnar explaining battle mechanics and quick battle tutorial @ MAKE
        tutorial_npc = tutorial.tutorial_npcs((character["X-coordinate"], character["Y-coordinate"]))
        skip_tutorial = tutorial.tutorial_interaction(tutorial_npc, character)
        # Skip tutorial flag.
        if skip_tutorial:
            break
        while True:
            direction = character_module.get_user_choice()
            if character_module.validate_move(tutorial_zone, character, direction):
                character_module.move_character(character, direction)
                break
            else:
                print("You cannot move in that direction. Please enter a different direction.")
        in_tutorial = tutorial.exit_tutorial(character)
    # Character obtains basic items @DONE
    basic_items = {'Helmet': 'Leather Cap', 'Armour': 'Leather Tunic'}
    character_module.equip_items(character, basic_items)
    # Character moves out of tutorial zone
    # Make main board @STARTED
    board = grid.make_board(5, 5)
    # Reset character starting location for next area
    character['X-coordinate'] = 2
    character['Y-coordinate'] = 4
    # If character Current Health == 0, lost game dialogue and end game @DONE
    character_alive = is_alive(character)
    # Critical game loop around if Crystals >= 100 @DONE
    crystals_100 = check_crystals(character)
    # Store NPC and Monster weights
    npc_count = {'Monsters': 13, 'Friendly': 7, 'Environment': 4}
    # Main board game loop
    while character_alive and crystals_100:
        # Validate character direction and move character is possible or ask for direction again
        while True:
            direction = character_module.get_user_choice()
            if character_module.validate_move(tutorial_zone, character, direction):
                character_module.move_character(character, direction)
                break
            else:
                print("You cannot move in that direction. Please enter a different direction.")
        # Check if there is an encounter
        if encounters.check_encounter(character, board):
            # Randomize an encounter
            random_encounter = encounters.obtain_random_npc(npc_count)
        else:
            # Go back to movement if there are no encounters
            continue
        # If hot spring, give option to heal or leave it for future use @ MAKE
        if random_encounter in NPC_DICT['Environment']:
        # If friendly NPC, give dialogue options
        # If monster, begin battle phase
        # If hot spring, give option to heal or leave it for future use
        # Gain new move set, stats, and title upgrade every level up
    # If true, notify Character a Calamity Monster approaches
        # Character healed for battle
    # Final boss battle
    # If won, obtain quest item
    # Recall back to tutorial zone
    # Give quest item to Darrow
    # Win dialogue and end game


def main():
    game()


if __name__ == "__main__":
    main()