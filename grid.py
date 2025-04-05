import random

"""
Contain the necessary functions and variables needed to create the 5x5 game board.
"""


# For each grid position, randomly choose from a set of characters which represents different encounters.
def make_board(rows: int, columns: int) -> dict:
    """
    Create a game board represented as a dictionary with coordinates as keys.

    Each coordinate contains an encounter marker '[!]'.
    The board uses (row, column) tuple coordinates as keys and encounter markers as values.

    :param rows: a positive integer == 5
    :param columns: a positive integer == 5
    :precondition: rows and columns must be positive integers == 5
    :postcondition: create a dictionary with (row, column):"[!]" (as a tuple with 0<=ints<5:string)
    :return: a dictionary with (row, column):"[!]" (as a tuple with 0<=ints<5:string)

    >>> actual_board = make_board(5, 5)
    >>> expected_board = {(0, 0): '[!]', (1, 0): '[!]', (2, 0): '[!]', (3, 0): '[!]', (4, 0): '[!]', (0, 1): '[!]',
    ... (1, 1): '[!]', (2, 1): '[!]', (3, 1): '[!]', (4, 1): '[!]', (0, 2): '[!]', (1, 2): '[!]', (2, 2): '[!]',
    ... (3, 2): '[!]', (4, 2): '[!]', (0, 3): '[!]', (1, 3): '[!]', (2, 3): '[!]', (3, 3): '[!]', (4, 3): '[!]',
    ... (0, 4): '[!]', (1, 4): '[!]', (2, 4): '[!]', (3, 4): '[!]', (4, 4): '[!]'}
    >>> actual_board == expected_board
    True
    """
    board = {(row, column): '[!]' for column in range(columns) for row in range(rows)}
    return board


# Check if character movement will lead to random encounter '[!]'
def check_encounter(character: dict, board: dict):
    """
    Determine if the character's current location contains an encounter marker '[!]'.

    :param character: a dictionary containing all character attributes including name, stats,
                      position, inventory, equipment, and status effects
    :param board: a dictionary with (row, column):"[!]" (as a tuple with 0<=ints<5:string)
    :precondition: character must contain 'X-coordinate' and 'Y-coordinate' integer keys between [0, 4]
    :precondition: board must be a dictionary with (row, column) tuple keys (as ints == 5)
    :precondition: board must contain '[!]' or '   ' as values
    :postcondition: determine if the character's current location has an encounter
    :postcondition: leave character unmodified
    :postcondition: replace '[!]' value with "   " if character's location equals its key
    :return: True if an encounter '[!]' is present at the character's location else False

    >>> test_character = {'X-coordinate': 1, 'Y-coordinate': 2}
    >>> test_board = {(2, 1): '[!]', (2, 2): '   '}
    >>> check_encounter(test_character, test_board)
    True
    >>> test_character = {'X-coordinate': 2, 'Y-coordinate': 2}
    >>> check_encounter(test_character, test_board)
    >>> test_board = {(2, 1): '[!]', (2, 2): "   "}
    False
    """
    character_location = (character['Y-coordinate'], character['X-coordinate'])
    # Get either encounter marker '[!]' or whitespace
    board_location = board.get(character_location)
    return board_location == '[!]'


# Create tutorial zone
def tutorial_area() -> dict:
    """
    Create a linear board for the tutorial section of the game.

    Generates a 1x5 board where each position contains a tutorial marker '[?]'.

    :postcondition: generate a dictionary with (row, column) tuple keys (as int = 1, int = 5) and '[?]' string values
    :return: a dictionary representing the tutorial zone
             with (row, column) tuple keys (as int = 1, int = 5) and '[?]' string values

    >>> actual = tutorial_area()
    >>> expected = {(0, 0): '[?]', (0, 1): '[?]', (0, 2): '[?]', (0, 3): '[?]', (0, 4): '[?]'}
    >>> actual == expected
    True
    """
    # Linear board for tutorial.
    tutorial_zone = {(row, column): '[?]' for row in range(1) for column in range(5)}
    return tutorial_zone


