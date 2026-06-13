import pygame
import settings
import sys 
import pygame_gui
from plant_base import Walnut
from plant_base import Sunflower
from plant_base import Pea
from plant_base import PeaBullet
from random import randint
import time 


class Plant_defense:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((settings.BACKROUND_LENGHT,settings.BACKROUND_HEIGHT))
        pygame.display.set_caption("Plant defense")
        self.game_backround = pygame.transform.scale(pygame.image.load(settings.BACKROUND_IMAGE), (settings.BACKROUND_LENGHT,settings.BACKROUND_HEIGHT))
        self.score_counter = pygame.transform.scale(pygame.image.load(settings.SCORE_COUNTER_PHOTO), (150, 60))
        self.energy = pygame.font.SysFont("Arial", 20)
        

        "plants object creation"
        self.walnut = Walnut(self, 120, 150, 380,420)
        self.sunflower = Sunflower(self, 120, 150, 770, 620, 5)
        self.pea = Pea(self,120,150, 80,100)
        
        self.bullet_group = pygame.sprite.Group()
        self.bullet_group_pea = pygame.sprite.Group()
        self.bullets = []
        self.peas = []
        #self.peas.append(self.pea) 
        self.sunflowers = []
        #self.sunflowers.append(self.sunflower)
        self.walnuts = []
        #self.walnuts.append(self.walnut)
        self.bulletCycle = []

        self.plantMove1 = 0
        self.plantPlace1 = True
        self.plantPlaced1 = []

        self.plantMove2 = 0
        self.plantPlace2 = True
        self.plantPlaced2= []
        
        self.plantMove3 = 0
        self.plantPlace3= True
        self.plantPlaced3 = []
        self.last_shot_time = {}
        self.ammo = 0
        self.time_cooldown = time.time()
        self.energy_inc = 5

    def run_game(self):
        
        while True:
            pressed_key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            self.screen.blit(self.game_backround,(0,0))
            self.screen.blit(self.score_counter,(5,5))
            self.screen.blit(self.energy.render(f"energy:{self.ammo}", True, (0, 0, 0)), (12, 25))
            
            if time.time() - self.time_cooldown >= 2.5:
                self.ammo += self.energy_inc
                self.time_cooldown = time.time()
            "plant call"
            #summons the plants
            if pressed_key[pygame.K_1] and len(self.sunflowers) == 0 and len(self.walnuts) == 0 and len(self.peas) < 2:
                self.pea = Pea(self,120,150, 80,100)
                self.peas.append(self.pea)
                self.plantMove1 = 1
                self.pea.putPlant = True
            

            if pressed_key[pygame.K_2] and len(self.peas) == 0 and len(self.walnuts) == 0 and len(self.sunflowers) < 2 :
                self.sunflower = Sunflower(self,120,150, 80,100,5)
                self.sunflowers.append(self.sunflower)
                self.plantMove2 = 1
                self.sunflower.putPlant = True

            if pressed_key[pygame.K_3] and len(self.sunflowers) == 0 and len(self.peas) == 0 and len(self.walnuts) < 2:
                self.walnut = Walnut(self,120,150, 80,100)
                self.walnuts.append(self.walnut)
                self.plantMove3 = 1
                self.walnut.putPlant = True
            
            if pressed_key[pygame.K_p]:
                for pea in self.peas:
                    if not pea.is_placed:
                        pea.fix_position()
                        self.plantPlaced1.append(pea)
                        self.last_shot_time[pea] = time.time()
                self.peas.clear()
            
                for sunflower in self.sunflowers:
                    if not sunflower.is_placed:
                        sunflower.fix_position()
                        self.plantPlaced2.append(sunflower)
                        self.energy_inc += self.sunflower.energy_gen
                        self.sunflower.energy_gen = 0
                self.sunflowers.clear()

                for walnut in self.walnuts:
                    if not walnut.is_placed:
                        walnut.fix_position()
                        self.plantPlaced3.append(walnut)
                self.walnuts.clear()

            for pea in self.peas:
                if self.pea.putPlant and not pea.is_placed:
                    pea.blitme()

            for sunflower in self.sunflowers:
                if self.sunflower.putPlant and not sunflower.is_placed:
                    sunflower.blitme()

            for walnut in self.walnuts:
                if self.walnut.putPlant and not walnut.is_placed:
                    walnut.blitme()
            
            for pea in self.peas:
                if pea.putPlant and not pea.is_placed:
                    pea.update()
            
            for sunflower in self.sunflowers:
                if sunflower.putPlant and not sunflower.is_placed:
                    sunflower.update()

            for walnut in self.walnuts:
                if walnut.putPlant and not walnut.is_placed:
                    walnut.update()

            for walnut in self.plantPlaced3:
                walnut.blitme()

            for sunflower in self.plantPlaced2:
                sunflower.blitme()
            
            current_time = time.time()
            for pea in self.plantPlaced1:
                pea.blitme()
                bullet = pea.shoot_bullet(current_time)
                if bullet:
                    self.bullet_group.add(bullet)
                    print("Bullet shot")
            
            self.bullet_group.update()
            self.bullet_group.draw(self.screen)

            
            pygame.display.flip()

if __name__ == '__main__':
    pd = Plant_defense()
    pd.run_game()
                    



