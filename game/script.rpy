# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Henry", color="#767676", callback = name_callback, cb_name = "Henry")
define cal = Character("Callie", color="#")
define chl = Character("Chloe", color="#4CA4A9", callback = name_callback, cb_name = "Chloe")
define p = Character("???", color="#2e1e66")
define m = Character("Madeline", color="#")
define l = Character("Leon", color="#4663cf")
define r = Character("Rigby", color="#7cdf68")
define cas = Character("Casper", color="#bd453c", callback = name_callback, cb_name = "Casper")

define uh = Character("???", color="#767676",  callback = name_callback, cb_name = "Henry")
define uchl = Character("???", color="#4CA4A9", callback = name_callback, cb_name = "Chloe")
define ucas = Character("???", color="#bd453c", callback = name_callback, cb_name = "Casper")

define player = Character("[player_name]", color ="#FFFFFF", callback = name_callback, cb_name = None)

##Narrator is defined in case the characters weren't greyed out when they should be
define narrator = Character(name=None, callback = name_callback, cb_name = None)

##Setup for auto highlight
image henry:
    "images/henry.png"
    function SpriteFocus('Henry')
image henry angry:
    "images/henry angry.png"
    function SpriteFocus('Henry')
image henry blush:
    "images/henry blush.png"
    function SpriteFocus('Henry')
image henry crazy:
    "images/henry crazy.png"
    function SpriteFocus('Henry')
image henry upset:
    "images/henry upset.png"
    function SpriteFocus('Henry')
image henry yandere:
    "images/henry yandere.png"
    function SpriteFocus('Henry')


image chloe:
    "images/chloe.png"
    function SpriteFocus('Chloe')
image chloe blush:
    "images/chloe blush.png"
    function SpriteFocus('Chloe')
image chloe drain:
    "images/chloe drain.png"
    function SpriteFocus('Chloe')
image chloe glitch:
    "images/chloe glitch.png"
    function SpriteFocus('Chloe')
image chloe upset:
    "images/chloe upset.png"
    function SpriteFocus('Chloe')


image casper:
    "images/casper.png"
    function SpriteFocus('Casper')
image casper angry:
    "images/casper angry.png"
    function SpriteFocus('Casper')
image casper blush:
    "images/casper blush.png"
    function SpriteFocus('Casper')
image casper glitch:
    "images/casper glitch.png"
    function SpriteFocus('Casper')
image casper gum:
    "images/casper gum.png"
    function SpriteFocus('Casper')



# The game starts here.

label start:
    scene bg blank
    
    #Let's player input their name
    $ player_name = renpy.input("What's your name?", length=10, exclude='{1,2,3,4,5,6,7,8,9,0,.,-,+,;:,/,?,`,¬,@,#,~,[,],=,*,!,",£,$,%,^,&,(,),_,|,\,<,>}')
    $ player_name = player_name.strip()

    #If player doesn't choose a name, assign one for them
    if player_name == "":
        $ player_name="Player"

    "You have put: [player_name]."
    "Is this correct?"
    menu:
        "Yes":
            "Nice to meet you, [player_name]!"
            jump prologue
        "No":
            jump start



