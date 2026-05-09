import pygame
import settings
import sys 
import pygame_gui
from plant_base import Walnut
from plant_base import Sunflower
from plant_base import Pea
from plant_base import PeaBullet
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
        

        self.bullet_group = pygame.sprite.Group()
        self.peas = []
        #self.peas.append(self.pea) 
        self.sunflowers = []
        #self.sunflowers.append(self.sunflower)
        self.walnuts = []
        #self.walnuts.append(self.walnut)


        self.plantMove1 = 0
        self.plantPlace1 = True
        self.plantPlaced1 = []

        self.plantMove2 = 0
        self.plantPlace2 = True
        self.plantPlaced2= []
        
        self.plantMove3 = 0
        self.plantPlace3= True
        self.plantPlaced3 = []
            

    def run_game(self):
        manager = pygame_gui.UIManager((1777, 1000), theme_path="quick_start.json")

        window_surface = pygame.display.set_mode((1777, 1000))
        clock = pygame.time.Clock()
        hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 400), (300, 150)),
                                             text='start game',
                                             manager=manager)
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
            
            self.bullet_group.add(self.pea.shoot_bullet())
            if self.bullet_group:
                self.bullet_group.draw(self.screen)
                self.bullet_group.update()
                print(len(self.bullet_group))

            #summons the plants
            if pressed_key[pygame.K_1] and len(self.sunflowers) == 0 and len(self.walnuts) == 0 and len(self.peas) < 2:
                self.pea = Pea(self,120,150, 80,100)
                self.peas.append(self.pea)
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


            #makes the plants placeble
            if pressed_key[pygame.K_p] and self.peas:
                self.plantPlaced1.append(self.pea)
                self.peas.clear()

            if pressed_key[pygame.K_p] and self.sunflowers:
                self.plantPlaced2.append(self.sunflower)
                self.sunflowers.clear()

            if pressed_key[pygame.K_p] and self.walnuts:
                self.plantPlaced3.append(self.walnut)
                self.walnuts.clear()


            #shows the plants that are currently moving 
            if self.pea.putPlant:
                for pea in self.peas:
                    pea.blitme()

            if self.sunflower.putPlant:
                for sunflower in self.sunflowers:
                    sunflower.blitme()

            if self.walnut.putPlant:
                for walnut in self.walnuts:
                    walnut.blitme()


            #updates the plants that are being moved
            if self.pea.putPlant and self.plantMove1 == 1 and self.plantPlace1:
                for pea in self.peas:
                    pea.update()

            if self.sunflower.putPlant and self.plantMove2 == 1 and self.plantPlace2:
                for sunflower in self.sunflowers:
                    sunflower.update()

            if self.walnut.putPlant and self.plantMove3 == 1 and self.plantPlace3:
                for walnut in self.walnuts:
                    walnut.update()
                    

            #shows already placed plants
            for walnut in self.plantPlaced3:
                walnut.blitme()
            
            for sunflower in self.plantPlaced2:
                sunflower.blitme()
            
            for pea in self.plantPlaced1:
                pea.blitme()

            manager.draw_ui(window_surface)
            pygame.display.flip()
            
            

if __name__ == '__main__':
    pd = Plant_defense()
    pd.run_game()


