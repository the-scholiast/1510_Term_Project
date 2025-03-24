"""
This module contains all necessary functionality for the tutorial zone.
"""


# Character interactions with NPCs in tutorial zone
def tutorial_npcs(character_location: (int, int)) -> str:
    # Tutorial Interactions
    tutorial_npc = {(0, 0): 'Self', (1, 0): 'Darrow', (2, 0): 'Misaki', (3, 0): 'Ragnar'}
    # Return which NPC you are interacting with
    return tutorial_npc.get(character_location)


def get_npc_dialogue(npc: str, character_name: str) -> list:
    """
    Return the dialogue options for a specific NPC.

    :return: a list of tuples (dialogue as a string, Boolean indicator if user input is required)
    """
    npcs = {
        'Self': [
            ("Today's the day! I'm going to become an official member of the Reaper's Guild!", False),
            ("Wait what time is it?! Ahhh I'm late!", False),
            (f"{character_name} enters the main room of the Guild.", False)
        ],
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


def handle_input(npc, dialogue_counter):
    # First tutorial NPC encounter. Option to skip tutorial.
    if npc == 'Darrow' and dialogue_counter == 0:
        user_response = input("Type 'Yes' for tutorial or 'No' to skip: ")
        if user_response.lower() == 'no':
            # Skip to dialogue index 1
            return 1
        else:
            # Skip to dialogue index 2 for tutorial
            return 2
    else:
        user_response = input("Type 'Yes' to repeat or 'No' to continue: ")
        # Repeat current dialogue
        if user_response.lower() == 'yes':
            return dialogue_counter
        # Move to next dialogue
        return dialogue_counter + 1


def tutorial_interaction(npc, character):
    name = character['Name']
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    # Get dialogue for the specified NPC
    npc_dialogue = get_npc_dialogue(tutorial_npcs(character_location), name)
    dialogue_counter = 0
    # Loop to continue NPC dialogue and handle user input if needed
    while dialogue_counter < len(npc_dialogue):
        # Get current dialogue and input requirement
        dialogue, input_required = npc_dialogue[dialogue_counter]
        # Display the dialogue
        print(f"{npc}: {dialogue}")
        # Exit tutorial dialogue if dialogue_counter == 1 and Darrow is NPC
        if npc == 'Darrow' and dialogue_counter == 1:
            return
        # If input is required after this dialogue
        if input_required:
            dialogue_counter = handle_input(npc, dialogue_counter)
        else:
            dialogue_counter += 1


def exit_tutorial(character) -> bool:
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    return character_location != (4, 0)


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