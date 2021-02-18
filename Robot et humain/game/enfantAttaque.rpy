label enfantAttaque:
    if pasDeBras == True:
        show robot bras neutre at right
    else:
        show robot neutre at right
    show athenais joie at right

    "*F4 et Athénaïs se rapprochent de plus en plus du câble si bien qu’il parait immense. La petite fille tellement émerveillée avance sans se soucier de ce qu’il y a autour d’elle. A cause de ce manque d’attention un drone surgit et lui saute dessus*"

    if pasDeBras == True:
        show robot bras peur at right
    else:
        show robot peur at right

    "Attention !"

    menu:
        "Se précipiter pour la sauver":

            show athenais peur

            "*F4 se rue sur le drone mais ce dernier étant à l'affût saute sur la jambe de F4, et la lacère de part en part. Le drone arrache la jambe du robot mais celui-ci lui donne un coup qui lui est fatal.*"

            a "F4, ta jambe…"

            r "Je t’ai... protégée c’est... le plus important"
            $ jambe = True

            jump cable
        "*Attendre le bon moment*":
            "*F4 analyse la situation, et au moment où le drone relâche son attention il l’embroche de sa main et le détruit*"

            show athenais contente

            a"Merci F4, tu es mon sauveur"
            "*En lui sautant dans le bras*"
            $ jambe = False

            jump cable
