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
    # Hot spring manager
    def hot_spring_manager(character: dict):
        # Display hot spring options
        encounters.hot_spring_encounter()
        # Get user choice
        user_choice = encounters.user_input_hot_spring()
        # Apply reward based on choice
        encounters.hot_spring_reward(character, user_choice)

    # Merchant manager
    def merchant_manager(character: dict):
        # Get merchant items based on character level
        merchant_items = encounters.merchant_offers(character)
        # Display merchant offers
        encounters.print_merchant_offers(merchant_items)
        # Get user choice for equipment
        equipment_choice = encounters.user_picks_equipment(merchant_items)
        # Equip the selected item
        character_module.obtain_and_equip(equipment_choice, character)
        # Apply the item stats
        character_module.apply_equipment(character)
        # Print Merchant Dialogue
        print(f"The merchant hands you the {equipment_choice[1]}.")
        print("Merchant: 'May it serve you well on your journey!'")
        # Print stat increase
        character_module.print_apply_equipment(equipment_choice, character)

    # Monster manager
    def monster_manager(character: dict, monster_name: str):
        # Create monster
        monster = battle.create_monster(monster_name)
        # Determine turn order
        turns, first_strike_message = battle.turn_order(monster_name)
        print(first_strike_message)
        # Battle loop
        current_turn = next(turns)
        character_is_alive = is_alive(character)
        monster_alive = not battle.monster_defeat(monster)
        # Character and monster must be alive for the battle loop to continue
        while character_is_alive and monster_alive:
            # Display health status -> decompose?
            print(f"Your Health: {character['Current Health']}/{character['Health']}")
            print(f"Your Ki: {character['Current Ki']}/{character['Ki']}")
            print(f"{monster_name}'s Health: {monster['Current Health']}/{monster['Health']}")
            # Monster's turn
            if current_turn == 'monster':
                # Check if monster is snared
                if not battle.skip_turn(monster):
                    # Get monster attack
                    monster_attack = battle.get_monster_attack(monster_name)
                    # Apply monster attack to character
                    battle.apply_monster_attack(monster_attack, character)
            # Character's turn -> FINISH
            else:
                # Display battle menu
                battle.display_battle_menu()
                # Get user choice
                battle_choice = battle.get_user_choice_battle_menu()
                # Option 1 is Stance
                if battle_choice == '1':
                    # Display available stances
                    battle.display_stances(character)
                    # Get user stance choice
                    battle.get_stance(character)
                # Option 2 is Item
                elif battle_choice == '2':
                    # Display available items
                    battle.display_items(character)
                    # Get user item choice
                    item_choice = battle.get_item(character)
                    # Use item
                    character_module.use_item(character, item_choice)
                # Option 3 is Fight
                elif battle_choice == '3':
                    # Get attack moves for current stance
                    attack_moves = battle.get_attack_moves(character, battle.CHARACTER_ATTACKS)
                    # Display attack options
                    battle.display_attack_options(character['Active Stance'], attack_moves)
                    # Get user attack choice
                    attack_choice = battle.get_attack_choice(character, attack_moves)
                    # Apply attack to monster
                    battle.apply_attack_move(attack_choice, character, monster)
                # Update status effects
            battle.update_status_effects(character, monster)
            # Next turn
            current_turn = next(turns)
            character_is_alive = is_alive(character)
            monster_alive = not battle.monster_defeat(monster)
            # Get rewards from beating monster
            if battle.monster_defeat(monster):
                battle.monster_rewards(character)

    # Manages all potential encounters
    def encounter_manager(character, npc_count):
        # Get random encounter
        new_random_encounter = encounters.obtain_random_npc(npc_count)
        print(f"You encountered: {new_random_encounter}")
        # Handle different encounter types
        if new_random_encounter == 'Hot Spring':
            hot_spring_manager(character)
        elif new_random_encounter == 'Merchant':
            merchant_manager(character)
        # Monster encounter -->> fix NPC_DICT
        elif new_random_encounter in NPC_DICT['Monsters']:
            monster_manager(character, new_random_encounter)

    # Ask user for proper character name @DONE
    name = character_module.proper_name()
    # Create new character @DONE
    new_character = character_module.make_character(name)
    # Make tutorial zone @STARTED
    tutorial_zone = grid.tutorial_area()
    in_tutorial = tutorial.exit_tutorial(new_character)
    # Character spawns in
    # Character goes through NPC interactions. Can skip to main zone. @DONE
    while in_tutorial:
        # Mark visited areas with empty space
        tutorial_zone = grid.mark_location_visited(tutorial_zone, new_character)
        # Get tutorial NPC interaction based on character location
        tutorial_npc = tutorial.tutorial_npcs((new_character["X-coordinate"], new_character["Y-coordinate"]))
        # Skip tutorial flag
        skip_tutorial = tutorial.tutorial_interaction(tutorial_npc, new_character)
        if skip_tutorial:
            break
        # Begin tutorial
        while True:
            grid.print_board(tutorial_zone, new_character)
            direction = character_module.get_user_choice()
            if character_module.validate_move(tutorial_zone, new_character, direction):
                character_module.move_character(new_character, direction)
                break
            else:
                print("You cannot move in that direction. Please enter a different direction.")
        # Check if character still in tutorial zone
        in_tutorial = tutorial.exit_tutorial(new_character)
    # Character obtains basic items ->>> FIX
    basic_items = ('Armour', 'Leather Tunic', 0.02)
    character_module.obtain_and_equip(basic_items, new_character)
    # Character moves out of tutorial zone
    # Make main board @STARTED
    board = grid.make_board(5, 5)
    # Reset character starting location for next area
    new_character['X-coordinate'] = 2
    new_character['Y-coordinate'] = 4
    # If character Current Health == 0, lost game dialogue and end game @DONE
    character_alive = is_alive(new_character)
    # Critical game loop around if Crystals >= 100 @DONE
    crystals_100 = check_crystals(new_character)
    # Store NPC and Monster weights
    npc_count = {'Monsters': 13, 'Friendly': 7, 'Environment': 4}
    # Main board game loop
    while character_alive and not crystals_100:
        grid.print_board(board, new_character)
        # Validate character direction and move character is possible or ask for direction again
        while True:
            direction = character_module.get_user_choice()
            if character_module.validate_move(board, new_character, direction):
                character_module.move_character(new_character, direction)
                break
            else:
                print("You cannot move in that direction. Please enter a different direction.")
        # Check if there is an encounter
        if encounters.check_encounter(new_character, board):
            # Operate proper encounter
            encounter_manager(new_character, npc_count)
        else:
            # Go back to movement if there are no encounters
            continue
        # Gain new move set, stats, and title upgrade every level up
        if new_character['Level'] > 1:
            character_module.level_up(new_character)
            character_module.print_level_up(new_character)
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
