# coding: utf-8

# imports
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

possibleMove = {
                "HAUT" : { "lineY" : -1, "letterX": 0}, 
                "BAS" : { "lineY" : +1, "letterX" : 0}, 
                "GAUCHE" : { "lineY"  : 0, "letterX": -1}, 
                "DROITE" : { "lineY"  : 0, "letterX" : +1}, 
                "QUITTER" : { "lineY" : 0, "letterX" : 0}
}

keys = 3
playerName = ""

game = True
nombreMystère = None

dataPlayer = None
dataMystère = None
dataCésar = None
dataFizzbuzz = None
dataSphynx = None