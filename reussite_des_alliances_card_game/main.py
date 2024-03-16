import Modules.traitement_fichier as traitement_fichier
import Modules.affichage as affichage
import Modules.logique as logique
import Modules.partie as partie
import Modules.jeu_stat as jeu_stat
import os

from random import shuffle



if __name__ == "__main__":
	print("Reussite Des Alliances")
	mode = input("(a)uto/(m)anuel? ")

	if mode == "a":
		partie.lance_reussite("auto", affiche=True)
	else:
		partie.lance_reussite("manuel")