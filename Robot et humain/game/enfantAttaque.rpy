label enfantAttaque:
    if pasDeBras == True:
        show robot normal at right
    else:
        show robot minusbras at right
    show athenais at right
    r " je pense qu'on est bientot arrivé Athenais"
    a " Oui j'imagine ..."
    r " Qu'est ce qu'il ne va p.. !!!"
    show drone at center
    d " renégat repéré. Récupération du biocarburant"
    r "Athenais attention"
    menu:
        "se précipiter pour la sauver":
            r "Rah laisse là"
            "Chomp"
            r " Argh"
            a "F4!!"
            r "viens Athenais on trace"
            jump cable
        "attendre le bon moment pour intervenir":
            r "wait wait"
            r "Maintenant !!"
            "BONK"
            r "viens Athenais on trace"
            jump cable
