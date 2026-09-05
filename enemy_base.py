
import pygame
import settings
import time as tm
from random import uniform 
from random import randint

class Enemy(pygame.sprite.Sprite): 
    def __init__(self, pd_game, enemy_width, enemy_height, enemy_postionx, enemy_positiony):
        super().__init__()
        self.screen = pd_game.screen
        random_enemy = randint(1,3)
        if random_enemy == 1:
            self.image = pygame.transform.scale(pygame.image.load(settings.ENEMY_PHOTO), (enemy_width, enemy_height))
            self.lifes = uniform(50,125)
            self.speed = uniform(0.5, 1.4)
        elif random_enemy == 2:
            self.image = pygame.transform.scale(pygame.image.load(settings.ENEMY_PHOTO2), (enemy_width, enemy_height))
            self.lifes = uniform(25,80)
            self.speed = uniform(1.0, 2.5)
        else:
            self.image = pygame.transform.scale(pygame.image.load(settings.ENEMY_PHOTO3), (enemy_width, enemy_height))
            self.lifes = uniform(150,250)
            self.speed = uniform(0.3, 1.0)
        self.rect = self.image.get_rect()
        self.rect.x = enemy_postionx
        self.rect.y = enemy_positiony




    def update(self):
        self.rect.x -= self.speed
    def blitme(self,):
        self.screen.blit(self.image, (self.rect.x,self.rect.y))

