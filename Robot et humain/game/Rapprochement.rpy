label rapprochement:
    if pasDeBras == True:
        show robot bras neutre at right
    else:
        show robot neutre at right
    show athenais neutre at right
    "F4 dans ses pensés :"

    r "Je ne comprends pas, je crois que je suis en train de m’attacher à elle et que sa présence m’apaise et m’apporte de la joie. Mais qu’est ce que la joie ?"
    r " Suis-je capable de ressentir des choses ? Est-ce une bonne idée de la ramener là haut ? Était-elle heureuse ? Est-ce qu’elle..."

    a "F4 ça va ? Tu as l’air perdu"

    if pasDeBras == True:
        show robot bras gene at right
    else:
        show robot gene at right

    r "Euh… oui ! Tu te souviens… de ta vie… d’avant… quand tu étais... là-haut ?"

    a "Non, j’ai seulement quelques flash de mes parents"

    if pasDeBras == True:
        show robot bras neutre at right
    else:
        show robot neutre at right

    r "Est ce… que tes parents… t’aimaient ?"

    a "Je me souviens juste qu’ils ont beaucoup pleurer à mon départ. Quand on perd quelqu’un qu’on aime on pleure, c’est peut être ça l’amour ? Tu as déjà été triste toi ? "

    r "Non… je ne crois pas… être capable… de ressentir… les choses... que vous appelez… sentiments."

    "F4 dans sa tête :"

    r "Pourtant j’ai l’impression de l’aimer comme un père, j’ai envie de la protéger, de la réconforter, de la chérir et je n'ai pas envie de la perdre. C’est peut-être ça l’amour ?"


    "*F4 et Athénaïs continuent d’avancer. Ils arrivent au milieu d’une plaine remplie de flaques de boues et F4 patine sur l’une d’elle et la petite fille commence à rigoler à chaudes larmes."

    show athenais contente

    a "Ahahah ! F4 depuis quand tu sais danser ?"

    r "Je ne… dansais… pas… j’essayais seulement... de tenir tout... droit."

    play sound "zapsplat_human_boy_3_years_old_british_laugh_004.mp3"

    a "Ahahah ! Tu prends tout au sérieux, t’es trop drôle !"

    "*Après ce moment de rigolade ils reprennent leur chemin vers le câble*"

    $ posture = False

    jump enfantAttaque