# Print board
def print_board(board: dict, character: dict):
    """
    Print the board, its borders, and the current character location.

    :param board: a dictionary with (row, column):"[!]" (as a tuple with 0<=ints<5:string)
    :param character: a dictionary containing all character attributes including name, stats,
                      position, inventory, equipment, and status effects
    :precondition: board must be a non-empty dictionary
    :precondition: board must contain (row, column):"[!]" (as a tuple with 0<=ints<5:string)
    :precondition: character must be a non-empty dictionary
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate"
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :postcondition: leave character and board unmodified
    :postcondition: print the board and its borders using border Unicode and
                    print the current location of the character (as "♦")

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> test_board = make_board(5, 5)
    >>> print_board(test_board, test_character)
    ┌─────────────────────────┐
    │  ♦   [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    └─────────────────────────┘
    >>> test_character = {"X-coordinate": 4, "Y-coordinate": 4}
    >>> test_board = make_board(5, 5)
    >>> print_board(test_board, test_character)
    ┌─────────────────────────┐
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]   ♦  │
    └─────────────────────────┘
    >>> test_character = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> test_board = make_board(5, 5)
    >>> print_board(test_board, test_character)
    ┌─────────────────────────┐
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]   ♦   [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    │ [!]  [!]  [!]  [!]  [!] │
    └─────────────────────────┘
    """
    # Define border characters
    borders = {
        'top_left': '┌',
        'top_right': '┐',
        'bottom_left': '└',
        'bottom_right': '┘',
        'horizontal': '─',
        'vertical': '│',
        'player': '♦'
    }
    # Get character position
    player_x, player_y = character["X-coordinate"], character["Y-coordinate"]
    # Get board dimensions
    rows = max(row for row, _ in board.keys()) + 1
    columns = max(column for _, column in board.keys()) + 1
    # Create the top border
    top_border = borders['top_left'] + (borders['horizontal'] * 25) + borders['top_right']
    print(top_border)
    # Print each row
    for row in range(rows):
        row_string = borders['vertical']
        for column in range(columns):
            # Display what is at each location
            if row == player_y and column == player_x:
                display_location = f"  {borders['player']}  "
            else:
                display_location = f" {board[(row, column)]} "
            row_string += display_location
        # Add the right border
        row_string += borders['vertical']
        print(row_string)
    # Create the bottom border
    bottom_border = borders['bottom_left'] + (borders['horizontal'] * 25) + borders['bottom_right']
    print(bottom_border)


# Update board after character visits a location to mark it as visited
def mark_location_visited(board: dict, character: dict):
    """
    Replace '[!]' or '[?]' with "   " for the board's value using character coordinates as the key.

    :param board: a dictionary with (row, column):"[!]" (as a tuple with 0<=ints<5:string)
    :param character: a dictionary containing all character attributes including name, stats,
                      position, inventory, equipment, and status effects
    :precondition: board must be a non-empty dictionary
    :precondition: board must contain (row, column):"[!]" (as a tuple with 0<=ints<5:string)
    :precondition: character must be a non-empty dictionary
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate"
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :postcondition: leave character unmodified
    :postcondition: replace '[!]' or '[?]' with "   " for the board's value using character coordinates as the key

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> small_board = {(0, 0): '[!]', (1, 0): '[!]', (2, 0): '[!]', (3, 0): '[!]', (4, 0): '[!]'}
    >>> mark_location_visited(small_board, test_character)
    >>> expected = {(0, 0): '   ', (1, 0): '[!]', (2, 0): '[!]', (3, 0): '[!]', (4, 0): '[!]'}
    >>> small_board == expected
    True
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 4}
    >>> small_board = {(0, 0): '[!]', (1, 0): '[!]', (2, 0): '[!]', (3, 0): '[!]', (4, 0): '[!]'}
    >>> mark_location_visited(small_board, test_character)
    >>> expected = {(0, 0): '[!]', (1, 0): '[!]', (2, 0): '[!]', (3, 0): '[!]', (4, 0): "   "}
    >>> small_board == expected
    True
    """
    # Get character's current location
    character_location = (character['Y-coordinate'], character['X-coordinate'])
    # Mark the location as visited by replacing '[!]' with an empty string
    if board[character_location] == '[!]':
        board[character_location] = '   '
    elif board[character_location] == '[?]':
        board[character_location] = '   '