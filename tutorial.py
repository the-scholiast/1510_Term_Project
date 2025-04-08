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

    Each dialogue is a tuple containing two elements: a dialogue string,
    a boolean indicating whether user input is required for this dialogue line.

    :param npc: a string representing the name of the NPC ('Self', 'Darrow', 'Misaki', 'Ragnar')
    :param character_name: a string representing the character name
    :precondition: npc must be a string of ('Self', 'Darrow', 'Misaki', 'Ragnar')
    :precondition: character_name must be a string representing the character name
    :postcondition: obtain a list of dialogue tuples as (str, boolean) for the specified NPC
    :return: a list of dialogue tuples as (str, boolean) for the specified NPC

    >>> get_npc_dialogue('Self', 'Alice')[0]
    ("Today's the day! I'm going to become an official member of the Reaper's Guild!", False)
    >>> get_npc_dialogue('Darrow', 'Bob')[0]
    ('Finally awake eh Bob? So how about it. Do you need to prep or are you ready to go?', True)
    >>> get_npc_dialogue('Misaki', 'Charlie')[6]
    ("Don't get yourself killed, okay? I bet Ragnar has some combat tips for you.", False)
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
            ("Hey idiot. Since you really plan on doing this, I might as well inform you about this world.", False),
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


def handle_input(npc: str, dialogue_counter: int) -> int:
    """
    Manage dialogue progression with special handling for the first Darrow encounter.

    For the first Darrow dialogue, provides an option to skip the tutorial.
    For other cases, advance to the next dialogue.

    :param npc: a string representing the current NPC name
    :param dialogue_counter: an integer >= 0
    :postcondition: obtain the next dialogue index as an integer > 0 based on NPC and current dialogue position
    :return: the next dialogue index as an integer
    """
    # First tutorial NPC encounter. Option to skip tutorial.
    if npc == 'Darrow' and dialogue_counter == 0:
        user_response = input("Type 1 for tutorial or anything else to skip: ")
        if user_response.lower() != '1':
            # Skip to dialogue index 1
            return 1
        else:
            # Skip to dialogue index 2 for tutorial
            return 2
    else:
        # Move to next dialogue
        return dialogue_counter + 1


def tutorial_interaction(npc: str, character: dict) -> bool:
    """
    Manage the tutorial interaction between the character and an NPC.
    Return True if the tutorial is exited else False.

    :param npc: a string representing the NPC name
    :param character: a dictionary containing character data including 'Name', 'X-coordinate', and 'Y-coordinate'
    :precondition: npc must be a valid NPC name: 'Self', 'Darrow', 'Misaki', 'Ragnar'
    :precondition: character must contain 'Name':value as (str, str),
                   'X-coordinate' and 'Y-coordinate' keys with integer values between [0, 4]
    :postcondition: print the NPC's dialogue
    :postcondition: if NPC is Darrow and character skips, update character's location and exit tutorial
    :postcondition: if user input is required, handle it and update the dialogue counter accordingly
    :return: True if the tutorial is exited else False

    >>> test_character = {'Name': 'Hero', 'X-coordinate': 0, 'Y-coordinate': 0}
    >>> tutorial_interaction('Self', test_character)
    Self: Today's the day! I'm going to become an official member of the Reaper's Guild!
    Self: Wait what time is it?! Ahhh I'm late!
    Self: Hero enters the main room of the Guild.
    False
    >>> test_character = {'Name': 'Hero', 'X-coordinate': 1, 'Y-coordinate': 0}
    >>> tutorial_interaction('Darrow', test_character)
    Darrow: Finally awake eh Hero? So how about it. Do you need to prep or are you ready to go?
    Type 1 for tutorial or anything else to skip: 1
    Darrow: Well I guess as your leader, it's my duty to explain a few things.
    """
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


def exit_tutorial(character: dict) -> bool:
    """
    Return True if character did not reach end of tutorial zone else return False.

    :param character: a dictionary containing character data with 'X-coordinate' and 'Y-coordinate' as keys with
                      integer values between [0, 4]
    :precondition: character must be a dictionary containing character data with
                   'X-coordinate' and 'Y-coordinate' as keys with integer values between [0, 4]
    :postcondition: check if character coordinates != (4, 0)
    :return: True if character coordinates != (4, 0) else False

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> exit_tutorial(test_character)
    True
    >>> test_character = {'X-coordinate': 3, 'Y-coordinate': 0}
    >>> exit_tutorial(test_character)
    True
    >>> test_character = {'X-coordinate': 4, 'Y-coordinate': 0}
    >>> exit_tutorial(test_character)
    False
    """
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    return character_location != (4, 0)