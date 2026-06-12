## Please turn on word-wrap (usually alt+Z). This makes reading these ## comments ## much easier

## These hashes/pounds # are the start of comments. Everything put after these # is ignored by the engine until the next line. I use these to explain code and/or leave notes for future me.

## This is a .rpy script which is basically a .txt file that is compiled when ran inside a Ren'Py project. Once MAS is ran, the .rpy turns into a .rpyc file. You can create a .rpy file by turning on file extensions in windows. Open the file explorer, click view towards the top then check the box that says "File name extensions". Then create a .txt file then delete the .txt and replace it with .rpy. So example.txt => example.rpy

## The easiest way to get started it to read the comments then copy this first "makemesmile" example and replace it with your own words and names.

init 5 python:  ## This is preparing the engine for some sort of data
    addEvent(   ## You are telling the engine that you have an event (dialogue) you want to add
        Event(  ## You are telling the engine everything about this event between these purple brackets
            persistent.event_database,
            eventlabel="dh_mascomp_makemesmile", ## This is the first half of the compliment where you set up the technical parts. You will use this later.
            category=['mas_compliment'], ## This tells MAS which catergory to put this dialogue in. mas_compliment will put the dialogue in the compliment folder
            prompt="You always make me smile [m_name]", ## The prompt is what you see when opening the compliment menu. The [m_name] has two parts. The brackets [] mean you're calling some sort of variable. The part inside the brackets is the variable you're calling. For getting your Monika's nickname, you use m_name inside [square brackets].
            unlocked=True ## This means that at the start of the game, you are able to say this to her
            ),
            code="CMP" ## The code is for organization into the compliment events folder
            )

label dh_mascomp_makemesmile: ## label is what the games engine, Ren'Py, uses for it's movement commands. It's like a bookmark to a paragraph in a physical book. This is also the second part of the compliment where you write the actual words you want Monika and/or yourself to say.
    m 5ekbsb "I'm glad I can make you smile [mas_get_player_nickname()]..." ## There's a lot in this sentence so lets start with the m. m is the way MAS represents that Monika is saying something. In Ren'Py, you declare a character to be something, usually a letter or two, then call that for every line of dialogue. This is to prevent having to write Monika 100,000 times in a normal visual novel. The string of letters and numbers, (in this case 5ekbsb) is what I call an expression code, it tells the engine how to render Monika. This code is what you'll want the dev_expressions installed for. finally you have the easiest part, the quotation marks. Put dialogue in the quotation marks "like so" and she will say it. The last bit [mas_get_player_nickname()] is checking for your nickname and putting it here.
    m 4hub "You mean the world to me, so making you happy makes my day" ## With what we learned, we put m to make Monika speak, 4hub to make her look a certain way, then "dialogue in quotation marks" to make the words she will say
return  ## return is telling the engine that the dialogue is over and that it needs to return to normal function. You place this at the end of your labels.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dh_mascomp_heartrace",
            category=['mas_compliment'],
            prompt="You always make my heart race [m_name]",
            unlocked=True
            ),
            code="CMP"
            )

label dh_mascomp_heartrace:
    m 2wsbfsdlb "Ah, that's a bit embarrasing [player], but thank you" ## [player] is checking for your name, this is different from your nickname
    m 2lkbfsdlb "I don't even know how to respond! You flatter me so much~"
    m 1eubsb "You make my heart race too [player], every single day"
    return


## dh_mascomp_wonderful event here
##








## I want you to try and write two things here. An event labled dh_mascomp_wonderful before this comment, and two labels titled dh_mascomp_wonderful_2 and dh_mascomp_wonderful_3 after the dh_mascomp_wonderful label. If done correctly, you'll have your first submod officially written.

label dh_mascomp_wonderful: ## Well what if I want to have two seperate dialogues for if I've already said this to Monika? You can create a buffer label like this
    if not renpy.seen_label("dh_mascomp_wonderful_2"):  ## Then check for if you've already seen it. The 'not' checks that this condition is not true. The renpy.seen_label("") checks if you've already visited that label. So this is asking, hey have I been here before? If the answer is yes, then it goes down the first path and calls dh_mascomp_wonderful_2
        call dh_mascomp_wonderful_2 ## This would be the first time you experience calling her wonderful, so we can give her special first experience dialogue
    else:
        call dh_mascomp_wonderful_3 ## If the check fails, as in you've already seen the first event, then you see this one
    return  ## You can also do this all in one dialogue by adding the if else statements at the start but this is cleaner looking.

## wonderful 2 and 3 here













## What if I want to do things like italics and suspensful waiting? Well there are commands for that too!







## label dh_logit:
##     m 3rubsd "Hey [player], how do trees remember a date?"
##     m 3eubsd "They {w=1.5} {i}log{/i} it." ## The {w=number} tells the engine to delay displaying the next line for that number of seconds. The {i}word{/i} italicizes the word between the two i's
##     return   ## This is commented out since Ren'Py likes to throw errors if it doesn't have both pieces of a puzzle, and it doesn't really belong in the compliments does it?



## But I want to say something to Monika. How do I do that?