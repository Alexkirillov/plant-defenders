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

        

        "plants object creation"
        self.walnut = Walnut(self, 120, 150, 380,420)
        self.sunflower = Sunflower(self, 120, 150, 770, 620)
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
        self.last_shot_time = 0
    

    def run_game(self):
        manager = pygame_gui.UIManager((1777, 1000), theme_path="quick_start.json")

        window_surface = pygame.display.set_mode((1777, 1000))
        clock = pygame.time.Clock()
        hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 400), (300, 150)),
                                             text='start game',
                                             manager=manager)
        cooldown = time.time()
        while True:
            time_delta = clock.tick(60)/1000.0
            pressed_key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        print('Hello World!')
                manager.process_events(event)
            
            manager.update(time_delta)

            self.screen.blit(self.game_backround,(0,0))
            "plant call"
            #summons the plants
            if pressed_key[pygame.K_1] and len(self.sunflowers) == 0 and len(self.walnuts) == 0 and len(self.peas) < 2:
                self.pea = Pea(self,120,150, 80,100)
                self.bullet = PeaBullet(28, self.pea.rect.centerx+20, self.pea.rect.centery-40, 5)
                self.peas.append(self.pea)
                self.bullets.append(self.bullet)
                self.plantMove1 = 1
                self.pea.putPlant = True

            if pressed_key[pygame.K_2] and len(self.peas) == 0 and len(self.walnuts) == 0 and len(self.sunflowers) < 2 :
                self.sunflower = Sunflower(self,120,150, 80,100)
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
            self.sunflowers.clear()

            for walnut in self.walnuts:
                if not walnut.is_placed:
                    walnut.fix_position()
                    self.plantPlaced3.append(walnut)
            self.walnuts.clear()

            for pea in self.peas:
                if self.putPlant and not pea.is_placed:
                    pea.blitme()

            for sunflower in self.sunflowers:
                if self.putPlant and not sunflower.is_placed:
                    sunflower.blitme()

            for walnut in self.walnuts:
                if self.putPlant and not walnut.is_placed:
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
                    self.bullets.append(bullet)
                    print("Bullet shot")
            
            self.bullet_group.update()
            self.bullet_group.draw(self.screen)

            manager.draw_ui(window_surface)
            pygame.display.flip()

if __name__ == '__main__':
    pd = Plant_defense()
    pd.run_game()
                    



