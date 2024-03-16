import pygame

class card(object):
    def __init__(self, x, y, pos_x, pos_y, image):
        self.x = x
        self.y = y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.img, (54, 72))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        #self.width = 54
        #self.height = 72
        self.width = 72
        self.height = 96
        self.vel_x = 10
        self.vel_y = 10
        self.IsCommunity = False
        self.IsPlayer = False
        self.IsVisible = True
        self.IsSetPos = False
        

    def set_image(self, image):
        self.img = pygame.image.load(image)


    def set_pos(self, x, y, pos_x, pos_y):
        self.x = x
        self.y = y
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_pos(self):
        return (self.x, self.y, self.pos_x, self.pos_y)

    def set_visible(self, bVisible):
        self.IsVisible = bVisible

    def set_player_card(self, bPlayer):
        self.IsPlayer = bPlayer

        if not self.IsSetPos:
            self.set_pos(self.x - 15, self.y, self.pos_x - 15, self.pos_y)

        self.IsSetPos = True

    def draw(self, win):
        if self.IsVisible:
            # if self.y > self.pos_y:
            #     self.vel_y = 0
            
            # if self.x > self.pos_x:
            #     self.vel_x = 0

            # self.y += self.vel_y
            # self.x += self.vel_x

            win.blit(self.img, (self.x, self.y))