label prologue:
    scene bg entrance

    with fade
    #Play audio
    play music "vntrack19.mp3"

    # Start of dialogue
    player "Ugh, I seriously need to get a new job."
    player "No raise in five years, yet double the responsibility since Kate quit."
    player "And all I have to show for it is shitty ramen and student loans."
    player "And apparently talking to myself like a crazy person."
    "You enter the bedroom, peeling off the layers of your work clothes and changing into something much more comfortable."
    
    scene bg singlebedroom
    with blinds
    "You turn on myour PC, ready to unwind with the new game that just came out."
    "You press the power button and..."
    "Nothing."
    player "Shit."
    scene bg singlebedroom
    with fade
    "After a few minutes of pulling and plugging various cables, the PC still won't turn on."
    player "Must be something wrong with the parts..."
    "You pick up some tools and start to remove the case."

    scene bg singlebedroom
    with pixellate
    player "The fuck...?"
    narrator "As you shake off the electricity running up your arm, you can hear several voices in the room."
    uchl "Oh no, did we kill them?!"
    uh "Of course not. Look, they are fine."
    ucas "If they ain't, they'll come to in like... a day or so."
    "Three faces are peering down at you."
    "One of them smiles at you."
    show chloe
    uchl "Hey! Glad you're okay, you scared us for a second!"
    show chloe at left with move
    show henry at right
    uh "Scared you, you mean."
    uchl "You were worried too!"
    narrator "The silver haired man huffs, but his eyes remain on you."
    show henry at center with move
    show casper at right
    narrator "The quiet one spares a glance, before looking away."
    "The girl leans close and studies your face."
    uchl "A little pale... You should drink something!"
    hide chloe
    show henry at left with move
    "She rushes out of the room before anyone has a chance to stop her."
    "The silver haired man sighs and pinches the bridge of his nose."
    uh "Apologies for her. She has a tendency to be a bit... scattered."
    uh "Par for the course with coolant, I am afraid."
    "He must notice your confused expression, because his own changes."
    show henry blush
    #This line is smaller, grey and autoskips
    uh "{size=-2}{color=#6d6d6d}You are cute when you are confused...{w=0.3}{nw}{/size}{/color}"
    show henry
    uh "Allow me to introduce myself."
    h "I am Henry, your hard drive."
    player "My... hard drive?"
    h "Correct."
    h "And you are aware of an issue with the Personal Computer, hence why we stand before you now."
    h "Perhaps you should get to know us, so you can find out which one of us is the part causing you such...issue."
    player "So you're like... my actual PC?"
    ucas "Yep. In the flesh. Or... metal, I guess."

    menu:
        "Get out of my house!":
            jump Bad_End_1
            #Jumps to the Prologue Bad End

        "I guess you can stay...":
            h "Splendid. Now then, let us continue with introductions."
            "Henry looks at the person next to him expectantly."
            ucas "Hm? Oh. Yeah."
            cas "Name's Casper. CPU, if you're interested."
            player "So the girl is...?"
            "A blur of blue bursts into the room."

            show henry at center with move
            show chloe at left
            chl "Chloe!! I'm your coolant! Here ya go!"
            "She hands you a glass of water, spilling some in her excitement to hand it to you."
            player "Right. I'm-"
            h "[player_name]. Yes, we know."
            h "We are your Personal Computer, remember?"
            player "Please just call it a PC..."
            cas "He's like physically allergic to that."
            cas "Some kind of directory thing, he has a habit of it."
            show henry angry
            h "Can you fault me? All the files would be {i}horribly{/i} arranged if I used abbreviations."
            chl "Come on, Casper, stop teasing him."
            chl "Let's all go and sit down, yeah? We can have a proper chat."
            "Chloe takes your hand and leads you out into the living room."

            scene bg lounge
            with blinds
            "You sit down on the sofa, trying to wrap your head around what was happening."
            show chloe upset
            chl "You look overwhelmed still..."
            show chloe at left with move
            show henry at right
            h "I think it is best that you collect yourself first."
            h "We will be around when you wish to speak with us."
            chl "I'll go hang out in the kitchen, I'm sure there's something I can do in there."
            hide chloe
            show henry at center with move
            "Chloe is already bouncing off again."
            show henry at left with move
            show casper at right
            cas "I guess I'll just go chill in like the dining room?"
            "Casper languidly makes their way out, yawning and stretching as they go."
            hide casper
            show henry at center with move
            h "I shall remain here."
            "Where would you like to go?"
            menu:
                "Living Room - Henry":
                    jump Henry_Route
                    #This is is a seperate script called henryscript.rpy
                    stop music
            return

label Bad_End_1:
    scene bg singlebedroom
    show henry upset at left
    show casper angry at right
    h "Oh. You do not even want to try?"
    player "No, I don't know who you people are."
    player "Get out of my house. Right now."
    "The two just stare at you in shock."
    "The girl bounces in, glass of water in hand."
    show henry upset at center with move
    show chloe upset at left
    uchl "Whoa, tension."
    uchl "What's going on?"
    player "Get out of my house!"
    "The three exchange glances before quietly leaving the room, and hopefully, the building."
    hide henry
    hide casper
    hide chloe
    "After a few minutes of trying to process what the fuck just happened, you go back to repairing your PC."
    player "Where the hell did my CPU go...?"
    scene bg blank
    "{b}-Bad Ending: What, it just grew legs and walked away?-{/b}"