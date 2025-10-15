init:
    # Character dialogue definitions
    define axel = Character("Axel", window_background=Transform("gui/txtbg2.png", xysize=(1400, 300), xalign=0.5, yalign=0.2), what_slow_cps=30, what_color="#000000", what_size=28, what_ypos=100, who_bold=True, who_color="#1a1a1a", who_size=39)
    define isabelle = Character("Isabelle", window_background=Transform("gui/txtbg2.png", xysize=(1920, 278)), what_size=28, what_slow_cps=30, who_xpos=-60, who_ypos=30,who_bold=True, who_color="#1a1a1a", who_size=35)
    define cody = Character("Cody", window_background=Transform("gui/txtbg2.png", xysize=(1920, 278)), what_size=28, what_slow_cps=30,who_xpos=-60, who_ypos=30,who_bold=True, who_color="#1a1a1a", who_size=35)
    define narrator = Character(None, window_background="gui/textbox.png", what_slow_cps=30, window_yalign=1.0, what_yalign=0.5,who_xpos=-60, who_ypos=30,who_bold=True, who_color="#1a1a1a", who_size=35)
    define tobby = Character("Tobby", window_background=Transform("gui/txtbg2.png", xysize=(1920, 278)), what_size=28, what_slow_cps=30, who_xpos=-60, who_ypos=30,who_bold=True, who_color="#1a1a1a", who_size=35)
    define valerie = Character("Valerie", window_background=Transform("gui/txtbg2.png", xysize=(1920, 278)), what_size=28, what_slow_cps=30, who_xpos=-60, who_ypos=30,who_bold=True, who_color="#1a1a1a", who_size=35)

    define selectable_characters = [

        {
            "name": "Axel",
            "image": "images/characters/axel.png",
            "image_hover": "images/characters/axel_hover.png",
            "id": "axel"
        },
        {
            "name": "Isabelle",
            "image": "images/characters/isabelle.png",
            "image_hover": "images/characters/isabelle_hover.png",
            "id": "isabelle"
        },
        {
            "name": "Cody",
            "image": "images/characters/cody.png",
            "image_hover": "images/characters/cody_hover.png",
            "id": "cody"
        }
    ]

    default player_character_id = None