import pygame

class Tree(pygame.sprite.Sprite):
    def __init__(self,joueur):
        super().__init__()
        self.velocity = 0.2
        self.image = pygame.image.load("img/tree.png")
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 100
        self.rect.y = joueur.rect.y - 200


    def static_d(self):
        self.rect.x += self.velocity

    def static_g(self):
        self.rect.x -= self.velocity
