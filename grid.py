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


def main():
    print(make_board(5, 5))
    # print(tutorial_area(5))
    # board = make_board(5, 5)
    # print(check_encounter(test_character, board))


if __name__ == "__main__":
    main()