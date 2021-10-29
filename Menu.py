# coding: utf-8

# imports
import time
import Map.Variables as Var
# variables


# functions

def Menu():

    print("\nDemarrons le jeu de l'Ile au Python\n")
    print("\nCe matin, tu n'as pas été réveillé par les mouvements du navire (ton dernier souvenir est de t’être endormi sur la  confortable couchette de ta cabine à bord de l’Argo),\nmais par le bruit des vagues, la chaleur du soleil et le champ  des oiseaux…\n")  
    print("\nIl semble que tu ne sois plus sur le bateau.") 
    print("\nTu es allongé sur une plage !")  
    print("\nTu te redresses doucement, et, un peu aveuglé par le soleil, tu regardes autour de toi. D'un côté la mer… de l'autre  un paysage sauvage, en partie steppe, en partie jungle.\nAssez loin, au-delà des arbres, tu penses apercevoir des  montagnes...\n")
    time.sleep(5)

    playerName = input("Avant d'aller plus loin dis moi comment tu t'appelles ?\n")
    Var.playerName = playerName

    print(f"\nBienvenu à toi {playerName}!\n")
    print("\nIl est clair que tu n’es pas arrivé ici par hasard, ce n'est pas un naufrage, on t’a déposé sur cette plage.\nMais entre le moment où tu t’es endormi et ton réveil il y a quelques minutes, c'est le trou noir…\n")
    time.sleep(3)

    input(f"\nDis moi ce que tu veux faire {playerName} ?\n(D)émarrer une nouvelle partie\n(C)harger une partie\n(Q)uitter le jeu\n").upper()


    """
        Code start
    """
    
    


# code starts here
if __name__ == "__main__":
    Menu()