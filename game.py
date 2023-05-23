import pygame
from joueur import Joueur
from objet import Tree
#class game utile pour lancer les events

class Game:
    def __init__(self):
        self.group_joueur = pygame.sprite.Group()
        self.joueur = Joueur(self)
        self.group_joueur.add(self.joueur)
        self.group_tree = pygame.sprite.Group()
        self.touche = {}

    def colision(self, sprite , group):
        return pygame.sprite.spritecollide(sprite , group , False, pygame.sprite.collide_mask)
