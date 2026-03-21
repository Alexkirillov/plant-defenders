import pygame
import settings
import sys 
from plant_base import Walnut
from plant_base import Sunflower
from plant_base import Pea
from random import randint


class Plant_defense:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((settings.BACKROUND_LENGHT,settings.BACKROUND_HEIGHT))
        pygame.display.set_caption("Plant defense")
        self.game_backround = pygame.transform.scale(pygame.image.load(settings.BACKROUND_IMAGE),(settings.BACKROUND_LENGHT,settings.BACKROUND_HEIGHT))

        "plants object creation"
        self.walnut = Walnut(self, 120, 150, 380,420)
        self.sunflower = Sunflower(self, 120, 150, 770, 620)
        self.pea = Pea(self,120,150, 80,100)
        self.peas = pygame.sprite.Group()
        self.sunflowers = pygame.sprite.Group()
        self.walnuts = pygame.sprite.Group()

            

    def run_game(self):

        while True:
            pressed_key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.blit(self.game_backround,(0,0))
            "plant call"

            if pressed_key[pygame.K_q]:
                self.pea.movePlant = True
                self.walnut = False
                self.sunflower = False
            
            if pressed_key[pygame.K_w]:
                self.pea.movePlant = True
                self.walnut = False
                self.sunflower = False

            if pressed_key[pygame.K_q]:
                self.pea.movePlant = True
                self.walnut = False
                self.sunflower = False

            if pressed_key[pygame.K_1]:
                self.pea.putPlant = True
            if self.pea.putPlant == True:
                self.pea.blitme()
                self.pea.update()

            if pressed_key[pygame.K_2]:
                self.walnut.putPlant = True
            if self.walnut.putPlant == True:
                self.walnut.blitme()
                self.walnut.update()

            if pressed_key[pygame.K_3]:
                self.sunflower.putPlant = True
            if self.sunflower.putPlant == True:
                self.sunflower.blitme()
                self.sunflower.update()

            pygame.display.flip()
            

if __name__ == '__main__':
    pd = Plant_defense()
    pd.run_game()


