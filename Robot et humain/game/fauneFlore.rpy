label fauneFlore:

    show bg ville2 jour

    if pasDeBras == True:
        show robot bras neutre at right
    else:
        show robot neutre at right
    show Athenais contente at left


    a "Ouah ! C’est beau ! Je n’avais jamais vu ça avant. Il n’y avait presque pas d’arbres dans chez moi."

    if pasDeBras == True:
        show robot bras joie
    else:
        show robot joie

    r "Il n’y en… avait pas… beaucoup… chez moi… non plus."

    if pasDeBras == True:
        show robot bras peur at right
    else:
        show robot peur at right

    show athenais peur at right behin robot

    "*Athénaïs et F4 voient les hautes herbes bouger et entendent des bruissements. F4 se place devant Athénaïs pour la protéger au cas où quelque chose viendrait les attaquer.*"


    r "Cache-toi... derrière moi...,  des D1... ou des S1... pourraient surgir."

    "*Une créature sort des hautes herbes et F4 décide de l‘analyser.*"

    a "C’est quoi ça F4 ?"

    if pasDeBras == True:
        show robot bras neutre at left
    else:
        show robot neutre at left

    show athenais neutre

    r "Une créature... inoffensive... dénommée cerf."

    "*Le cerf balaye l’horizon du regard et aperçoit Athénaïs et F4, suite à ça il s’enfuit et disparaît dans les hautes herbes*"

    a "Oh, il est parti… C’est dommage je le trouvait beau…"

    "* Après cet aparté ils reprennent leur avancée vers le câble, puis F4 se rend compte qu’il apprécie de plus en plus Athénaïs*"
    jump rapprochement
