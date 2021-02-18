

label sansbras:
    $ pasDeBras = True
    show bg ville1 jour
    show robot bras neutre at left
    show athenais neutre at right
    "*Après avoir passé la porte, F4 et Athénaïs arrivent dans l’ancienne ville humaine dans laquelle la nature a repris ses droits*"
    $ timeout = 5.0
    $timeout_label = "timerUno"


    menu:

        "Continuer à avancer":
            $timeout_label = None
            "*F4 et Athénaïs décident de continuer leur chemin en suivant la route.*"

            "*Athénaïs tend sa main à F4*"

            r "Pourquoi… Me tends-tu… Ta main… Athénaïs?"

            a "Mes parents me tenaient la main pour me réconforter"

            "*F4 prend la main d’Athénaïs*"

            show athenais peur

            a "AH ! Mais ta main est super froide !"

            r "Pardon...attends quelques secondes"

            "*F4 active son système auto chauffant*"

            show athenais contente

            a "C’est bien mieux comme ça !"

            "*Quelques minutes de marche plus tard, F4 inquiet de ses poursuivants, lance des regards de temps à autre derrière lui. Jusqu’au moment où il arrive à discerner des S1 derrière lui*"

            show robot bras peur

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


            "*F4 et Athénaïs après quelques minutes de marche arrivent au fameux refuge que F4 avait repéré*"

            r "On va... pouvoir se reposer…. un peu ici… en attendant que les soldats... passent"

            "*Après avoir vu les S1 passer ils décident de reprendre prudemment leur route*"

            "*Ils arrivent à un carrefour et ils remarquent que la route de gauche est impraticable, pour continuer ils doivent choisir de passer par des escaliers ou de continuer la route*"

            menu:
                "Prendre les escaliers":

                    show

                    "*Après avoir monté les escaliers F4 et Athénaïs arrivent dans une grande étendue au milieu d’arbres et de hautes herbes*"

                    jump fauneFlore
                "Continuer la route":

                    $ Arc2 = True
                    jump drone

                    menu:
                        "aller à droite et Découvrir faune et flore":
                            r "go à droite ce coup-ci"
                            jump fauneFlore
                        "aller à gauche":
                            r "fulllllllll gauche let's go"
                            jump drone


return
