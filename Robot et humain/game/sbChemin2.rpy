label courir:
    if pasDeBras == True:
        show robot normal at right
    else:
        show robot minusbras at right
    show athenais at right
    r "on court Athenais il faut qu'on quitte cet endroit le plus vite possible"
    "Après quelques heures de cours poursuite"
    show robotbad
    m "ici l'unité S1-25C j'ai perdu la trace de la cible"
    show drone calme
    d " ici l'unité D1-11T j'ai également perdu la trace de la cible"
    "......."
    m "tant pis on retourne à la base"
    hide robotbad
    hide drone calme

    "A quelques kms de là"
    r " Je ne les voit plus du tout Athenais je pense qu'on est safe"
    a "Nice"
    r "Vas y on continue a avancer"
    jump rapprochement
