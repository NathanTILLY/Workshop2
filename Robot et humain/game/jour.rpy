label jour:
    a " Je préfère voyager de jour, j’ai peur du noir…"
    show bg ville1 jour
    r "Très bien tu préfères continuer d’avancer à l’intérieur du bâtiment ou à l’extérieur ?"



    menu:
        "*Passer à l’intérieur*":
            a "Je préfère passer par l’intérieur."

            r "Très bien, allons y"
            show bg ville2 jour
            with Dissolve(.5)
            "*F4 et Athénaïs travers diverse bâtiment de la ville tout en se dirigeant vers le câble*"

            show robot joie at center


            "*Ils arrivent au niveau d’un grand parc, dans lequel se trouve des jeux pour enfants, mais qui est à découvert*"

            a "Oh ! Des jeux, c’était réservé à des gens riches là-haut, on peut y aller ?"

            menu:
                "Non":
                    "*Non, c’est… trop dangereux…*"

                    a "Oui d’accord... Tu as peut-être raison…"

                    jump finUno
                "Oui":

                    jump soldat
        "*Passer à l’extérieur*":
            a " Je préfère passer par l’extérieur" # (SI ARC 1 V2)
            $ Arc2 = False
            jump drone
