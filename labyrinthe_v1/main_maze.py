import os
from classe import Labyrinthe
from fonctions import mainMenu, newGameMenu

while True:
    choix1=mainMenu()

    if choix1 == "q":
        print("vous quittez le jeu...")
        break

    elif choix1 == "1":
        choix2=newGameMenu()
        if choix2 =="1":
            lab=Labyrinthe("facile")
            lab.jeu()



        elif choix2 =="2":
            lab=Labyrinthe("prison")
            lab.jeu()

    elif choix1 == "2":
        exists = os.path.isfile("cartes/Save.txt")
        if exists:
            lab=Labyrinthe("Save")
            lab.jeu()
        else:
            print("Pas de sauvegarde\nRetour au menu principal")
            break

