import os
from fonctions import directionPas
class Labyrinthe:

    """Classe représentant un labyrinthe."""

########### Constructeur et attribut ###########
    def __init__(self, mapName):
        """Constructeur, prend uniquement en paramètre le nom de la carte"""
        # Listes des attributs

        # Nom de la carte, 'prison', 'facile'
        self.mapName=mapName

        # Commande pour ouvrir le fichier en écriture
        self.fileName=open("cartes/"+self.mapName+".txt","r")

        # Readlines => Permet de lire ligne par ligne, on récupère ces lignes dans une liste
            # Cette liste de ligne constitue notre grille
        self.listeLignes=self.fileName.readlines()

        # Commande pour fermer le fichier
        self.fileName.close()

        # Booléen de victoire, initialisé à faux
         # Ce booléen nous permettra de configurer la condition de victoire et son effet
        self.victoire=False

        # Afin de pouvoir gérer l'action lorsque 'X' est passe à travers une porte, il faut récupérer les coordonnées de toutes les portes
        ######### Pour récupérer les coordonnées des portes #########
        i=0
        j=0
        self.listePorte=[]
        for ligne in self.listeLignes:
            j+=1
            i=0
            for elt in ligne:
                i+=1
                if elt==".":
                    self.listePorte.append((i,j))
        #############################################################
############################################

