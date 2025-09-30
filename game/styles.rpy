# Intro text screen with outline
screen intro_text(text_content, ypos=0.5):
    text text_content:
        size 38
        color "#FFFFFF"
        outlines [(4, "#000000", 0, 0), (2, "#000000", 2, 2)]
        text_align 0.5
        xalign 0.5
        yalign ypos

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