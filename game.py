"""
Woojin Song, A01431327
This module drives the entire game.
"""
import ascii
import battle
import character_module
import encounters
import grid
import random
import sys
import tutorial


def check_crystals(character: dict) -> bool:
    """
    Return True if character has 100 Crystals or else return False.

    Checks if the character has gathered enough crystals to trigger the final boss battle.

    :param character: a dictionary containing character data with a 'Crystals' key with an integer value >= 0
    :precondition: character must be a dictionary containing a 'Crystals' key with an integer value >= 0
    :postcondition: leave character unmodified
    :postcondition: check if the character has at least 100 Crystals for the final battle
    :return: True if character Crystals value is >= 100 else False

    >>> test_character = {'Crystals': 100}
    >>> check_crystals(test_character)
    True
    >>> test_character = {'Crystals': 99}
    >>> check_crystals(test_character)
    False
    >>> test_character = {'Crystals': 0}
    >>> check_crystals(test_character)
    False
    """
    # Obtain Crystals value from character
    crystals = character['Crystals']
    return crystals >= 100


def is_alive(character: dict) -> bool:
    """
    Return True if character's Current Health is greater than 0 or else return False.

    :param character: a dictionary containing character data with a 'Current Health' key with an integer value
    :precondition: character must be a dictionary containing character data with
                   a 'Current Health' key with an integer value
    :postcondition: leave character unmodified
    :postcondition: check if character Current Health value is > 0
    :return: True if character Current Health value is > 0 else False

    >>> test_character = {"Current Health": 100}
    >>> is_alive(test_character)
    True
    >>> test_character = {"Current Health": 0}
    >>> is_alive(test_character)
    False
    >>> test_character = {"Current Health": -10}
    >>> is_alive(test_character)
    False
    """
    current_health = character['Current Health']
    return current_health > 0


def game_lost() -> None:
    """
    Print game over message when the character dies and terminate the program.

    :postcondition: print text describing the character's death
    :postcondition: terminate the program with sys.exit
    """
    print("Your quest to become Accepted has ended.")
    print("So much blood spills from your guts.")
    print("You let go of your family heirloom.")
    print("There is only regret as you close your eyes for the final time.")
    sys.exit(0)


