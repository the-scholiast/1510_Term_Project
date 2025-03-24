"""
This module contains all necessary functionality for the tutorial zone.
"""


# Character interactions with NPCs in tutorial zone
def tutorial_npcs(character_location: (int, int)) -> str:
    # Tutorial Interactions
    tutorial_npc = {(1, 0): 'Darrow', (2, 0): 'Ragnar', (3, 0): 'Misaki'}
    # Return which NPC you are interacting with
    return tutorial_npc.get(character_location)


def get_npc_dialogue(npc: str, character_name: str) -> list:
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
    dialogue_counter = 0
    # Create a while loop to continue NPC dialogue and handle user input if needed
    while dialogue_counter < len(npc_dialogue):
        # Get current dialogue and input requirement
        npc_line = npc_dialogue[dialogue_counter][0]
        print(npc_line)
        dialogue_counter += 1
    pass


def main():
    """
    Drive the program.
    """
    character = {'Name': 'Test', 'Title': 'the Amateur', 'Level': 1, 'Health': 100, 'Strength': 15,
                 'Speed': 10, 'Luck': 5, 'Honour': 0, 'Ki': 50, 'Current Ki': 50, 'Spirit': 10, 'Experience': 0,
                 'Crystals': 0, 'Shards': 10, 'Current Health': 100, 'X-coordinate': 1, 'Y-coordinate': 0,
                 'Items': set()}
    tutorial_interaction("Darrow", character)


if __name__ == "__main__":
    main()