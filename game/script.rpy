label start:
    # We add a check here in case the user loads a game. If the ID is already
    # set, we can go straight to their story. Otherwise, we show the selection screen.
    if player_character_id is None:
        # The 'call screen' statement will pause the game until the player
        # makes a choice. The character_selection_screen uses Return()
        # to give control back here.
        call screen character_selection_screen

    # If after calling the screen, there's still no character, it means
    # the player went back to the main menu. We should stop execution.
    if player_character_id is None:
        return

    # After a character is selected, or if one was already selected (e.g., loaded game),
    # jump to the appropriate story based on the character ID.
    if player_character_id == "axel":
        jump axel_story
    elif player_character_id == "isabelle":
        jump isabelle_story
    elif player_character_id == "cody":
        jump cody_story


# The existing intro.rpy seems to be Axel's story.
label axel_story:
    jump intro

label isabelle_story:
    jump isabelle_intro

label cody_story:
    jump cody_intro