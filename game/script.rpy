# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Henry", color="#909090")
define cal = Character("Callie", color="#")
define chl = Character("Chloe", color="#8FEDF1")
define p = Character("???", color="#2e1e66")
define m = Character("Madeline", color="#")
define l = Character("Leon", color="#4663cf")
define r = Character("Rigby", color="#7cdf68")
define cas = Character("Casper", color="#")

$ relationship = 0

# The game starts here.

label start:
    scene bg entrance
    show henry at center

    # Start of dialogue

    "This is Henry"
    "He's one of the characters in the game"

    h "This is just to show how the game will look"
    h "Each character has unique colour codes for their name"

    chl "For example, Chloe's dialogue box will look like this"

    h "I can also be in different places on the screen"
    show henry at left with move 
    h "See?"
    h "Now we have room for someone else"
    show chloe at right
    chl "Heeeey!"

    h "I can also change sprites"
    show henry blush
    h "See...?"
    show henry

    h "The player can also choose a name"
    h "If they don't, one is assigned to them"

    #Let's player input their name
    $ player_name = renpy.input("What's your name???")
    $ player_name = player_name.strip()

    #If player doesn't choose a name, assign one for them
    if player_name == "":
        $ player_name="Player"

    h "Nice to meet you, %(player_name)s!"

    # Simple show of a dialogue option
    menu:
        "Here are some options:"

        "Option A":
            "You chose option A!"

        "Option B":
            "You chose option B!"

        "Option C":
            "You chose option C!"


    h "End of choices"
    h "This is mostly an engine test, not actual gameplay"
    h "This will all be replaced later"
    # This ends the game.

    return
