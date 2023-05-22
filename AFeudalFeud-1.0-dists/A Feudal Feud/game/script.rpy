# The script of the game goes in this file.

define n = Character("")
define s = Character("Sasaki")
define h = Character("Hinano")
define m = Character("Masataka")
define a = Character("Amane")
define r = Character("Ryuuji")
define t1 = Character("Big Thug")
define t2 = Character("Thug with bow")
define t3 = Character("Short Thug")
define t4 = Character("Small Thug")
define t5 = Character("Thug with eyepatch")
define t6 = Character("Scarred Thug")
define t7 = Character("Drunk Thug")
define o1 = Character("Old Man")
define g1 = Character("Women in pink kimono")
define g2 = Character("Women in blue kimono")
define u = Character("The Lord")
define m1 = Character("Unknown Man")
define w1 = Character("Unknown Woman")

define offright = Position(xalign=1.5)
define offleft = Position(xalign=-0.5)
define middle = Position(xalign=0.5)
define middleleft = Position(xalign=0.25)
define middleright = Position(xalign=0.75)
define leftmiddleleft = Position(xalign=0.12)
define rightmiddleright = Position(xalign=0.88)
define middleleftmiddle = Position(xalign=0.38)
define middlerightmiddle = Position(xalign=0.62)

define offupleft = Position(yalign=9)
define offabove = Position(yalign=10)
define offunder = Position(xalign=-1)

# Changes size of images

init:
    image dirt road:
        "dirt road.png"
        zoom 2.6
    image village1:
        "village1.png"
        zoom 0.65
    image village2:
        "village2.png"
        zoom 0.65
    image village3:
        "village3.png"
        zoom 2.6
    image village3-5:
        "village3-5.png"
        zoom 3.8
    image mansion1:
        "mansion1.png"
        zoom 0.65
    image mansion2:
        "mansion2.png"
        zoom 0.65
    image mansion3:
        "mansion3.png"
        zoom 0.65
    image dirt road2:
        "dirt road2.png"
        zoom 2.6
    image sasaki:
        "sasaki.png"
        zoom 1.0
    image old man:
        "old man.png"
        zoom 0.35
    image girls1:
        "girls1.png"
    image girls2:
        "girls2.png"
        zoom 1.1
    image thugs1:
        "thugs1.png"
        zoom 1.1
    image hinano:
        "hinano.png"
        zoom 0.45
    image amane:
        "amane.png"
        zoom 0.45
    image thugs2:
        "thugs2.png"
        zoom 1.1
    image masataka:
        "masataka.png"
        zoom 1.1
    image ryuuji:
        "ryuuji.png"
        zoom 1.1
    image theend:
        "theend.png"
        zoom 1.5

# The game starts here.

