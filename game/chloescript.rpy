#Chloe's route script file
label Chloe_Route:
    $ chlgoodpoint = 0
    $ chlbadpoint = 0

    scene bg lounge
    "You decide to head to the kitchen to spend time with Chloe."

    scene bg kitchen
    with blinds
    play music ["Lava Lamp.mp3", "Try New Things.mp3", "Golden Pig.mp3"]

    show chloe at center
    chl "Oh hey! You wanna hang out with me?"
    chl "Come here, let's do something fun!"
    "Chloe grabs your arm and pulls you closer."
    chl "I found this recipe book, so I thought I'd try baking!"
    chl "I've always wanted to make something!"
    menu:
        "Are you sure you know what you're doing?":
            $ chlbadpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            show chloe upset
            chl "It can't be that hard, right?"
            chl "...Right?"

        "Why don't we do it together?":
            $ chlgoodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship") 
            show chloe blush
            chl "I hoped you'd say that!"
            chl "Let's pick a recipe!"

    show chloe
    "You and Chloe pick out a simple recipe, a Victoria Sponge."
    chl "It sounds delicious!"
    player "I'll get the ingredients ready, can you get out the bowls and spoons?"
    "Chloe nods and excitedly starts on her task of getting out the equipment."
    player "You're lucky I have the ingredients already."
    player "We don't have to go shopping, that's a nightmare..."
    chl "I wouldn't have minded that, anything is fun with you!"
    "You and Chloe get everything arranged on the counter."
    "Chloe starts to measure the ingredients out, making a bit of a mess as she does so."
    chl "Hey, why don't we go off book?"
    chl "We could add sprinkles to make it one of those colourful cakes!"
    player "Funfetti?"
    chl "Yeah, that!"
    menu:
        "Let's follow the recipe.":
            $ chlbadpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            show chloe upset
            chl "Oh. Really?"
            chl "If that's what you want, then... sure."
            "You and Chloe mix the batter together exactly as the recipe states."

        "That's a great idea!":
            $ chlgoodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship")  
            show chloe blush
            chl "Yay! Let's get started!"
            "Chloe is already dumping way too many sprinkles into the batter, but she's happy."
            chl "This cake is gonna look so good!"

    show chloe
    "After the batter is mixed, you move onto the next step."
    chl "Now to put it into a tin!"
    "Chloe grabs the bowl, tipping it up and pouring the contents into two large cake tins."
    "The amount is uneven, but Chloe's goofy smile makes it worth it."
    chl "Oven time!"
    "You carefully put the cake tins into the oven and set the timer."
    chl "And now we wait!"
    chl "And while we wait..."
    chl "You got any questions for me?"
    $ choice_1_chosen = False
    $ choice_2_chosen = False
    $ choice_3_chosen = False

    jump Chloe_Question_Choice 

label Chloe_Question_Choice:
    menu:
        "Ask about Henry and Casper." if choice_1_chosen == False:
            $ choice_1_chosen = True
            chl "Those two?"
            chl "Henry is super serious."
            chl "But he's a sweetheart under all the pomp and circumstance."
            chl "Between you and me, he's a bit like a prince from those games you play."
            chl "And Casper is the definition of chilled out."
            chl "They basically just sit around, waiting for something to do."
            chl "But they mean well, they truly do."
            jump Chloe_Question_Choice

        "What do you do for fun?" if choice_2_chosen == False:
            $ choice_2_chosen = True
            chl "For fun?"
            chl "Nothing."
            chl "Hard to have a hobby when you're cooling a PC all day."
            player "Oh, right. Yeah."
            chl "Did you forget?"
            player "Maybe..."
            jump Chloe_Question_Choice

        "I have nothing to ask.":
            jump Chloe_Route_Continue

label Chloe_Route_Continue:
    "After chatting for a while, the cake is finally finished."
    "You put it on a plate, ready to decorate."
    chl "Can we do coloured buttercream?"
    chl "Oh and sugar flowers!!"
    "Chloe had already pulled out a whole arsenal of decorating supplies."
    "She was looking over them, not sure where to start."

    menu:
        "Use Chloe's suggestions.":
            $ chlgoodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship") 
            "You grab a piping bag and fill it with bright pink icing."
            "Chloe throws on some edible decorations made of sugar."
            "The cake is a mess of colour, but it's delicious."

        "Ignore Chloe's suggestions.":
            $ chlbadpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            show chloe upset
            "You grab a piping bag and fill it with regular buttercream."
            "Chloe just watches you, she looks upset but she makes no moves to stop you."
            "The cake is perfect, albeit bland looking."

    #Decides if the player is on the good or bad ending route
    if chlbadpoint >= 2:
        jump Chloe_Bad_End
    if chlgoodpoint >= 2:
        jump Chloe_Good_End

