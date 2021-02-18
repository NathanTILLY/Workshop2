define al = Character("Alerte", color = "#82040c")
define g = Character("Gérant ", color = "#588A66")
define fe = Character("Mère ", color = "#d7f542")
define pe = Character("Père ", color = "#d7f542")
define pa = Character("Parents ", color = "#d7f542")

label cable:
    "*Après un certain temps de marche, ils arrivent enfin au câble, de peur Athénaïs se colle contre F4.*"

    a "J’ai peur d’y retourner, je peux rester avec toi s’il te plaît F4 ?"

    "F4 dans sa tête :"

    r "Que dois-je répondre à ça ? Que dois-je faire ? Dois-je vraiment imposer mon choix ? Suis-je légitime à la garder ?"
    r "Pourrais-je la protéger des dangers d’un monde qui m'est inconnu ? Peut-être que ses parents veulent la retrouver ? Sera-t-elle vraiment heureuse avec moi ?"

    a "F4, tu fumes !"

    r "Comment… ça ?"

    a "Il y a de la fumée qui sort de ta tête !"

    r "Pardon... je réfléchissais... à ta question… je pense te dire…que..."

    if pasDeBras == True and jambe == True:
        menu:
            "Oui (pas le choix)":
                jump finFuite
    elif posture == True and pasDeBras == True:
        menu:
            "Oui (pas le choix)":
                jump finFuite
    elif jambe == True and posture == True:
        menu:
            "Oui (pas le choix)":
                jump finFuite
    else:
        menu:
            "Oui":
                jump finFuite
            "Non":
                label finRamene:
                    play music "les_autres_fins.mp3"

                    r "Je… ne peux… pas… te garder… tes parents veulent… sûrement te… retrouver. Je ne… me sens pas… apte… et légitime... à m’occuper de toi"

                    a "Mais je ne veux pas y retourner... Je veux rester avec toi"

                    r "Désolé… je ne peux… vraiment pas... te garder, tu… dois y… retourner."

                    "*Arrivés au câble F4 et Athénaïs commence à gravir ce dernier, le processus est périlleux. Dans la ville volante une alerte retentit*"

                    al "Avis à toute la population, un robot gravit le câble Gamma. Rester chez vous, ne sortez pas, je répète rester chez vous, ne sortez pas."

                    "*Les humains intrigués par ce qu’il se passe se ruent en masse au câble Gamma prêt à accueillir le robot. Dès que F4 arrive en haut de celui-ci, il aperçoit une foule d'humains. Certains sont paniqués et d'autres intrigués.*"

                    "*Le gérant de la ville et une dizaine de membres des forces de l’ordre arrivent sur les lieux, pour constater les faits.*"

                    r "Humain… je vous… ramène, un membre… de votre… clan qui était… malencontreusement… tombé de… votre cité."

                    play sound "human_audience_laughter_comedy_club_x200_people_komedia_brighton_comic_boom_012.mp3"

                    "*Le gérant et les humains présent sur les lieux, éclatent de rire et se moque de F4*"
                    g "Stupide robot, cette gamine n’est pas malencontreusement tombée de notre cité, nous l’avons expulser. A qui appartient cette enfant ?"

                    "*Un couple s’avance et reconnaissent qu’elle était leur fille*"

                    g "Vous serez jugés, pour non respect de la loi et pour alliance avec l’ennemi"
                    pa "Mais nous n’avons rien fait, on ne pensait pas qu’elle reviendrait !"
                    g "Vous osez contester mon autorité ? Vous osez vous rebeller ?"

                    pa "Non… Nous acceptons notre sort…"

                    fe "Tu ne nous auras apporté que du malheur, j’aurais aimé ne jamais t’avoir mise au monde ! "
                    "*En pointant Athénaïs*"

                    pe "Si tu n’avais jamais existé, nous serions tellement plus heureux, je te hais"
                    "*En regardant Athénaïs méchamment*"

                    "*Le gérant fait signe aux autorités d’expulser le robot par dessus la cité, et de capturer la fillette*"

                    r "En réalité… c’est vous… les… monstres."
                    "*F4 tente tant bien que mal de se défendre et de sauver Athénaïs. Mais les autorités étant trop nombreuse prirent le dessus et expulsent ce dernier*"

                    r "Athénaïs… Non ! Je dois… la… protéger"

                    "*Dit F4 en tombant de la cité volante, sans espoir de la sauver, voulant désespérément rester auprès d’elle*"

                    r "Je t’aimais… Soit forte… dé...so...lé !"

                    "*F4 implose sur le sol dans un bruit sourd laissant place, après le choc, à un silence pesant. Chacune des pièces de son corps se dispersent.*"

                    "*Pendant ce temps là, dans la cité volante. Athénaïs se fait capturer et amener à une capsule pour être expulsé une nouvelle fois dans les tréfonds du bas monde.*"
