label drone:
    if pasDeBras == True:
        show robot normal at right
    else:
        show robot minusbras at right
    show athenais at right
    if Arc2 == True:
        a " Continuons par la route " #(SI ARC 2 V1)
        r "Très bien, allons y "
        "*En continuant par la route, F4 et Athénaïs repèrent un D1, et celui-ci commence à les prendre en chasse*"
    else :
        a "Je préfère passer par l’extérieur"
        r "Très bien, allons y "

        "*En sortant du bâtiment dans lequel ils s’étaient réfugiés, F4 et Athénaïs repèrent un D1, et celui-ci commence à les prendre en chasse*" #(SI ARC 1V2)



    menu:
        "courir pour le fuir":
            "*Courir et semer le drone*"

            r "Cours… vite… cache toi dès… que tu… peux"

            "*F4 et Athénaïs réussissent à semer le drone en se cachant parmis la flore local*"

            r "On l’a… semé...c’est bon... "

            "*Ils continuent leur route et arrivent au niveau d’un grand parc, dans lequel se trouve des jeux pour enfants, qui est à découvert*"

            a "Oh ! Des jeux, c’était réservé à des gens riches là-haut, on peut y aller ?"

            jump soldat


        "*Se cacher et attendre que le drone passe*":
        
            jump ours
