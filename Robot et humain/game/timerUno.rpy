image bg ville1 jour = "bg_ville1jour.png"

image bg ville2 jour = "bg_ville2jour.png"

define d = Character("D1-11T")


label timerUno:

    show bg ville1 jour

    show drone colere at left

    show robot bras peur at center

    show athenais peur at right

    "*F4 et Athénaïs après avoir, tant bien que mal, passé la porte s’enfoncent dans la ville mais se font ratrapper plus vite que prévu par un drone D1.*"

    $timeout_label = "mortUno1"
    $timeout = 3.00
    menu:
        "Continuer de courir":

            jump mortUno1

        "Tenter de duper le drone":

            "*F4 s’arrête et tente de duper le drone, grâce aux connaissances qu’il a sur ces derniers.*"

            $timeout_label = None

            menu:
                "*Prendre un chemin impraticable.*":

                    "*F4 et Athénaïs se ruent vers un chemin impraticable pour eux et pour le drone, mais se cachent au dernier moment pour le duper.*"

                    hide drone

                    "*Arrivé au niveau de l'impasse, le drone ne voit plus ses cibles et fait demi-tour pour continuer ses recherches.*"

                    "*Après avoir semé le drone F4 et Athénaïs reprennent leur route.*"

                    jump courir

                "*Continuer sur la route.*":

                    "*F4 prend Athénaïs par la main et commence à courir avec elle.*"

                    "*Après quelques instants de course poursuite, F4 se rend compte qu’ils ont perdu le drone de vue.*"

                    show robot bras neutre

                    show athenais neutre

                    r   "Je… crois… qu’on l’a… semé."

                    show drone colere at left

                    show robot bras jambe peur

                    "*Avant même qu’Athénaïs ne puisse répliquer, le drone surgit et attrape la jambe de F4. Il commence à le mordre pour l’arracher.*"

                    "*Athénaïs voit au loin des S1 et des D1 arriver et prévient F4.*"

                    a   "Vite F4, d’autres robots méchants arrivent !"

                    $timeout_label = "finTimerTimerUno1"
                    $timeout = 3.00
                    menu:

                        "*Rentrer dans un bâtiment.*":

                            $timeout_label = None

                            hide drone

                            "*F4 et Athénaïs se débarrassent du drone qui attaquait la jambe de F4 et se précipitent à l’intérieur d’un bâtiment proche pour se cacher.*"

                            show robot bras jambe peur at left

                            "*Après le passage des S1 et des D1, ils décident de continuer leur route prudemment.*"

                            show athenais neutre

                            a   "Dis F4, tu faisais quoi avant de me trouver ?"

                            show robot bras jambe neutre

                            r   "Je ramassais... des ordures... et des débris... qui tombaient du ciel... comme toi."

                            a   "Alors je suis un débris ?"

                            r   "Euh... Non... Je ne voulais pas... Dire ça, un débris... C’est moche... Et c’est en métal..."

                            show athenais joie

                            a   "Oh ? Alors je suis jolie et pas en métal ?"

                            show robot bras jambe joie

                            r   "Oui... Toi, tu es jolie et en chair."

                            show athenais neutre

                            a   "Mais toi t’es en métal ? Donc t’es un débris ?"

                            show robot bras jambe gene

                            r   "Oui je... Suis en... Métal, mais est… Ce que… Je suis… Moche ? Si oui... Alors, je suis un débris."

                            show athenais joie

                            a   "Non je te trouve beau moi ! Donc t’es pas un débris !"

                            show robot bras jambe joie

                            r   "Mer... Ci."

                            jump cacher


                        "*Tenter de se cacher.*":

                            $timeout_label = None

                            hide drone

                            "*F4 et Athénaïs se débarrassent du drone qui attaquait la jambe de F4 et se cache dans les hautes herbes à proximité.*"

                            r   "Attention...  ils arrivent... j’espère qu’ils... ne nous... verrons pas..."

                            "*F4, dans la précipitation, ne réussit pas à se camoufler entièrement et se fait repérer par un S1 embusqué qui lui tire dessus."

                            "*Après avoir reçu cette balle, F4 ordonne à Athénaïs de courir.*"

                            r   "Vite... cours Athénaïs... reste devant... Moi, je vais... servir de bouclier."

                            jump soldatEmbusquer

                        "*Fuir.*":

                            hide drone

                            "*F4 et Athénaïs se débarrassent du drone qui attaquait la jambe de F4 et commencent à courir dans la direction opposée des S1 et de D1 et se cache dans les hautes herbes à proximité.*"

                            "*F4, dans la précipitation, ne réussit pas à se camoufler entièrement et se fait repérer par un S1 embusqué qui lui tire dessus."

                            "*Après avoir reçu cette balle, F4 ordonne à Athénaïs de courir.*"

                            r   "Vite... cours Athénaïs... reste devant... Moi, je vais... servir de bouclier."

                            "*La petite fille s'exécute et passe devant F4.*"

                            "*Plusieurs balles sifflent à côté des capteurs de F4, mais aucune ne le touche.*"

                            "*Pendant la course, F4 vérifie l’endroit où il a reçu la balle il ne décèle rien de particulier et continue donc sa course.*"

                            jump soldatEmbusquer


