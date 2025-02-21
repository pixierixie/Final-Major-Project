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
define cas = Character("Casper", color="#911111")
define u = Character("???")
define player = Character("[player_name]")

#unused variable for now
$ relationship = 0

# The game starts here.

label start:
    scene bg blank
    
    #Let's player input their name
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()

    #If player doesn't choose a name, assign one for them
    if player_name == "":
        $ player_name="Player"

    "Nice to meet you, %(player_name)s!"

    scene bg entrance
    with fade
    # Start of dialogue
    player "Ugh, I seriously need to get a new job."
    player "No raise in five years, yet double the responsibility since Kate quit."
    player "And all I have to show for it is shitty ramen and student loans."
    player "And apparently talking to myself like a crazy person."
    "I go into the bedroom, peeling off the layers of my work clothes and changing into something much more comfortable."
    
    scene bg singlebedroom
    with blinds
    "I turn on my PC, ready to unwind with the new game that just came out."
    "I press the power button and…"
    "Nothing."
    player "Shit."
    "After a few minutes of pulling and plugging various cables, the PC still won’t turn on."
    player "Must be something wrong with the parts…"
    "I pick up some tools and start to remove the case."

    scene bg singlebedroom
    with fade
    player "The fuck..?"
    "As I blink away the blinding light, trying to get my bearings, several voices can be heard."
    u "Oh no, did we kill them?!"
    u "Of course not. Look, they are fine."
    u "If they ain’t, they’ll come to in like… a day or so."
    "Three faces are peering down at me."
    "One of them smiles at me."
    show chloe 
    u "Hey! Glad you’re okay, you scared us for a second!"
    show chloe at left with move
    show henry at right
    u "Scared you, you mean."
    u "You were worried too!"
    "The silver haired man huffs, but his eyes remain on me."
    show henry at center with move
    show casper at right
    "The quiet one spares a glance, before looking away."
    "The girl leans close and studies my face."
    u "A little pale… You should drink something!"
    hide chloe
    show henry at left with move
    "She rushes out of the room before anyone has a chance to stop her."
    "The silver haired man sighs and pinches the bridge of his nose."
    u "Apologies for her. She has a tendency to be a bit… scattered."
    u "Par for the course with coolant, I am afraid."
    "He must notice my confused expression, because his own changes."
    show henry blush
    u "You are cute when you are confused…"
    show henry
    u "Allow me to introduce myself."
    h "I am Henry, your hard drive."
    player "My... hard drive?"
    h "Correct."


    return
