label ours:


    "*Ils entrent dans un bâtiment en vitesse pour échapper au drone. Mais ils tombent nez à nez avec un ours, ils doivent réagir vite.*"
    $ timeout = 3.0
    $ timeout_label = "timerours"
    menu:
        "Prendre Athénaïs et se cacher":
            $ posture = False
            $ timeout_label = None

            r "Ne...bouge plus...et ne fais... pas de bruit."

            "*F4 et Athénaïs attendent que le drone passe et ne font pas de bruit pour ne pas alerter l’ours*"

            "*Après que le drone soit parti, ils reprennent leur route.*"

            jump enfantAttaque
        "Protéger Athénaïs de l’ours en la faisant reculer":
            $ timeout_label = None
            $ posture = True
            play sound "animals_bear_growl_002.mp3"
            "*L’ours remarque que F4 se met en position de défense et il décide de protéger son territoire en sautant sur ce dernier. Il est projeté au sol.*"

            a "F4 ! Non !"
            "*F4 trouve un morceau de métal à côté de lui et frappe l’ours avec pour s’échapper des griffes de celui-ci*"

            "*Lorsque F4 s’en sort, il prend Athénaïs par la main et commence à courir, difficilement, avec elle*"


            jump enfantAttaque


label timerours:
    $ posture = True
    $ timeout_label = None
    "*L’ours se jette sur Athénaïs, mais F4 s’interpose pour la protéger. Il est projeté au sol.*"
    "*F4 trouve un morceau de métal à côté de lui et frappe l’ours avec pour s’échapper des griffes de celui-ci*"

    "*Lorsque F4 s’en sort, il prend Athénaïs par la main et commence à courir, difficilement, avec elle*"
jump enfantAttaque
