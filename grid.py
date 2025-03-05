# Contain the necessary functions and variables needed to create the 5x5 grid

# For each grid position, randomly choose from a set of characters which represents different encounters.
def make_board(row, column):
    # Substitute '[!]' with a data structure to randomly select other characters as well
    grid = [['[!]' for column_count in range(column)] for row_count in range(row)]
    return grid

# Given the grid character, randomly choose from an element from within its group type.
# Weighted system to guarantee certain numbers of NPCs/Monsters
def obtain_random_npc(group_type):
    """

    :param group_type:
    :return:
    >>> obtain_random_npc('[!]')
    Werewolf
    >>> obtain_random_npc('[!]')
    Civilian
    >>> obtain_random_npc('[!]')
    Merchant
    """
    pass


def main():
    print(make_board(5, 5))


if __name__ == "__main__":
    main()