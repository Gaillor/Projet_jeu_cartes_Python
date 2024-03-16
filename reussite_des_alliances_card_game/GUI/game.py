import pygame
from traitement_fichier import *


class Game:

    def __init__(self, mode) -> None:
        self.mode = mode
        #self.card_infos = init_pioche_fichier(f"jeu_{mode}.txt")
        self.card_infos = init_pioche_alea(mode)
    

