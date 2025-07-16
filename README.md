# camera-animaux
Repère les sangliers, cerfs, renards, hommes, arbres. Active une alarme pour les sangliers (buzzer, mais peu être modifié avec à la place un relai qui active une alarme plus puissante). Prend en photo et enregistre sur clé usb les images des animaux seulement.

Le modèle utilisé est un mobilenet modifié présent dans la librairie keras.applications. la dernière couche a été enlevée et remplacée par une couche Dense de 5 sorties (pour les 5 classes à distinguer) avec une activation softmax. J'ai fait du transfer learning avec des datasets présents dans kaggle pour obtenir un dataset de photos d'arbres, hommes et animaux (sangliers, cerfs, renards). On obtient un score de 95 % environ sur le jeu test, pareil sur le jeu de validation.

La caméra s'éteind via un interrupteur pour éteindre normalement la raspberrypi, et l'autre interrupteur éteind l'alarme au besoin. Quand une photo est prise, elle est intitulée avec l'heure et la date de la prise(quand il y a une connexion wifi avec la raspberry).

matériel:
-boitier étanche pour caméra et électronique avec couvercle transparent, boitier étanche pour la batterie.
-caméra nocturne raspberry
-raspberrypi 4
-interrupteurs (2)
-buzzer
-clé usb
-régulateur de charge
-batterie 44 a/h
-panneau solaire



