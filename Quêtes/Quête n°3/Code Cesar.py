# coding: utf-8

# imports

import random

# variables


# functions

def CodeCesar():
    """
        Code start
    """
    print("\n                                       Zen de Python            \n")
    print("                 « Récite le crédo du  Python, puis trace ton nom secret »           \n")
    print("\nAu nord de la plage, tu trouves un petit temple taillé dans la paroi rocheuse. Au-dessus de l’arche d’entrée, est écrit un message dans une langue apparemment inconnue mais utilisant l’alphabet habituel.") 
    print("Sur les colonnes de l’arche, sont d’ailleurs gravées en relief toutes les lettres de l’alphabet.\n")
    
    zenPython ="\x1b[42mexplicit is better than implicit beautiful is better than ugly simple is better than complex\x1b[0m"
    print(zenPython)

    codeAlphabet =[
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        ]

    keyAlphabet = random.randint(0,25)
    # letterCode = codeAlphabet[0][keyAlphabet]

    # if letterCode in codeAlphabet :
    #     decalage = codeAlphabet.index(letterCode)
    #     debutAlphabet = decalage+keyAlphabet
    #     finAlphabet = debutAlphabet + 26
    #     newAlphabet = codeAlphabet[debutAlphabet:finAlphabet]
    #     print(newAlphabet)

        
    newZenpython = ""

    for letter in zenPython:
        if letter == " ":
            newZenpython += " "
        for index, listLetter in enumerate(codeAlphabet[0]):
            if letter == listLetter:
                newLetter = index + keyAlphabet
                newZenpython += codeAlphabet[1][newLetter]
    print(newZenpython)
    print("\nNe voyant pas trop quoi faire d’autre pour le moment, tu  décides d’entrer dans le temple...\n")
    # # for letter in zenPython :

        # newZenpython = zenPython.replace(alphabet[letter], newAlphabetzen[letter])
        
    def CodeName ():   
        
        namePlayer = input("\nAh te voilà entré dans le temple !\nRappelles moi ton prénom ? ")
        print(f"\nTrès bien {namePlayer} si tu veux obtenir la clé derrière la grille,\nnous allons vérifier si tu connais les secrets du Code Cesar.\nInscris ton prénom codé et si tu réussis, tu auras ta seconde clé ! ")
    
        newName = ""

        for letter in namePlayer:
            if letter == " ":
                namePlayer += " "
            for index, listLetter in enumerate(codeAlphabet[0]):
                if letter == listLetter:
                    newLetter = index + keyAlphabet
                    newName += codeAlphabet[1][newLetter]
        # print(newName)
        
        return newName, namePlayer

    newName, namePlayer = CodeName()

    def Result ():

        # print(newName)
        # print(namePlayer)
        
        codeCesar = True
        
        while codeCesar :
        
            codeName = input("\nA toi de jouer : ")
            if codeName == newName :
                print("\nBravo le code Cesar n'a plus de secret pour toi !")
                codeCesar = False
            else :
                print(f"Eh non {namePlayer} tu as du faire une erreur !\nRecommence ")
            

    Result()
if __name__ == "__main__":
    CodeCesar()
 