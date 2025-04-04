#Chloe's route script file
label Chloe_Route:
    $ goodpoint = 0
    $ badpoint = 0

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
            $ badpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            show chloe upset
            chl "It can't be that hard, right?"
            chl "...Right?"

        "Why don't we do it together?":
            $ goodpoint += +1
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
            $ badpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            show chloe upset
            chl "Oh. Really?"
            chl "If that's what you want, then... sure."
            "You and Chloe mix the batter together exactly as the recipe states."

        "That's a great idea!":
            $ goodpoint += +1
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
        "Ask about Henry and Casper" if choice_1_chosen == False:
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
            $ goodpoint += +1
            play sound "UI Simple Confirm.mp3"
            $ renpy.notify("+1 relationship") 
            "You grab a piping bag and fill it with bright pink icing."
            "Chloe throws on some edible decorations made of sugar."
            "The cake is a mess of colour, but it s delicious."

        "Ignore Chloe's suggestions.":
            $ badpoint += +1
            play sound "UI Simple Cancel.mp3"
            $ renpy.notify("-1 relationship")
            show chloe upset
            "You grab a piping bag and fill it with regular buttercream."
            "Chloe just watches you, she looks upset but she makes no moves to stop you."
            "The cake is perfect, albeit bland looking."

    #Decides if the player is on the good or bad ending route
    if badpoint >= 2:
        jump Chloe_Bad_End
    if goodpoint >= 2:
        jump Chloe_Good_End

label Chloe_Bad_End:
    scene bg kitchen
    show chloe at center
    play music "Birds At The Window.mp3"
    chl "BAD END"
    return


label Chloe_Good_End:
    scene bg kitchen
    show chloe at center
    play music "Lounging Lads.mp3"
    chl "GOOD END"
    return




