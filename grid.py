import random

"""
Contain the necessary functions and variables needed to create the 5x5 grid
"""


# For each grid position, randomly choose from a set of characters which represents different encounters.
def make_board(rows, columns):
    # Substitute '[!]' with a data structure to randomly select other characters as well
    grid = [['[!]' for column in range(columns)] for row in range(rows)]
    return grid


def tutorial_area(rows):
    # Linear grid for tutorial. There should be a skip option.
    row = ['[?]' for row in range(rows)]
    return row


def main():
    print(make_board(5, 5))
    print(tutorial_area(5))


if __name__ == "__main__":
    main()