define al = Character("Alerte", color = "#82040c")
define g = Character("Gérant de la ville", color = "#588A66")
define me = Character("Mère d'Athenais", color = "#d7f542")
define pe = Character("Père d'Athenais", color = "#d7f542")
define pa = Character("Parents d'Athenais", color = "#d7f542")

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
        menu:
            "Grimper au tube":
                label finRamene:

                    r "Je… ne peux… pas… te garder… tes parents veulent… sûrement te… retrouver. Je ne… me sens pas… apte… et légitime... à m’occuper de toi"

                    a "Mais je ne veux pas y retourner... Je veux rester avec toi"

                    r "Désolé… je ne peux… vraiment pas... te garder, tu… dois y… retourner."

                    "*Arrivés au câble F4 et Athénaïs commence à gravir ce dernier, le processus est périlleux. Dans la ville volante une alerte retentit*"

                    al "Avis à toute la population, un robot gravit le câble Gamma. Rester chez vous, ne sortez pas, je répète rester chez vous, ne sortez pas."

                    "*Les humains intrigués par ce qu’il se passe se ruent en masse au câble Gamma prêt à accueillir le robot. Dès que F4 arrive en haut de celui-ci, il aperçoit une foule d'humains. Certains sont paniqués et d'autres intrigués.*"

                    "*Le gérant de la ville et une dizaine de membres des forces de l’ordre arrivent sur les lieux, pour constater les faits.*"

                    r "Humain… je vous… ramène, un membre… de votre… clan qui était… malencontreusement… tombé de… votre cité."

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


            "Demander à Athenais de rester vivre avec F4":
                jump finFuite
