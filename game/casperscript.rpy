#Casper's route script file

label Casper_Route:
    $ casgoodpoint = 0
    $ casbadpoint = 0

    scene bg lounge
    "You decide to head to the dining room to see Casper."

    scene bg dining
    with blinds
    play music ["Blue and Black.mp3", "Shove An Ice Cube All The Way.mp3", "Jorts Season.mp3", "Goggles On.mp3"]
    "Casper looks up from a handheld console."
    show casper at center
    cas "Sick, you're here."
    cas "Nice games you got on here."
    "Casper continues playing."
    player "What are you playing?"
    cas "Moonfrost Hollow."
    cas "Started a new farm, don't worry."
    "You sit next to them and watch for a while."

    menu:
        "Suggest some ideas.":
            $ casgoodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship") 
            player "You could add a sprinkler here so these crops get watered as well."
            cas "Good shout."
            "Casper takes your advice and starts to build up the farm."
            "You work together and in no time at all, the farm is running perfectly."

        "Criticise their farm.":
            $ casbadpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            player "You farm is looking a bit shit."
            "Casper ignores you and continues playing."
            "They ignore all of your other attempts at advice, even doing the exact opposite."

    cas "Should we play something else? You got a few multiplayer games on here."
    player "Sure, how about something faster paced? I got a fighting game that I don't wanna fight against the CPU for."
    cas "..."
    cas "That's me."
    "Casper's lips curl into an amused smile."
    show casper blush
    cas "You forgot."
    "You nod, embarrassed."
    player "You know what I meant, I want to play against someone...real."
    cas "Casper chuckles to themselves, before booting up the game."
    "They hand you a set of controllers and the game begins."
    hide casper
    "It's a tight match, you're both equal in skill."
    "You notice that Casper starts to shift in their seat."
    show casper gum
    player "Casper, you good?"
    cas "Yeah. Just need to overclock a bit, you're good at this."
    player "Overclock? Isn't that... dangerous?"
    cas "Just a little bit is fine. Focus on the game."
    "The round finishes and Casper wins by a small margin."
    cas "GG. Guess you still can't win against the CPU."
    player "Guess not..."
    player "One more round?"
    "Casper nods and navigates the menu screen."

    menu:
        "Overclock Casper.":
            $ casbadpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            player "Hey, do the overclock thing again. It made the game super intense."
            cas "A thrill seeker? Damn, alright."
            "As you play, you notice Casper moving more, unable to sit still."
            "Their once quiet mutters turn into out loud once sided conversations as they strategise against you."

        "Tell Casper to take it easy.":
            $ casgoodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship") 
            player "Take it easy this round, yeah?"
            player "I don't wanna break you too much."
            cas "Hm? Yeah, okay."
            "As you play, Casper remains the same as they did in the last round."

    "This time, you win the round by a hair."
    cas "Congrats, mate. I knew you could do it."
    "Casper seems happy for you and goes to start up one more round."
    cas "Best of three?"
    player "Hell yeah!"
    "You start another round, your characters flashing across the screen with bright visuals and loud voice lines."
    "You sneak a glimpse at Casper."
    show casper glitch
    play music ["Fish Tank Bubbles.mp3"]
    "They're beyond thrilled, chewing on their gum as they concentrate on countering your moves."
    "It looks like they might win."
    "They start moving around restlessly on their chair, their fingers moving faster across the buttons, their eyes darting around the screen."

    menu:
        "Warn Casper.":
            $ casgoodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship") 
            player "Hey, Casper?"
            cas "Yeah?"
            player "You're getting a bit restless. Maybe you should calm down a bit?"
            "Casper stops for a second and pauses the game."
            "They take a few deep breaths before continuing the game, less agitated than before."

        "Let Casper overlock.":
            $ casbadpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            "You ignore Casper's frantic behaviour, thinking this could give you an advantage."
            "Casper only gets more agitated, shifting and muttering as they get absorbed into the game."

    "You continue to play round after round, both of you winning and losing in equal measure."
    cas "Fuck!"

    #Decides if the player is on the good or bad ending route
    if casbadpoint >= 2:
        jump Casper_Bad_End
    if casgoodpoint >= 2:
        jump Casper_Good_End

