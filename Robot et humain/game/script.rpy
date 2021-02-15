# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrateur", kind = nvl)
define c = Character("Choix")
define r = Character("F4-112R")
define h = Character("Athénaïs ")
define m = Character("S1-25C")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg ville

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    n "Année 3100"

    n "Elkjaer, dernier bastion de l'humanité"

    n "Athenais se fait dégage de la cité et attérit en bas"

    scene bg villedestroy

    show robot normal

    r "Ouah zebi un humain ... Qu'est ce que je fait avec ça ????"

    define menu = menu

    menu:

        c "Que faire de l'humain ?"



        "Coup de botte.":

            nvl clear

            r "Voila qui est fait"

        "Receuillir":

            nvl clear

            r "Bon bah je supose que je vais m'en occuper"


    # This ends the game.

    return
