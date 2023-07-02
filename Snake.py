import pygame
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.size = 0
        self.image = pygame.Surface((20, 20))
        self.image.fill((173, 247, 182))
        self.rect = self.image.get_rect(topleft=(pos))
        self.Heads = pygame.sprite.Group()
        self.Dir = 0
        self.screen = screen
        self.speed = 4
        self.LockX = False
        self.LockY = False

    def update(self):
        self.Get_Input()
        self.Movement()


    def Get_Input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.LockY == False:
            if self.rect.y % 20 == 0 and self.rect.x % 20 == 0:
                self.Dir = 1
                self.LockX = False
                self.LockY = True
        elif keys[pygame.K_s] and self.LockY == False:
            if self.rect.y % 20 == 0 and self.rect.x % 20 == 0:
                self.Dir = 2
                self.LockX = False
                self.LockY = True
        elif keys[pygame.K_a] and self.LockX == False:
            if self.rect.y % 20 == 0 and self.rect.x % 20 == 0:
                self.Dir = 3
                self.LockX = True
                self.LockY = False
        elif keys[pygame.K_d] and self.LockX == False:
            if self.rect.y % 20 == 0 and self.rect.x % 20 == 0:
                self.Dir = 4
                self.LockX = True
                self.LockY = False

    def EVO(self):
        self.Heads.add(Head((-50, -50)))
        self.size += 1

    def Movement(self):
        bckx = self.rect.x
        bcky = self.rect.y

        if self.Dir == 1:
            self.rect.y -= self.speed
            if self.rect.y % 20 == 0:
                bcky += -4
        if self.Dir == 2:
            self.rect.y += self.speed
            if self.rect.y % 20 == 0:
                bcky -= -4
        if self.Dir == 3:
            self.rect.x -= self.speed
            if self.rect.x % 20 == 0:
                bckx += -4
        if self.Dir == 4:
            self.rect.x += self.speed
            if self.rect.x % 20 == 0:
                bckx -= -4
        

        if self.Heads.sprites():
            if self.rect.y % 20 == 0 and self.rect.x % 20 == 0:
                for i in range(self.size - 1, 0, -1):
                    self.Heads.sprites()[i].rect.y = self.Heads.sprites()[i - 1].rect.y
                    self.Heads.sprites()[i].rect.x = self.Heads.sprites()[i - 1].rect.x
                self.Heads.sprites()[0].rect.x = bckx
                self.Heads.sprites()[0].rect.y = bcky



            
            



class Head(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((173, 247, 182))
        self.rect = self.image.get_rect(topleft=(pos))