########### Méthode de classe ###########

    def afficherLabyrinthe(self):
        """Méthode pour afficher le labyrinthe dans la console"""
        for elt in self.listeLignes:
            print(elt,end="")
        print()

    def getPosition(self,char="X"):
        """Fonction qui permet de récupérer la position d'un caractère
        par défaut 'X'. Renvoie un couple (x,y) """
        y = 0
        for elt in self.listeLignes:
            y += 1
            if (elt.find(char) != -1):
                x=elt.find(char)
                return (x+1,y)
    
    def getObject(self,x,y):
        """Récupère le contenu d'une case, prend des coordonnées en paramètres et retourne le caractère à ces coordonnées"""
        return self.listeLignes[y-1][x-1] # -1 parce que le tableau commence à 0    

    def sauvegarde(self):
        """Sauvegarde dans le fichier 'Save.txt'"""

        # On vérifie que le fichier existe
            # 'exists' est un booléen
        exists = os.path.isfile("cartes/Save.txt")
        if exists:
            # Le fichier existe => On l'ouvre en écriture 'r'
            with open ("cartes/Save.txt","w") as f: 
                for elt in self.listeLignes:
                    f.write("%s" %elt)
        else:
            with open ("cartes/Save.txt","x") as f: 
                # Le fichier n'existe pas, on le créer et on l'ouvre en écriture 'x'
                for elt in self.listeLignes:
                    f.write("%s" %elt)
    
    ############## Les méthodes de déplacement ##############
    """Avant de se déplacer, il faut vérifier qu'il n'y a pas de mur dans la direction dans
    laquelle nous nous dirigeons et en prenant en compte le nombre de pas"""
    def verifMur(self,direction,num):
        """Méthode qui vérifie la presence d'un mur.
        Prend une direction et un nombre en entrée.
        Retourne un booléen (présence ou non d'un mur: True or False)"""
        i=1
        if direction not in ["e","o","s","n"]:
            print(direction+" n'est pas une entrée valide, merci de rentrer\n'e','o','s' ou 'n'")
        else:
            x,y=self.getPosition("X")
            if direction =="e":
                presenceMur=False
                while(not presenceMur and i<num+1):
                    if self.getObject(x+1*i,y)=="U":
                        self.victoire=True
                        break
                    elif self.getObject(x+1*i,y)=="O":
                        presenceMur=True
                    i+=1
                return presenceMur
         
            if direction =="o":
                presenceMur=False
                while(not presenceMur and i<num+1):
                    if self.getObject(x-1*i,y)=="U":
                        self.victoire=True
                    elif self.getObject(x-1*i,y)=="O":
                        presenceMur=True
                    i+=1
                return presenceMur

            if direction=="s":
                presenceMur=False
                while(not presenceMur and i<num+1):
                    if self.getObject(x,y+1*i)=="U":
                        self.victoire=True
                    elif self.getObject(x,y+1*i)=="O":
                        presenceMur=True
                    i+=1
                return presenceMur

            if direction=="n":
                presenceMur=False
                while(not presenceMur and i<num+1):
                    if self.getObject(x,y-1*i)=="U":
                        self.victoire=True
                    elif self.getObject(x,y-1*i)=="O":
                        presenceMur=True
                    i+=1
                return presenceMur
    
    """
    Les déplacements se gèrent à partir de la grille de labyrinthe, soit la listeLignes
    définit en attribut plus haut.
    Pour chaque déplacement on réecrit la ligne correspondante selon le déplacement
    """
    def moveEst(self):
        """Méthode d'instance qui permet de déplacer le robot à droite"""
        # Les commentaires sont valable pour les méthodes:
            # moveOuest
            # moveNord
            # moveSud
        # Le principe reste le même: On réecrit la ligne selon le déplacement


        # Récupération des coordonnées de 'X'
        x,y=self.getPosition("X") 
        coordX=(x,y)

        # Condition si X est sur une porte
        if coordX in self.listePorte:
            a="."
        else:
            a=" "
        
        # Si on se dirige vers la sortie -> Victoire
        if self.getObject(x+1,y)=="U":
            self.victoire=True
        
        # Sinon, s'il y a un mur, on ne se déplace pas
        elif self.getObject(x+1,y)=="O":
            print("déplacement impossible")
        
        # Sinon, c'est que le champs est libre -> on peut se déplacer
        else:
            self.listeLignes[y-1]=self.listeLignes[y-1][0:x-1]+a+"X"+self.listeLignes[y-1][x+1:] # Réécriture de la ligne
            self.sauvegarde()
    def moveOuest(self):
        """Méthode d'instance qui permet de déplacer le robot à gauche"""
        x,y=self.getPosition("X") # Récupération des coordonnées de 'X'
        coordX=(x,y)
        if coordX in self.listePorte:
            a="."
        else:
            a=" "
        if self.getObject(x-1,y)=="U":
            self.victoire=True
        elif self.getObject(x-1,y)=="O":
            print("déplacement impossible")  # On vérifie qu'il n'y a pas de mur
        else:
            self.listeLignes[y-1]=self.listeLignes[y-1][0:x-2]+"X"+a+self.listeLignes[y-1][x:]# Réécriture de la ligne
            self.sauvegarde()
    def moveNord(self):
        """Méthode d'instance qui permet de déplacer le robot en haut"""
        x,y=self.getPosition("X") # Récupération des coordonnées de 'X'
        coordX=(x,y)
        if coordX in self.listePorte:
            a="."
        else:
            a=" "
        if self.getObject(x,y-1)=="U":
            self.victoire=True
        elif self.getObject(x,y-1)=="O":
            print("déplacement impossible")  # On vérifie qu'il n'y a pas de mur
        else:
            self.listeLignes[y-2]=self.listeLignes[y-2][0:x-1]+"X"+self.listeLignes[y-2][x:]
            self.listeLignes[y-1]=self.listeLignes[y-1][0:x-1]+a+self.listeLignes[y-1][x:]
            self.sauvegarde()
    def moveSud(self):
        """Méthode d'instance qui permet de déplacer le robot bas"""
        x,y=self.getPosition("X") # Récupération des coordonnées de 'X'
        coordX=(x,y)
        if coordX in self.listePorte:
            a="."
        else:
            a=" "
        if self.getObject(x,y+1)=="U":
            self.victoire=True            
        if self.getObject(x,y+1)=="O":
            print("déplacement impossible")  # On vérifie qu'il n'y a pas de mur
        else:
            self.listeLignes[y]=self.listeLignes[y][0:x-1]+"X"+self.listeLignes[y][x:]
            self.listeLignes[y-1]=self.listeLignes[y-1][0:x-1]+a+self.listeLignes[y-1][x:]
            self.sauvegarde()



    ##########################################################
    

    def jeu(self):
        """Méthode principale qui va se service des méthodes précédentes pour gérer le jeu"""
         # Boucle principale d'entrée dans le jeu
        while True:
            
            self.afficherLabyrinthe() # A chaque tour de boucle on affiche le labyrinthe
            print("Saisissez une direction et un nombre de pas")           
            direction,nbrPas=directionPas()# On utilise la fonction directionPas() (cf fonction.py)
            
            # On vérifie la saisie utilisateur
            if direction not in ["e","o","s","n","q"]:
                print("Mauvaise saisie")
                continue
            
            # Conditionnelle pour le 'q' => quitter la partie
            if direction=="q":
                input("Vous quittez le jeu...")
                break

            # A ce stade la saisie de la direction est: n, s, e ou o
            else:
                # On vérifie la présence ou non d'un mur
                mur=self.verifMur(direction,nbrPas)

                # S'il y a un mur => on ne bouge pas
                if mur:
                    print("impossible, il y a un mur")
                    continue
                
                # Sinon on adapte le code en fonction de la direction
                # et on se déplace autant de fois qu'il faut (cf nbrPas)
                elif direction =="o":
                    i=0
                    while (i<nbrPas):
                        self.moveOuest()
                        i+=1
                elif direction =="e":
                    i=0
                    while (i<nbrPas):
                        self.moveEst()
                        i+=1

                elif direction =="n":
                    i=0
                    while (i<nbrPas):
                        self.moveNord()
                        i+=1

                elif direction =="s":
                    i=0
                    while (i<nbrPas):
                        self.moveSud()
                        i+=1
            
            # Si le code nous renvoie l'information d'une victoire on casse la boucle => le jeu est fini
            if self.victoire==True:
                print("VICTOIRE")
                break
