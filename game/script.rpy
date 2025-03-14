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
define cas = Character("Casper", color="#bd453c")

define uh = Character("???", color="#909090")
define uchl = Character("???", color="#8FEDF1")
define ucas = Character("???", color="#bd453c")
define player = Character("[player_name]", color ="#c86bae")


# The game starts here.

label start:
    scene bg blank
    
    #Let's player input their name
    $ player_name = renpy.input("What's your name?", length=20, exclude='{1,2,3,4,5,6,7,8,9,0,.,-,+,;:,/,?,`,¬,@,#,~,[,],=,*,!,",£,$,%,^,&,(,),_,|,\,<,>}')
    $ player_name = player_name.strip()

    #If player doesn't choose a name, assign one for them
    if player_name == "":
        $ player_name="Player"

    "Nice to meet you, [player_name]!"

    scene bg entrance
    with fade
    #Play audio
    play music "vntrack19.mp3"

    # Start of dialogue
    player "Ugh, I seriously need to get a new job."
    player "No raise in five years, yet double the responsibility since Kate quit."
    player "And all I have to show for it is shitty ramen and student loans."
    player "And apparently talking to myself like a crazy person."
    "I enter the bedroom, peeling off the layers of my work clothes and changing into something much more comfortable."
    
    scene bg singlebedroom
    with blinds
    "I turn on my PC, ready to unwind with the new game that just came out."
    "I press the power button and..."
    "Nothing."
    player "Shit."
    scene bg singlebedroom
    with fade
    "After a few minutes of pulling and plugging various cables, the PC still won’t turn on."
    player "Must be something wrong with the parts..."
    "I pick up some tools and start to remove the case."

    scene bg singlebedroom
    with pixellate
    player "The fuck..?"
    "As I shake off the electricity running up my arm, I can hear several voices in the room."
    uchl "Oh no, did we kill them?!"
    uh "Of course not. Look, they are fine."
    ucas "If they ain’t, they’ll come to in like... a day or so."
    "Three faces are peering down at me."
    "One of them smiles at me."
    show chloe
    uchl "Hey! Glad you’re okay, you scared us for a second!"
    show chloe at left with move
    show henry at right
    uh "Scared you, you mean."
    uchl "You were worried too!"
    "The silver haired man huffs, but his eyes remain on me."
    show henry at center with move
    show casper at right
    "The quiet one spares a glance, before looking away."
    "The girl leans close and studies my face."
    uchl "A little pale... You should drink something!"
    hide chloe
    show henry at left with move
    "She rushes out of the room before anyone has a chance to stop her."
    "The silver haired man sighs and pinches the bridge of his nose."
    uh "Apologies for her. She has a tendency to be a bit... scattered."
    uh "Par for the course with coolant, I am afraid."
    "He must notice my confused expression, because his own changes."
    show henry blush
    #This line is smaller, grey and autoskips
    uh "{size=-2}{color=#6d6d6d}You are cute when you are confused...{w=0.3}{nw}{/size}{/color}"
    show henry
    uh "Allow me to introduce myself."
    h "I am Henry, your hard drive."
    player "My... hard drive?"
    h "Correct."
    h "And you are aware of an issue with the Personal Computer, hence why we stand before you now."
    h "Perhaps you should get to know us, so you can find out which one of us is the part causing you such…issue."
    player "So you’re like… my actual PC?"
    ucas "Yep. In the flesh. Or... metal, I guess."

    menu:
        "Get out of my house":
            jump Bad_End_1
            

        "I guess you can stay...":
            h "Splendid. Now then, let us continue with introductions."
            "Henry looks at the person next to him expectantly."
            ucas "Hm? Oh. Yeah."
            cas "Name’s Casper. CPU, if you’re interested."
            player "So the girl is...?"
            "A blur of blue bursts into the room."

            show henry at center with move
            show chloe at left
            chl "Chloe!! I’m your coolant! Here ya go!"
            "She hands me a glass of water, spilling some in her excitement to hand it to me."
            player "Right. I’m-"
            h "[player_name]. Yes, we know."
            h "We are your Personal Computer, remember?"
            player "Please just call it a PC..."
            cas "He’s like physically allergic to that."
            cas "Some kind of directory thing, he has a habit of it."
            show henry angry
            h "Can you fault me? All the files would be {i}horribly{/i} arranged if I used abbreviations."
            chl "Come on, Casper, stop teasing him."
            chl "Let’s all go and sit down, yeah? We can have a proper chat."
            "Chloe takes my hand and leads me out into the living room."

            scene bg lounge
            with blinds
            "Currently there is only one route, the end of the prologue is unfinished."
            "Select your route."
            menu:
                "Henry Route":
                    jump Henry_Route
                    stop music
            return

label Bad_End_1:
    scene bg singlebedroom
    show henry upset at left
    show casper angry at right
    h "Oh. You do not even want to try?"
    player "No, I don’t know who you people are."
    player "Get out of my house. Right now."
    "The two just stare at me in shock."
    "The girl bounces in, glass of water in hand."
    show henry upset at center with move
    show chloe upset at left
    uchl "Whoa, tension."
    uchl "What’s going on?"
    player "Get out of my house!"
    "The three exchange glances before quietly leaving the room, and hopefully, the building."
    hide henry
    hide casper
    hide chloe
    "After a few minutes of trying to process what the fuck just happened, I go back to repairing my PC."
    player "Where the hell did my CPU go...?"
    scene bg blank
    "{b}-Bad Ending: What, it just grew legs and walked away?-{/b}"