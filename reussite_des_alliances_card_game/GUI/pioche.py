import pygame

class Pioche(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(f"assets_game/cartes/carte-dos-dos.png")
        self.image = pygame.transform.scale(self.image,(72,96))
        self.imageFin = pygame.image.load(f"assets_game/cartes/carte-fin-fin.png")
        self.imageFin = pygame.transform.scale(self.imageFin,(72,96))
        self.rect = self.image.get_rect()
        self.all_cards = pygame.sprite.Group()
        self.clicked = False
        self.rect.x = 15
        self.rect.y = 15



    def launch_card(self, carte):
      #on prend une carte on le met à la position de la pioche
        self.all_cards.add(carte)   #ajout dans le groupe de carte

    def remove_card(self, carte):
        self.all_cards.remove(carte)

    def reset_pioche(self):
        self.all_cards.empty()