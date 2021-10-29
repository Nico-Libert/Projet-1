# coding: utf-8

# import

import time
import random
import json
import Map.Variables as Var
import Map.Player as Player
import Map.Carte as Map
import Game as Game
from Map.RichConsole import ColorPrintAt


def TexteFizzBuzz () : # affichage du texte du jeu au bon endroit 

    with open("Map/DataTexte.json", "r", encoding = "utf-8") as Myfile :
        Var.texte = json.load(Myfile)

    
    ColorPrintAt (
        Var.texte['Icone'], 
        Var.texte['Foreground'],
        Var.texte['Background'],
        42,
        Var.texte['X'])

    print("\n                                            Le jeu du FizzBuzz                                   \n")
    print("En explorant la jungle, tu remarques une bande de singes braillards évoluant dans les arbres\nEn écoutant avec un  peu plus d’attention, tu te rends comptes que les singes semblent articuler des nombres et que deux sons  reviennent régulièrement : Fizz et Buzz…\n")
    print("Les cris s’arrêtent et tu te retrouves subitement entouré par les singes. ")
    print("Le chef Gorille, s’approche de toi.\nIl te toise un  instant puis, du doigt, te désigne un endroit en hauteur. Tu aperçois une clé en or, pendue à liane mais les singes ne semble pas disposés à te la donner comme ça !")
    print("Le chef Gorille se rapproche de toi et commence à te parler…\n« Toi jouer ! Si gagner alors clé à toi ! »\n Jouer ? Mais à quoi ? Semblant lire dans tes pensées, le chef dit alors\n« Nous montrer. »\nPuis il dit « 1 ». Un autre singe dans les arbres  dit alors « 2 », puis un troisième « Fizz » et ainsi de suite : « 4 », « Buzz », « Fizz », « 7 », « 8 », « Fizz », « Buzz »,  « 11 », « 12 »…\nÀ ce moment, tous les autres singes se mettent à rire et celui qui vient d’annoncer 12 pousse un  cri de déception et se retourne sur sa branche en boudant, puis le jeu recommence avec les singes restants : « 1 »,  « 2 », « Fizz »… \nAu bout de quelques tours tu comprends le principe du jeu et tu tentes ta chance pour obtenir la clé.\n")
    time.sleep(1)
    print(input("Demarrons la partie !\nAppuye sur Enter quand tu es prêt.\n"))
    time.sleep(3)

def FizzBuzz():

    with open("Quêtes\Player.json", "r", encoding = "utf-8") as Myfile :
        player = json.load(Myfile)
    
    # création d'une liste vide pour ajouter les joueurs
    name = []
    # création d'une liste vide pour ajouter les chances des joueurs
    chance = []
    

    for i in range(len(player)): # calcule des probabilités de chances pour chaque joueurs

        probaPlayers = random.randint(player[i]['minProba'],player[i]['maxProba'])
        name.append(player[i]['name'])
        chance.append(probaPlayers)
    
       

    goodAnswer = True

    # donne un nombre au hasard pour déterminer ensuite l'ordre de passage des joueurs
    
    firstPlayer = random.randint(0,len(name)-1)

    while goodAnswer :
        
        turn = 0    
        
        while turn >= 0 :
            turn += 1

            numeroChance = random.randint(1,101)

            
            if firstPlayer >= len(name)-1:
                firstPlayer = 0
            
            else:
                firstPlayer += 1
            
            if len(name) > 1 :
                
                # bonnes et mauvaises réponses au fizzbuzz

                if turn%3==0 and turn%5==0 : 
                    goodResponse = "Fizzbuzz"
                    badResponse = "Buzz"
                elif turn%3==0 :
                    goodResponse = "Fizz"
                    badResponse = turn
                elif turn%5==0 :
                    goodResponse = "Buzz"
                    badResponse = "Fizzbuzz"
                else :
                    goodResponse = turn
                    badResponse = "Fizz" 

                # mauvaise réponse >> on supprime le joueur de la liste et on recommence le jeu

                if numeroChance > chance[firstPlayer] :
                    print(f"{name[firstPlayer]} : {badResponse} !\nmauvaise réponse il fallait dire {goodResponse} il est donc éliminé !\n\n")
                    name.pop(firstPlayer)
                    chance.pop(firstPlayer)
                       
                    if len(name) > 1 :
                        print(f"Nous recommencons au début, sont encore en jeu :\n{name}\n")
                        time.sleep(2)
                        turn = 0

                    # c'est le joueur qui a gagné la partie, il obtient une nouvelle clé    
                   
                    else :
                        if name[0] == "Toi" :
                            print(f"\nBravo c'est {name} qui as gagné le Fizzbuzz")
                            print("Tu peux aller chercher la clé d'or en haut de l'arbre !")
                            Var.keys += 1 
                            print(f"\nDésormais tu as {Var.keys} clé(s)")
                            time.sleep(1)
                            break

                        # c'est un des singes qui gagne la partie, le joueur décide s'il recommence le jeu
                        
                        else :
                            print(f"\nBravo c'est {name} qui a gagné le Fizzbuzz")    
                            print("Je ne te félicite pas ! Les singes se moquent de toi et ils ont raison !!! C'est pourtant pas compliqué !\n")
                            replay = input("Veux tu recommencer la partie ?\n (O)ui / (N)on\n").upper()
                            if replay == "O" :
                                print("Allez c'est reparti ! Je compte sur toi pour ne pas être la risée de toute cette bande de Singes !!!\n")
                                time.sleep(3)
                                return FizzBuzz()
                            else :
                                print("Les singes ont hâtent de te revoir pour pouvoir t'humilier une nouvelle fois !")

                # les joueurs donnent la bonne réponse
                
                else :
                    print(f"{name[firstPlayer]} : {goodResponse}\n")
                    time.sleep(3)
                
            else :
                goodAnswer = False
                break 

if __name__ == "__main__":
    FizzBuzz()
   