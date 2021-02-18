label nuit:

    a "Je préfère voyager de nuit, les vilains robots seront pas là n’est ce pas ?"
    r "Affirmatif…"
    show bg bonrefugeNuit
    "*Ils attendent quelques heures avant la tombée de la nuit, ils continuent leur périple.*"
    # show bg exterieurunnuit
    r "Nous devons… nous déplacer furtivement… pour ne pas réveiller un D1-11T*"

    "*Ils sortent du refuge*"

    "*Arrivés à un embranchement ils doivent choisir entre deux chemins*"
    show athenais_neutre at left
    show robot_neutre at left

    menu:
        "Passer à l’extérieur":
            r "Passons... par là."
            jump finUno

        "Passer par l’intérieur":
            r "Continuons dans... le bâtiment."

            "*Lorsqu’ils avancent, F4 tape malencontreusement un cadre de porte et réveille un drone qui dormait à cet endroit.*"
            show drone_neutre at center

            "*F4 se retourne et cache Athénaïs avec son corps pour la protéger du drone*"

            r "Ne...bouge plus...et ne fais... pas de bruit."

            "*Le drone se rendort après quelques instants*"
            hide drone_neutre

            "*F4 et Athénaïs ,après avoir traversé le bâtiment, se retrouvent à l’extérieur* "
            show athenais_neutre at right
            show robot_neutre at right
            r "Passons... par là."

            jump finUno