def game():
    """
    Manage the entire game.
    """

    # Hot spring manager
    def hot_spring_manager(character: dict) -> None:
        """
        Manage hot spring interactions.

        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :postcondition: run functions interacting with hot spring encounter
        """
        # Display hot spring options
        encounters.hot_spring_encounter()
        # Get user choice
        user_choice = encounters.user_input_hot_spring()
        # Apply reward based on choice
        encounters.hot_spring_reward(character, user_choice)

    # Merchant manager
    def merchant_manager(character: dict) -> None:
        """
        Manage merchant interactions.

        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :postcondition: run functions interacting with merchant encounter
        :postcondition: print merchant accepted equipment message
        """
        # Get merchant items based on character level
        merchant_items = encounters.merchant_offers(character)
        # Display merchant offers
        encounters.print_merchant_offers(merchant_items)
        # Get user choice for equipment
        equipment_choice = encounters.user_picks_equipment(merchant_items)
        # Remove modifiers of current equipment
        character_module.remove_equipment_modifiers(character)
        # Equip the selected item
        character_module.obtain_and_equip(equipment_choice, character)
        # Apply the item stats
        character_module.apply_equipment(character)
        # Print Merchant Dialogue
        print(f"The merchant hands you the {equipment_choice[1]}.")
        print("Merchant: 'May it serve you well on your journey!'")
        # Print stat increase
        character_module.print_apply_equipment(equipment_choice, character)

    # Handles monster attack
    def apply_monster_attack(attack: list, character: dict, monster: dict) -> None:
        """
        Process a monster's attack against the character based on attack type.

        :param attack: a list containing [attack_name, description, attack_type, damage] as [str, str, str, int]
        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :param monster: a dictionary containing all monster data
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :precondition: monster must be a dictionary containing all monster data
        :precondition: attack must contain exactly 4 elements: attack_name, description, attack_type, and damage
        :precondition: attack_type must be one of: 'Attack', 'Heal', 'Poison', 'Bleed', or any other value for 'Buff'
        :postcondition: process the appropriate attack against the character based on attack_type
        :postcondition: check if character is defeated and update message
        :postcondition: print the attack result message
        """
        # Unpack attack list
        attack_name, description, attack_type, damage = attack
        # Obtain 'Damage Modifier' value from monster
        monster_modifier = monster['Damage Modifier']
        # Obtain 'Active Defense Modifier' value from character
        defense_modifier = character['Active Defense Modifier']
        # Process attack based on type
        if attack_type == 'Attack':
            message = battle.process_attack(character, monster_modifier, defense_modifier, damage, attack_name,
                                            description)
        elif attack_type == 'Heal':
            message = battle.process_heal_attack(character, monster, damage, defense_modifier, attack_name,
                                                 description)
        elif attack_type == 'Poison':
            message = battle.process_poison_attack(character, monster_modifier, defense_modifier, damage,
                                                   attack_name, description)
        elif attack_type == 'Bleed':
            message = battle.process_bleed_attack(character, monster_modifier, defense_modifier, damage,
                                                  attack_name, description)
        # Buff type
        else:
            message = battle.process_buff_attack(monster, attack_name, description)
        # Check if character is defeated
        message = battle.check_character_defeat(character, message)
        # Display the message
        print(message)

    # Manager function to apply character attack move
    def apply_attack_move(attack_move: tuple, character: dict, monster: dict) -> None:
        """
        Execute a character's attack move against a monster.

        :param attack_move: a tuple containing (attack_name, attack_details) where attack_details
                            is a list of [description, attack_type, damage] as [str, str, int]
        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :param monster: a dictionary containing all monster data
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :precondition: monster must be a dictionary containing all monster data
        :precondition: attack_move must be a tuple with exactly 2 elements
        :precondition: attack_details must be a list with exactly 3 elements
        :postcondition: execute the attack if valid
        :postcondition: print the result of the attack attempt
        """
        # Unpack attack details
        attack_name, attack_details = attack_move
        description, attack_type, damage = attack_details
        # Get damage modifier from character
        damage_modifier = character['Damage Modifier']
        # Check if the attack is valid and execute it
        success, message = battle.execute_attack(attack_type, attack_name, description,
                                                 damage, damage_modifier, character, monster)
        # Print the result
        battle.print_attack_result(attack_type, success, message)

    # Manager to process status effects
    def process_status_effects(character: dict, monster: dict) -> None:
        """
        Process active status effects for both character and monster.

        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :param monster: a dictionary containing all monster data
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :precondition: monster must be a dictionary containing all monster data
        :postcondition: apply damage from active status effects to the character
        :postcondition: print status effect damage messages if any
        :postcondition: update and decrement all status effect durations
        """
        # First apply damage from active status effects to character
        character_status_message = battle.apply_status_damage(character)
        # Print status effect damage messages
        if character_status_message:
            print(character_status_message)
        # Then update status effect durations
        battle.update_status_effects(character, monster)

    # Monster manager
    def monster_manager(character: dict, monster_name: str, custom_monster=None) -> None:
        """
        Manage a battle between character and monster.

        Handles turn order, battle loop, and user actions until either the monster or character is defeated.
        Resets character statuses and awards rewards when the monster is defeated.

        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :param monster_name: a string representing monster name
        :param custom_monster: optional pre-created monster dictionary
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :precondition: monster_name must be a string
        :precondition: custom_monster must be None or a dictionary containing monster data
        :postcondition: run all functions to handle battle mechanic
        """
        # Create monster or use custom one if provided
        monster = custom_monster if custom_monster else battle.create_monster(monster_name, character['Level'])
        # Determine turn order
        turns, first_strike_message = battle.turn_order(monster_name)
        print(first_strike_message)
        # Battle loop
        current_turn = next(turns)
        character_is_alive = is_alive(character)
        monster_alive = not battle.monster_defeat(monster)
        # Character and monster must be alive for the battle loop to continue
        while character_is_alive and monster_alive:
            # Display health status
            print(f"Your Health: {character['Current Health']}/{character['Health']}")
            print(f"Your Ki: {character['Current Ki']}/{character['Ki']}")
            print(f"{monster['Name']}'s Health: {monster['Current Health']}/{monster['Health']}")
            # Monster's turn
            if current_turn == 'monster':
                # Check if monster is snared
                if not battle.skip_turn(monster):
                    # Get monster attack. Split handles situation for final boss.
                    monster_attack = battle.get_monster_attack(monster['Name'].split()[-1])
                    # Apply monster attack to character
                    apply_monster_attack(monster_attack, character, monster)
                # Move to next turn after monster's action
                current_turn = next(turns)
            # Character's turn
            else:
                # Flag to track if player completed an action
                action_completed = False
                # Loop until player completes an action
                while not action_completed:
                    # Display battle menu
                    battle.display_battle_menu()
                    # Get user choice for battle menu
                    battle_choice = battle.get_user_choice_battle_menu()
                    # Option 1 is Stance
                    if battle_choice == '1':
                        # Display available stances
                        battle.display_stances(character)
                        # Get user stance choice
                        stance_choice = battle.get_stance(character)
                        # Only mark action as completed if a stance was chosen not back
                        if stance_choice is not None:
                            action_completed = True
                    # Option 2 is Item
                    elif battle_choice == '2':
                        # Display available items
                        battle.display_items(character)
                        # Get user item choice
                        item_choice = battle.get_item(character)
                        # Only mark action as completed if an item was used not back
                        if item_choice is not None:
                            character_module.use_item(character, item_choice)
                            action_completed = True
                    # Option 3 is Fight
                    elif battle_choice == '3':
                        # Get attack moves for current stance
                        attack_moves = battle.get_attack_moves(character)
                        # Display attack options
                        battle.display_attack_options(character['Active Stance'], attack_moves)
                        # Get user attack choice
                        attack_choice = battle.get_attack_choice(attack_moves)
                        # Only proceed if an attack was chosen, not back
                        if attack_choice is not None:
                            # Check if it's a Ki attack and if there's enough Ki
                            attack_name, attack_details = attack_choice
                            attack_type = attack_details[1]
                            if attack_type == 'Ki' and character['Current Ki'] < 10:
                                print("You don't have enough Ki to use this attack! Choose another action.")
                            else:
                                # Apply attack to monster
                                apply_attack_move(attack_choice, character, monster)
                                action_completed = True
                # Only move to next turn if player completed an action
                if action_completed:
                    current_turn = next(turns)
            # Process status effects after each turn
            process_status_effects(character, monster)
            # Check battle status
            character_is_alive = is_alive(character)
            monster_alive = not battle.monster_defeat(monster)
        # Reset character statuses at the end of battle
        battle.reset_statuses(character)
        # Get rewards from beating monster if monster was defeated
        if battle.monster_defeat(monster):
            battle.monster_rewards(character)

    # Manages all potential encounters
    def encounter_manager(character, npc_counts):
        """
        Handle random encounters in the game world (Friendly, Monsters, Environment).

        :param character: a dictionary containing all character attributes including name, stats,
                          position, inventory, equipment, and status effects
        :param npc_counts: a dictionary tracking encounter type weights for encounter selection
        :precondition: character must be a dictionary containing all character attributes including name, stats,
                       position, inventory, equipment, and status effects
        :postcondition: proper encounter is triggered based on random selection
        :postcondition: correct manager function is called to handle the encounter
        """
        npc_dict = {'Friendly': ['Merchant'],
                    'Monsters': ['Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire'],
                    'Environment': ['Hot Spring']}
        # Get random encounter
        new_random_encounter = encounters.obtain_random_npc(npc_counts)
        print(f"You encountered: {new_random_encounter}")
        # Handle different encounter types
        if new_random_encounter == 'Hot Spring':
            hot_spring_manager(character)
        elif new_random_encounter == 'Merchant':
            merchant_manager(character)
        # Monster encounter
        elif new_random_encounter in npc_dict['Monsters']:
            monster_manager(character, new_random_encounter)

    # Welcome ascii
    ascii.welcome()
    # Ask user for proper character name
    name = character_module.proper_name()
    # Create new character
    new_character = character_module.make_character(name)
    # Make tutorial zone
    tutorial_zone = tutorial.tutorial_area()
    in_tutorial = tutorial.exit_tutorial(new_character)
    # Character goes through NPC interactions. Can skip to main zone
    while in_tutorial:
        # Mark visited areas with empty space
        grid.mark_location_visited(tutorial_zone, new_character)
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
    # Make main game board
    board = grid.make_board(5, 5)
    # Reset character starting location for next area
    new_character['X-coordinate'] = 2
    new_character['Y-coordinate'] = 4
    # If character Current Health == 0, lost game dialogue and end game
    character_alive = is_alive(new_character)
    # Critical game loop around if Crystals >= 100
    crystals_100 = check_crystals(new_character)
    # Store NPC and Monster weights
    npc_count = {'Monsters': 14, 'Friendly': 6, 'Environment': 4}
    # Main board game loop
    while character_alive and not crystals_100:
        grid.mark_location_visited(board, new_character)
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
            # Check if character is still alive after the encounter
            character_alive = is_alive(new_character)
            if not character_alive:
                ascii.game_over()
                game_lost()
            # Check if character has reached 100 crystals
            crystals_100 = check_crystals(new_character)
        # Gain new move set, stats, and title upgrade every level up
        leveled_up = character_module.level_up(new_character)
        if leveled_up:
            character_module.print_level_up(new_character)
    # If player has collected 100 crystals, start final boss sequence
    if crystals_100:
        # Notify player about approaching calamity
        ascii.boss_fight()
        print("\nYou feel a powerful presence approaching...")
        print("The ground trembles beneath your feet.")
        print("A massive creature emerges from the shadows!\n")
        # Heal character for final battle
        new_character['Current Health'] = new_character['Health']
        new_character['Current Ki'] = new_character['Ki']
        print("You prepare yourself for the final battle!")
        # Create monster for final boss. Modified version of a regular monster
        monsters = ['Djinn', 'Skinwalker', 'Ghoul', 'Wendigo', 'Shapeshifter', 'Werewolf', 'Vampire']
        boss_monster_type = random.choice(monsters)
        # Create a regular monster first
        boss_monster = battle.create_monster(boss_monster_type)
        # Enhance the boss monster stats
        boss_monster['Health'] = 500
        boss_monster['Current Health'] = 500
        boss_monster['Damage Modifier'] = 1.7
        # Handle final boss battle
        print(f"The Calamity Beast {boss_monster_type} appears!")
        monster_manager(new_character, boss_monster_type, boss_monster)
        # Check if character survived the battle
        character_alive = is_alive(new_character)
        if character_alive:
            print("\nCongratulations! You have defeated the Calamity Beast!")
            print("You collect its rare Crystal and return to the Reaper's Guild.")
            print("\nDarrow: 'ZEHAHAHAHA! You've done it! You are now an Accepted member of the Reaper's Guild!'")
            print(f"{new_character['Name']}, you have completed your quest.")
            ascii.game_won()
            sys.exit(0)
        else:
            ascii.game_over()
            game_lost()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()