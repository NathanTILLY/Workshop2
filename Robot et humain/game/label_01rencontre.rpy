label rencontre:

    scene bg ville

    n   "En l’an 3000, à la suite d’une rébellion des robots, les humains ont dû se réfugier dans des cités volantes. Notre histoire se déroule un siècle plus tard au pied de la cité Elkjaer."
    n   "Le gouvernement en place à mis en œuvre une politique d'enfant unique suite à la surpopulation de la ville. Dès leur plus jeune âge, les enfants se font éjecter dans les tréfonds du bas monde."
    n   "Dans ce monde où la présence humaine n'est plus, les robots sont maîtres : ils se servent des \"offrandes\" du monde d'en haut pour survivre."
    n   "Ils récupèrent les capsules dans lesquelles se trouvent les enfants, puis ils utilisent leur énergie vitale comme combustible pour leur propre survie."

    nvl clear

    scene bg villedestroy

    play sound "tumbleweed-sound-effect-hq.mp3"

    show robot neutre at center

    r   "C'est l'heure... Je dois y..."
    r   "Retourner..."

    "*Quelques douloureuses heures plus tard.*"

    r   "Qu'est-ce que...?"

    "*Il aperçoit une capsule, un enfant piègé en son sein.*"

    r   "Je dois... Sortir... L'être de chair... De là."

    "*Il sort l'enfant de la capsule.*"

    show robot neutre at left

    show athenais triste at right

    ath   "Papa, maman... J’ai peur où êtes vous ?"

    "*Elle commence à pleurer.*"

    "\"Alerte, alerte, défaillance système, anomalie détectée. Unité F4 vous devez regagner la centrale, votre système est sûrement endommagé.\""


    menu:

        "*Couper la connexion avec la centrale.*":

            r   "Viens petite... Ca va... On va retrouver tes... Parents."

            "*La fille se calme.*"

            show athenais contente

            ath   "Merci, monsieur le robot..."

        "*Se rendre à la centrale.*":

            r   "Je dois retourner à… Centrale, bon courage… Petite."

            ath "Me laisse pas toute seule, j'ai si peur !"

            r   "Désolé, mais je dois vraiment retourner à la centrale."

            "*La fillette s'accroche la jambe du robot.*"

            ath "Je veux rester avec toi... Ne me laisse pas..."

            "*Insupporté par le bruit de l'alerte, le robot décide de retirer sa puce.*"

            r   "Viens petite... Ca va... On va retrouver tes... Parents."

            "*La fille se calme.*"

            show athenais contente

            ath "Merci, monsieur le robot..."

    r   "Je suis l'unité F4... Numéro 112... De la brigade des récupérateurs... Et toi, quel... est ton... matricule ?"

    ath "Je... je ne me souviens plus..."

    r   "Que dirais tu de... H1-1F ?"

    show athenais neutre

    ath "Euh… je suis pas un robot moi."

    "*F4 trouve une page déchirée d’un livre parlant d’une divinité.*"

    r   "A... Thé... Naïs... Athénaïs ?"

    show athenais contente

    a   "Oui, j’aime beaucoup, c’est joli."

    "*F4 marche avec Athénaïs vers la porte de la décharge.*"

    m   "Unité F4-112R, arrêtez-vous !"

    "*F4 s’arrête avec Athénaïs.*"

    show robotbad at center

    show athenais peur

    m "Veuillez retourner à la centrale pour effectuer une maintenance et remettez nous l’enfant, premier avertissement."

    r   "Qu’allez vous... Faire de la petite... ?"

    show robot neutre at right

    show athenais peur at right behind robot

    "*F4 protège Athénaïs avec son corps.*"

    m   "Veuillez retourner à la centrale pour effectuer une maintenance et remettez-nous l’enfant. Dernier avertissement avant désactivation."

    "*Un autre officier mécanique interpelle votre assaillant, vous avez une dizaine de secondes devant vous.* "

    $ timeout = 10.0

    $ timeout_label= "start"

    menu:

        "balader":

            "bla"

        "balader":

            "bla"

    jump start



python:
    """

____________________________________________________________________________________________________





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


    """




return
