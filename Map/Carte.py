# coding: utf-8

# imports

import os, sys
os.system('')
import Map.RichConsole as RC
import json
import Map.Variables as Var



# variables
def loadFromJson():

    # with open("Map/MapElements.json", "r", encoding = "utf-8") as Myfile :
    #     mapElements = json.load(Myfile)


    sable ="\x1b[43m░░\x1b[0m"
    plaine = "\x1b[42m  \x1b[0m"
    jungle = "\x1b[42mϡ \x1b[0m"
    rocher =  "\x1b[40m▒▒\x1b[0m"
    eau = "\x1b[46m  \x1b[0m"
    mer = "\x1b[44m ~\x1b[0m"
    quete = "\x1b[31mЖЖ\x1b[0m"
    player = "\x1b[45m☺\x1b[0m"
    

    s = sable
    p = plaine
    j = jungle
    r = rocher
    e = eau
    m = mer
    q = quete
    l = player




    Var.L1 = [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r]
    Var.L2 = [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r]
    Var.L3 = [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,p,e,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r]
    Var.L4 = [r,r,r,r,r,r,p,p,r,r,r,r,p,r,p,e,e,r,r,r,r,r,r,r,p,p,r,r,r,r,r,r,j,r,r,r,r,j,r,r,r,r,r,r,r,r,r,r,r,r]
    Var.L5 = [r,r,r,r,r,r,p,p,r,p,r,p,p,p,p,e,e,p,p,p,r,p,r,r,p,p,r,p,p,r,p,r,j,j,r,j,j,j,j,j,r,r,r,r,r,r,r,r,r,r]
    Var.L6 = [r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,r,p,p,j,j,j,j,j,j,j,j,j,j,r,j,r,r,r,r,r,r]
    Var.L7 = [r,r,r,r,r,r,r,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,r,r]
    Var.L8 = [r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,j,j,r,r,r,r,r,r]
    Var.L9 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,r,r,r,r,r,r,r]
    Var.L10 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,r,r,r,r,r,r]
    Var.L11 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,r,r,r,r,r]
    Var.L12 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,r,r,r,r,r]
    Var.L13 = [r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,r,r,r,r,r,r]
    Var.L14 = [r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,p,p,p,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,r,r,r,r,r]
    Var.L15 = [r,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,j,j,j,j,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,r,r,r,r]
    Var.L16 = [r,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,j,j,j,j,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,r,r,r,m]
    Var.L17 = [m,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,p,p,p,p,p,p,p,p,p,p,p,s,s,s,s,s,s,p,p,r,r,r,m,m]
    Var.L18 = [m,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p,s,s,s,s,s,s,s,s,s,s,r,m,m,m]
    Var.L19 = [m,r,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,s,s,s,s,s,s,s,s,s,s,m,m,m,m]
    Var.L20 = [m,m,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,s,s,s,s,s,s,s,s,s,m,m,m,m,m]
    Var.L21 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,p,p,p,r,s,s,s,s,s,s,s,s,m,m,m,m,m,m]
    Var.L22 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,j,j,j,j,j,j,j,j,j,j,j,j,p,r,r,s,s,s,s,s,s,s,m,m,m,m,m,m,m]
    Var.L23 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,s,s,s,s,s,s,m,m,m,m,m,m,m,m]
    Var.L24 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,s,s,s,s,s,m,m,m,m,m,m,m,m,m]
    Var.L25 = [m,r,j,j,r,r,j,j,r,r,j,j,j,r,r,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,r,s,s,s,s,m,m,m,m,m,m,m,m,m,m]
    Var.L26 = [m,m,r,r,r,r,r,j,r,r,r,j,r,r,r,r,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,r,r,s,s,m,m,m,m,m,m,m,m,m,m,m]
    Var.L27 = [m,m,r,m,m,r,r,r,r,r,r,r,m,r,r,r,e,e,r,r,r,r,r,m,r,j,r,j,r,r,r,r,r,r,r,r,r,s,m,m,m,m,m,m,m,m,m,m,m,m]
    Var.L28 = [m,m,m,m,m,m,r,m,m,m,r,m,m,m,r,m,m,m,m,r,r,m,m,m,m,r,m,r,m,m,m,m,m,m,m,m,r,m,m,m,m,m,m,m,m,m,m,m,m,m]
    Var.L29 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]
    Var.L30 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]

    Var.carte = [Var.L1,Var.L2,Var.L3,Var.L4,Var.L5,Var.L6,Var.L7,Var.L8,Var.L9,Var.L10,Var.L11,Var.L12,Var.L13,Var.L14,Var.L15,Var.L16,Var.L17,Var.L18,Var.L19,Var.L20,Var.L21,Var.L22,Var.L23,Var.L24,Var.L25,Var.L26,Var.L27,Var.L28,Var.L29,Var.L30]

# création de la carte avec tout les éléments (par lignes et par lettres)

def draw() :

    RC.ClearConsole()

    for line in Var.carte :
        for letter in line :
            print(letter, end="")
        print(letter)


if __name__ == "__main__":
    loadFromJson()
  
        