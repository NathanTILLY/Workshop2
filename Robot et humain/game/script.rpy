# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrateur", kind = nvl)
define c = Character("Choix")
define r = Character("F4-112R")
define a = Character("Athénaïs ")
define m = Character("S1-25C")
define p = Character("P6-4D")


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

    n "Athenais se fait yeet de la cité et attérit en bas"

    nvl clear

    play sound "tumbleweed-sound-effect-hq.mp3"

    scene bg villedestroy

    show robot normal at right

    r "Ouah zebi un humain ... Qu'est ce que je fait avec ça ????"

    show athenais at left



    define menu = menu

    menu:

        c "Que faire de l'humain ?"

        "Récupérer l'enfant pour l'élever":
            r "Salut moi c'est F4-112R"
            r "Mhh ça à pas l'air facile pour toi aller je vais te prendre avec moi"
            a "Ca marche"

        "La laisser":
            a "Prend moi avec toi ou je te suis partout"
            r " bon ok"


    r "Bon allez vient on va se balader"

    show athenais at right

    show robot normal at right

    show robotbad at center

    r "Oh fuck un robot soldat"

    m "Blood for the blood god"



    menu:

        c "Que faire ?"

        "Fuire":
            r "taille Athenais taille taille taille"
            show athenais at left

            show robot normal at left

            m "Je vais vous fumer"

            r "Ah fuck il nous as vu cache toi dans cette botte de paille Athenais"

            show paille at left

            m "?????"

            m "Bah alors ils sont passé où"

            hide robotbad

            r "..."
            r "Il à l'air d'être partit"

            hide paille

            r "Ok goh continuer de se balader"

        "Se cacher":
            r "Viens on va se cacher dans cette botte de paille Athenais"

            show paille at right

            m "MHHHH rien a voir ici"

            hide robotbad
            r "..."
            r "Il à l'air d'être partit"

            hide paille

            r "Ok goh continuer de se balader"

    n "Après quelques heures de marche Athenais et F4-112R arrive devant une porte garder par un robot douanier"

    show bg porte

    show athenais at left

    show robot normal at left

    show robotdoaunier at center

    r "Salut mec tu nous laisse passer stp ?"

    p "Que venez vous faire ici ?"

    menu:
        "Dire la vérité":
            r "Je souhaite passer afin de ramener cette enfant chez elle"
            a "..."
            p"mhhh"
            p"et d'où elle vient cette enfant ?"
            menu:
                "de la cité des humains":
                    r "Elle vient de chez les humains habitant au dessus"
                    p "ouais ça fait du sens vous pouvez passer"

                    jump avecbras

                "je l'ai trouvé":
                    r "je l'ai trouvé dans une benne pas loin"
                    p "..."
                    p "tu te paie ma tronche gringo ???"
                    p "A toutes les unités ici P6-4D en charge de la porte 45B renégat repéré envoyer des renforts"

                    r "Oh la poucave vient Athenais on passe en force"

                    p "tu ne va nul part !"
                    hide bg porte
                    hide athenais
                    hide robot normal
                    hide robotdoaunier

                    show bg white
                    with Dissolve(2)

                    pause .5

                    r "Argh"

                    show bg porte

                    show athenais at right

                    show robot minusbras at right

                    a "F4-112R ! Ton bras !"

                    r "t'en occupe pas Athenais continue de courir"

                    hide athenais
                    hide robot minusbras

                    show robotdoaunier at center

                    p "..."
                    p "A toutes les unités le renégat se dirige vers la cité des humains"

                    jump sansbras

        "Mentir":
            r "Je souhaite passer afin de ramener cette enfant chez mon employeur"
            a "..."
            p "mhhh"
            p "et c'est qui votre employeur ?"
            menu:
                "réponse fun":
                    r "J34n C45tuX"
                    p "..."
                    p "tu te paie ma tronche gringo ???"
                    p "A toutes les unités ici P6-4D en charge de la porte 45B renégat repéré envoyer des renforts"

                    r "Oh la poucave vient Athenais on passe en force"

                    p "tu ne va nul part !"
                    hide bg porte
                    hide athenais
                    hide robot normal
                    hide robotdoaunier

                    show bg white
                    with Dissolve(2)

                    pause .5

                    r "Argh"

                    show bg porte

                    show athenais at right

                    show robot minusbras at right

                    a "F4-112R ! Ton bras !"

                    r "t'en occupe pas Athenais continue de courir"

                    hide athenais
                    hide robot minusbras

                    show robotdoaunier at center

                    p "..."
                    p "A toutes les unités le renégat se dirige vers la cité des humains"

                    jump sansbras
                "réponse sérieuse":
                    r "je vais livrer à C4B32 il a besoin de biocarburant pour un projet"
                    p "ouais ça fait du sens vous pouvez passer"

                    jump avecbras

        "Passer en force":
            r "Frérot t'a déjà entendu parler de l"
            r "DERRIERE TOI !!!"
            p "mmmmh?"
            r "taille taille taille Athenais on trace !"

            p "tu ne va nul part !"
            hide bg porte
            hide athenais
            hide robot normal
            hide robotdoaunier

            show bg white
            with Dissolve(2)

            pause .5

            r "Argh"

            show bg porte

            show athenais at right

            show robot minusbras at right

            a "F4-112R ! Ton bras !"

            r "t'en occupe pas Athenais continue de courir"

            hide athenais
            hide robot minusbras

            show robotdoaunier at center

            p "..."
            p "A toutes les unités le renégat se dirige vers la cité des humains"

            jump sansbras

    # This ends the game.

    return
