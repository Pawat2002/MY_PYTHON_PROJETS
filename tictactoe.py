import pygame
from pygame.constants import K_SPACE

pygame.init()
#Game window
WIDTH = 650
HEIGHT = 650

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

first = pygame.draw.rect(WINDOW, (50,205,50), (45, 45, 150, 150))
second = pygame.draw.rect(WINDOW, (50,205,50), (245, 45, 150, 150))
third = pygame.draw.rect(WINDOW, (50,205,50), (445, 45, 150, 150))
fourth = pygame.draw.rect(WINDOW, (50,205,50), (45, 245, 150, 150))
fifth = pygame.draw.rect(WINDOW, (50,205,50), (245, 245, 150, 150))
sixth = pygame.draw.rect(WINDOW, (50,205,50), (445, 245, 150, 150))
seventh = pygame.draw.rect(WINDOW, (50,205,50), (45, 445, 150, 150))
eighth = pygame.draw.rect(WINDOW, (50,205,50), (245, 445, 150, 150))
ninth = pygame.draw.rect(WINDOW, (50,205,50), (445, 445, 150, 150))


running = True
draw_object = 'rect'
open_slot1 = True
open_slot2 = True
open_slot3 = True
open_slot4 = True
open_slot5 = True
open_slot6 = True
open_slot7 = True
open_slot8 = True
open_slot9 = True
while running:
    
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                open_slot1 = True
                open_slot2 = True
                open_slot3 = True
                open_slot4 = True
                open_slot5 = True
                open_slot6 = True
                open_slot7 = True
                open_slot8 = True
                open_slot9 = True

                first = pygame.draw.rect(WINDOW, (50,205,50), (45, 45, 150, 150))
                second = pygame.draw.rect(WINDOW, (50,205,50), (245, 45, 150, 150))
                third = pygame.draw.rect(WINDOW, (50,205,50), (445, 45, 150, 150))
                fourth = pygame.draw.rect(WINDOW, (50,205,50), (45, 245, 150, 150))
                fifth = pygame.draw.rect(WINDOW, (50,205,50), (245, 245, 150, 150))
                sixth = pygame.draw.rect(WINDOW, (50,205,50), (445, 245, 150, 150))
                seventh = pygame.draw.rect(WINDOW, (50,205,50), (45, 445, 150, 150))
                eighth = pygame.draw.rect(WINDOW, (50,205,50), (245, 445, 150, 150))
                ninth = pygame.draw.rect(WINDOW, (50,205,50), (445, 445, 150, 150))

        #detecting position
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if first.collidepoint(pos) and open_slot1:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (70,70, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(WINDOW, (255,255,0), (120,120,), 50)
                    draw_object = 'rect'
                open_slot1 = False

            if second.collidepoint(pos) and open_slot2:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (270,70, 100, 100))
                    draw_object = 'circle'
                else:   
                    pygame.draw.circle(WINDOW, (255,255,0), (320,120,), 50)
                    draw_object = 'rect'
                open_slot2 = False
            if third.collidepoint(pos) and open_slot3:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (470,70, 100, 100))
                    draw_object = 'circle'
                else:    
                    pygame.draw.circle(WINDOW, (255,255,0), (520,120,), 50)
                    draw_object = 'rect'
                open_slot3 = False
            if fourth.collidepoint(pos) and open_slot4:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (70,270, 100, 100))
                    draw_object = 'circle'
                else:   
                    pygame.draw.circle(WINDOW, (255,255,0), (120,320,), 50)
                    draw_object = 'rect'
                open_slot4 = False
            if fifth.collidepoint(pos) and open_slot5:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (270,270, 100, 100))
                    draw_object = 'circle'
                else:   
                    pygame.draw.circle(WINDOW, (255,255,0), (320,320), 50)
                    draw_object = 'rect'
                open_slot5 = False
            if sixth.collidepoint(pos) and open_slot6:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (470,270, 100, 100))
                    draw_object = 'circle'
                else:   
                    pygame.draw.circle(WINDOW, (255,255,0), (520,320,), 50)
                    draw_object = 'rect'
                open_slot6 = False
            if seventh.collidepoint(pos) and open_slot7:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (70,470, 100, 100))
                    draw_object = 'circle'
                else:    
                    pygame.draw.circle(WINDOW, (255,255,0), (120,520,), 50)
                    draw_object = 'rect'
                open_slot7 = False
            if eighth.collidepoint(pos) and open_slot8:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (270,470, 100, 100))
                    draw_object = 'circle'
                else:    
                    pygame.draw.circle(WINDOW, (255,255,0), (320,520,), 50)
                    draw_object = 'rect'
                open_slot8 = False
            if ninth.collidepoint(pos) and open_slot9:
                if draw_object == 'rect':
                    pygame.draw.rect(WINDOW, (255,0,0), (470,470, 100, 100))
                    draw_object = 'circle'
                else:  
                    pygame.draw.circle(WINDOW, (255,255,0), (520,520,), 50)
                    draw_object = 'rect'
                open_slot9 = False


         
    
    
    pygame.display.update()
pygame.quit()