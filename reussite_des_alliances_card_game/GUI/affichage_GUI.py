import pygame
import sys
import os
from partie import reussite_mode_auto
from cartes import Carte
from game import Game
from pioche import Pioche
from logique import saut_si_possible
from time import sleep
from button import Button

pygame.display.set_caption("Alliance des réussites")
screen = pygame.display.set_mode((1280, 720))


num_cartes = 32
mode = 'manuel'

def get_font(size): 
    return pygame.font.Font("assets_main_menu/font.ttf", size)

def main_menu():
    global mode 

    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

    BG = pygame.image.load("assets_main_menu/Background.png")
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.image.load("assets_main_menu/Play Rect.png"), pos=(640, 300), #250
                            text_input="JOUER", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets_main_menu/Options Rect.png"), pos=(640, 450), 
                            text_input="OPTIONS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets_main_menu/Quit Rect.png"), pos=(640, 600), 
                            text_input="QUITTER", font=get_font(40), base_color="#d7fcd4", hovering_color="White")


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    partie(mode)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_nb_cartes()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


def select_nb_cartes():
    global num_cartes
    while True:
        select_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        OPTIONS_TEXT = get_font(45).render("Nombre de cartes?", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_32 = Button(image=None, pos=(320, 460), 
                            text_input="32", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_52 = Button(image=None, pos=(960, 460), 
                            text_input="52", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_32.changeColor(select_mouse_pos)
        OPTIONS_52.changeColor(select_mouse_pos)

        OPTIONS_32.update(screen)
        OPTIONS_52.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_32.checkForInput(select_mouse_pos):
                    num_cartes = 32
                    select_mode()
                if OPTIONS_52.checkForInput(select_mouse_pos):
                    num_cartes = 52
                    select_mode()

        pygame.display.update()


def select_mode():
    global mode
    while True:
        select_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        OPTIONS_TEXT = get_font(45).render("Mode de jeu?", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_MANUEL = Button(image=None, pos=(320, 460), 
                            text_input="manuel", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_AUTO = Button(image=None, pos=(960, 460), 
                            text_input="auto", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_MANUEL.changeColor(select_mouse_pos)
        OPTIONS_AUTO.changeColor(select_mouse_pos)

        OPTIONS_MANUEL.update(screen)
        OPTIONS_AUTO.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_MANUEL.checkForInput(select_mouse_pos):
                    mode = 'manuel'
                    main_menu()
                if OPTIONS_AUTO.checkForInput(select_mouse_pos):
                    mode = 'auto'
                    main_menu()

        pygame.display.update()


def init_liste_card_pos(pos_X = 15, pos_Y = 200): #au départ la 1ere carte est en bas de la pioche
    
    global num_cartes
    game = Game(num_cartes)

    dic_cartes = game.card_infos.copy()
    i, j = 0, 0
    while(i < len(game.card_infos)):

        if (pos_X + 72) < (screen.get_width()-87): #87 = bordure fin + une carte
            pos_X = 15+90*j
            carte = Carte(game.card_infos[i]['valeur'],game.card_infos[i]['couleur'],pos_X, pos_Y)
            #liste_card.append(carte)
            dic_cartes[i]['carte'] = carte
            j += 1
        
        else:
            pos_X = 15
            pos_Y += 115
            j = 0
            i -= 1
        i +=1
    
    return dic_cartes









def partie(mode):
    background = pygame.image.load('assets_game/bg.jpg')
    background = pygame.transform.scale(background,(2000,720))

    jeu = [] # cartes visibles 
    pioche = Pioche() 

   #SOUND 
    single = pygame.mixer.Sound(os.path.join('sound', 'single.mp3'))
    possible = pygame.mixer.Sound(os.path.join('sound', 'possible.mp3'))
    impossible = pygame.mixer.Sound(os.path.join('sound', 'impossible.mp3'))

    running = True
    clock = pygame.time.Clock()
    list_pioche_pos = init_liste_card_pos()
    win_len = len(reussite_mode_auto(list_pioche_pos))


    while running:
        screen.blit(background, (0, 0))

        if len(list_pioche_pos) != 0:
            screen.blit(pioche.image, (pioche.rect.x,pioche.rect.y))

        mouse_pos = pygame.mouse.get_pos()

        if mode == 'auto':
            pioche.clicked = True


        
        if pioche.clicked == True and len(list_pioche_pos)!=0:
            if mode == 'manuel':
                pygame.mixer.Sound.play(single)
            pioche.launch_card(list_pioche_pos[0]["carte"])
            jeu.append(list_pioche_pos[0])
            del list_pioche_pos[0]
        
        pioche.clicked = False

        if mode == 'manuel':
            i=0
            while (i<len(jeu)):
                if jeu[i]["carte"].clicked == True:
                    print(i)
                    jeu_temp = list(jeu)
                    if i == 0 or i == len(jeu_temp)-1:
                        pygame.mixer.Sound.play(impossible)
                        break
                    else:
                        if(saut_si_possible(jeu, i)):
                            pygame.mixer.Sound.play(possible)
                            pioche.remove_card(jeu_temp[i-1]["carte"])
                            break
                        else:
                            pygame.mixer.Sound.play(impossible)
                            break
                i += 1


        if mode == 'auto' and len(jeu)>win_len:
            i=0
            while (i<len(jeu)):
                jeu_temp = list(jeu)
                if len(jeu) == win_len:
                    break
                if i == 0 or i == len(jeu_temp)-1:
                    print("impossible")
                else:
                    if(saut_si_possible(jeu, i)):
                        pioche.remove_card(jeu_temp[i-1]["carte"])
                        break
                i+=1

            

        PLAY_BACK = Button(image=None, pos=(screen.get_width() - 87, screen.get_height()-80), 
                            text_input="RETOUR", font=get_font(20), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(mouse_pos)
        PLAY_BACK.update(screen)
        
        for carte in pioche.all_cards:
            carte.clicked = False

        for carte in pioche.all_cards:
            carte.move()

        pioche.all_cards.draw(screen)  


        pygame.display.flip()

    # _______________________BUTTON__________________________#

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pioche.rect.collidepoint(event.pos):
                    if pygame.mouse.get_pressed()[0] == 1:
                        pioche.clicked = True

                    elif pygame.mouse.get_pressed()[0] == 0:
                        pioche.clicked = False

                for card in pioche.all_cards:
                    if card.rect.collidepoint(event.pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            card.clicked = True

                    elif pygame.mouse.get_pressed()[0] == 0:
                        card.clicked = False

                if PLAY_BACK.checkForInput(mouse_pos):
                    pioche.reset_pioche()
                    main_menu()

    clock.tick(70)