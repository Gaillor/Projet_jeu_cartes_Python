import pygame
import game
from random import shuffle
from pioche import Pioche

class Carte(Pioche):

    def __init__(self, value, color, pos_x, pos_y) -> None:
        super().__init__()
        self.color = color
        self.value = value
        self.image = pygame.image.load(f"assets_game/cartes/carte-{value}-{color}.png")
        self.image = pygame.transform.scale(self.image,(72,96))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.origin_image = self.image #une copie de l'image originale
        self.angle = 0
        self.velocity = 3
        self.clicked = False
        self.Isvisible = True
    
    def set_pos(self, x, y, pos_x, pos_y):
        self.x = x 
        self.y = y
        self.pos_x = pos_x
        self.pos_y = pos_y

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect =self.image.get_rect(center = self.rect.center)


    def moveMouse(self):
        positionMouse = pygame.mouse.get_pos()  #position de la souris
        

    def move(self):
        if(self.rect.x < self.pos_x):
            self.rect.x += self.velocity
        if(self.rect.y < self.pos_y):
            self.rect.y += self.velocity


    def set_visible(self, bVisible):
        if bVisible == False:
            self.image = pygame.image.load("assets_game/cartes/carte-dos-dos.png")
            self.image = pygame.transform.scale(self.image,(72,96))
