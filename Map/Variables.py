# coding: utf-8

# données de la carte

carte = ""
L1 = ""
L2 = ""
L3 = ""
L4 = ""
L5 = ""
L6 = ""
L7 = ""
L8 = ""
L9 = ""
L10 = ""
L11 = ""
L12 = ""
L13 = ""
L14 = ""
L15 = ""
L16 = ""
L17 = ""
L18 = ""
L19 = ""
L20 = ""
L21 = ""
L22 = ""
L23 = ""
L24 = ""
L25 = ""
L26 = ""
L27 = ""
L28 = ""
L29 = ""
L30 = ""

# mouvements possibles

possibleMove = {
                "HAUT" : { "lineY" : -1, "letterX": 0}, 
                "BAS" : { "lineY" : +1, "letterX" : 0}, 
                "GAUCHE" : { "lineY"  : 0, "letterX": -1}, 
                "DROITE" : { "lineY"  : 0, "letterX" : +1}, 
                "QUITTER" : { "lineY" : 0, "letterX" : 0}
}

# clé pour le sphynx
keys = 0

# nom du joueur demandé au début du jeu
playerName = ""

# lancement du jeu
game = True

nombreMystère = None

# données pour l'affichage du joueurs, des quêtes et du texte
dataPlayer = None
dataMystère = None
dataCésar = None
dataFizzbuzz = None
dataSphynx = None

texte = ""