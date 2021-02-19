label nuit:
    play music "arc_1_1.mp3" fadeout 2
    a "Je préfère voyager de nuit, les vilains robots seront pas là n’est ce pas ?"
    r "Affirmatif…"

    "*Ils attendent quelques heures avant la tombée de la nuit, ils continuent leur périple.*"
    show bg ville1 nuit
    r "Nous devons… nous déplacer furtivement… pour ne pas réveiller un D1-11T*"

    "*Ils sortent du refuge*"

    "*Arrivés à un embranchement ils doivent choisir entre deux chemins*"
    show athenais neutre at left behind robot
    show robot neutre:
        xalign 0.3
        yalign 1.0

    menu:
        "Passer à l’extérieur":
            r "Passons... par là."
            jump finUno

        "Passer par l’intérieur":
            r "Continuons dans... le bâtiment."

            "*Lorsqu’ils avancent, F4 tape malencontreusement un cadre de porte et réveille un drone qui dormait à cet endroit.*"
            show drone neutre:
                xalign 0.9
                yalign 1.2

            "*F4 se retourne et cache Athénaïs avec son corps pour la protéger du drone*"

            r "Ne...bouge plus...et ne fais... pas de bruit."

            "*Le drone se rendort après quelques instants*"
            hide drone neutre

            "*F4 et Athénaïs ,après avoir traversé le bâtiment, se retrouvent à l’extérieur* "
            scene bg ville2 nuit
            show athenais neutre at right behind robot
            show robot neutre:
                xalign 0.8
                yalign 1.0
            r "Passons... par là."

            jump finUno
