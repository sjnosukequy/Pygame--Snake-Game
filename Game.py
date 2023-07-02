import pygame
import sys
import random
from Snake import Snake
from Apple import Apple


class Game:
    def __init__(self):
        player_image = Snake(
            (random.randrange(0, screen_w, 20), random.randrange(0, screen_h, 20)), screen)
        self.Player = pygame.sprite.GroupSingle(player_image)

        self.Apples = pygame.sprite.Group()
        self.Apple_Delay = 80
        self.Apple_Timer = 0
        self.Lose = False

        # FONT
        self.font = pygame.font.Font("font/Pixeltype.ttf", 35)
        self.font2 = pygame.font.Font("font/Pixeltype.ttf", 50)

    def run(self):
        self.Player.sprite.Heads.draw(screen)
        self.Player.update()
        self.Player.draw(screen)

        self.Apple_Timer += 1
        self.Placing_apple()
        self.Apples.draw(screen)

        self.Collison()
        self.Slomo()

    def Placing_apple(self):
        x = random.randrange(20, screen_w - 20, 20)
        y = random.randrange(20, screen_h - 20, 20)
        if len(self.Apples.sprites()) <= 3:
            if self.Apple_Timer >= self.Apple_Delay:
                self.Apples.add(Apple((x, y)))
                self.Apple_Timer = 0

    def Collison(self):
        if self.Apples.sprites():
            if pygame.sprite.spritecollide(self.Player.sprite, self.Apples, True):
                self.Apple_Timer = 0
                self.Player.sprite.EVO()

        if self.Player.sprite.rect.top < 0:
            self.Lose = True
            self.Player.sprite.rect.y = 0
            self.Player.draw(screen)
        if self.Player.sprite.rect.midbottom[1] > screen_h:
            self.Lose = True
            self.Player.sprite.rect.y = screen_h - 20
            self.Player.draw(screen)
        if self.Player.sprite.rect.left < 0:
            self.Lose = True
            self.Player.sprite.rect.x = 0
            self.Player.draw(screen)
        if self.Player.sprite.rect.right > screen_w:
            self.Lose = True
            self.Player.sprite.rect.x = screen_w - 20
            self.Player.draw(screen)

        count = 1
        if self.Player.sprite.Heads:
            for i in self.Player.sprite.Heads:
                if count != 1:
                    if pygame.sprite.collide_rect(self.Player.sprite, i):
                        self.Lose = True
                count += 1

    def Slomo(self):
        global slomo
        if self.Player.sprite.rect.top < 40:
            slomo = 30
        elif self.Player.sprite.rect.midbottom[1] > screen_h - 40:
            slomo = 30
        elif self.Player.sprite.rect.left < 40:
            slomo = 30
        elif self.Player.sprite.rect.right > screen_w - 40:
            slomo = 30
        else:
            slomo = 60

    def Lost(self):
        if self.Lose:
            if self.lose_sound_counter == 0:
                self.lose_sound_counter += 1
            return True
        return False

    def DisplayScore(self):
        display = self.font.render(
            f'SCORE {self.Player.sprite.size}', True, 'white')
        display_rect = display.get_rect(topleft=(5, 5))
        screen.blit(display, display_rect)

    def DisplayLost(self):
        display = self.font2.render(
            'YOU LOST', True, 'white')
        display_rect = display.get_rect(center=(screen_w/2, screen_h/2 - 20))
        screen.blit(display, display_rect)
        again = self.font2.render('Press Space to play again', True, 'White')
        again_rect = again.get_rect(center=(screen_w/2, screen_h/2 - 20 + 60))
        screen.blit(again, again_rect)

    def DisplayPause(self):
        display = self.font2.render(
            'Pause', True, 'white')
        display_rect = display.get_rect(center=(screen_w/2, screen_h/2 - 20))
        screen.blit(display, display_rect)
        again = self.font2.render('Press ESC to continue', True, 'White')
        again_rect = again.get_rect(center=(screen_w/2, screen_h/2 - 20 + 60))
        screen.blit(again, again_rect)

    def DisplayStart(self):
        display = self.font2.render(
            'WASD TO MOVE', True, 'white')
        display_rect = display.get_rect(center=(screen_w/2, screen_h/2 - 20))
        screen.blit(display, display_rect)

class CRT:
    def __init__(self):
        self.tv = pygame.image.load('graphics/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (screen_w, screen_h))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(screen_h / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos),
                             (screen_w, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(random.randint(75, 90))
        self.create_crt_lines()
        screen.blit(self.tv, screen.get_rect())


if __name__ == '__main__':
    pygame.init()
    screen_h = 540
    screen_w = 960
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()

    game = Game()
    crt = CRT()
    Ending = False
    Pause = False

    Start = False
    
    slomo = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Ending == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Start = False
                        Ending = False
                        game = Game()
            elif Start == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        Start = True
                    if event.key == pygame.K_d:
                        Start = True
                    if event.key == pygame.K_w:
                        Start = True
                    if event.key == pygame.K_s:
                        Start = True
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if Pause == False:
                            Pause = True
                        elif Pause == True:
                            Pause = False


        if Pause == False:
            Ending = game.Lost()

            if Ending == False:
                screen.fill((121, 173, 220))
                game.run()
            else:
                game.DisplayLost()
        else:
            game.DisplayPause()

        if Start == False:
            game.DisplayStart()

        game.DisplayScore()
        crt.draw()
        pygame.display.flip()
        clock.tick(slomo)
