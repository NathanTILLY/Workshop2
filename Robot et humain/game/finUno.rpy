label finUno:
    "*F4 et Athénaïs découvrent la ville tout en se dirigeant vers le câble*"

    a "Dit F4, tu faisais quoi avant de me trouver ?"

    r "Je ramassais... des ordures... et des débris... qui tombaient du ciel... comme toi"

    a "Alors je suis un débris ?"

    r "Euh… Non… je ne voulais pas… dire ça, un débris... c’est moche... et c’est en métal..."

    a "Oh ? alors je suis jolie et pas en métal ?"

    r "Ou… i… oui, toi tu es jolie et en chair"

    a "Mais toi t’es en métal ? donc t’es un débris ?"
    r "Oui je… suis en… métal, mais est… ce que… je suis… moche ? Si oui… je suis un débris…"

    a "Non je te trouve beau moi ! Donc t’es pas un débris !"

    r "Merc...i"


    "*Plus ils avancent vers le câble, plus F4 se rend compte qu’il apprécie Athénaïs*"

    "F4 dans ses pensés : "

    r "Je ne comprends pas, je crois que je suis en train de m’attacher à elle et que sa présence m’apaise et m’apporte de la joie."
    r "Mais qu’est ce que la joie ? Suis-je capable de ressentir des choses ? Est-ce une bonne idée de la ramener là haut ? Était-elle heureuse ? Est-ce qu’elle..."

    a "F4 ça va ? Tu as l’air perdu"

    r "Euh… oui ! Tu te souviens… de ta vie… d’avant… quand tu étais... là-haut ?"

    a "Non, j’ai seulement quelques flash de mes parents"
    r "Est ce… que tes parents… t’aimaient ?"


    a " Je me souviens juste qu’ils ont beaucoup pleurer à mon départ. Quand on perd quelqu’un qu’on aime on pleure, c’est peut être ça l’amour ? Tu as déjà été triste toi ? "


    r "Non… je ne crois pas… être capable… de ressentir… les choses... que vous appelez… sentiments."

    "F4 dans sa tête : "

    r "Pourtant j’ai l’impression de l’aimer comme un père, j’ai envie de la protéger, de la réconforter, de la chérir et je n'ai pas envie de la perdre. C’est peut-être ça l’amour ?"

    "*F4 et Athénaïs se rapprochent de plus en plus du câble si bien que maintenant il parait immense* "
    scene bg cable
    with Dissolve(.5)
    show athenais neutre at left behind robot
    show robot neutre:
        xalign 0.3
        yalign 1.0
    "*Après un certain temps de marche, ils arrivent enfin au câble, de peur Athénaïs se colle contre F4.*"
    show athenais triste at center
    a "J’ai peur d’y retourner, je peux rester avec toi s’il te plaît F4 ?"

    "F4 dans sa tête :"

    r "Que dois-je répondre à ça ? Que dois-je faire ? Dois-je vraiment imposer mon choix ? Suis-je légitime à la garder ? "
    r "Pourrais-je la protéger des dangers d’un monde qui m'est inconnu ? Peut-être que ses parents veulent la retrouver ? Sera-t-elle vraiment heureuse avec moi ?"
    show athenais neutre at center behind robot
    a "F4, tu fumes !"

    r "Comment… ça ?"

    a "Il y a de la fumée qui sort de ta tête !"

    r "Pardon... je réfléchissais... à ta question… je pense te dire…que..."


    menu:
        "Je veux rester avec toi":
            label finFuite:
                play music "les_autres_fins.mp3"
                show robot joie at left
                r "Je ne veux… pas… t’abandonner, je… veux… rester avec toi"
                show athenais contente at center
                "Le visage de la fillette s’illumina de bonheur et de soulagement, elle était tellement heureuse d’avoir retrouvé une famille… Athénaïs se rue sur F4 pour l’enlacer."
                "Des larmes se mettent à couler sur son visage, non pas de tristesse mais de soulagement et de joie.*"

                "Après ce câlin riche en émotion F4 prit la main d’Athénaïs et ils continuèrent leur route en s'enfonçant plus loin dans la forêt."

                "*Ce fut la fin d’un chapitre de leur histoire, et le début d’un nouveau..."
                jump credit



        "Tu dois retourner auprès de tes parents":

            $ posture = False
            $ jambe = False
            jump finRamene
