python:
    flag = True
# Règle le timer sur un certain nombre de secondes. Peut-être modifié avec en plein milieu du code avec $timeout = 10.0 par exemple
default timeout = 5.0

# timeout_label renvoie au label vers lequel le joueur sera redirigé en cas de temps écoulé.
# pour y assigner un label, écrivez $timeout_label = "start" par exemple
# ne pas oublier de remettre le timeout_label à None pour ne pas que les futurs choix soient aussi timés.
#Prenez en note qu'un nom de label doit être entre guillemets, mais pas None.
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


# Tout ça est à coller, de préférence au tout début du code.
# Pour que votre choix sois timé, attribuez juste avant à votre timeout_label une valeur autre que None

label sansbras:
    show bg villedestroy
    r "ok on est plus ou moins good"
    $timeout_label = "timerUno"
    menu:
        "Continuer à avancer":

            r "let's go on avance"


        "Se reposer dans un refuge médiocre":
            r "Oh regarde une cabane destroy"
            r "go faire une petite pause"
            a "ça marche"


return
