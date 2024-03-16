def carte_to_chaine(carte):
    symb = {'P': 9824,'C': 9825,'K': 9826, 'T': 9827}
    esp = 0

    if(carte['valeur'] != 10):
        esp = 1
    
    
    if(carte['couleur'] == 'P'):
        result = " " * esp + f"{carte['valeur']}{chr(symb['P'])}"
    if(carte['couleur'] == 'C'):
        result = " " * esp + f"{carte['valeur']}{chr(symb['C'])}"
    if(carte['couleur'] == 'K'):
        result = " " * esp + f"{carte['valeur']}{chr(symb['K'])}"
    if(carte['couleur'] == 'T'):
        result = " " * esp + f"{carte['valeur']}{chr(symb['T'])}"
    
    
    return result

def afficher_reussite(liste_carte):
    if (liste_carte):
        i = 0
        while(i < len(liste_carte) - 1): 
            print(carte_to_chaine(liste_carte[i])+ " ", end="")
            i += 1

        print(carte_to_chaine(liste_carte[i]), end="")
    print("\n")


def affiche_liste(liste_tas, affiche):
    if (affiche == True):
        afficher_reussite(liste_tas)


def pioche_un_a_un(pioche):
    i = 0

    while (i<len(pioche)):
        print(carte_to_chaine(pioche[i]), end='')
        i += 1