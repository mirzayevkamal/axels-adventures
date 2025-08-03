# Declare characters used by this game.
define a = Character("Axel")
define i = Character("Isabelle")
define c = Character("Cody")
define ch = Character("Chad")

# Intro text style
style intro_text:
    size 38
    color "#FFFFFF"

# Positioning transforms
transform top_text:
    xalign 0.5
    yalign 0.2

transform center_text:
    xalign 0.5
    yalign 0.5

transform bottom_text:
    xalign 0.5
    yalign 0.85

# Background pan and zoom effect
transform pan_zoom:
    zoom 1.2
    xalign 0.5
    yalign 0.5
    linear 15.0 zoom 1.0 xalign 0.4 yalign 0.45

# Start of the game
label start:

    scene story_1 at pan_zoom with dissolve
    pause 1.0

    show text "Once upon a time, in the scorching heat of the far western deserts, there was an army of soldiers, toiling tirelessly, bound by a deep sense of loyalty to their country, serving its security." at top_text with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    show text "Months under harsh conditions, uncertain and difficult weather, and at times hunger, not to mention the longing they felt being separated from their families, were already tough." at center_text with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    show text "But what truly disturbed them, wore down their nerves, and sometimes made them willing to even take their own lives, was living under the command of someone they feared." at bottom_text with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    scene story_2 
    pause 1.0

    show text "Yes, you heard that right. Someone they feared so much they'd rather take their own lives. A man who considered himself the alpha male in a pack of wolves; cunning, self-centered, demeaning even to other men to prove his own dominance, overly confident, strong, masculine, and, in a strange way, incredibly attractive despite all his wickedness." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_3 at pan_zoom with dissolve
    pause 1.0

    show text "Beyond all these traits, perhaps it was the tension brought on by high testosterone, which he sought to alleviate in many ways. His flirtatiousness and dominance must have been at an extreme level, as he had subjugated all the women in the army, from secretaries to nurses." at bottom_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_4 
    pause 1.0
    
    show text "Once, upon discovering that a soldier was in love with a nurse, he took the girl into his room and, in front of the soldier, had sex with her, shouting: 'All the women here belong to me!' and humiliated the soldier in front of the girl." at bottom_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_5 at pan_zoom with dissolve
    pause 1.0

    show text "For Axel, these were not problems. He would invite young nurses and secretaries to his room, charm them, and have sex with them without mercy. Anyone who tried to challenge him would fail." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    show text "And the strangest part was that the women who initially seemed to resist him were actually just putting on a show, secretly burning with desire for him to have sex with them. Immediately afterward, they would willingly ask him to do it. Some would even beg him and try to sneak into his room at night." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_6 at pan_zoom with dissolve
    pause 1.0

    show text "Yes, he made his soldiers endure hard times, and as for the women, he had reduced them to mere tools for his pleasure. The girls he had sex with would tell no one. If word got out, he would be in trouble, and he wouldn't stand for it." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_7 
    pause 1.0

    show text "The severe and sometimes humiliating punishments he inflicted on the soldiers must have been truly cruel, as no one dared to defy him. Months chased each other, and the days in the tormented army seemed endless." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_8 at pan_zoom with dissolve
    pause 1.0

    show text "Occasional thirst and hunger made everything even harder for the soldiers. Rumors began to circulate in the army: if a soldier wanted extra food and water, they had to be Axel's guest for a night, and when Axel had sex with the nurses, the soldier had to play along with their fantasies." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_9 
    pause 1.0

    show text "But this obligation later transformed into pleasure. As days passed, it was even rumored that he would line up 5-6 women at once in his room and have sex with them. The moans coming from his room at night did not fail to frighten the other soldiers." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_10 
    pause 1.0

    show text "But despite everything, the women were still proud to be under his muscular, large body. They themselves were surprised at how they had come to this. Was it a devil's charm, or was it his ability to be both very dark and alluring at the same time...?" at center_text with dissolve 
    $ renpy.pause(10.0)
    hide text with dissolve

    scene story_11 at pan_zoom with dissolve
    pause 1.0

    show text "The soldiers who were secretly Axel's sex slaves knew these rumors were true, because Axel enjoyed all of it. It was even said that some couldn't bear the thirst and found themselves in Axel's room." at center_text with dissolve
    $ renpy.pause(10.0)
    hide text with dissolve

    play movie "videos/army.webm" loop
    scene movie with dissolve

    pause 5  
    
    stop movie

    play movie "videos/army_two.webm" loop
    scene movie with dissolve

    pause 5  
    
    stop movie

    return
