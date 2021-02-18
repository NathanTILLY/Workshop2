label jour:
    r" ok on y va "
    menu:
        "aller à gauche":
            r "go à gauche"
            "Nos deux amis se déplacent sans problème"
            "Découvrent la ville en avançant"
            r "encore une intersection"
            menu:
                "gauche":
                    r "go à gauche"
                    r " ça m'a l'air pas mal"
                    jump finUno
                "droite":
                    r "go à droite"
                    jump soldat
        "aller à droite":
            r "go à droite"
            jump drone
