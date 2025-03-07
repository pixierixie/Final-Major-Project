#Henry's route script file



label Henry_Route:
    $ goodpoint = 0
    $ badpoint = 0
    
    scene bg lounge
    show henry at center
    h "Ah, me? A wise choice."
    h "Then perhaps I should explain a bit more about us and our purpose here."
    h "We all, of course, wish for your Personal Computer to remain working."
    h "So we will help you find the broken piece and put everything back to how it should be."
    h "I will personally assist you as much as my abilities allow."
    
    menu:
        "You don't have to do that":
            $ badpoint += +1
            h "Oh. It is no trouble, [player_name]."
            h "I insist on helping."
            
        "Thanks, I want to fix this too.":
            $ goodpoint += +1
            h "Perfect. Then perhaps we can troubleshoot together?"
            h "I happen to be quite knowledgeable about everyone."

    "Me and Henry start to list out every part and I make notes based on Henry’s descriptions."
    h "From my perspective, everyone has been behaving relatively well."
    h "That does not mean to say that somebody is not hiding something from you."
    player "Then why don’t we take a break?"
    player "No point in staring at the page as if the answer will jump out at us."
    h "You do have a point."
    "Henry stands from his spot on the sofa."
    h "Chloe is still in the kitchen, I will go and get some refreshments. Sit tight."
    hide henry
    "Henry exits the room, leaving me alone for the first time since this crazy shit started."
    "But the peace is soon shattered by a shout."
    chl "[player_name]!!"
    show chloe at center
  
    "She throws herself next to me on the sofa, shoving a can into my hands."
    chl "Henry said this was your favourite, so I grabbed one for ya!"
    show henry at right
    show chloe at left with move
    "Henry comes back into the room, quietly settling down on my other side."
    "He holds out a bag of crisps."
    h "Apologies for raiding your cupboards."
    h "Eat. You need your strength."
    "He smiles, opening the bag and placing it on my lap."
    chl "I’ll go get Casper and we can have a picnic!"
    
    hide chloe
    show henry at center with move
    "Chloe, once again, is off like a shot."
    player "Does she ever stop running around?"
    h "I am afraid not. It is in her nature to be constantly moving."
    player "Oh yeah, coolant and all..."
    h "Precisely."
    h "I hope her personality is not too much for you? She means well."
    h "I suppose I could consider her a little sister of sorts..."
    
    "As if on cue, Chloe bounces back in, Casper in tow."
    show henry at right with move
    show chloe at left
    chl "Found them!! Now we can have a proper picnic."
    show chloe at center with move
    show casper at left
    cas "Don't mind me, just gonna sit here."
    "Chloe and Casper get comfortable in their own seats, a few snacks and drinks in hand."
    hide chloe
    hide casper
    show henry at center with move
    h "As I was saying, I am one of the oldest parts."
    h "It feels like being a big brother to the others, to put it in more human terms."
    
    menu:
        "Ask about Henry":
            $ goodpoint += +1
            show henry blush
            h "You wish to learn about me?"
            h "I would be delighted to share things with you, [player_name]."
            h "I work tirelessly to make sure your files are kept safe and organised in the correct places."
            show henry
            h "To compare it to a human job… I suppose I am an archivist."
            h "Ah, I suppose you do not care much about that though."
            h "I quite enjoy it when you download something, it keeps me busy."
            h "Even when the contents is… less than pure, shall we say."
        
        
        "Ask about Chloe":
            $ badpoint += +1
            hide henry
            show chloe blush at center
            chl "Me?! Sure!"
            chl "I work pretty hard, you know!"
            chl "Without me, your entire setup would go boom!"
            chl "But I love my job, I get to go around all day and check on everyone."
            chl "The others say I’m kinda like the glue that holds everything together."
        
        "Ask about Casper":
            $ badpoint += +1
            hide henry
            show casper at center
            cas "Hm?"
            cas "Oh. Sure."
            cas "I just kinda hand out instructions."
            cas "Easy shit really."
            cas "Until you overclock me, of course."
            cas "That’s fun."
            cas "And chaotic. Very chaotic."
        
    hide henry
    hide casper
    hide chloe
    "The atmosphere settles into light hearted banter and casual conversation."
    "After a while, all the snacks and drinks are finished."
    show henry at center
    h "Now then, we should get back to work."
    h "Chloe, Casper, if you would not mind."
    "The other two exchange a knowing glance and leave the room without protest."
    h "[player_name], I wish to know something."
    h "Do you already have a suspicion on who is the broken one?"
        
    menu:
        "Henry":
            $ badpoint += +1
            h "..."
            h "Me?"
            h "May I ask why?"
            menu:
                "You're weird":
                    h "Weird…"
                    h "I suppose I cannot blame you too much."
                    h "We are hardly in an ideal or usual situation."
                    "He goes silent."
                    "I shouldn’t have said that."
                    
                "I'm not sure":
                    h "Just the… ‘vibes’ then?"
                    h "I am off putting to you."
                    h "Well, I do hope that changes in time."
                    "He smiles, but it’s empty."
                    "I probably shouldn't have said that."
            
        "Chloe":
            $ badpoint += +1
            h "Chloe? How odd."
            h "I suppose her hyperactivity may be a tad much for you."
            h "I do apologise on her behalf."
            "Henry looks upset."
            
        "Casper":
            $ badpoint += +1
            h "Casper?"
            h "They are rather quiet, but that is not out of the ordinary."
            h "But if that is your opinion, I have no right to argue it."
            "Henry looks upset."
                
        "I don't know":
            $ goodpoint += +1
            h "I see."
            h "Neither do I, if I am being honest."
            h "Shall we continue our investigation?"
            "Henry goes right back to our notes, organising them like the files of my computer."
                
                
    "After some more consideration, we’re back to square one again."
    show henry
    h "[player_name], I must come clean."
    h "I have been distracted this entire time."
    h "I must confess something."
    h "Over these past few hours, I have found myself... attached."
    show henry blush
    h "Dear [player_name], I believe I have caught... feelings."
       
    #Decides if the player is on the good or bad ending route
    if badpoint >= 2:
        jump Henry_Bad_End
    if goodpoint >= 2:
        jump Henry_Good_End
   

