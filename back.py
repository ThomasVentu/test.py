import pygame

class background:
    def __init__(self):
        self.screen = self.screen
        self.scroll = self.scroll
        self.image = pygame.image.load("Parallax/ground.png").convert_alpha()
        self.g_width = self.image.get_width()
        self.g_height = self.image.get_height()
        self.bg_images = []

    def parallax(self):
        for i in range(1,6):
            self.bg_image = pygame.image.load(f"Parallax/plx-{i}.png").convert_alpha()
            self.bg_images.append(self.bg_image)
        self.bg_width = self.bg_images[0].get_width()
        def Draw():
            for x in range (5):
                speed = 1
            for i in self.bg_images:
                self.screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed+= 0.2

        def draw2():
            for x in range (15):
                self.screen.blit(self.ground_image, ((x * self.ground_width) - self.scroll * 2.2, 800 - self.ground_height))

        Draw()
        draw2()