label Casper_Bad_End:
    scene bg dining
    play music "Somebody Said Youre An Owl.mp3"
    show casper angry
    cas "{sc=[2]}I can't believe I lost to you again!{/sc}"
    "Casper looks furious."
    "Volatile."
    cas "I mean, seriously!"
    cas "That cheesy move?!"
    cas "You can't just spam that fire attack again and again and again!"
    player "Hey... It's just a game. I'm sorry, but those are the mechanics."
    cas "Oh fuck off."
    cas "{bt=2}{sc=1}'It's the mechanics'.{/sc}{/bt}"
    cas "Learn some real fucking skill!"
    cas "Casper launchs the controllers across the room and storms out, leaving you in shocked silence."
    hide casper
    "Not long after, Henry comes into the room."
    show henry
    h "[player_name]? Are you alright?"
    "He sits next to you."
    h "I am sorry about them."
    h "They tend to get quite emotional when they overclock like this."
    h "Do not take it personally."
    player "It's my fault..."
    h "Hm?"
    player "My fault. I let them overclock."
    h "Oh, my dear. No. They did that to themselves."
    h "You can not be blamed for their foolish behaviour."
    "Henry places a hand on your shoulder, squeezing gently."
    h "I can speak with them and help them calm down."
    h "Stay here."
    hide henry
    "With another reassuring squeeze, Henry gets up and leaves the room."
    "You can hear muffled shouting from the other room."
    "Then..."
    scene bg dining
    with vpunch
    "{b}{sc=2}BANG.{/sc}{/b}"
    "You don't dare move."
    "Don't dare speak."
    "Dare breathe."

    scene bg dining
    with fade
    "After what feels like an eternity, you head back to your bedroom."

    scene bg singlebedroom
    with blinds
    "All you find is a pile of parts."
    "The hard drive is dented."
    "And the CPU..."
    "Is burnt."

    scene bg blank
    "{b}-Bad Ending: Player vs CPU-{/b}"
    return

label Casper_Good_End:
    scene bg dining
    show casper blush
    cas "Good job dude!"
    cas "That fire tactic?"
    cas "Sick as hell."
    cas "You gotta teach me your strategy."
    "Casper insists on another round, listening intently to your guidance."
    "After a few more rounds, Henry enters the room."
    show casper blush at right with move
    show henry at left
    h "[player_name]? Casper?"
    h "I think it is time for you both to take a break from that game."
    show casper angry
    "Casper groans and puts the controllers down."
    cas "You're not my mother..."
    h "And you are not my child, but here we are."
    h "If you must play games, go back to that calm farming one."
    h "You are overclocked and cranky, Casper."
    player "If they need to relax, why don't we get comfy in my room? Casper can nap."
    h "A brilliant idea."
    h "Come along, Casper."
    "You hold Casper's hand as the three of you go back to your bedroom."

    scene bg singlebedroom
    with blinds
    show casper
    "Casper sits awkwardly on your bed, not quite sure if they can fully relax."
    "But the moment you wrap a blanket around them, they're out like a light."
    "Snuggled, safe and warm, Casper finally settles down and falls asleep."
    hide casper
    "Their breathing is slow and even."
    "They look quite... cute."
    show henry
    h "Apologies, [player_name]."
    h "But they must be quite comfortable with you to sleep like this."
    h "They think they are too tough for soft moments like this."
    h "You bring out the best in them."
    h "You should cuddle them."
    player "Huh?!"
    player "Cudddle?!"
    "You feel your face flush a deep red."
    "Henry chuckles as he too wraps you in a blanket."
    h "Rest."
    hide henry
    "Despite your protest, your eyelids do start to feel heavy."
    "You were just so comfortable."
    "And so warm."
    "And..."

    scene bg singlebedroom
    with fade
    player "Hm...?"
    "As you blink awake, you reach for Casper."
    "But your hand only closes around a tiny CPU."

    scene bg singlebedroom
    with fade
    "With the last piece in place, your PC whirs to life."
    "You load up Moonfrost Hollow."
    "And there, inside your house, is Casper's avatar."
    "{b}-Good Ending: Snuggled, safe and warm.-{/b}"
    return