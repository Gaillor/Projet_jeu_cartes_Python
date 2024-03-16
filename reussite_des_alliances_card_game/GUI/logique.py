import affichage



import os

def alliance(carte1, carte2):
    if (carte1['valeur'] == carte2['valeur'] or carte1['couleur'] == carte2['couleur']):
        return True

    return False

def saut_si_possible(liste_tas, num_tas):
    num_tas += 1 #On passe l'index en argument, et ce qui suit prends le numero de la carte donc l'index + 1

    if (len(liste_tas) >= 3 and num_tas < len(liste_tas) and num_tas > 0): # CONDITIONS:
                                                                           # Au moins 3 cartes restantes
                                                                           # Numéro de tas a vérifier est
                                                                           # compris entre le deuxième et
                                                                           # l'avant dernier tas
        carte_avant = liste_tas[num_tas - 2]
        carte_apres = liste_tas[num_tas]

        if( alliance(carte_avant, carte_apres) ):
            liste_tas.pop(num_tas - 2) # Si l'alliance est possible, la carte avant le tas passé en argument
                                       # est supprimée 
            return True

    return False

def une_etape_reussite(liste_tas, pioche, affiche=False):
    carte_pioche = pioche[0]
    liste_tas.append(carte_pioche)
    pioche.pop(0)
    affichage.affiche_liste(liste_tas, affiche)

    if(saut_si_possible(liste_tas, len(liste_tas) - 2)): #On passe l'index de l'avant dernière carte

        i = 1 # On commence par la deuxième carte

        affichage.affiche_liste(liste_tas, affiche) 

        while (i >= 1): # l'index de la carte passée en argument sera toujours entre la deuxieme et l'avant dernière

            if (saut_si_possible(liste_tas, i)):
                i = 0 
                affichage.affiche_liste(liste_tas, affiche)
            if (i == len(liste_tas) - 1 or len(liste_tas) < 3): #dernière carte atteinte ou le jeu a été gagné
                break

            i += 1 # Quand le saut n'est pas possible on passe a la prochaine carte
                   # i est réinitialisé a 0 plus haut, puis incrémenté de 1 a la fin pour revenir a la deuxieme
                   # carte quand le saut est possible

def verifier_pioche(pioche, nb_cartes=32): #Verifie l'existence de doublons
    if len(pioche) == nb_cartes:
        i = 0
        doublon = False
        while (i < len(pioche)):
            j = 0
            while (j < len(pioche)):
                if (pioche[i] == pioche[j] and j != i):
                    return False
                j += 1
            i += 1

        return True
    
    return False

def pioche_liste(jeu, pioche): # Fait une simple pioche
    jeu.append(pioche[0])
    pioche.pop(0)
            