import pygame
import settings
import time as tm

class Enemy(pygame.sprite.Sprite): 
    def __init__(self, pd_game, enemy_width, enemy_height, enemy_postionx, enemy_positiony):
        super().__init__()
        self.screen = pd_game.screen
        self.image = pygame.transform.scale(pygame.image.load(settings.ENEMY_PHOTO), (enemy_width, enemy_height))
        self.rect = self.image.get_rect()
        self.rect.x = enemy_postionx
        self.rect.y = enemy_positiony
        self.lifes = 100
        self.speed = 0.5




    def update(self):
        self.rect.x -= self.speed
    def blitme(self,):
        self.screen.blit(self.image, (self.rect.x,self.rect.y))

