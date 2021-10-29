# coding: utf-8

# imports
import Map.Carte as Map
import Map.Player as Player
import Map.Variables as Var

# variables


# functions

def Main():
    """
        Code start
    """
    Map.loadFromJson()
    Player.LoadData()

# pour chaque action affiche la Map, le joueur et son déplacement 
    
    while Var.game :
        Map.draw()
        Player.draw() 
        Player.Move()
        Player.Quest()
    


# code starts here
if __name__ == "__main__":
    Main()