#Bad ending
label Henry_Bad_End:
    scene bg lounge
    show henry blush at center
    player "Feelings?"
    player "You’re not serious?"
    show henry
    h "You do not feel the same?"
    player "No! Of course I don’t, you weirdo!"
    h "What...?"
    h "You..."
    h "You do not like me…?"
    h "Even after everything I have helped you with...?"
    h "[player_name]..."
    scene bg blank
    h "{color=#b00000}{b}You idiot.{/color}{/b}"
    
    scene bg lounge
    show henry angry
    h "Is it Chloe?"
    h "Has she stolen you from me?"
    h "Or Casper... that lazy bastard."
    h "You have been nothing but cruel, [player_name]."
    h "Toying with me like this. Like I am just some USB you throw away when it snaps."
    h "You chose me."
    h "Nevermind, I will help you see."
    "Before I can register anything else, a sharp shock pierces through my body."
    
    scene bg distortbedroom
    with fade
    show henry yandere
    h "You are awake?"
    h "Good, I was beginning to worry."
    "As I blink awake, my eyes drift over to Henry."
    "He was looking at me with a sick expression, one of twisted evil."
    "In his hands were shattered parts and blood."
    h "Oh, these?"
    "Henry’s face twists into a smirk."
    h "They are not needed anymore."
    h "I took care of everything."
    "I go to move my hands but find that I can’t."
    player "Wh..."
    "My tongue doesn’t move how it should."
    "What the hell is going on?"
    "Why can’t I-"
    h "Why can you not move?"
    h "Take it easy now. You have had a stressful day."
    h "How about you just relax and eat something, yes?"
    "He cups my cheek with an unexpected gentleness."
    h "I made ramen."
    scene bg blank
    "{b}-Bad Ending - Do hard drives dream of electric [player_name]?-{/b}"
    return

#Good ending
label Henry_Good_End:
    scene bg blank
    h "Good ending not yet implemented."