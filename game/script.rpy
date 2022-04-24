# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bb = Character("Bret")
define mc = Character("MC")
# The game starts here.

label start:
    $ a = "apple"
    $ inv = [a,"aopple"]
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    mc "Hello?"

    mc "Anyone there?"

    show bret_sexy
    with fade

    "???" "Hey there!"

    mc "Who are you? Where am I?"

    "???" "Well..."

    "???" "My name is Bret..."

    scene bret_laboratory

    show bret_offer

    bb "... and you're in my lab!"

    menu:
        "As I wake up, I say..."

        "WHAT THE HAY MAN!?":
            jump dinner

        "Why am I here?":
            jump dinner

        "Show inventory":
            "[inv[0]]"
            jump dinner




label dinner:

    mc "WHAT THE HECK MAN!? YOU CAN'T JUST DO THAT!"

    bb "Why yes I can!"

    bb "Come with me."

    # Come with what now!?

    hide bret_offer
    show bret_smug
    with fade

    bb "Do you want something to eat? Fruit snacks? Pizza rolls?"

    menu:
        "I want..."

        "vent":
            $ snack = "vent"
            jump fruit_snack

        "Pizza Rolls":
            $ snack = "hot"
            jump fruit_snack

        "Sorry, I'm not hungry...":
            $ snack = "boring"
            jump fruit_snack


    label fruit_snack:
    if snack == "vent":
        bb "Ohhh so you're a vent type."
        bb "I'll remember that"
    bb "This is the end of what's done so far. You will be sent to the menu momentarily."

    return


