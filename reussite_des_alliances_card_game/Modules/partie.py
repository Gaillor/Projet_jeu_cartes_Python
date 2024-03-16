import Modules.traitement_fichier as traitement_fichier
import Modules.affichage as affichage
import Modules.logique as logique
import os

def reussite_mode_auto(pioche, affiche=False): #PIOCHE: Liste de cartes déjà mélangées
    pi = list(pioche)                          #PI: Copie de PIOCHE
    affichage.affiche_liste(pioche, affiche)
    jeu_init = []
    i = 0
    while(i<3):                                #Piocher 3 cartes au début
        jeu_init.append(pi[0])
        pi.pop(0)
        affichage.affiche_liste(jeu_init, affiche)
        i += 1

    logique.saut_si_possible(jeu_init, 1)              #1 est l'index de la carte du milieu(index + 1= 2eme)

    j=0
    num_cartes_pioche = len(pi)                #len(pi) ici vaut len(pi) début moins les 3 cartes piochées
    while(j<num_cartes_pioche):
        logique.une_etape_reussite(jeu_init, pi, affiche)
        j += 1
    
    return jeu_init

def reussite_mode_manuel(pioche, nb_tas_max=2):
    success = False
    pi = list(pioche)
    jeu = []
    logique.pioche_liste(jeu, pi)

    while(success == False):
        os.system('clear')                      
        affichage.afficher_reussite(jeu) 
        rep = input("(s)aut/(p)ioche/(e)xit: ")
        rep.lower()
        if rep == 'p':
            logique.pioche_liste(jeu, pi)
        if rep == 's':
            num = int(input("Preciser numéro de la carte a bouger: "))  
            if (logique.saut_si_possible(jeu, num-1) == False):
                      print("SAUT IMPOSSIBLE!")
        
        if(len(pi) == 0):
            if(len(jeu) == nb_tas_max):
                success = True
            else:
                print("VOUS AVEZ PERDU")
                exit()
        if rep == 'e':
            print("VOUS AVEZ PERDU")
            affichage.afficher_reussite(jeu)
            affichage.pioche_un_a_un(pi)
            exit()

    print("VOUS AVEZ GAGNE")
    exit()
        
def lance_reussite(mode, nb_cartes=32, affiche=False,nb_tas_max=2):
    pioche = traitement_fichier.init_pioche_alea(nb_cartes)

    if(mode=="manuel"):
        reussite_mode_manuel(pioche, nb_tas_max)
    if(mode=="auto"):
        reussite_mode_auto(pioche, affiche)