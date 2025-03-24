import random

"""
Contain the necessary functions and variables needed to create the 5x5 grid
"""


# For each grid position, randomly choose from a set of characters which represents different encounters.
def make_board(rows, columns):
    # Substitute '[!]' with a data structure to randomly select other characters as well
    grid = [['[!]' for column in range(columns)] for row in range(rows)]
    return grid


# Create tutorial zone
def tutorial_area(rows):
    # Linear grid for tutorial. There should be a skip option.
    tutorial_zone = ['[?]' for row in range(rows)]
    return tutorial_zone


# Character interactions with NPCs in tutorial zone
def tutorial_npcs(character_location):
    # Tutorial Interactions
    tutorial_npc = {(1, 0): 'Darrow', (2, 0): 'Ragnar', (3, 0): 'Misaki'}
    # Return which NPC you are interacting with
    return tutorial_npc.get(character_location)


def get_npc_dialogue(npc, character_name):
    """
    Return the dialogue options for a specific NPC.

    :return: a list of tuples (dialogue as a string, Boolean indicator if user input is required)
    """
    npcs = {
        'Darrow': [
            (f'Finally awake eh {character_name}? So how about it. Do you need to prep or are you ready to go?', True),
            ("ZEHAHAHAHAHAHA! That's the spirit! Go bring me the head of a worthy beast!", False),
            ("Well I guess as your leader, it's my duty to explain a few things.", False),
            ("Your goal is to defeat a Calamity-Level Monster and bring me its rare Crystal.", False),
            ("All monsters drop Crystals when they die, but we're only after the rarest!", False),
            ("Obtain normal Crystals by defeating weaker monsters, from the environment, or civilians.", False),
            ("When you have 100 Crystals, the big bad Monster will be attracted to you, so be ready!", False),
            ("Now get out of my face! Maybe your friends have some more tips for you.", False)],
        'Misaki': [
            ("Hey idiot. Since you really plan on doing this, I might as well inform you about this world.", True),
            ("Combat in this world is turn-based. You'll need to choose your actions wisely.", False)],
        'Ragnar': []
    }
    return npcs.get(npc)


def tutorial_interaction(npc, character):
    name = character['Name']
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    # Get dialogue for the specified NPC
    npc_dialogue = get_npc_dialogue(tutorial_npcs(character_location), name)
    pass


def main():
    print(make_board(5, 5))
    print(tutorial_area(5))


if __name__ == "__main__":
    main()
