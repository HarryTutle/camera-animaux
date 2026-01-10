# camera-animaux
Repère les sangliers, cerfs, renards, hommes, arbres. Active une alarme pour les sangliers (buzzer, mais peu être modifié avec à la place un relai qui active une alarme plus puissante). Prend en photo et enregistre sur clé usb les images des animaux seulement.

Le modèle utilisé est un mobilenet modifié présent dans la librairie keras.applications. la dernière couche a été enlevée et remplacée par une couche Dense de 5 sorties (pour les 5 classes à distinguer soit cerfs, sangliers, renards, arbres, humains) avec une activation softmax. J'ai fait du transfer learning avec des datasets présents dans kaggle pour obtenir un dataset de photos d'arbres, hommes et animaux (sangliers, cerfs, renards). On obtient un score de 95 % environ sur le jeu test, pareil sur le jeu de validation. 

La caméra s'éteind via un interrupteur pour éteindre normalement la raspberrypi, et l'autre interrupteur éteind l'alarme au besoin. Quand une photo est prise, elle est intitulée avec l'heure et la date de la prise (quand il y a une connexion wifi avec la raspberry).

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



Le programme resnet50 gère le transfer learning.

Il reste à ajouter le céclenchement automatique du mode nocturne de la camera, avec l'ajout d'une photorésistance.

Important: la caméra fonctionne par contraste, il faut l'installer face à des arbres. Elle est entrainée à distinguer ses classes par contraste avec les arbres. Si elle est placée face à autre chose il peut y avoir des bugs.


![1768044470997](https://github.com/user-attachments/assets/e12a770d-10d6-4148-a166-858812437494)

![1768044470982](https://github.com/user-attachments/assets/87498bcf-cb1b-4c14-b82e-3cf82660376f)


