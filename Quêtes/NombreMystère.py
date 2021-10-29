# "

# import
import random
import time
import Map.Variables as Var

def Mystère():

    colorNarateur1 = "\x1b[36m" 
    colorNarateur2 =  "\x1b[0m"
    colorPlayer1 = "\x1b[32m" 
    colorPlayer2 =  "\x1b[0m"

    nbMin = 0
    nbMax = 100
    nbTirage = ("1er Nombre", "2ème Nombre", "3ème Nombre")

    nbTry = 20
    nbNumber = 3

    tryNumber = 0
    encouragement = ["Continue !","Essaye encore !", "Tu vas y arriver continue !","5ème essai ! ", "Allez encore un effort !", "Tu te rapproches !", "Continue !","Décidement !","On y croit !","Déjà 10 essais !", "Concentre toi !", "Tu n'es plus très loin !", "Essaye encore !", "Ne lâche pas !", "Plus que 5 essais", "Allez tu vas y arriver !", "Encore 3 essais !", "Plus que 2 essais !", "Allez dernière chance c'est maintenant !", "Dommage tu n'as pas trouvé le nombre mystère\nRecommence la partie !"]

    print("\nEn haut de la falaise, en bordure de forêt et pas très loin de la plage, tu découvres la statue d’un Sphinx avec une  grosse clé en bronze posée sur les pattes.") 
    print("\nLorsque tu t’en approches, les yeux de la statue s’illuminent et une voix se fait entendre :") 
    print("\n« Bonjour explorateur ! Pour ouvrir la porte de la montagne, atteindre le cœur de l’île et rejoindre tes compagnons,  tu devras tout d’abord prouver ta valeur individuelle en gagnant les 3 clés que tu obtiendras en relevant les défis appropriés. Ceci est le premier d’entre eux. »")
    time.sleep(5)
    print (f"\n{colorNarateur1}Pour la 1ère quête, 3 fois de suite, tu devras deviner le nombre que j’ai en tête, tu as 20 essais maximum pour les  trouver tous, es-tu prêt ?\nAlors allons y !»{colorNarateur2}")
    time.sleep(2)
    
    for nb in range(nbNumber) :
        nbMystere = random.randint(nbMin,nbMax)
        print(f"{colorNarateur1}\nTrouve le {nbTirage[nb]} mystère entre {nbMin} et {nbMax} ? {colorNarateur2}")
        
        for i in range(0,nbTry):

            tryNumber = (int(input(f"\n{colorNarateur1}Quelle est ta proposition ? {colorNarateur2}")))
            
            if nbMystere == tryNumber :

                position = encouragement[1+i]
                print(f"\n{colorPlayer1}Bravo tu as trouvé {nbMystere} le nombre mystère en {encouragement.index(position)} essais !\x1b[0m")
                break
            
            elif nbMystere < tryNumber :

                print(f"\nDommage le nombre mystere est plus petit !\n{encouragement[0+i]}")
            
            elif nbMystere > tryNumber : 

                print(f"\nEt non pas de chance le nombre mystère est plus grand !\n{encouragement[0+i]}")
            
    
    Var.keys += 1            
    print(f"\n\x1b[31mBravo ton courage et ta perseverance t'ont permis d'obtenir ta clé.\nTu as {Var.keys} clé(s).\n\x1b[0m")
    time.sleep(3)
    

if __name__ == "__main__":
    Mystère()



