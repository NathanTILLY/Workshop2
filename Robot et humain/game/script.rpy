# PERMETTANT DE REALISER UN TIMER

default timeout = 5.0

default timeout_label = None

default persistent.timed_choices = True

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    if (timeout_label is not None) and persistent.timed_choices:

        bar:
            xalign 0.5
            ypos 400
            xsize 740
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action Jump(timeout_label)

# DEFINITION DE PERSONNAGES

define n = Character(kind = nvl)
define c = Character("Choix")
define r = Character("F4-112R", color = "#464CBD")
define a = Character("Athénaïs", color = "#B361C9")
define ath = Character("Fillette", color = "#B361C9")
define m = Character("S1-25C", color = "#B0413E")
define p = Character("P6-4D", color = "#588A66")

# DEFINITION DES IMAGES

image bg blanc = "bg_blanc.png"

image bg noir = "bg_noir.png"

image bg ville = "bg_ville.png"

image bg villedestroy = "bg_villedestroy.png"

image bg porte = "bg_porte.png"

image athenais neutre = "athenais_neutre.png"

image athenais peur = "athenais_peur.png"

image athenais contente = "athenais_contente.png"

image athenais triste = "athenais_triste.png"

image robotbad neutre = "robotbad_neutre.png"

image robotbad colere1 = "robotbad_colere1.png"

image robotbad colere2 = "robotbad_colere2.png"

image robotbad2 neutre = "robotbad_neutre.png"

image robotbad2 colere1 = "robotbad_colere1.png"

image robotbad2 colere2 = "robotbad_colere2.png"

image douane neutre = "douane_neutre.png"

image douane colere = "douane_colere.png"

image douane2 neutre = "douane_neutre.png"

image douane2 colere = "douane_colere.png"

image drone neutre = "drone_neutre.png"

image drone colere = "drone_colere.png"

# SPRITES DE F4

#NEUF

image robot colere = "F4_colere.png"

image robot gene = "F4_gene.png"

image robot joie = "F4_joie.png"

image robot neutre = "F4_neutre.png"

image robot peur = "F4_peur.png"

image robot triste = "F4_triste.png"

# BRAS

image robot bras colere = "F4_sansBras_colere.png"

image robot bras gene = "F4_sansBras_gene.png"

image robot bras joie = "F4_sansBras_joie.png"

image robot bras neutre = "F4_sansBras_neutre.png"

image robot bras peur = "F4_sansBras_peur.png"

image robot bras triste = "F4_sansBras_triste.png"

# JAMBE

image robot jambe colere = "F4_sansJambe_colere.png"

image robot jambe gene = "F4_sansJambe_gene.png"

image robot jambe joie = "F4_sansJambe_joie.png"

image robot jambe neutre = "F4_sansBras_neutre.png"

image robot jambe peur = "F4_sansJambe_peur.png"

image robot jambe triste = "F4_sansJambe_triste.png"

# DOS

image robot dos colere = "F4_dosCasse_colere.png"

image robot dos gene = "F4_dosCasse_gene.png"

image robot dos joie = "F4_dosCasse_joie.png"

image robot dos neutre = "F4_dosCasse_neutre.png"

image robot dos peur = "F4_dosCasse_peur.png"

image robot dos triste = "F4_dosCasse_triste.png"

# BRAS JAMBE

image robot bras jambe colere = "F4_sansJambe_sansBras_colere.png"

image robot bras jambe gene = "F4_sansJambe_sansBras_gene.png"

image robot bras jambe joie = "F4_sansJambe_sansBras_joie.png"

image robot bras jambe neutre = "F4_sansJambe_sansBras_neutre.png"

image robot bras jambe peur = "F4_sansJambe_sansBras_peur.png"

image robot bras jambe triste = "F4_sansJambe_sansBras_triste.png"

# BRAS DOS

image robot bras dos colere = "F4_dosCasse_sansBras_colere.png"

image robot bras dos gene = "F4_dosCasse_sansBras_gene.png"

image robot bras dos joie = "F4_dosCasse_sansBras_joie.png"

image robot bras dos neutre = "F4_dosCasse_sansBras_neutre.png"

image robot bras dos peur = "F4_dosCasse_sansBras_peur.png"

image robot bras dos triste = "F4_dosCasse_sansBras_triste.png"

# JAMBE DOS

image robot jambe dos colere = "F4_dosCasse_sansJambe_colere.png"

image robot jambe dos gene = "F4_dosCasse_sansJambe_gene.png"

image robot jambe dos joie = "F4_dosCasse_sansJambe_joie.png"

image robot jambe dos neutre = "F4_dosCasse_sansJambe_neutre.png"

image robot jambe dos peur = "F4_dosCasse_sansJambe_peur.png"

image robot jambe dos triste = "F4_dosCasse_sansJambe_triste.png"

# BRAS JAMBE DOS

image robot bras jambe dos colere = "F4_dosCasse_sansBras_sans_Jambe_colere.png"

image robot bras jambe dos gene = "F4_dosCasse_sansBras_sans_Jambe_gene.png"

image robot bras jambe dos joie = "F4_dosCasse_sansBras_sans_Jambe_joie.png"

image robot bras jambe dos neutre = "F4_dosCasse_sansBras_sans_Jambe_neutre.png"

image robot bras jambe dos peur = "F4_dosCasse_sansBras_sans_Jambe_peur.png"

image robot bras jambe dos triste = "F4_dosCasse_sansBras_sans_Jambe_triste.png"

# FLAGS

define perteDeBras = False
define perteDeJambe = False
define perteDeDos = False



label start:

    jump suiteVerte

    jump rencontre

return
