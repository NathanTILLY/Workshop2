
label avecbras:
        #show bg exterieurun
        show robot_neutre at left
        show athenais_neutre at left
        "*Après avoir passé la porte, F4 et Athénaïs arrivent dans l’ancienne ville humaine dans laquelle la nature a repris ses droits*"
        menu:
            "Continuer à avancer":

                r "let's go on avance"
                menu:
                    "se retourner":
                        r " Je me demande si on est poursuivi voyons voir"
                        r " je vais monter sur cette pile pour scout la zone Athenais bouge pas"
                        "*grimpe*"
                        r " ok voyons voir"
                        r " oh fuck ils sont vraiment pas loin"
                        r " que faire est ce qu'on se planque et on se repose ou est ce qu'on coure en éspérant les semer ?..."
                        menu:
                            "Courir":
                                r "vaut mieux pas prendre de risque et courrir"
                                jump courir
                            "se reposer":
                                r "Autant prendre le risque et se reposer en se cachant, Athenais a l'air fatigué"
                                jump fauneFlore


            "Aller dans le refuge à droite":
                r "Oh regarde une cabane destroy"
                r "go faire une petite pause"
                a "ça marche"
                "le lendemain"
                r " ok c'est carré Athenais les soldats ont tracé"
                a "nickel"
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


            "Aller dans le refuge à gauche":
                r" Allons...à gauche… mes sens de robot… m’indique un bon… refuge par là bas."

                "*Athénaïs tend sa main à F4*"

                r "Pourquoi… Me tends-tu… Ta main… Athénaïs?"

                a "Mes parents me tenaient la main pour me réconforter"

                "*F4 prend la main d’Athénaïs*"

                a " AH ! Mais ta main est super froide !"

                r "Pardon...attends quelques secondes"

                "*F4 active son système auto chauffant*"

                a "C’est bien mieux comme ça !"

                "*F4 et Athénaïs après quelques minutes de marche arrivent au fameux refuge que F4 avait repéré*"
                show bg bonrefuge
                r "On va... pouvoir se reposer…. un peu ici"

                "*F4 prend Athénaïs dans ses bras et l’assoie sur le fauteuil/canapé*"

                "*Scouik Scouik*"

                a "AAAHH ! Au secours, qu’est ce que c’est que ça !?"

                "*F4 analyse la créature qui vient de terroriser la fillette*"

                r "Analyse terminée… c’est seulement… un rat… une petite créature inoffensive…"

                a "Ah ouf j’ai eu peur, j’ai cru que…"

                r "Chut ! Un drone... Cache toi… Et ne fais pas... De bruit"
                hide athenais_neutre
                hide robot_neutre
                #show bg exeterieurun
                show drone_loin at center

                "*F4 regarde par le seul trou de lumière qui donne sur l’extérieur et aperçoit le drone passer au loin*"

                hide drone
                show bg bonrefuge
                show athenais_neutre at right
                show robot_neutre at left
                r "Athénaïs… préfère tu… partir maintenant ?... ou attendre… que la nuit tombe ? "

                menu:
                    "voyager de jour":
                        jump jour
                    "voyager de nuit":
                        jump nuit


return
