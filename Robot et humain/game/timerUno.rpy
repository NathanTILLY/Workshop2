

define d = Character("D1-11T")

label timerUno:

    r " Ah fuck un drone nous as rattrapé!"
    $timeout_label = None
    menu:
        "Continuer de courrir":
            show robot minusbras at right
            show athenais at right
            r "taille taille taille"
            "course poursuite"
            r " ils nous ont rattrapés"
            show robotbad at left
            m " Renégat repéré fumez le"
            "*piou piou piou*"
            r "argh je meurt"

            a"Nonnnnnn F4-112R !"
            m "unité D1-11T déchiquetez le"
            "*chomp chomp chomp *"
            hide robot minusbras
            m "la gamine tu vient avec nous on va te transformer en biocarburant"
            a "nooon F4 aide moi"
            a "F4 !!!!!"
            n "GAME OVER"


        "Tentez de le persuader":
            r " je te paye un boulon si tu nous laisse tranquille"
            d " mhhh quel genre de boulon"
            menu:
                "cylindrique":
                    r "un boulon cylindrique ?"
                    d "jure un boulon hexagonale ? ça marche"
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
                                    jump Cachette
                        "Courir":
                            r " Huf huf"
                            r " t'arrete pas de courir Athenais"
                            jump fin3
