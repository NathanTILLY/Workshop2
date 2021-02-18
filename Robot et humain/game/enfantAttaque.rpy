label enfantAttaque:
    if pasDeBras == True:
        show robot normal at right
    else:
        show robot minusbras at right
    show athenais at right

    "*F4 et Athénaïs se rapprochent de plus en plus du câble si bien qu’il parait immense. La petite fille tellement émerveillée avance sans se soucier de ce qu’il y a autour d’elle. A cause de ce manque d’attention un drone surgit et lui saute dessus*"

    "Attention !"

    menu:
        "Se précipiter pour la sauver":

            "*F4 se rue sur le drone mais ce dernier étant à l'affût saute sur la jambe de F4, et la lacère de part en part. Le drone arrache la jambe du robot mais celui-ci lui donne un coup qui lui est fatal.*"

            a "F4, ta jambe…"

            r "Je t’ai... protégé c’est... le plus important"
            $ jambe = True
            
            jump cable
        "*Attendre le bon moment*":
            "*F4 analyse la situation, et au moment où le drone relâche son attention il l’embroche de sa main et le détruit*"

            a"Merci F4, tu es mon sauveur"
            "*En lui sautant dans le bras*"
            $ jambe = False

            jump cable
