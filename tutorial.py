"""
This module contains all necessary functionality for the tutorial zone.
"""


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


# Character interactions with NPCs in tutorial zone
def tutorial_npcs(character_location: (int, int)) -> str:
    """
    Return the NPC the character is interacting with in the tutorial zone.

    :param character_location: a tuple of (row, column) coordinates in the tutorial zone
    :precondition: character_location must be a tuple of two integers
    :precondition: character_location must be one of: (0, 0), (1, 0), (2, 0), (3, 0)
    :return: a string representing the NPC at the given location

    >>> tutorial_npcs((0, 0))
    'Self'
    >>> tutorial_npcs((1, 0))
    'Darrow'
    >>> tutorial_npcs((2, 0))
    'Misaki'
    >>> tutorial_npcs((3, 0))
    'Ragnar'
    """
    # Tutorial Interactions
    tutorial_npc = {(0, 0): 'Self', (1, 0): 'Darrow', (2, 0): 'Misaki', (3, 0): 'Ragnar'}
    # Return which NPC you are interacting with
    return tutorial_npc[character_location]


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
            ("Obtain normal Crystals by defeating weaker monsters.", False),
            ("When you have 100 Crystals, the big bad Monster will be attracted to you, so be ready!", False),
            ("Now get out of my face! Maybe your friends have some more tips for you. ZEHAHAHAHAHA!", False)
        ],
        'Misaki': [
            ("Hey idiot. Since you really plan on doing this, I might as well inform you about this world.", True),
            ("You'll encounter a bunch of random monsters out in the world.", False),
            ("Sometimes you'll come across a merchant who'll offer you equipment to improve your damage"
             "or defense", False),
            ("Or maybe you'll find a hot spring to replenish you.", False),
            ("The [!] symbol on the map marks one of these three encounters.", False),
            ("Input the movement commands and move into one of these encounter symbols to initiate it.", False),
            ("Don't get yourself killed, okay? I bet Ragnar has some combat tips for you.", False)
        ],
        'Ragnar': [
            (f"Lo, {character_name}! I can't let you leave without you knowing how to defend yourself.", False),
            ("Don't let your Current Health fall to zero or you'll die!", False),
            ("Ki based attacks are more powerful but be careful as it drains your Current Ki.", False),
            ("Your weapon, Clavem, has three stances and each stance has their own set of attack moves.", False),
            ("You start with Bear stance and you'll gain another stance each level.", False),
            ("Combat in this world is turn-based. You'll need to choose your actions wisely.", False),
            ("You'll have three options in the battle menu: STANCE, ITEMS, FIGHT.", False),
            ("Any successful action will end your turn.", False),
            ("Defeat any monster by getting their Health to zero.", False),
            ("Every battle won will grant you experience. You need 100 experience to level up.", False),
            ("Every level up will give you a new stance, Health, Ki, and Damage.", False),
            ("We'll that's pretty much the basics. Now come back with that Crystal!.", False)
        ]
    }
    return npcs[npc]


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
        # Move to next dialogue
        return dialogue_counter + 1


def tutorial_interaction(npc, character) -> bool:
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
            character['X-coordinate'] = 4
            return True
        # If input is required after this dialogue
        if input_required:
            dialogue_counter = handle_input(npc, dialogue_counter)
        else:
            dialogue_counter += 1
    return False


def exit_tutorial(character) -> bool:
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    return character_location != (4, 0)