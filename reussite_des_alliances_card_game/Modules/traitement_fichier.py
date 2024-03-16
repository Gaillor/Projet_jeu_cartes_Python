import Modules.traitement_fichier as traitement_fichier

from random import shuffle
import os

def init_pioche_fichier(nom_fic):
    main_lst = []
    if (os.stat(nom_fic).st_size != 0): #Si le fichier n'est pas vide elle procède 
        f = open(nom_fic, "r") 
        lst_crt = f.read().strip().split(" ")

        for carte in lst_crt:
            crt = carte.split("-")
            crt_dct = {}
            
            if crt[0].isnumeric():
                crt_dct['valeur'] = int(crt[0])
            else:
                crt_dct['valeur'] = crt[0]

            crt_dct['couleur'] = crt[1]
            main_lst.append(crt_dct)

        f.close()

        
    return main_lst

def ecrire_fichier_reussite(nom_fic, pioche):
    f = open(nom_fic, 'w')

    for carte in pioche:
        f.write(f"{carte['valeur']}-{carte['couleur']} ")

    f.close()

def init_pioche_alea(nb_cartes=32):
    
    jeu = init_pioche_fichier(f"jeu_{nb_cartes}.txt")
    
    if (len(jeu) == 32 or len(jeu) == 52):
    
        shuffle(jeu)
        
        return jeu