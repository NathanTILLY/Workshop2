label jour:
    a " Je préfère voyager de jour, j’ai peur du noir…"
    r "Très bien tu préfères continuer d’avancer à l’intérieur du bâtiment ou à l’extérieur ?"

    "*Passer à l’intérieur*"
    "*Passer à l’extérieur*"

    menu:
        "*Passer à l’intérieur*":
            a "Je préfère passer par l’intérieur."

            r "Très bien, allons y"

            "*F4 et Athénaïs travers diverse bâtiment de la ville tout en se dirigeant vers le câble*"

            a "Dit F4, tu faisais quoi avant de me trouver ?"

            r "Je ramassais... des ordures... et des débris... qui tombaient du ciel... comme toi"

            a "Alors je suis un débris ?"

            r "Euh… Non… je ne voulais pas… dire ça, un débris... c’est moche... et c’est en métal..."

            a "Oh ? alors je suis jolie et pas en métal ?"

            r "Ou… i… oui, toi tu es jolie et en chair"

            r "Mais toi t’es en métal ? donc t’es un débris ?"
            r "Oui je… suis en… métal, mais est… ce que… je suis… moche ? Si oui… je suis un débris…"

            a "Non je te trouve beau moi ! Donc t’es pas un débris !"

            r "Merc...i"


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
