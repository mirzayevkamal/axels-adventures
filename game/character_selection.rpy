screen character_selection_screen():
    # Use the 'menu' tag to allow the player to go back to the main menu.
    tag menu

    # A background image for the screen.
    add "images/characters/bg.png"
    # Make sure to have a file named "bg_selection_screen.png" in your images folder.

    # A main frame to hold all the elements and center them on the screen.
    frame:
        xalign 0.5
        yalign 0.5
        background None
        padding (40, 40)

        # A vertical box to stack the title and the character selection.
        vbox:
            spacing 30
            xalign 0.5

            # The title of the screen.
            # A horizontal box to place the character buttons side-by-side.
            hbox:
                spacing 50
                xalign 0.5

                # Loop through the list of characters defined in characters.rpy.
                for char_data in selectable_characters:
                    # A vertical box for each character's image and name.
                    vbox:
                        spacing 10
                        xalign 0.5

                        # The clickable image button.
                        # When clicked, it sets the player_character_id variable
                        # and then jumps to the 'start' label to begin the game.
                        imagebutton:
                            idle Transform(char_data["image"])
                            hover Transform(char_data["image_hover"])
                            action [
                                SetVariable("player_character_id", char_data["id"]),
                                Return()
                            ]
                            hovered Play("sound", "menu_hover.mp3")


# Define some basic styles for the text on the screen.
style character_selection_title:
    size 48
    color "#FFFFFF"
    text_align 0.5

style character_selection_name:
    size 30
    color "#DDDDDD"
    text_align 0.5