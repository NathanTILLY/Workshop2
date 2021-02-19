label enfantAttaque:
    if pasDeBras == True and posture == False:
        show robot bras neutre at right
    elif pasDeBras == False and posture == True:
        show robot dos neutre at left
    elif pasDeBras == True and posture == True:
        show robot bras dos neutre at left
    else:
        show robot neutre at right

    show athenais contente at right

    "F4 et Athénaïs se rapprochent de plus en plus du câble si bien qu’il parait immense. La petite fille tellement émerveillée avance sans se soucier de ce qu’il y a autour d’elle."
    " A cause de ce manque d’attention un drone surgit et lui saute dessus"
    show drone colere at left
    if pasDeBras == True and posture == False:
        show robot bras peur at right
    elif pasDeBras == False and posture == True:
        show robot dos peur at left
    elif pasDeBras == True and posture == True:
        show robot bras dos peur at left
    else:
        show robot peur at right

    "Attention !"

    menu:
        "Se précipiter pour la sauver":

            show athenais peur

            "*F4 se rue sur le drone mais ce dernier étant à l'affût saute sur la jambe de F4, et la lacère de part en part. Le drone arrache la jambe du robot mais celui-ci lui donne un coup qui lui est fatal.*"
            if pasDeBras == True and posture == False:
                show robot bras jambe colere at left
            elif pasDeBras == False and posture == True:
                show robot jambe dos colere at left
            elif pasDeBras == True and posture == True:
                show robot bras jambe dos colere at left
            else:
                show robot jambe colere at left
            hide drone colere
            a "F4, ta jambe…"

            r "Je t’ai... protégée c’est... le plus important"
            $ jambe = True

            jump cable
        "*Attendre le bon moment*":
            "*F4 analyse la situation, et au moment où le drone relâche son attention il l’embroche de sa main et le détruit*"
            hide drone colere
            show athenais contente
            if pasDeBras == True and posture == False:
                show robot bras joie at right
            elif pasDeBras == False and posture == True:
                show robot dos joie at left
            elif pasDeBras == True and posture == True:
                show robot bras dos joie at left
            else:
                show robot joie at right
            a"Merci F4, tu es mon sauveur"
            "*En lui sautant dans le bras*"
            $ jambe = False

            jump cable
