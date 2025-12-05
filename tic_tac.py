import numpy as np
import random as rd

class Joueur:
    def __init__(self,num):
        self.numero = num
        self.actions = []
    
    def action(self, grille,i,j):
        if grille[i][j] == 0:
            self.actions.append((i,j))
            grille[i][j] = self.numero
        else:
            print("Case déjà occupée !")

def jeu():
    grille = np.zeros((3,3), dtype = int)
    joueur_1 = Joueur(1)
    joueur_2 = Joueur(2)
    start = rd.randint(1,2)
    print(f"Le joueur {start} commence !")

    while np.any(grille == 0):  # ajouter winner
        print(f"Joueur {start} :")
        i = int(input("Entrez l'indice de la ligne:"))
        j = int(input("Entrez l'indice de la colonne:"))
        if start == 1:
            joueur_1.action(grille,i,j)
            start = 20
        else:
            joueur_2.action(grille,i,j)
            start = 1
        print(grille)
    
    print('Fin du jeu !')

jeu()
    

        

    

    

