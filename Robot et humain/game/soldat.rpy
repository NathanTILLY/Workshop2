label soldat:
    r " ok c'est bon on l'a semé et ..."
    r "oh purée des soldats devant ne dit pas un mot athenais ne bouge pas"
    $timeout_label = "enfantAttaque"
    menu:
        "essayer de s'enfuir":
            r " ok on va essayer de s'enfuir par l"
            m " Eh vous là bas "
            m " je le recconnais c'est le renégat"
            r " on trace Athenais cours"
            "*running in the 90's"
            jump soldatEmbusquer
