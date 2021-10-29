# coding: utf-8

# imports

import random
import time
import Map.Variables as Var
import json
from Map.RichConsole import ColorPrintAt


def CodeCesar():
    """
        Code César, le joueur doit afficher son nom codé à l'aide du Zen de Python codé
    """
    with open("Map/DataTexte.json", "r", encoding = "utf-8") as Myfile :
        Var.texte = json.load(Myfile)

    ColorPrintAt (
        Var.texte['Icone'], 
        Var.texte['Foreground'],
        Var.texte['Background'],
        42,
        Var.texte['X'])
    
    
    print("\n                                       Zen de Python            \n")
    print("                 « Récite le crédo du  Python, puis trace ton nom secret »           \n")
    print("\nAu nord de la plage, tu trouves un petit temple taillé dans la paroi rocheuse. Au-dessus de l’arche d’entrée, est écrit un message dans une langue apparemment inconnue\nmais utilisant l’alphabet habituel.") 
    print("Sur les colonnes de l’arche, sont d’ailleurs gravées en relief toutes les lettres de l’alphabet.\n")
    time.sleep(5)
    zenPython ="\x1b[42mexplicit is better than implicit beautiful is better than ugly simple is better than complex\x1b[0m"
    print(zenPython)
    time.sleep(3)
    
    # 2 listes avec alphabet pour réaliser le décalage
    codeAlphabet =[
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        ]
    # clé de décalage

    keyAlphabet = random.randint(0,25)

    # zen de python codé
        
    newZenpython = ""

    # codage du zen de python

    for letter in zenPython:
        if letter == " ":
            newZenpython += " "
        for index, listLetter in enumerate(codeAlphabet[0]):
            if letter == listLetter:
                newLetter = index + keyAlphabet
                newZenpython += codeAlphabet[1][newLetter]
    print(newZenpython)
    time.sleep(3)
    
    print("\nNe voyant pas trop quoi faire d’autre pour le moment, tu  décides d’entrer dans le temple...\n")
    time.sleep(2)    

      
        
    namePlayer = input("\nAh te voilà entré dans le temple !\nRappelles moi ton prénom ? ")
    print(f"\nTrès bien {namePlayer} si tu veux obtenir la clé derrière la grille,\nnous allons vérifier si tu connais les secrets du Code Cesar.\nInscris ton prénom codé et si tu réussis, tu auras ta seconde clé ! ")

    newName = ""

    # codage du nom du joueur

    for letter in namePlayer:
        if letter == " ":
            namePlayer += " "
        for index, listLetter in enumerate(codeAlphabet[0]):
            if letter == listLetter:
                newLetter = index + keyAlphabet
                newName += codeAlphabet[1][newLetter]
    print(newName)
    
        
    codeCesar = True
    
    # on vérifie si le nom écrit par le joueur correspond à son nom, oui > clé, non > il recommence
    
    while codeCesar :
    
        codeName = input("\nA toi de jouer : ")
        if codeName == newName :
            Var.keys += 1
            print(f"\nBravo le code Cesar n'a plus de secret pour toi !\nTu obtiens la clé d'argent ! Tu as {Var.keys} clé(s).")
            time.sleep(5)
            codeCesar = False
        else :
            print(f"Eh non {namePlayer} tu as du faire une erreur !\nRecommence ")


if __name__ == "__main__":
    CodeCesar()
 