label finTimerTimerUno1:

    hide drone

    "*Alors qu’il essayait d’enlever le drone accroché à sa jambe, F4 reçoit une balle, il arrive tout de même à arracher le drone de sa jambe et commence à courir avec Athénaïs.*"

    "*Après quelques minutes de course F4 se rend compte que les S1 et les D1 ont arrêté de les poursuivre.*"

    "*Il décide de vérifier l’endroit où il a reçu la balle mais ne décèle rien de particulier, il continue alors d’avancer vers le câble avec Athénaïs.*"

    "*En marchant vers ce dernier, Athénaïs commence à se questionner sur le passé d’F4.*"

    a   "F4, j’ai une question, est ce que toi aussi t’as des parents ?"

    "F4 se retourne et pointe du doigt la décharge."

    r   "Je sors d’une... Usine... Donc si j’ai des parents... je ne les ai pas connus... "

    r   "Mes créateurs... sont des machines..."

    a   "Donc tu n’as jamais eu de vraie famille...?"

    r   "Non... Pas vraiment..."

    a   "T’aimerais en avoir une ?"

    r   "Oui... j’aimerais bien... connaître... cela."

    a   "Je veux bien être ta famille si tu veux !"

    a   "T’es d'accord ?"

    r   "Oui... J’approuve cette... proposition"

    a   "Trop bien, on t’a trouvé une famille !"

    jump soldatEmbusquer



label mortUno1:

    "*F4 et Athénaïs commencent à courir à l’opposé du D1.*"

    show douane colere at left behind drone

    show robotbad colere2 at left behind douane

    "*Après quelques seconde de course F4, voit au loin, derrière le drone, des S1 et encore plus de D1 leur courir après.*"

    "*F4 et Athénaïs continuent leur course à l’opposé d’où se trouvent les S1 et D1.*"

    r   "Vite... cours Athénaïs... reste devant... Moi, je vais... servir de bouclier."

    "*La petite fille s'exécute et passe devant F4.*"

    "*Plusieurs balles sifflent à côté des capteurs de F4, mais aucune ne le touche.*"

    "Pendant cette intense course poursuite, des drones lacèrent les jambes de F4 à répétition, tandis que les S1 le mitraillent de balle IEM pour l'immobiliser.*"

    "*A bout de force, F4 tombe au sol.*"

    r   "Continue... de courir... Athénaïs... ne t’occupe... pas de moi."

    "*Athénaïs entendant ces paroles, refuse et fait demi-tour pour l’aider.*"

    a   "Non F4, je ne t’abandonnerai jamais ! Je… Je ne veux pas te laisser"

    r   "Je t’en... supplie... fuis, ils... arrivent..."

    "*Alors que Athénaïs essaye de traîner F4, les S1 et les D1 qui les poursuivaient les rattrapent.*"

    "AAAARGH... au... se...cours…"

    "*Les drones commencent à lacérer F4 de part en part, les membres de celui-ci volent en éclat dans un bruit atroce.*"

    "*Athénaïs assiste à ce spectacle horrifique avec impuissance. Elle essaye tant bien que mal de pousser les drones qui agressent F4, mais elle se fait attraper et maîtriser par un S1.*"

    "*F4 dans une douleur atroce, pointe sa main vers Athénaïs essayant de la libérer des griffes du S1 mais en vain.*"

    r   " Laissez-la tranquille... je jure de... vous..."

    show bg noir

    hide drone

    hide robotbad

    hide douane

    hide robot

    hide athenais

    "*Avant même qu’il termine sa phrase F4 tombe au sol inerte, son œil robotique brisé laissant couler une larme d’huile...*"

    "*Pendant que les S1 et les D1 ayant accompli leur mission rentrent à la centrale avec l’enfant...*"

    "BAD ENDING"

    return
