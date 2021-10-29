# coding: utf-8

# imports


from Map.RichConsole import ColorPrintAt
import Map.Variables as Var
import json
from Quêtes.CodeCesar import CodeCesar
from Quêtes.FizzBuzz import FizzBuzz, TexteFizzBuzz
from Quêtes.NombreMystère import Mystère
from Quêtes.FizzBuzz import FizzBuzz
from Quêtes.Sphynx import Sphynx

# variables


# functions

def LoadData () :


    with open("Map/DataPlayer.json", "r", encoding = "utf-8") as Myfile :
        Var.dataPlayer = json.load(Myfile)

    with open("Map/DataMystère.json", "r", encoding = "utf-8") as DataM :  
       Var.dataMystère = json.load(DataM)
    
    with open("Map/DataCésar.json", "r", encoding = "utf-8") as DataC :  
       Var.dataCésar = json.load(DataC)
    
    with open("Map/DataFizzbuzz.json", "r", encoding = "utf-8") as DataF :  
       Var.dataFizzbuzz = json.load(DataF)

    with open("Map/DataSphynx.json", "r", encoding = "utf-8") as DataS :  
       Var.dataSphynx = json.load(DataS)

def Move():
    """
        Code start
    """
    
#   stocker position de depart
    
    playerY = Var.dataPlayer['Y'] 
    playerX = Var.dataPlayer['X'] 

#   gerer les directions
   
    action = input("\nQue veux tu faire ?\n Aller en (H)aut\n Aller en (B)as\n Aller à (G)auche\n Aller à (Droite)\n(Q)uitter\n").upper()

    if action == "H" :
        
        playerY -= 1
    
    elif action == "B" :
    
        playerY += 1
        
    elif action == "G" :
        
        playerX -= 2
        
    elif action == "D" :
        
        playerX += 2
    
    elif action == "Q" : 
        
        Var.game = False
        print("Tu quittes le jeu !")
    
    else :
        print("\n Tu n'as pas fait le bon choix !")
 

#   sauver la nouvelle position

    Var.dataPlayer['Y'] = playerY
    Var.dataPlayer['X'] = playerX

def Quest():
    
    if Var.dataPlayer['Y'] == Var.dataMystère['Y'] and Var.dataPlayer['X'] == Var.dataMystère['X'] :
        Mystère()

    elif Var.dataPlayer['Y'] == Var.dataCésar['Y'] and Var.dataPlayer['X'] == Var.dataCésar['X'] :
        CodeCesar()

    elif Var.dataPlayer['Y'] == Var.dataFizzbuzz['Y'] and Var.dataPlayer['X'] == Var.dataFizzbuzz['X'] :
        TexteFizzBuzz()
        FizzBuzz()
        
    elif Var.dataPlayer['Y'] == Var.dataSphynx['Y'] and Var.dataPlayer['X'] == Var.dataSphynx['X'] :
        Sphynx()
        
def draw () :

    ColorPrintAt (
        Var.dataPlayer['Icone'], 
        Var.dataPlayer['Foreground'],
        Var.dataPlayer['Background'],
        Var.dataPlayer['Y'],
        Var.dataPlayer['X'])
    ColorPrintAt (
        Var.dataMystère['Icone'], 
        Var.dataMystère['Foreground'],
        Var.dataMystère['Background'],
        Var.dataMystère['Y'],
        Var.dataMystère['X'])
    ColorPrintAt (
        Var.dataCésar['Icone'], 
        Var.dataCésar['Foreground'],
        Var.dataCésar['Background'],
        Var.dataCésar['Y'],
        Var.dataCésar['X'])
    ColorPrintAt (
        Var.dataFizzbuzz['Icone'], 
        Var.dataFizzbuzz['Foreground'],
        Var.dataFizzbuzz['Background'],
        Var.dataFizzbuzz['Y'],
        Var.dataFizzbuzz['X'])
    ColorPrintAt (
        Var.dataSphynx['Icone'], 
        Var.dataSphynx['Foreground'],
        Var.dataSphynx['Background'],
        Var.dataSphynx['Y'],
        Var.dataSphynx['X'])


if __name__ == "__main__":
        Move()