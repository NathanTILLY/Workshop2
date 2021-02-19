label soldat:

    if pasDeBras == True:
        show robot bras joie at left
    else:
        show robot joie at left
    show athenais contente at right

    r "*On peut… y aller… si tu veux.*"

    a "Ouais ! Trop bien, je t’adore F4"

    "*Athénaïs cours vers les jeux et commence à s’amuser, F4 la suit pour la regarder jouer*"

    if pasDeBras == True:
        show robot bras peur at left
    else:
        show robot peur at left

    "*Après quelques instants, F4 aperçoit un groupe de S1 au loin*"

    $ timeout = 3.0
    $timeout_label = "soldatEmbusquer"
    menu:

        "essayer de s'enfuir":

            if pasDeBras == True:
                show robot bras peur at right
            else:
                show robot peur at right
            show athenais peur at right
            show robotbad colere2 at left
            show robotbad colere1:
                xalign 0.3
                yalign 1.0

            $timeout_label = None
            "*Prendre Athénaïs par la main et courir*"

            "*F4 et Athénaïs commencent à courir à l’opposé d’où se trouvent les S1, mais se ils font repérer dans leur course*"

            r "Vite… cours Athénaïs… reste devant… Moi, je vais… servir de bouclier."

            "*La petite fille s'exécute et passe devant F4*"

            "*Plusieurs balles sifflent à côté des capteurs de F4, mais quasiment aucune ne le touche*"

            "*Pendant cette intense course poursuite, F4 reçoit une balle au niveau de son cou mais il continue de courir et de protéger Athénaïs. Après cela F4 voit les soldats arrêter de courir et le laisse fuir avec la petite*"

            jump soldatEmbusquer
        "Prévenir Athénaïs et se cacher":
            $timeout_label = None

            if pasDeBras == True:
                show robot bras peur at right
            else:
                show robot peur at right
            show athenais peur at right


            "*F4 prend Athénaïs et se cache dans un bâtiment*"
            show robotbad neutre at left
            show robotbad2 neutre:
                xalign 0.3
                yalign 1.0

            r "Ne...bouge plus...et ne fais... pas de bruit."

            "*F4 attend que les S1 passent avant de reprendre la route*"
            hide robotbad
            $ posture = False
            jump enfantAttaque
