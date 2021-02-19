
label avecbras:
        scene bg ville1 jour
        show robot neutre at center
        show athenais neutre at left behind robot
        $ pasDeBras = False
        "*Après avoir passé la porte, F4 et Athénaïs arrivent dans l’ancienne ville humaine dans laquelle la nature a repris ses droits*"
        play music "arc_2.mp3"
        menu:
            "Continuer à avancer":

                "*F4 et Athénaïs décident de continuer leur chemin en suivant la route.*"

                "*Athénaïs tend sa main à F4*"

                "Pourquoi… Me tends-tu… Ta main… Athénaïs?"

                a "Mes parents me tenaient la main pour me réconforter"

                "*F4 prend la main d’Athénaïs*"

                show athenais peur

                a "AH ! Mais ta main est super froide !"

                r "Pardon...attends quelques secondes"

                "*F4 active son système auto chauffant*"
                show athenais contente

                a"C’est bien mieux comme ça !"

                "*Quelques minutes de marche plus tard, F4 inquiet de ses poursuivants, lance des regards de temps à autre derrière lui. Jusqu’au moment où il arrive à discerner des S1 derrière lui*"
                show robot peur

                menu:
                    "*Courir pour les semer*":

                        show athenais peur
                        "*Athénaïs se retourne et voit les S1*"

                        a "F4, les méchants robots sont derrière nous il faut courir !"

                        r "Tu… as raison... "

                        "*F4 et Athénaïs se mettent à courir pour fuir les S1*"

                        jump courir
                    "*Se cacher*":
                        r "Viens petite… il ne faut pas… qu’ils nous voient."
                        show athenais peur

                        "*Après avoir éviter les S1, F4 et Athénaïs continuent leur route et ils arrivent dans une grande étendue au milieu d’arbres et de hautes herbes*"

                        jump fauneFlore


            "Aller dans le refuge à droite":

                r "Allons...à droite… j’ai un bon... pressentiment… "

                show bg abri

                "*Athénaïs tend sa main à F4*"

                "Pourquoi… Me tends-tu… Ta main… Athénaïs?"

                a "Mes parents me tenaient la main pour me réconforter"

                "*F4 prend la main d’Athénaïs*"

                show athenais peur

                a "AH ! Mais ta main est super froide !"

                r "Pardon...attends quelques secondes"

                "*F4 active son système auto chauffant*"
                show athenais contente

                a"C’est bien mieux comme ça !"

                "*F4 et Athénaïs après quelques minutes de marche arrivent au fameux refuge que F4 avait repéré*"

                r "On va... pouvoir se reposer…. un peu ici… en attendant que les soldats... passent"

                "*Après avoir vu les S1 passer ils décident de reprendre prudemment leur route*"

                "*Ils arrivent à un carrefour et ils remarquent que la route de gauche est impraticable, pour continuer ils doivent choisir de passer par des escaliers ou de continuer la route*"

                menu:
                    "*Prendre les escaliers*":


                        "*Après avoir monté les escaliers F4 et Athénaïs arrivent dans une grande étendue au milieu d’arbres et de hautes herbes*"

                        jump fauneFlore
                    "Continuer la route":


                        $ Arc2 = True
                        jump drone



            "Aller dans le refuge à gauche":
                r " Allons...à gauche… mes sens de robot… m’indique un bon… refuge par là bas."

                "*Athénaïs tend sa main à F4*"

                r "Pourquoi… Me tends-tu… Ta main… Athénaïs?"

                a "Mes parents me tenaient la main pour me réconforter"

                "*F4 prend la main d’Athénaïs*"

                show athenais peur

                a " AH ! Mais ta main est super froide !"

                r "Pardon...attends quelques secondes"

                "*F4 active son système auto chauffant*"

                show athenais contente

                a "C’est bien mieux comme ça !"

                "*F4 et Athénaïs après quelques minutes de marche arrivent au fameux refuge que F4 avait repéré*"
                show bg bon abri
                r "On va... pouvoir se reposer…. un peu ici"

                "*F4 prend Athénaïs dans ses bras et l’assoie sur le fauteuil/canapé*"

                "*Scouik Scouik*"
                show athenais peur at right
                a "AAAHH ! Au secours, qu’est ce que c’est que ça !?"

                "*F4 analyse la créature qui vient de terroriser la fillette*"
                show robot neutre at center

                r "Analyse terminée… c’est seulement… un rat… une petite créature inoffensive…"
                show athenais neutre at right
                a "Ah ouf j’ai eu peur, j’ai cru que…"

                r "Chut ! Un drone... Cache toi… Et ne fais pas... De bruit"
                hide athenais
                hide robot
                show bg ville1 jour
                show drone neutre:
                    xalign 0.5
                    yalign 1.2

                "*F4 regarde par le seul trou de lumière qui donne sur l’extérieur et aperçoit le drone passer au loin*"

                hide drone
                show bg bon abri
                show athenais neutre at right
                show robot neutre at left
                r "Athénaïs… préfère tu… partir maintenant ?... ou attendre… que la nuit tombe ? "

                menu:
                    "voyager de jour":
                        jump jour
                    "voyager de nuit":

                        jump nuit


return
