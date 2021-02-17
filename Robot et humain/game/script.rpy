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

image robot neutre = "robot_neutre.png"

image robot manchot = "robot_minusbras.png"

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


label start:

    jump rencontre

return
