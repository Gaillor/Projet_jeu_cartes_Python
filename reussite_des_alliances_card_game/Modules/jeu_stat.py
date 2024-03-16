import Modules.traitement_fichier as traitement_fichier

from statistics import mean
import os

def res_multi_simulation(nb_sim, nb_cartes=32):

    melanges = []
    res = []
    
    i = 0
    while (i<nb_sim):
        melanges.append(traitement_fichier.init_pioche_alea(nb_cartes))
        i += 1
        
    i = 0
    while (i<nb_sim):
        res.append(len(traitement_fichier.reussite_mode_auto(melanges[i], False)))
        i += 1
        
    return res


def statistiques_nb_tas(nb_sim, nb_cartes=32):
    
    jeu = res_multi_simulation(nb_sim, nb_cartes)

    print("Après ", nb_sim, " simulations on a :")
    print("Le plus grand nombre de tas obtenu a la fin de la simulation : ", max(jeu))
    print("Le plus petit nombre de tas obtenu a la fin de la simulation : ", min(jeu))
    print("La moyenne des tas obtenu a la fin de la simulation : ", mean(jeu))

def stat_reussite(nb_sim, nb_min_reussite=2, nb_cartes=32):
    prob = None
    if (nb_min_reussite >= 2 and nb_min_reussite <= 32):
        res = res_multi_simulation(nb_sim, nb_cartes)
        count = 0
        for i in res:
            if (i <= nb_min_reussite):
                count += 1
        prob = round(count / nb_sim, 4)
        
    return prob
        
def stat_tout_nombre(nb_sim, nb_cartes=32):
    res_stat = []
    i = 2
    while (i<=nb_cartes):
        res_stat.append(stat_reussite(nb_sim, i, nb_cartes))
        i += 1

    return res_stat