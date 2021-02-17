label ours:
    r "ok on est good on peut sortir par là"
    r "oh purée un ours"
    menu:
        "essayer de s'infiltrer à travers l'ours":
            r "on va essayer de passer discrètement"
            a "ok"
            "GRAOU"
            r "Athenais attention !!"
            "SCHLACK"
            r "argh"
            r " prend ça boule de poils"
            "BONK"
            r "il a l'air KO on trace Athenais"
            a " qu'est ce qu'il t'est arrivé F4? Pourquoi tu es plié comme ça ?"
            r " il a coupé mon cable qui me sert à garder une posture droite"
            a " désolé F4 c'est ma faute"
            r " tkt pas pour ça"
            r " vient on s'en va"
            jump enfantAttaque
        "rester cacher":
            r "ok bon bah on reste cacher on attend que les deux partent"
            a " ok"
            "Quelques minutes plus tard"
            r "ok c'est bueno on trace"

            jump enfantAttaque
