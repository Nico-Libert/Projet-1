# coding: utf-8

# import

# from os import name
import random
import json

# print("En explorant la jungle, tu remarques une bande de singes braillards évoluant dans les arbres. En écoutant avec un  peu plus d’attention, tu te rends comptes que les singes semblent articuler des nombres et que deux sons  reviennent régulièrement : Fizz et Buzz…")
# print("À un moment, les cris s’arrêtent et tu te retrouves subitement entouré par les singes. ")
# print("L’un d’eux, probablement le chef vu sa démarche assurée, descend de l’arbre et s’approche de toi. Il te toise un  instant puis, du doigt, te désigne un endroit en hauteur. En levant la tête, tu aperçois une grosse clé en or, pendue  à une solide liane, tu commences à chercher un moyen de grimper dans les arbres, mais cela déclenche une vive  réaction de la part des singes. Il semble qu’ils ne soient pas disposés à te donner la clé comme ça !")
# print("Tu te ravises alors, et le chef se rapproche de toi et commence à te parler… « Toi jouer ! Si gagner alors clé à toi ! » Jouer ? Mais à quoi ? Semblant lire dans tes pensées, le chef dit alors « Nous montrer. » Puis il dit « 1 ». Un autre singe dans les arbres  dit alors « 2 », puis un troisième « Fizz » et ainsi de suite : « 4 », « Buzz », « Fizz », « 7 », « 8 », « Fizz », « Buzz »,  « 11 », « 12 »… À ce moment, tous les autres singes se mettent à rire et celui qui vient d’annoncer 12 pousse un  cri de déception et se retourne sur sa branche en boudant, puis le jeu recommence avec les singes restants : « 1 »,  « 2 », « Fizz »… Au bout de quelques tours tu comprends le principe du jeu et tu tentes ta chance pour obtenir la clé.")


def loadFromJson():

    with open("Quêtes\Quête n°2\Player.json", "r", encoding = "utf-8") as Myfile :
        player = json.load(Myfile)

    # print(player)
    tirage = {
        "name" : "",
        "chance" : ""
    }
    
    goodAnswer = True


    for i in range(len(player)):
        probaPlayers = random.randint(player[i]['minProba'],player[i]['maxProba'])
        # print(f"{player[i]['name']} {probaPlayers}")
        tirage['name'] = player[i]['name']
        tirage['chance'] = probaPlayers
        # print(tirage)
        
        while goodAnswer :
            
            for turn in range(1,200) :
                result = turn
                numeroChance = random.randint(1,101)
                for j in range(len(tirage)) :
                    # print(tirage['chance'])
                    if result%3==0 and result%5==0 : 
                        goodResponse = "Fizzbuzz"
                    elif result%3==0 :
                        goodResponse = "Fizz"
                    elif result%5==0 :
                        goodResponse = "Buzz"
                    else :
                        goodResponse = result
                if numeroChance < int(tirage["chance"]): 
                    print(f"Le {tirage['name']} dit {goodResponse}")
                else :
                    if result%3==0 and result%5==0 : 
                        badResponse = "Fizz"
                    elif result%3==0 :
                        badResponse = "Buzz"
                    elif result%5==0 :
                        badResponse = "Fizzbuzz"
                    else :
                        badResponse = "euuh je ne sais pas !"
                    print(f"Le {tirage['name']} dit {badResponse} !\net non mauvaise réponse tu aurais du dire {goodResponse} tu es donc éliminé !")
                    goodAnswer = False
                    # tirage.pop(tirage['name'])
    # 
    
    # print(tirage)
    
    # print(numeroChance)

    
   
    # while goodAnswer :

    #     
    #         
    #         
            
            

                
# #         print(result)
# # # print(f"{listPlayers[i]} {result}")
if __name__ == "__main__":
    loadFromJson()
   