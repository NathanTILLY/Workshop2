label drone:

    show bg ville1 jour

    if (pasDeBras == True):
        show robot bras neutre at right
    else:
        show robot neutre at right
    show athenais at center
    if Arc2 == True:
        a " Continuons par la route " #(SI ARC 2 V1)
        r "Très bien, allons y "

        if (pasDeBras == True):
            show robot bras peur
        else:
            show robot peur

        show athenais peur

        show drone colere at left

        "*En continuant par la route, F4 et Athénaïs repèrent un D1, et celui-ci commence à les prendre en chasse*"
    else :
        a "Je préfère passer par l’extérieur"
        r "Très bien, allons y "

        if (pasDeBras == True):
            show robot bras peur
        else:
            show robot peur

        show athenais peur

        show drone colere at left

        "*En sortant du bâtiment dans lequel ils s’étaient réfugiés, F4 et Athénaïs repèrent un D1, et celui-ci commence à les prendre en chasse*" #(SI ARC 1V2)



    menu:
        "courir pour le fuir":
            "*Courir et semer le drone*"

            r "Cours… vite… cache toi dès… que tu… peux"

            hide drone

            "*F4 et Athénaïs réussissent à semer le drone en se cachant parmi la flore locale*"

            if (pasDeBras == True):
                show robot bras neutre
            else:
                show robot neutre

            show athenais neutre

            r "On l’a… semé...c’est bon... "

            "*Ils continuent leur route et arrivent au niveau d’un grand parc, dans lequel se trouvent des jeux pour enfants, qui est à découvert*"

            show athenais contente

            a "Oh ! Des jeux, c’était réservé à des gens riches là-haut, on peut y aller ?"

            jump soldat


        "*Se cacher et attendre que le drone passe*":

            jump ours