label Chloe_Bad_End:
    scene bg kitchen
    play music "Birds At The Window.mp3"

    "Despite your best efforts, the cake is less than stellar."
    show chloe upset at center
    chl "This looks... edible."
    chl "Want a slice?"
    "Chloe hesitantly cuts up the cake and places the slices onto plates."
    "Chloe hands a plate to you and picks at her own."
    "She doesn't seem very keen."
    show chloe drain
    chl "Let's go and see if the others want any?"
    "Chloe leaves with her hands full of plates."
    "You follow her out to the dining room."

    scene bg dining
    with blinds
    "Casper is sat at the table, chewing some gum as they watch you and Chloe put the plates down."
    show casper gum at center
    cas "Hm? You made... What did you make?"
    show casper gum at right with move
    show chloe drain at left
    chl "Cake. Want some?"
    "Casper looks at the soulless sponge and hesitates."
    show casper
    cas "I guess...? Lemme grab Henry and we can eat together."
    "Casper lazily stands up and exits the room."
    hide casper
    show chloe drain at center with move
    "Leaving just you and Chloe."
    chl "..."
    player "..."
    show chloe glitch
    chl "...Sorry."
    chl "Didn't mean for this to turn into a mess..."
    "Chloe picks at her slice, eating small bites at a time."
    "The air is so awkward."
    "You can't think of anything to say, so you pick at your own slice."
    "Casper returns with Henry after a while and the two also sit down."
    "The silence is suffocating."
    hide chloe

    scene bg dining
    with fade
    show chloe glitch at center
    show henry at left
    show casper at right
    "Eventually, Henry speaks up."
    h "I have fixed the issue, so you may now fix your Personal Computer, [player_name]."
    "Chloe is the first to leave."
    hide chloe
    "You all file out of the room one after the other."
    hide casper
    hide henry
    "You're the last one to leave."

    scene bg singlebedroom
    with blinds
    "By the time you're back in your room, they've already turned back into a pile of parts."

    scene bg singlebedroom
    with fade
    "You finally reboot your PC and open up the game you wanted to play earlier."
    "Your PC overheats no matter what you try to do."
    "You decide it's best to replace the entire coolant system."
    "Chloe was useless after all."
    scene bg blank
    "{b}-Bad Ending: Soulless Sponge-{/b}"
    return


label Chloe_Good_End:
    scene bg kitchen
    show chloe at center
    play music "Lounging Lads.mp3"
    "Somehow, the cake ends up beautiful."
    chl "Woah, this looks amazing!"
    chl "We should share it with the others, I'm sure they'd love some!"
    "Chloe is already cutting slices and placing them onto plates."
    "You help out and grab some plates, bringing them into the dining room."

    scene bg dining
    "Casper is sat at the table, chewing some gum as they watch you and Chloe put the plates down."
    show chloe at left
    show casper gum at right
    cas "Cake? Sweet."
    "Casper drags a plate closer to them."
    chl "I'll go and get Henry then, since you're gonna stuff your face."
    "With a teasing smile, Chloe rushes off to find Henry."
    hide chloe
    show casper at center with move
    cas "You know she did this because she was worried, right?"
    player "Huh? Worried about what?"
    cas "Being replaced. Don't get me wrong, she is this nice."
    cas "She was just worried you'd chuck her out if you didn't like her."
    "Casper starts to eat their slice of cake, as if they'd just revealed something casual."
    player "I wouldn't do that, I like her."
    "Casper doesn't say another word."
    "Chloe bursts in, tugging Henry by the arm."
    hide casper
    show chloe at left
    show henry at right
    chl "Sit! Eat!"
    "She smiles as she practically shoves Henry into a seat."
    h "Yes, yes. Calm down, Chloe."
    "Henry adjusts his clothes from Chloe's rough handling and begins to dig into his slice."
    chl "Is it good?!"
    h "Yes. Well done, both of you. I assume [player_name] helped you out a lot?"
    show chloe blush
    chl "Maaaaybe."
    chl "[player_name], are you not gonna have some too?"
    player "Oh, yeah. Sure."
    hide henry
    hide chloe
    "You sit down at the table and enjoy a nice slice of cake with the others."
    "The evening is full of laughter and jokes."
    "You really feel like you've formed a bond with these three."
    "Especially Chloe."
    
    scene bg dining
    with fade
    show henry at center
    h "[player_name], you will be glad to know that I have fixed the issue."
    h "We can all return to the Personal Computer now."
    show henry at right with move
    show chloe at left
    chl "Already? But we're having so much fun!"
    h "But [player_name] will probably want their Personal Computer fixed, no?"
    show chloe upset
    chl "I guess..."
    chl "Okay, fine. Let's go and get put back."
    hide henry
    show chloe upset at center with move
    "Chloe is the last to stand up from the table."
    "You gently hold her arm and guide her up."
    player "Hey, it's gonna be okay. You aren't going away forever, yeah?"
    chl "Yeah... Yeah, I'll still be there."
    "You and Chloe head back to your room."

    scene bg singlebedroom
    with blinds
    show chloe blush
    "Chloe takes your hands."
    chl "Well, this was fun. Getting to spend time with you and all."
    chl "This is just see you later."
    chl "Just sit and look away, this bit is embarrassing..."
    chl "Okay?"
    "You nod and sit down at your desk chair."
    "The last thing you see before you swivel around is Chloe's smiling face."
    hide chloe
    "When you turn back around, all that's left is a pile of parts."

    scene bg singlebedroom
    with fade
    "You boot up your PC."
    "It runs smoother than before, and the temperature is low."
    "You boot up the game you wanted to play earlier, the taste of sugar still on your lips."

    scene bg blank
    "{b}-Good Ending: A slice of perfection-{/b}"

    return