import random

"""
Contain the necessary functions and variables needed to create the 5x5 grid
"""


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


# Print board --> FIX DOCSTRING
def print_board(board, character):
    """
    Print the board, its borders, and the current character location.

    :param board:
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
    # Create the bottom border (same width as top)
    bottom_border = borders['bottom_left'] + (borders['horizontal'] * 25) + borders['bottom_right']
    print(bottom_border)


# Update board after character visits a location to mark it as visited
def mark_location_visited(board, character):
    # Get character's current location
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    # Mark the location as visited by replacing '[!]' with an empty string
    if board[character_location] == '[!]':
        board[character_location] = '   '
    return board