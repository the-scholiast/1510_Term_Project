# Future import files below
import character_module
import grid
import sys
import tutorial


def get_user_choice():
    """
    Return the direction ("Up", "Down", "Left", "Right") the user inputs.

    :postcondition: obtain a direction ("Up", "Down", "Left", "Right") as a string from the user
    :return: the direction ("Up", "Down", "Left", "Right") as a string based on the user input
    """
    directions = {"Up", "Down", "Left", "Right"}
    while True:
        user_direction = input("Please enter Up, Down, Left, or Right to move: ").title().strip()
        if user_direction in directions:
            return user_direction


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


def validate_move(board, character, direction):
    """
    Return True if the character's coordinates after moving are in the board else return False.

    :param board: a dictionary of length rows * columns where (row, column) tuples containing integers of every possible
                  combination are the dictionary keys, and their values are descriptions of the locations as strings
    :param character: a dictionary containing "X-coordinate":value and "Y-coordinate":value
                      (as string:int within range [0, 4]), and "Current HP":value (as string:int of range [1, 5])
    :param direction: a string
    :precondition: board and character must be non-empty dictionaries
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate", and "Current HP" as strings
    :precondition: board must contain all possible combinations of (X-coordinate, Y-coordinate) keys as tuples
                   of ints within range [0, 4] and random location descriptions as values of strings
    :precondition: character (X-coordinate value, Y-coordinate value) must be in board
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :precondition: Current HP value must be an integer within range [1, 5]
    :precondition: direction must be a string
    :precondition: direction must be 'Up', 'Down', 'Left', or 'Right'
    :postcondition: leave board and character unmodified
    :postcondition: check if the character's coordinates after moving are in the board
    :return: True if the character's coordinates after moving are in the board else return False

    >>> small_board = {(0, 0): "Empty room", (0, 1): "Corridor", (0, 2): "Colonnade", (0, 3): "Empty room"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(small_board, test_character, 'Up')
    False
    >>> small_board = {(0, 0): "Empty room", (1, 0): "Corridor", (2, 0): "Colonnade", (3, 0): "Empty room"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(small_board, test_character, 'Down')
    True
    >>> small_board = {(4, 4): "Empty room", (4, 3): "Corridor", (4, 2): "Colonnade", (4, 1): "Empty room"}
    >>> test_character = {"Y-coordinate": 4, "X-coordinate": 3, "Current HP": 5}
    >>> validate_move(small_board, test_character, 'Right')
    True
    """
    # Leave character unmodified
    new_x_coordinate = character["X-coordinate"]
    new_y_coordinate = character["Y-coordinate"]
    # Update the coordinate depending on direction
    if direction == 'Up':
        new_y_coordinate -= 1
    elif direction == 'Down':
        new_y_coordinate += 1
    elif direction == 'Right':
        new_x_coordinate += 1
    elif direction == 'Left':
        new_x_coordinate -= 1
    # Return True if coordinates in board else False
    return (new_y_coordinate, new_x_coordinate) in board


def move_character(character, direction):
    """
    Increment or decrement the character's X- or Y-coordinate depending on the direction.

    :param character: a dictionary containing "X-coordinate":value and "Y-coordinate":value
                      (as string:int within range [0, 4]), and "Current HP":value (as string:int of range [1, 5])
    :param direction: a string
    :precondition: character must be a non-empty dictionary
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate", and "Current HP" as strings
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :precondition: Current HP value must be an integer within range [1, 5]
    :precondition: direction must be a string
    :precondition: direction must be 'Up', 'Down', 'Left', or 'Right'
    :postcondition: X- and Y-coordinates values are integers within range [0, 4]
    :postcondition: increment or decrement character's X- or Y-coordinate depending on the direction

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> move_character(test_character, 'Down')
    >>> test_character == {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
    True
    >>> test_character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5}
    >>> move_character(test_character, 'Right')
    >>> test_character == {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5}
    True
    >>> test_character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5}
    >>> move_character(test_character, 'Up')
    >>> test_character == {"Y-coordinate": 3, "Current HP": 5, "X-coordinate": 3}
    True
    """
    # Modify the original character dictionary coordinates
    if direction == 'Up':
        character["Y-coordinate"] -= 1
    elif direction == 'Down':
        character["Y-coordinate"] += 1
    elif direction == 'Right':
        character["X-coordinate"] += 1
    elif direction == 'Left':
        character["X-coordinate"] -= 1


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
        # Dialogue with Ragnar explaining battle mechanics and quick battle tutorial
        tutorial_npc = tutorial.tutorial_npcs((character["X-coordinate"], character["Y-coordinate"]))
        skip_tutorial = tutorial.tutorial_interaction(tutorial_npc, character)
        # Skip tutorial flag.
        if skip_tutorial:
            break
        while True:
            direction = get_user_choice()
            if validate_move(tutorial_zone, character, direction):
                move_character(character, direction)
                break
            else:
                print("You cannot move in that direction. Please enter a different direction.")
        in_tutorial = tutorial.exit_tutorial(character)
    # Character obtains basic items
    # Character moves out of tutorial zone
    # Make main board @STARTED
    # If character Current Health == 0, lost game dialogue and end game @DONE
    # Critical game loop around if Crystals >= 100 @DONE
        # Validate character direction
        # Move character
        # Check if there is an encounter
        # Randomize an encounter
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