

label sansbras:
    show bg villedestroy
    show robot minusbras at right
    show athenais at right
    "*Après avoir passé la porte, F4 et Athénaïs arrivent dans l’ancienne ville humaine dans laquelle la nature a repris ses droits*"
    $timeout_label = "timerUno"
    menu:
        "Continuer à avancer":

            r "let's go on avance"
            $timeout_label = None
            menu:
                "se retourner":
                    r " Je me demande si on est poursuivi voyons voir"
                    r " je vais monter sur cette pile pour scout la zone Athenais bouge pas"
                    "*grimpe*"
                    r " ok voyons voir"
                    r " oh fuck ils sont vraiment pas loin"
                    r " que faire est ce qu'on se planque et on se repose   ou est ce qu'on coure en éspérant les semer ?..."
                    menu:
                        "Courir":
                            r "vaut mieux pas prendre de risque et courrir"
                            jump courir
                        "se reposer":
                            r "Autant prendre le risque et se reposer en se cachant, Athenais a l'air fatigué"
                            jump fauneFlore
                "se reposer":
                    r "go se reposer t'a l'air fatiguer"


        "Se reposer dans un refuge médiocre":
            r "Oh regarde une cabane destroy"
            r "go faire une petite pause"
            a "ça marche"
            "le lendemain"
            r " ok c'est carré Athenais les soldats ont tracé"
            a "nickel"
            $timeout_label = None
            menu:
                "aller à droite et Découvrir faune et flore":
                    r " go à droite"
                    jump fauneFlore
                "aller à gauche et Découvrir la ville":
                    r "go à gauche"
                    "Nos deux amis découvre la ville"
                    r " encore un croisement"
                    menu:
                        "aller à droite et Découvrir faune et flore":
                            r "go à droite ce coup-ci"
                            jump fauneFlore
                        "aller à gauche":
                            r "fulllllllll gauche let's go"
                            jump drone


return
