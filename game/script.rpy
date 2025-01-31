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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg entrance

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show henry

    # These display lines of dialogue.

    h "You've created a new Ren'Py game."

    h "Once you add a story, pictures, and music, you can release it to the world!"

    #Let's player input their name
    $ player_name = renpy.input("What's your name???")
    $ player_name = player_name.strip()

    #If player doesn't choose a name, assign one for them
    if player_name == "":
        $ player_name="LMAO"


    h "Nice to meet you, %(player_name)s!"



    # This ends the game.

    return
