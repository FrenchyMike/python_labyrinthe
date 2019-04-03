###################### Affichage et menu ######################

def mainMenu():
    """Fonction qui affiche le menu principale
    Retourne 1,2 ou q"""
    while True:
        print("======== Labyrinthe ========")
        choixJoueur=input("1- Nouvelle partie\n2- Charger la dernière partie\nq- Quitter le jeu\n> ")
        if choixJoueur =="q" or choixJoueur =="1" or choixJoueur =="2":
            return choixJoueur
        else: 
            print("Saisie invalide.\nMerci de saisir: 1, 2 ou q")
            continue
def newGameMenu():
    """Fonction qui affiche le deuxième menu. Il s'agit du menu pour un nouveau jeu.
    Retourne 1, 2 ou q"""
    while True:
        print("------ Nouvelle Partie ------\nLabyrinthes existants :\n1 - facile\n2 - prison\nq - Quitter")
        choix=input("> ")
        if choix =="1" or choix =="2":
            return choix
        elif choix=="q":
            print("retour au menu")
            break
        else:
            print("Saisie invalide.\nMerci de saisir: 1, 2 ou q")
            continue

###################### Autres ######################  

def directionPas():
    """ Fonction qui retourne un str et un int, pour la direction et le nombre de pas"""

    # Cette fonction permet de contrôler la saisie utilisateur lorsque celui-ci joue
        # Dir = direction
        # Q = quantité (nombre de pas)
    while True:
        # Saisie joueur
        play=input("> ")
        
        # Si le joueur ne saisie rien: on revient au début de la boucle='continue'
        if play=="":
            continue
        
        # si l'utilisateur saisie un seul caractère
        if (len(play)==1):
            playDir=play[0]

            # On vérifie que le caractère saisie est conforme
            if play not in ["e","o","s","n","q"]:
                print("Mauvaise saisie")
                continue
            else:
                # On configure le nombre de pas à 1
                playQ=1
                return playDir, playQ
        # si l'utilisateur saisie plusieurs caractère
        elif(len(play)>1):
            playDir=play[0]

            # gestion d'exception sur les autres caractères saisis 
            try:
                playQ=int(play[1:])
            except ValueError:
                print("Mauvaise saisie")
                continue

        # On retourne un couple:
            # playDir (direction): 'e','o','s' ou 'n'  <str>
            # playQ (quantité): entre 1 et l'infinie <int>
        return playDir, playQ