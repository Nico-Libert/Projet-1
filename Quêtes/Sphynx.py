# coding: utf-8

# imports
import time
import Map.Variables as Var

# variables


# functions





def Sphynx():
    """
        Code start
    """
    print("\nTout au nord de la zone, à côté d’une magnifique cascade descendant de la montagne, tu remarques une grotte.\n Intrigué, tu y pénètres mais l’intérieur est très sombre.\nHeureusement, une torche et un silex pour l’allumer se trouvent sur une pierre près de l’entrée.\nTu allumes donc  la torche et tu t’enfonces dans la grotte. Au bout de quelques minutes, tu trouves une grosse porte en bois qui  bloque le passage.\nAu milieu de cette porte, trois grosses serrures qui semblent refléter les couleurs de 3 métaux  précieux : bronze, argent et or.\n") 
    time.sleep(5)
    print("Si tu as brillamment récupéré les 3 clés de bronze, d'argent et d'or insère les dans chaque serrures et découvre si la porte s'ouvre !\n")

    keysSphynx = 3
    keysM = keysSphynx - Var.keys

    if Var.keys == keysSphynx :
        print(f"\n\x1b[42mBravo tu es un vrai aventurier tu as réussi à obtenir toutes les clés !\nLe jeu est maintenant terminé\n\x1b[0m")
        time.sleep(10)
    else :
        print(f"\n Oh non il te manque encore {keysM} retourne à l'aventure... ")
        time.sleep(5)


# code starts here
if __name__ == "__main__":
    Sphynx()