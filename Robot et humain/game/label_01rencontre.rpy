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

    show robotbad neutre at center

    show athenais peur

    m "Veuillez retourner à la centrale pour effectuer une maintenance et remettez nous l’enfant, premier avertissement."

    r   "Qu’allez vous... Faire de la petite... ?"

    show robot neutre at right

    show athenais peur at right behind robot

    "*F4 protège Athénaïs avec son corps.*"

    show robotbad colere1

    m   "Veuillez retourner à la centrale pour effectuer une maintenance et remettez-nous l’enfant. Dernier avertissement avant désactivation."

    show robotbad2 neutre at left

    "*Un autre officier mécanique interpelle votre assaillant, vous avez une dizaine de secondes devant vous.* "

    $ timeout = 10.0

    $ timeout_label= "cachette"

    menu:

        "*Fuir.*":

            "*F4 et Athénaïs commencent à courir en direction de la porte*"

            show robotbad colere2

            show robotbad2 colere1

            m   "HALTE ! A toutes les unités disponibles, le F4 est en fuite, il a un humain avec lui !"

            "*Commence à courir après F4 et Athénaïs.*"

            r   "Vite... cours... Athénaïs..."

            "*Athénaïs court de mieux possible, mais commence à être essoufflée.*"

            jump cachette

        "*Se cacher.*":

            jump cachette


label cachette:

    hide robotbad

    hide robotbad2

    show robot at left

    r   "Cache toi... ici..."

    "*F4 Montre la direction d’une épave de voiture.*"

    hide athenais

    "*Il la place sous l’épave puis se glisse au milieu des débris de robots.*"

    "*Quelques minutes plus tard, après avoir semé les gardes, F4 retourne chercher Athénaïs.*"

    r    "Ca... va... petite ?"

    show athenais neutre

    a   "Oui, merci de m'avoir aidée."

    r   "Méfie-toi... Ils sont encore proches."

    show bg porte

    r   "Il... faut... qu’on passe... cette porte..."

    a   "Qu’est-ce qu’il y a derrière cette porte ?"

    r   "Je…je ne… sais pas… C’est notre seule… issue."

    $ timeout_label= None

    menu:

        "*Courir vers la porte.*":

            r   "Cours... Toujours tout droit...Et ne t'arrête... Pas."

            "*Athénaïs passe la porte suivie par F4.*"

            show douane neutre at left

            show douane2 neutre at right

            hide athenais

            hide robot

            p   " Je crois qu’ils viennent de passer la porte."

            p   "Ah ! Je pensais que tu ne les avais pas vus..."

            "*Les P6-4D lancent une alarme qui alerte les S1 à proximité.*"

            jump suiteVerte


        "*Mentir aux douaniers.*":

            p   "Veuillez vous identifier."

            r   "Je suis l’unité F4... Numéro 112... de la brigade des récupérateurs..."

            p   "Que faites vous ici ?"

            $ chanceDePasser = 50

            menu:

                "\"Je... dois... passer.\"":

                    $ chanceDePasser = chanceDePasser - 10

                "\"La centrale... m'a... demandé d'amener... cette chose... hors de la... décharge.\"":

                    $ chanceDePasser = chanceDePasser + 10

            p   "Hum, très bien et où amenez vous cette chose ?"

            "*Il pointe l'enfant du doigt.*"

            menu:

                "\"La centrale… m’a… demandé de l'exécuter... à l’extérieur... de la décharge\"":

                    $ chanceDePasser = chanceDePasser - 20

                "\"Vous... n’avez pas... besoin de le... savoir\"":

                    $ chanceDePasser = chanceDePasser + 30

            a   "Ils me font peur..."

            "*Athénaïs pointe les douaniers du doigt.*"

            p   "OH ! La chose parle ! Qu’est ce que c’est que ce truc ?"

            menu:

                "\"Notre pire... cauchemar... c’est pour... cela que... je dois l’éliminer...\"":

                    $ chanceDePasser = chanceDePasser + 20

                "\"C’est un... enfant, je... dois l’éliminer...\"":

                    $ chanceDePasser = chanceDePasser - 50

            "*L’un des douaniers reçoit un appel.*"

            "\"A toutes les unités, une unité F4 et un enfant sont en fuite.\""

            if (chanceDePasser >= 50):

                p   "Je crois qu'on les a laissés partir..."

                p   "On prévient la centrale ?"

                p   "On risque pas de se faire engueuler ?"

                p   "Oups..."

                jump suiteBleue

            else:

                p "Veuillez patienter quelques instants, nous allons procéder à des vérifications supplémentaires."

                "*L’un des P6 appel discrètement une unité de S1.*"

                "*Après quelques minutes, une patrouille de S1 arrive à la porte.*"

                "*F4 les repère et commence à courir avec Athénaïs.*"

                jump suiteVerte

        "*Dire la vérité aux douaniers.*":

            $ chanceDePasser = 50

            p   "Veuillez vous identifier."

            r   "Je suis l’unité F4... Numéro 112... De la brigade des récupérateurs..."

            p   "Que faites-vous ici ?"

            menu:

                "\"Je... dois ramener... cette enfant... chez elle...\"":

                    $ chanceDePasser = chanceDePasser + 10

                "\"Je... dois passer... avec l’enfant...\"":

                    $ chanceDePasser = chanceDePasser - 10

            p   "Hum, très bien et où amenez vous cette chose ?"

            "*Il pointe l'enfant du doigt.*"

            menu:

                "\"Je... la ramène à la... cité volante, pour... qu’elle retrouve... sa famille.\"":

                    $ chanceDePasser = chanceDePasser + 30

                "\"Je... dois la sortir... de la décharge.\"":

                    $ chanceDePasser = chanceDePasser - 20

            a   "Il est mignon lui avec sa tête."

            "*Elle pointe l’un des douaniers du doigt.*"

            p   "OH ! Merci bien petite chose !"

            p   "Mais qu'est-ce qu'un enfant ?"

            menu:

                "\"Un... humain, qui ne doit... pas être la.\"":

                    $ chanceDePasser = chanceDePasser - 50

                "\"Un humain... fragile, qui a besoin... de sa famille.\"":

                    $ chanceDePasser = chanceDePasser + 30

            "*L’un des douaniers reçoit un appel.*"

            "\"A toutes les unités, une unité F4 et un enfant sont en fuite.\""

            if (chanceDePasser >= 50):

                p   "Je crois qu'on les a laissés partir..."

                p   "On prévient la centrale ?"

                p   "On risque pas de se faire engueuler ?"

                p   "Oups..."

                jump suiteBleue

            else:

                p "Veuillez patienter quelques instants, nous allons procéder à des vérifications supplémentaires."

                "*L’un des P6 appel discrètement une unité de S1.*"

                "*Après quelques minutes, une patrouille de S1 arrive à la porte.*"

                "*F4 les repère et commence à courir avec Athénaïs.*"

                jump suiteVerte


















$"""

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
