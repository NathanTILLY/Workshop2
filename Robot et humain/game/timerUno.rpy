

define d = Character("D1-11T")

label timerUno:

    "*F4 et Athénaïs après avoir, tant bien que mal, passé la porte ils s’enfoncent dans la ville mais se font ratrapper plus vite que prévu par un drone D1.*"

    $timeout_label = None
    menu:
        "Continuer de courrir":
            show robot bras at right
            show athenais at right

            "*F4 et Athénaïs commencent à courir à l’opposé du D1.*"

            "*Après quelques seconde de course F4 voit au loin, derrière le drone, des S1 et encore plus de D1 leur courir après.*"

            "*F4 et Athénaïs continuent leur course à l’opposé d’où se trouvent les S1 et D1.*"

            r   "Vite... cours Athénaïs... reste devant... Moi, je vais... servir de bouclier."

            "*La petite fille s'exécute et passe devant F4.*"

            "*Plusieurs balles sifflent à côté des capteurs de F4, mais aucune ne le touche.*"

            "Pendant cette intense course poursuite, des drones lacère les jambes de F4 à répétition, tandis que les S1 le mitraille de balle IEM pour l'immobiliser.*"

            "*A bout de force, F4 tombe au sol.*"

            r   "Continue... de courir... Athénaïs... ne t’occupe... pas de moi."

            "*Athénaïs entendant ces paroles, refuse et fait demi-tour pour l’aider.*"

            a   "Non F4, je ne t’abandonnerai jamais ! Je… Je ne veux pas te laisser"

            r   "Je t’en... supplie... fuis, ils... arrivent..."

            "*Alors que Athénaïs essaye de traîner F4, Les S1 et les D1 qui les poursuivaient les rattrapent.*"

            "AAAARGH... au... se...cours…"

            "*Les drones commencent à lacérer F4 de part en part, les membres de celui-ci volent en éclat dans un bruit atroce.*"

            "*Athénaïs assiste à ce spectacle horrifique avec impuissance. Elle essaye tant bien que mal de pousser les drones qui agresse F4, mais elle se fait attrapper et maîtriser par un S1.*"

            "*F4 dans une douleur atroce, pointe sa main vers Athénaïs essayant de la libérer des griffes du S1 mais en vain.*"

            r   " Laissez-la tranquille... je jure de... vous..."

            show bg noir

            hide robot

            hide athenais

            "*Avant même qu’il termine sa phrase F4 tombe au sol inerte, son œil robotique brisé laissant couler une larme d’huile...*"

            "*Pendant que les S1 et les D1 ayant accompli leur mission rentrent à la centrale avec l’enfant...*"

            "BAD ENDING"

            return





        "Tenter de duper le drone":

            "*F4 s’arrête et tente de duper le drone, grâce aux connaissances qu’il a sur ces derniers.*"




            r " je te paye un boulon si tu nous laisse tranquille"
            d " mhhh quel genre de boulon"
            menu:
                "cylindrique":
                    r "un boulon cylindrique ?"
                    d "jure un boulon cylindrique ? ça marche"
                    jump sbChemin2
                "hexagonale":
                    r "un boulon hexagonale ?"
                    d "niet je vais te croquer toi"

                    r "taille taille taille athenais"
                    "*chomp *"
                    r "AIE sale bête"
                    $timeout_label = "soldatEmbusquer"
                    menu:
                        "se cacher":
                            r "Il faut qu'on se cache Athenais trouve une cachette"
                            a "ok"
                            menu:
                                "se cacher dans  une benne":
                                    a "là bas il y a une benne go se cacher dedans"
                                    r "ok"
                                    jump soldatEmbusquer
                                "se cacher dans un tas de déchet":
                                    a " go se planquer sous un tas de déchet"
                                    r "ok"
                                    jump cacher
                        "Courir":
                            r " Huf huf"
                            r " t'arrete pas de courir Athenais"
                            jump soldatEmbusquer
