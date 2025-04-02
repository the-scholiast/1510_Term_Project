import random

"""
Contain the necessary functions and variables needed to create the 5x5 grid
"""
# TEST CHARACTER --> REMOVE WHEN DONE
test_character = {'Name': 'Tester', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Strength': 15,
                  'Speed': 10, 'Luck': 5, 'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Spirit': 10, 'Experience': 0,
                  'Crystals': 0, 'Shards': 10, 'Current Health': 100, 'X-coordinate': 1, 'Y-coordinate': 0,
                  'Items': set()}


# For each grid position, randomly choose from a set of characters which represents different encounters.
def make_board(rows, columns):
    # Substitute '[!]' with a data structure to randomly select other characters as well
    grid = {(row, column): '[!]' for column in range(columns) for row in range(rows)}
    return grid


# Check if character movement will lead to random encounter '[!]'
def check_encounter(character, board):
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    board_symbol = board[character_location[0]][character_location[1]]
    return board_symbol == '[!]'


# Create tutorial zone
def tutorial_area():
    # Linear grid for tutorial. There should be a skip option.
    tutorial_zone = {(row, column): '[?]' for row in range(1) for column in range(5)}
    return tutorial_zone


# Print board
def print_board(rows, columns, character):
    """
    Print the board, its borders, and the current character location.

    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :param character: a dictionary containing "X-coordinate":value and "Y-coordinate":value
                      (as string:ints within range [0, 4]), and "Current HP":value (as string:int of range [1, 5])
    :precondition: both rows and columns must integers == 5
    :precondition: character must be a non-empty dictionary
    :precondition: character must contain the keys "X-coordinate", "Y-coordinate", and "Current HP" as strings
    :precondition: X- and Y-coordinates values must be integers within range [0, 4]
    :precondition: Current HP value must be an integer within range [1, 5]
    :postcondition: leave character unmodified
    :postcondition: print the board and its borders (as "X") using rows and columns as the grid,
                    also print the current location of the character (as "#")
    """
    # Add one to coordinates to account for outer border
    character_x = character["X-coordinate"] + 1
    character_y = character["Y-coordinate"] + 1

    # Create total dimensions including borders
    total_rows = rows + 2
    total_columns = columns + 2

    # Print top border
    print("X " * total_columns)

    # Print middle rows with side borders
    for row in range(1, total_rows - 1):
        row_string = "X "
        for column in range(1, total_columns - 1):
            # Print character location as "#" or empty space
            if row == character_y and column == character_x:
                row_string += "# "
            else:
                row_string += "  "
        row_string += "X"
        print(row_string)

    # Print bottom border
    print("X " * total_columns)

print_board(5, 5, test_character)