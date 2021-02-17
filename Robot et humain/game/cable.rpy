define gh = Character("Garde humain")
define ra = Character("F4 et Athenais")

label cable:
    r "Nous voila arriver au cable..."
    if pasDeBras == True:
        r " Ah bah mince comment je t'envoie en haut c'est fermé"
        r "je t'aurai bien ramener en grmipant mais je ne suis pas en état"
        r "bon bah pas le choix je crois qu'il va falloir que tu reste avec moi Athenais"
        a "Yes"
        r "Ok ça marche vient on va s'installer dans la forêt"
        a "YAY"
        " HAPPY ENDING"
    else:
        r " Ah bah mince comment je t'envoie en haut c'est fermé"
        r "je peut toujours t'amener en haut en grimpant au tube..."



        menu:
            "Grimper au tube":
                r "accroche toi à moi Athenais je vais t'emmener en haut"
                a "ok"
                "Après quelque heure F4 arrive tant bien que mal en haut du cable"
                r " nous voila arriver"
                gh " eh vous deux comment vous êtes arriver là ?!!"
                gh "INVASION ROBOT TIREZ"
                "PIOU PIOU PIOU"
                r " argh"
                ra " aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhh"
                "F4 et Athenais tombe du tube"
                "*YOU DIED*"
                "GAME OVER"

            "Demander à Athenais de rester vivre avec F4":
                r "Athenais..."
                a " ?"
                r " J'ai bien réfléchit et j'aimerai que tu reste avec moi finalement"
                r "ça te dirai ?"
                a " Oui !! "
                r "Ok ça marche vient on va s'installer dans la forêt"
                a "YAY"
                " HAPPY ENDING"
