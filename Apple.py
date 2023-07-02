import pygame

class Apple(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill((245, 92, 122))
        self.rect = self.image.get_rect(topleft = pos)