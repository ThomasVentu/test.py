import pygame
import objet
from objet import Tree
from game import *
pygame.init()
clock = pygame.time.Clock()
fps = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("background")

scroll = 0



ground_image = pygame.image.load("Parallax/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()


bg_images = []
for i in range(1,6):
    bg_image = pygame.image.load(f"Parallax/plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def Draw():
    for x in range (5):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed+= 0.2

def draw2():
    for x in range (15):
        screen.blit(ground_image, ((x * ground_width) - scroll * 2.2, SCREEN_HEIGHT - ground_height))

game = Game()

run = True
while run:
    clock.tick(fps)


    Draw()
    draw2()
    screen.blit(game.joueur.image, game.joueur.rect)
    game.joueur.group_tree.draw(screen)


    if game.touche.get(pygame.K_q) and scroll > 0:
        scroll -= 3
        game.joueur.move_gauche()
    if game.touche.get(pygame.K_d) and scroll < 3000:
        scroll += 3
        game.joueur.move_droite()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            game.touche[event.key] = True

            if event.key == pygame.K_l:
                game.joueur.spawn_tree()

        elif event.type == pygame.KEYUP:
            game.touche[event.key] = False
    pygame.display.update()

pygame.quit()