label start:

    ##PART ONE ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

    scene dirt road

    play music "audio/mysterious shrine.mp3" volume 0.05

    n "The sun began to set over the lush green fields. The harvest had been good this season but you couldn't tell when confronted with the farmers' solemn faces."

    n "A lonely road cut through these fields and held very few travellers. One of the few was a young man that held nunchucks."

    show sasaki with Dissolve(0.8)

    s "Not far now."

    n "A village could be seen in the distance and an old man was coming from it. Sasaki bows as the man gets closer."

    show sasaki at middleright with move

    show old man at middleleft with Dissolve(0.8)

    o1 "I would turn around if I were you son."

    s "..."

    s "I'm afraid I cannot do that sir."

    o1 "I see..." 

    o1 "Then good luck, you'll need it."

    hide old man with Dissolve(0.8)

    show sasaki at middle with move

    n "Sasaki bows again as the old man leaves."

    show sasaki at middle with move

    n "Sasaki moves forward, unperturbed by the man's words."

    n "The village draws near."

    hide sasaki with Dissolve(0.8)

    stop music fadeout 1.0

    scene village1 with Dissolve(0.8)

    n "The village is eerily quiet. Not a soul could be seen outside."

    show sasaki with Dissolve(0.8)

    n "Sasaki looks around but finds little except whispers."

    n "He approaches a shop's open window that whispers were coming from."

    s "Excuse m-"

    n "The window violently shuts."

    s "That bad huh."

    n "He continues to wander, hearing few people and seeing far fewer."

    n "Hearing a scream, Sasaki runs towards where the sound came from."

    hide sasaki with Dissolve(0.8)
    
    ##PART TWO ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

    scene village2 with Dissolve(0.8)

    n "The scene was unfolding a couple streets away."

    show thugs1 at middleleft with Dissolve(0.8)

    show girls1 at middleright with Dissolve(0.8)

    t1 "Keep it down will ya? You'll scare the neighbours."

    t2 "Yeah come on all he asked for was a little kiss... on his dick!"

    t3 "Ha ha good one."

    t1 "Let's go back inside huh? I'd hate to have to hurt such a pretty face."

    g1 "N-no, I will not."

    t2 "That's one weird way of saying yes."

    t3 "Ha ha good one."

    g2 "Please d-don't do this. I'm begging you."

    t1 "I only accept begging when it's done while licking my boots."

    g1 "Wh-what do we do?"

    t1 "Didn't you hear? I said-"

    n "A crash is heard as a figure holding a sword lands between them!"

    play music "audio/shamisen-samurai-rock.mp3" volume 0.05

    show thugs1 at left
    show girls1 at right 
    with move

    show hinano at middle with Dissolve(0.8)

    w1 "Now that's no way to treat a lady is it?"

    t3 "Who the fuck's this?"

    t1 "I don't know or care, but she's in the way, get her!"

    n "The women quickly flee."

    show girls1 at offright with move

    show hinano at middlerightmiddle
    show thugs1 at middleleftmiddle
    with move

    play sound "audio/sword clang.mp3" volume 0.6

    hide girls1

    n "The Big Thug's sword and the Womans's interlock with a clang!"

    n "The Thugs are all taken aback at the Woman's strength as she stands resolute."

    n "Sasaki arrives nearby and quickly assesses the situation."

    w1 "Oh my, is that all you have?"

    t1 "Tch, boys help me out here!"

    menu:

        "Sasaki aids the Woman":

            jump choice1_1

        "Sasaki waits and watches":

            jump choice1_2

    label choice1_1:

        $ menu_flag1 = True

        show sasaki at offleft

        show sasaki at left with move

        s "Not so fast fellas."

        n "The two smaller Thugs turn to face Sasaki."

        show hinano at right
        show thugs1 at middle
        with move

        t2 "Urgh, let's finish this quick."

        t3 "Let's do it!"

        n "The Short Thug rushes in pulling a knife out of his sleeve."

        n "Sasaki dodges to the side as the Thug strikes making him miss."

        n "Before the Thug can turn around Sasaki strikes him in the temple with the bottom of a nunchuck."

        t3 "Ugh."

        n "The Thug loses consciousness and collapses."

        s "One down."

        t2 "You'll pay for that!"

        n "The Thug pulls an arrow from his quiver and nocks it."

        n "Sasaki dashes into a nearby adjacent alleyway."

        hide sasaki with Dissolve(0.2)

        t2 "Leaving so soon! Guess I'll switch targets!"

        n "The Thug turns to face the woman while waiting for Sasaki to emerge from the alley."

        n "..."

        t2 "Fine then."

        n "The Thug lifts his bow and pulls back the drawstring."

        n "As he lines up the shot nunchucks fly through the air and unnock the arrow!"

        n "The Thug looks up to see Sasaki before being kicked in the face!"

        show sasaki at left with Dissolve(0.2)

        n "The Thug drops his bow as he falls onto his back."

        n "Sasaki, standing over him, gives him a bright smile before leaning down..."

        t2 "Hey man l-let's call a truc-"

        n "Sasaki strikes him, knocking him out."

        n "Sasaki picks up his nunchucks before turning to to look at the other two."

        n "The Big Thug is down and the Woman is wiping her blade."

        hide thugs1 with Dissolve(0.8)

        stop music fadeout 1.0

        show sasaki at middleleft with move

        show hinano at middleright with move

        jump choice1_done

    label choice1_2:

        $ menu_flag1 = False

        n "Sasaki crosses his arms and observes."

        show thugs1 at middleleft
        show hinano at middleright
        with move

        n "The Thug with the bow nocks an arrow and fires."

        n "The Woman deflects the Big Thugs sword and cuts the arrow out of the air!"

        t2 "What the-"

        n "The Short Thug runs in as the Big Thug prepares a wide slash."

        n "The Woman ducks under the slash before stabbing the Short Thug in the abdomen!"

        t3 "Argh!"

        n "The Thug falls, clutching his stab wound."

        t1 "You'll pay for that!"

        n "The Big Thug prepares a mighty downward strike!"

        n "The woman goes on the offensive and starts slashing at the Big Thug."

        n "The Thug cancels his strike as he desperately tries to defend himself."

        n "The Woman presses her attack, and moves the Big Thug away from the other Thug."

        n "With her back turned, the Thug with a bow realises his chance."

        n "He nocks another arrow and fires!"

        n "The woman sidesteps and the arrow hits the Big Thug in the chest!"

        t1 "Gah!"

        n "He falls to one knee, clutching the arrow."

        n "He looks up as The Woman brings her sword through his neck."

        n "The Big Thug falls to the ground in two pieces."

        n "The Woman turns towards the remaining Thug."

        n "He gulps as he shakily pulls out another arrow."

        w1 "Decide."

        n "The Thug jumps, dropping his arrow."

        w1 "You either leave and save your friend, or you stay and die."

        t2 "Well... I choose option three!"

        n "The Woman readies herself."

        t2 "Leaving by myself!"

        n "Without another word, he drops his bow, and runs away screaming."

        t3 "H-ha ha... good... one."

        n "He loses consciousness."

        hide thugs1 with Dissolve(0.8)

        stop music fadeout 1.0

        n "The woman sighs."

        s "Still as strong as ever I see"

        show sasaki at offleft

        show sasaki at middleleft with move

        jump choice1_done

    label choice1_done:

    play music "audio/mysterious shrine.mp3" volume 0.05

    w1 "Long time no see, Sasaki."

    s "You as well, Hinano-san."

    n "The two bow."

    h "Hinano is fine."

    s "What brings you here Hinano?"

    h "Same as you I imagine, a certain dictators head."

    s "Where is he?"

    h "Probably up in his mansion, but he could be elsewhere."

    s "Hmm." 

    s "What do you say we track down someone who knows for sure?"

    h "Way ahead of you. Follow me."

    n "The two leave the street and head towards the centre of the village."

    #PART THREE ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

    scene village3 with Dissolve(0.8)

    n "The street was littered with corrupt guards and dirty thugs, all gambling their coins away while laughing in merriment."

    show girls2 at offright

    show sasaki at middleleft
    show hinano at middleright
    with Dissolve(0.8)

    h "This makes me sick."

    s "Which part?"

    h "The guards gambling away the money they got from exorbitant taxes."

    s "Ah. I was gonna say the guards being all chummy with common criminals."

    show sasaki at left
    show hinano at middle 
    with move

    show girls2 at right with move

    g1 "Thank you so much for saving us earlier."

    g2 "We are in your debt, but we have little to offer."

    n "The two women bow."

    h "Don't worry about it."

    h "For now please hurry home, it's dangerous here."

    n "The two nod in agreeance and bow again before departing."

    hide girls2 with Dissolve(0.8)

    show hinano at middleright
    show sasaki at middleleft
    with move

    h "Our guys alone, let's go"

    hide hinano
    hide sasaki
    with Dissolve(0.8)

    n "The two slip past the gamblers and drunks before they come across a strong looking thug"

    show amane at left with Dissolve(0.8)

    show hinano at middle
    show sasaki at right
    with Dissolve(0.8)

    m1 "Who the hell are you two?"

    h "Um We're lost could you show us the way?"

    m1 "I could... how much money you got?"

    h "A few coins sir."

    m1 "hmm..."

    m1 "I'm sick of this lot anyway, follow me."

    t7 "Fuck you too Amane!"

    n "The drunks laugh as the three move out of earshot."

    a "What do you want Hinano I'm working?"

    h "What else? We're taking down the lord."

    a "Ehh you think you two can accomplish that?"

    n "He looks Sasaki up and down."

    h "He's tougher than he looks."

    if menu_flag1:

        a "He better be if I'm losing my cover over this."

    else:

        h "At least I think he is, he did leave me to deal with the thugs from earlier alone."

        s "I knew you had it covered."

        a "I'm losing my cover over this so he better be good"

    s "So where is he?"

    a "In his mansion."

    s "Figured."

    a "But he's not alone, and I don't mean his thugs."

    h "Mercenaries?"

    a "Mercenary. Singular."

    s "He's that strong?"

    a "Stronger."

    n "The three ruminate in silence for a moment."

    n "..."

    h "Well I'm sure you know he's planning to go overseas soon."

    h "We can't let him walk after all the pain he's wrought."

    s "Hear hear."

    a "Alright then, it's your funeral."

    a "I'm not suicidal so I'll lead you up a hidden road then I'm getting out of this village."

    s "As you wish."

    n "The three depart for the estate on the hill."

    stop music fadeout 1.0

    scene village3-5 with Dissolve(0.8)

    n "The trio weave through an old battered path covered in overgrowth. It clearly had seen very little traffic in recent years."

    n "After cresting the top of the hill and hopping over a fence, they had arrived."

    ##PART FOUR ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

    scene mansion1 with Dissolve(0.8)

    n "The air was stale and cold outside the mansion. The village felt desolate but here felt... hostile."

    show sasaki at right
    show hinano at middleright
    show amane at middleleft 
    with Dissolve(0.8)

    a "Alright, from here it's a straight shot."

    h "Sure you don't want to tag along? We could use the extra hands." 

    h "You can even take some money from the treasury while no-one's looking."

    a "Ha! Money doesn't matter to a corpse."

    a "Besides, I'm getting plenty from this job."

    s "Hm? I didn't think spies got paid much..."

    n "..."

    play music "audio/shamisen-samurai-rock.mp3" volume 0.05

    show ryuuji at offleft

    show amane at left with move

    show hinano at middleleftmiddle
    show ryuuji at middleleft
    with move

    play sound "audio/sword clang.mp3" volume 0.6

    a "Phew, that was a close one. Uh thanks Ryuuji."

    r "I do not require your thanks."

    show hinano at middleright with move

    h "He wasn't lying about him being strong."

    s "Our backs are against the wall on this one."

    h "Amane probably won't go down without a fight either..." 
    
    h "What should we do?"

    menu:

        "Sasaki fights Ryuuji, Hinano fights Amane":

            jump choice2_1

        "Hinano fights Ryuuji, Sasaki fights Amane":

            jump choice2_2

        "They both fight Ryuuji first":

            jump choice2_3

    label choice2_1:

        $ menu_flag2 = True

        s "I'll take him, you deal with the traitor."

        h "Let's do it."

        show sasaki at middleleftmiddle with move

        play sound "audio/sword clang.mp3" volume 0.4

        n "Sasaki rushes Ryuuji and catches his blade with the nunchuck's chain."

        show amane at offscreenleft
        show hinano at offscreenleft
        with move

        show sasaki at middleright with move

        hide amane

        s "This should be interesting."

        r "Come."

        n "Sasaki obliges, unleasing a flurry of strikes with his nunchucks as he does."

        n "Ryuuji stands unwavering, only blocking strikes that would hit him in the head."

        r "You lack resolve."

        s "You lack weak points."

        n "Ryuuji winds up a strike, Sasaki jumps backwards."

        n "Ryuuji matches his direction and strikes."

        n "The attack barely misses as Sasaki loses his balance."

        n "Ryuuji grabs Sasaki and hurls him at a nearby wood fence!"

        n "The fence breaks as Sasaki slams into it."

        s "Geh... this guy's got moves."

        n "Ryuuji waits for his opponent to get back up."

        n "Sasaki stands and takes a breath."

        n "..."

        n "Ryuuji attacks with a quick overhead strike."

        n "Sasaki dodges and hits Ryuuji's hand causing his sword to fly out of his hand."

        n "Ryuuji takes a few steps back, looking at his hand."

        r "Your movements are adequate."

        s "Well thank you ve-"

        r "But your resolve is still weak."

        n "Suddenly Ryuuji closes the distance between them!"

        n "Sasaki goes to block but is punched in the gut before he can."

        s "Argh!"

        n "Sasaki attempts to retaliate but his attack is sidestepped."

        n "In the opening, Ryuuji strikes him in chest."

        n "Sasaki winces as he stumbles back."

        r "Do you know why you cannot win?"

        s "*huff* *huff*... because you're way too fast with such heavy armour?"

        r "It is because you are trying to incapacitate, not kill."

        r "You think you are strong for giving such a mercy..."

        r "You are wrong."

        r "Your moves are blunt, they cannot beat me."

        n "Ryuuji walks up to Sasaki."

        n "Sasaki offers a meagre defence as Ryuuji lands strike after strike."

        n "Sasaki falls."

        hide sasaki with Dissolve (0.4)

        r "Unfortunate."

        show ryuuji at middleright with move

        show hinano at left with move

        h "Leave him alone!"

        n "Ryuuji turns to face her."

        h "Now you face me."

        r "..."

        s "... no."

        s "I'm not... done yet."

        n "Sasaki rises and braces himself."

        show ryuuji at middle with move

        show sasaki at right with Dissolve(1)

        n "..."

        n "Ryuuji cracks a smile."

        r "Now that is resolve."

        stop music fadeout 3.0

        n "He sighs."

        r "I am done here."

        h "... wait what?"

        hide ryuuji with Dissolve(0.8)

        n "Ryuuji walks away towards the village."

        h "What was that about?"

        s "I... don't know. Where's Amane?"

        h "He ran, I'll track him down later."

        s "In the meantime, let's have a chat with the lord."

        h "Agreed."

        jump choice2_done

    label choice2_2:

        s "I'll deal with the traitor, you distract the big guy."

        if menu_flag1 == False:

            h "..."

            h "How about I take the traitor and you take the big guy?"

            s "Are you still mad about earlier?"

            h "Not even a little."

            n "She lied as naturally as she breathed."

            s "Fine..."

            jump choice2_1

        $ menu_flag2_5 = True

        h "Let's do it."

        show hinano at middleleftmiddle with move

        play sound "audio/sword clang.mp3" volume 0.6

        n "Hinano rushes Ryuuji and their blades lock with a spark."

        show amane at offscreenleft
        show sasaki at offscreenleft
        with move

        show hinano at middleright with move

        hide amane

        h "Prepared to meet your maker, Ryuuji?."

        r "Come."

        h "Fine then."

        n "Hinano strikes at Ryuuji but he blocks it."

        n "She prepares for a counter attack but it does not come."

        n "Hinano attacks again and again but gains no ground."

        r "You lack conviction."

        h "Excuse me?"

        n "Ryuuji lets out a fierce upwards strike directed at Hinano's sword."

        n "She blocks but her sword is flung up in the air!"

        n "Ryuuji catches it in his off hand."

        r "What are you without your sword?"

        h "..."

        r "Are your convictions so weak that you would admit defeat now?"

        h "*tsk* don't underestimate me."

        n "Hinano dashes in and unshealths Ryuuji's dagger."

        n "She slashes at his arms but he dodges with ease."

        n "Ryuuji knees Hinano in the stomache causing her to fall to one knee."

        h "Argh!"

        r "Will you yield?"

        n "She looks up agrily and is met with a sword hilt to the face!"

        n "Hinano falls to her hands and knees."

        hide hinano with Dissolve (0.4)

        r "Do you know why you cannot win?"

        h "..."

        r "You are not willing to fail for your goals."

        r "You would rather flee and fight another day, then give everything you've got to win now."

        h "..."

        r "Unfortunate."

        show ryuuji at middleright with move

        show sasaki at left with move

        s "Leave her alone!"

        n "Ryuuji turns to face him."

        s "You'll pay for hurting her."

        r "..."

        h "... I can still fight."

        n "She gets up."

        show ryuuji at middle with move

        show hinano at right with Dissolve(1)

        h "I will still fight, no matter what."

        n "..."

        n "Ryuuji cracks a smile."

        r "Now that is conviction."

        stop music fadeout 3.0

        n "He sighs."

        r "I am done here."

        s "... pardon?"

        hide ryuuji with Dissolve(0.8)

        n "After ditching Hinano's sword, Ryuuji walks away towards the village."

        s "What is going on?"

        h "I... am unsure. What happened to the traitor?"

        s "He's out cold, we can apprehend him later."

        n "Hinano gets up and picks up her sword."

        h "Then I'd say it's time to deal with the lord."

        s "let's do it."

        jump choice2_done

    label choice2_3:

        $ menu_flag2 = False

        s "We'll take him together."

        h "Let's do it, but watch out for Amane."

        n "Sasaki nods."

        show amane at offscreenleft with move

        show ryuuji at middle
        show hinano at left
        with move

        hide amane

        h "Prepared to meet your maker, Ryuuji?."
        
        r "Come."

        n "The comrades nod at each other as they both attack."

        n "Hinano strikes low then Sasaki strikes high."

        n "Ryuuji blocks Hinano with his sword and Sasaki with his other arm."

        n "The two press on, attacking their opponent as the other one prepares their next attack."

        r "You lack effective coordination."

        s "What? How?"

        n "Ryuuji turns to Hinano as she attacks."

        n "He dodges and counter-throws her towards Sasaki!"

        show hinano at right with move

        n "Sasaki catches her and softens her landing."

        n "Ryuuji presses his advantage, kicking Hinano hard enough to send them both sprawling to the ground."

        n "The two groan as they lay splayed out on the dirt road."

        r "You were likely trained to fight in this matter, taking turns, never giving your opponent an opening."

        r "But this strategy lacks a decisive factor."

        r "A superior opponent will not be brought to heel so easily."

        s "I thought he was the silent type, now he won't stop talking."

        n "The two get up and brace themselves."

        show hinano at middleright with move

        n "Ryuuji unsheaths his dagger and holds it in his offhand."

        r "Observe."

        n "Ryuuji simultaneously attacks them, slashing at Hinano and Sasaki."

        n "The two are barely holding their own against his ceaseless barrage."

        a "Haarrggh!"
        
        n "Amane leaps out and attacks Sasaki!"

        show amane at offright

        show sasaki at rightmiddleright with move
        
        show amane at right with move

        n "He manages to block his strike, but is hit hard by Ryuuji's blade's hilt at the same time!"

        n "Sasaki falls, clutching his head."

        hide sasaki with Dissolve (0.4)

        h "Sasaki!"

        show ryuuji at left with move

        r "A combined, simultaneous attack, leads to better results."

        n "Amane attacks Hinano with an overhead strike while she is distracted."

        n "She manages a block but is pushed to the ground."

        hide hinano with Dissolve (0.4)

        a "No hard feelings right?"

        show amane at middleright with move

        n "He winds up another attack."

        s "None at all"

        show sasaki at right with Dissolve(0.2)

        n "Sasaki winds up an attack."

        n "Amane moves to block."

        n "Hinano rises and also prepares an attack."

        show hinano at middle with Dissolve(0.2)

        a "Wait sto-"

        n "The two attack at the same time, quickly overwhelming Amane."

        a "Argh!"

        n "Amane collapses as the two land a decisive blow each."

        hide amane with Dissolve(0.4)

        n "The two catch their breath quickly before facing Ryuuji."

        n "..."

        n "Ryuuji cracks a smile."

        r "Now that is potent coordination."

        stop music fadeout 3.0

        n "He sighs."

        r "I am done here."

        s "... Excuse me what?"

        hide ryuuji with Dissolve(0.8)

        n "Ryuuji walks away towards the village."

        h "Should we stop him?"

        s "I... would rather not fight him again"

        h "Me neither."

        h "I guess it's time to face the lord then."

        s "Must be."

    label choice2_done:

    n "After the two briefly rest to regain their stamina and bandage any wounds, they continue on and enter the mansion."

    ##PART FIVE ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

    scene mansion2 with Dissolve(0.8)

    n "The mansion is dusty and empty. It's clear no one had cared about the place's upkeep for far too long."

    show sasaki at middlerightmiddle
    show hinano at right
    with Dissolve(0.7)

    s "This place is creepily quiet."

    h "You can say that again."

    n "The two reach a chamber with dangerous looking thugs in it."

    show thugs2 at left with Dissolve(0.7)

    t5 "Been awhile since the last guests came through here."

    t6 "Three weeks I think."

    n "Sasaki and Hinano brace themselves."

    t4 "Now now hold your horses. This can go a way where we don't fight."

    s "And which way would that be?"

    t4 "The name of the man outside the mansion, what was it?"

    n "Sasaki and Hinano exchange a glance."

    h "Ryuuji."

    t4 "Ding Dong! That's correct. What do they win?"

    t5 "An audience with the lord."

    n "The guards sheath their weapons and step aside."

    hide thugs2 with Dissolve(0.7)

    s "This is helpful but kind of concerning."

    h "Stay on your toes."

    n "The two progress, exchanging looks with the thugs."

    show sasaki at middle
    show hinano at rightmiddleright 
    with move

    t4 "Good luck... you'll need it."

    scene mansion3 with Dissolve(0.8)

    play music "audio/mysterious shrine.mp3" volume 0.05

    n "The massive chamber had clearly seen many fights, as slashes and blow indents served as decoration around the room."

    show sasaki at middleleft
    show hinano at middleright
    with Dissolve(0.7)

    h "Three weeks... you don't think..."

    s "... Yes. They were probably referring to Ayanokoji."

    h "..."

    n "Hinano utters a short prayer under her breath."

    s "Let's stop this guy, once and for all."

    u "Oooooo I'm shaking in my boots."

    n "The two quickly scan the area but find no-one."

    s "Why don't you come out? If you ask nicely we might take you alive."

    u "Oh I know you won't. Ayanokoji was it? He certainly wasn't the first to fall..."

    u "...Nor will he be the last."

    h "You will pay for all you've done!"

    n "The Lord cackles"

    u "Will I?"

    if menu_flag2:

        u "He's injured, and you still think your opposition scares me?."

    elif menu_flag2_5:

        u "You're injured, and you still think your opposition scares me?."

    else:

        u "You're both injured, and you still think your opposition scares me?."

    s "Is that why the mercenary is out there, to soften up your targets?"

    u "Not quite. I loathe having to face weaklings in combat."

    u "He makes sure only the strongest of opponents are allowed in."

    n "..."

    h "I grow tired of this. Face us!"

    stop music fadeout 1.0

    u "As you wish."

    n "The two look up to see a dark figure jump off a wooden beam near the roof."

    show sasaki at left
    show hinano at right
    with move

    n "He lands between them with a flourish."

    show masataka at middle with Dissolve(0.4)

    play music "audio/yasha.mp3" volume 0.05

    m "The name's Masataka, what are yours?"

    h "Wasted on your ears."

    m "Very well..."
    
    m "... then you will die nameless!"

    if menu_flag2:

        n "Masataka darts to Hinano and overwhelms her quickly."

        n "Sasaki moves in to attack him from behind but Masataka ducks it."

        m "Nice speed, but..."

        n "He cuts Hinano up her side before attacking Sasaki."

        hide hinano with Dissolve(0.4)

        m "Not fast enough!"

        n "He unleashes a flurry of incredibly fast strikes."

        n "Sasaki dodges and blocks most but sustains a few shallow wounds."

        n "Sasaki looks over at the injured Hinano and grits his teeth."

        s "You want fast!?"

        n "Sasaki takes a deep breath."

        m "Hahaha yes show me!"

        n "Sasaki closes his eyes and feels the air pass around his body."

        n "He opens his eyes and seemingly teleports behind Masataka!"

        show sasaki at middlerightmiddle with Dissolve(0.1)

        m "Wha-"

        n "Sasaki unleashes a swirl of nunchuck strikes."

        n "Masataka blocks most but takes a few hits."

        n "Masataka jumps a few metres away from Sasaki."

        show masataka at left with move

        m "Not bad... not bad at all."

        n "Sasaki moves over to Hinano."

        show sasaki at middleright with move

        n "You okay Hinano?"

        show hinano at right with Dissolve(1)

        h "It's not that deep, I can still fight."

    elif menu_flag2_5:

        n "Masataka darts to Sasaki and overwhelms him quickly."

        n "Hinano attacks with a wide horizontal slash but Masataka blocks it."

        m "Nice power, but..."

        n "He roundhouse kicks Sasaki in the head before attacking Hinano."

        hide sasaki with Dissolve(0.4)

        m "Not strong enough!"

        n "He unleashes a series of incredibly stong strikes."

        n "Hinano blocks them, causing her arms to go numb."

        n "Her hands shake as she looks at the injured Sasaki."

        h "I'll show you strong!"

        n "Hinano takes a deep breath."

        m "Hahaha yes show me!"

        n "Hinano closes her eyes and feels the blood coursing through her body."

        n "She opens her eyes, steps forward, and attacks with a large downward strike!"

        show hinano at middlerightmiddle with move

        n "Masataka attempts a quick block but it caves under her strength."

        m "Wha-"

        n "Masataka gets clipped by the strike before jumping away a few metres."

        show masataka at left with move

        m "Not bad... not bad at all."

        n "Hinano moves over to Sasaki."

        show hinano at right with move

        n "Are you alright Sasaki?"

        show sasaki at middleright with Dissolve(1)

        s "Yeah, I'm mostly fine."

    else:

        n "Masataka darts between the two, attacking them in turns."

        n "The pair find it difficult to find an opening faced with such intensity."

        n "Masataka ceases his strikes and motions for them to attack."

        n "The two allies nod at each other as they attempt to strike at the same time."

        n "Masataka realises Sasaki will hit first and counters him with a kick."

        n "Hinano attempts to capitalise on this but is met by a jump kick."

        n "The allies stand back wincing."

        m "Nice intensity, but..."

        n "He strikes them both nearly in the same instant."

        m "Not intense enough!"

        n "He demonstrates the same move a couple times, inflicting damage to the two."

        n "Sasaki notices a small opening in his moves."

        n "He looks at Hinano who nods in response."

        n "Hinano feigns a stumble, causing Masataka to hesitate in attacking Sasaki."

        n "As Masataka turns to redirect his attack, both of them spring towards him!"

        show hinano at middlerightmiddle 
        show sasaki at middleleftmiddle
        with move

        m "Wha-"

        n "Masataka takes a few hits before jumping a few metres away from the pair."

        show masataka at left with move

        m "Not bad... not bad at all."

        n "The other two stand back as well."

        show hinano at right
        show sasaki at middleright
        with move

        s "You alright?"

        h "Yes, you?"

        s "Yeah."

    n "Across the room Masataka is doing light stretches."

    h "What now?"

    menu:

        "Sasaki takes the lead":

            jump choice3_1

        "Hinano takes the lead":

            jump choice3_2

    label choice3_1:

        s "Follow my lead."

        h "Understood."

        m "I'm warmed up, how about round two?"

        n "Sasaki rushes Masataka and attacks."

        show masataka at middleleft
        show sasaki at middle
        with move

        if menu_flag2 == True:

            $ menu_flag3 = True

            $ menu_flag4 = True

            n "Sasaki and Masataka are locked in a dead heat as they both use lightning fast moves."

            show hinano at offright with move

            hide hinano

            n "Masataka starts to adjust to Sasaki's rhythm and pushes him back."

            show sasaki at middleright
            show masataka at middle
            with move 

            m "Is this all you can muster?!"

            h "Maybe... but maybe not all we can muster!"

            n "Sasaki retreats as Hinano returns."

            show hinano at offleft

            show sasaki at right with move

            show hinano at middleleft with move

            n "Masataka turns around."

            m "Hmpf, you think you stand better odds?"

            n "As Masataka goes to swing, Hinano narrowly dodges by jumping back."

            show hinano at left with move

            m "Where are you go-"

            n "Sasaki rushes Masataka and unleashs a volley of strikes to his back!"

            show sasaki at middleright with move

            m "Argh!"

            n "Masataka swings violently but Sasaki evades."

            show sasaki at right with move

        else:

            $ menu_flag3 = False

            $ menu_flag4 = False

            n "Sasaki loses ground quickly as he tries to face Masataka alone."

            n "Hinano rushes in behind Sasaki and starts sneaking in slashes between Sasaki's moves."

            show hinano at middlerightmiddle with move

            m "Hah! You think this puny offence stands a chance against me?"

            n "Masataka adjusts to their pattern and prepares to counterattack."

            n "The allies exchange a look as they change up their timimg."

            n "Masataka frowns as the two start to push him back."

            m "Persistent insects aren't you?"

            n "The allies continually change their fight patterns to overwhelm Masataka."

            m "Enough of this!"

            n "Masataka takes the brunt of a couple hits as he gets between them."

            show masataka at middle
            show sasaki at middleleftmiddle
            with move

            m "Huaarrrghhh!"

            n "Masataka does a wide swinging attack that forces the allies to dodge away."

            show hinano at right
            show sasaki at left
            with move

        jump choice3_done

    label choice3_2:

        $ menu_flag4 = False

        s "I'll follow your lead."

        h "Alright let's do this."

        m "I'm warmed up, how about round two?"

        n "Hinano rushes Masataka and attacks."

        show masataka at middleleft
        show hinano at middle
        with move

        if menu_flag2_5 == True:

            $ menu_flag3 = True

            $ menu_flag4 = False

            n "Hinano and Masataka are locked in a dead heat as they both use powerful slashes."

            show sasaki at offright with move

            hide sasaki

            n "Masataka starts to adjust to Hinano's power and pushes her back."

            show hinano at middleright
            show masataka at middle
            with move 

            m "Is this all you can muster?!"

            h "Tch, possibly... but I'm not alone!"

            n "Hinano takes a couple steps back as Sasaki advances."

            show sasaki at offleft

            show hinano at right with move

            show sasaki at middleleft with move

            n "Masataka turns around."

            m "Ha, you think you stand better odds?"

            n "As Masataka goes to swing Sasaki jumps back dodging it."

            show sasaki at left with move

            m "You can run but-"

            n "Hinano rushes Masataka and slashs him in the back!"

            show hinano at middleright with move

            m "Argh!"

            n "Masataka swings violently and makes Hinano jumps back."

            show hinano at right with move

        else:

            $ menu_flag3 = False

            $ menu_flag4 = True

            n "Hinano loses ground fast as she tries to face Masataka alone."

            n "Sasaki rushes in beside Hinano and starts sneaking in hits between Hinano's moves."

            show sasaki at middlerightmiddle with move

            m "Hah! You think this weak offence stands a chance against me?"

            n "Masataka adjusts to their pattern and prepares to counterattack."

            n "The allies exchange a look as they change up their timimg."

            n "Masataka frowns as the two start to push him back."

            m "Persistent bugs aren't you?"

            n "The allies continually change their fight patterns to overwhelm Masataka."

            m "Enough of this!"

            n "Masataka takes the brunt of a couple hits as he gets between them."

            show masataka at middle
            show hinano at middleleftmiddle
            with move

            m "Huaarrrghhh!"

            n "Masataka does a wide swinging attack that forces the allies to fall back."

            show sasaki at right
            show hinano at left
            with move

        jump choice3_done

    label choice3_done:

    n "The three warriors pant."

    h "We need to finish this."

    n "Sasaki nods."

    if menu_flag3 == True:

        m "Excellent. Truly Excellent."

    else:

        m "I grow tired of this."

    n "Masataka pulls out his dagger with his offhand as he shifts to an agressive fighting pose."

    m "It's time I go all out."
    
    if menu_flag2 == True:

        s "I think it's time you got serious too."

        h "I agree."

        n "Hinano closes her eyes and draws on every ounce of strength she has left."

        n "She opens her eyes as the three of them assume their battle positions."

    elif menu_flag2_5 == True:

        h "It's high time you showed him what you're capable of."

        s "Mmm."

        n "Sasaki closes his eyes and draws on every ounce of energy he has left."

        n "He opens his eyes as the three of them assume their battle positions."

    else:

        s "I think it's time we used everything we got too."

        h "Agreed."

        n "The two close their eyes and muster every ounce of strength and energy in their bodies."

        n "They open their eyes and assume their battle positions."

    if menu_flag3 == True:

        m "This has been quite the battle."

        m "Are you sure you won't tell me your names?"

        n "..."

        m "Very well."

    else:

        m "It is time to die nameless ones."

        m "Lament your regrets."

        m "And say your prayers."

    n "..."

    n "The three warriors engage in their final skirmish."

    if menu_flag4 == True:

        show sasaki at middleright
        show hinano at middleleft
        with move

    else:

        show hinano at middleright
        show sasaki at middleleft
        with move

    n "Sasaki strikes with lightning speed, but Masataka moves his dagger at the same pace."

    n "Meanwhile Hinano slashes with incredible strength, but Masataka holds a firm defence with his sword."

    n "Masataka switches it up, attacking Sasaki with strength and Hinano with speed."

    n "The two manage to put up a fair defence but they know they won't last long."

    if menu_flag2 or menu_flag2_5 == True:

        n "Sasaki falls to one knee as he blocks a strong strike."

        n "Hinano increases her speed by as much as she can to cover him."

        m "Meaningless!"

        n "Masataka parries her making her fall off balance."

        n "Sasaki desperately tries to cover for her but Masataka is too strong."

        m "Pointless!"

        n "Masataka kicks Sasaki away."

        if menu_flag4 == True:

            show sasaki at right with move

        else:

            show sasaki at left with move

        n "Masataka grins as he prepares to finish off Hinano."
        
        n "While his back is turned, Sasaki throws his nunchucks with all his might." 
        
        n "Masataka's sword arm is hit causing him to drop his sword."

        m "Insolent fo-"

        n "Masataka's eyes widen as Hinano puts everything she has into another slash."

        n "He desperately defends with his dagger."

        n "Hinano's sword cuts straight through it and him!"

        m "Arrrggghhhh!"

        n "He clutches his deep wound, as he falls to his knees, then collapses onto the floor."

        if menu_flag4 == True:

            show sasaki at middleright with move

        else:

            show sasaki at middleleft with move

    else:
        
        n "The two allies nod at each other."

        n "Hinano goes for a grand attack and Sasaki matches the timing."

        n "Masataka looks for an opening but doesn't find one!"

        m "Impossi-"

        n "He blocks both attacks with a grunt."

        n "The allies don't stop, and consecutively hit him at the same time."

        m "Tch!"

        n "Masataka attempts to strike Hinano during her wind-up."

        n "Sasaki cuts him off with extremely quick attacks."

        m "Damnit!"

        n "Masataka considers going for Sasaki instead."

        n "He realises if he does so he'll probably take a direct hit from Hinano."

        m "DAMNIT!!!"

        n "The two muster everything they have into a final coordinated strike."

        n "Masataka panics, deciding to put everything into blocking Hinano."

        n "Sasaki capitalises on this as he unleashes his strongest strike to Masataka's head!"

        n "An visceral crack is heard, as Masataka drops his weapons, and slumps onto the ground."
        
    hide masataka with Dissolve(0.6)

    stop music fadeout 2.0

    n "The two pant for a moment."

    n "Hinano leans down to confirm the kill."

    n "After she's done she nods at Sasaki."

    n "Sasaki's vision goes dark."

    scene black with Dissolve(0.6)

    n "Several hours later, Sasaki awakes."

    scene mansion3 with Dissolve(1)

    show sasaki at middle with Dissolve(1)

    s "Urgh."

    s "Di-did I blackout?"

    n "He realises his wounds are bandaged and that Hinano is nowhere to be seen."

    n "He feels something foreign in his kimono and removes it."

    s "She left me a note, how sweet."

    n "He opens it and reads its contents."

    n "..."

    s "Very well."

    n "Sasaki stands and takes his leave."

    scene black with Dissolve(0.8)

    play music "audio/tasogare.mp3" volume 0.05

    h "Sasaki,"

    h "I'm afraid I must take my leave for there are other matters I must attend to."

    h "I've dealt with the thugs in the building so you should be safe."

    if menu_flag2:

        h "Amane was nowhere nearby so I'll track him down before I move on."

    elif menu_flag2_5:

        h "I've taken Amane into my custody." 
        
        h "A fair trial is more than he deserves but those are the rules."

    else:

        h "Amane died of his wounds, serves him right."

    h "When I get back to the estate I'll file an inquiry on him and on this Ryuuji character."
    
    h "It was good to see again, perhaps next time we'll have a chance to reminisce about days gone."

    h "Stay well and stay strong."

    h "Your friend, Hinano."

    scene dirt road2 with Dissolve(0.8)

    n "As Sasaki left the village he found that the corrupt guards and thugs were already starting to lose their influence."

    n "Now that the immoral lord had been pacified, a garrison could now be dispatched by a competent lord nearby to ensure peace and prosperity."

    show sasaki at middle with Dissolve(0.7)

    s "What a beautiful day."

    n "He stands still, soaking in the rays of sunshine for a moment."

    n "..."

    s "Well, time for my next mission."

    hide sasaki with Dissolve(1)

    n "Sasaki walks off towards the next village in need of aid."

    show theend at truecenter with Dissolve(3)

    pause 4.0

    scene black with Dissolve(4)

    stop music fadeout 3.0

    pause 3.2

    # This ends the game.

    return