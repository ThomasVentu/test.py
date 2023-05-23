import pygame
from objet import Tree

# class du joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 0.2
        self.image = pygame.image.load("img/mummy.png")
        self.rect = self.image.get_rect()
        self.group_tree = pygame.sprite.Group()
        self.rect.x = 50
        self.rect.y = 250

    def move_droite(self):
        if not self.game.colision(self, self.game.group_tree):
            self.rect.x += self.velocity

    def move_gauche(self):
        self.rect.x -= self.velocity

    def spawn_tree(self):
        self.group_tree.add(Tree(self))
