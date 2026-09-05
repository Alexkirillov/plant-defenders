"""self.playing = True
        self.paused = False
        self.game_started = False
        self.clock = pygame.time.Clock()
        self.play_button = None
        self.pause_button = None
        self.pause_buttons = []
        self.main_menu()
        self.pause_flag = False
        self.pause_game_button()
        if self.pause_button is not None:
            self.pause_button.hide()
        self.state = "main_menu"""

import pygame
import settings
import sys 
import pygame_gui
from plant_base import Walnut
from plant_base import Sunflower
from plant_base import Pea
from enemy_base import Enemy
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
        self.menu_screen = pygame.transform.scale(pygame.image.load(settings.BACKROUND), (settings.BACKROUND_LENGHT, settings.BACKROUND_HEIGHT))
        self.energy = pygame.font.SysFont("Arial", 20)
        

        "plants object creation"
        self.walnut = Walnut(self, 120, 150, 380,420)
        self.sunflower = Sunflower(self, 120, 150, 770, 620, 5)
        self.pea = Pea(self,120,150, 80,100)
        self.enemy = Enemy(self, 120,150,1700,100)
        
        self.bullet_group = pygame.sprite.Group()
        self.bullet_group_pea = pygame.sprite.Group()
        self.sprite_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
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
        self.ammo = 200
        self.time_cooldown = time.time()
        self.enemy_spawn_cooldown = time.time()
        self.game_lost_font = pygame.font.SysFont("Arial", 50)
        
        self.energy_inc = 5
        self.manager = pygame_gui.UIManager((settings.BACKROUND_LENGHT, settings.BACKROUND_HEIGHT))
        self.state = "menu"
        self.main_menu()
        self.pause_buttons = []
        self.music_volume = None
        self.menu_button = None
        self.pause_menu_visible = False
        self.volume_status = "volume: 100%"
        self.game_score = 0
        self.lives = 3
        self.wave_modifier_cooldown = 10
        

       
        self.menu_button = None
        pygame.mixer.init()
        pygame.mixer.music.load("plant-defenders/music/menu_music.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

    def main_menu(self):
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(750,500,200,40), text="Play game", manager=self.manager, object_id="#play_button")
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(750,600,200,40), text="Quit game", manager=self.manager, object_id="#quit_button")

    def hide_main_menu_buttons(self):
        self.play_button.hide()
        self.quit_button.hide()

    def create_game_menu_button(self):
        if self.menu_button is None:
            self.menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1500, 50, 200, 40), text="Game menu", manager=self.manager, object_id="#menu_button")

    def show_game_menu_button(self):
        if self.menu_button:
            self.menu_button.show()

    def hide_game_menu_button(self):
        if self.menu_button:
            self.menu_button.hide()

    def create_pause_buttons(self):
        if not self.pause_buttons:
            resume_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1500, 300, 200, 40), text="Resume", manager=self.manager, object_id="#resume_button")
            quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1500, 400, 200, 40), text="Quit", manager=self.manager, object_id="#quit_button")
            self.pause_buttons = [resume_button, quit_button]
            self.hide_pause_buttons()

    def show_pause_buttons(self):
        for btn in self.pause_buttons:
            btn.show()

    def hide_pause_buttons(self):
        for btn in self.pause_buttons:
            btn.hide()

    def sound_control(self):
        self.music_volume = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1500, 10, 200, 40), text=self.volume_status, manager=self.manager, object_id="#sound_control_button")

    def pea_upgrade(self):
        self.shot_upgrade = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1500, 100, 200, 40), text="Upgrade Pea", manager=self.manager, object_id="#pea_upgrade_button")

    def handle_button_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                sys.exit()
            self.manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.state = "playing"
                    self.hide_main_menu_buttons()
                    self.create_game_menu_button()
                    self.show_game_menu_button()
                    self.create_pause_buttons()
                    self.sound_control()
                    self.lives = 3
                    self.game_score = 0

                elif event.ui_element == self.quit_button:
                    sys.exit()

                if event.ui_element == self.menu_button:
                    self.state = "paused"
                    self.show_pause_buttons()
                    self.hide_game_menu_button()

                    

                if event.ui_element == self.pause_buttons[0]:
                    self.state = "playing"
                    self.hide_pause_buttons()
                    self.show_game_menu_button()
                elif event.ui_element == self.pause_buttons[1]:
                    sys.exit()

                if event.ui_element == self.music_volume:
                    if self.volume_status == "volume: 100%":
                        self.volume_status = "volume: 75%"
                        self.music_volume.set_text(self.volume_status)
                        pygame.mixer.music.set_volume(0.75)
                    elif self.volume_status == "volume: 75%":
                        self.volume_status = "volume: 50%"
                        self.music_volume.set_text(self.volume_status)
                        pygame.mixer.music.set_volume(0.5)
                    elif self.volume_status == "volume: 50%":
                        self.volume_status = "volume: 25%"
                        self.music_volume.set_text(self.volume_status)
                        pygame.mixer.music.set_volume(0.25)
                    elif self.volume_status == "volume: 25%":
                        self.volume_status = "volume: 0%"
                        self.music_volume.set_text(self.volume_status)
                        pygame.mixer.music.set_volume(0.0)
                    elif self.volume_status == "volume: 0%":
                        self.volume_status = "volume: 100%"
                        self.music_volume.set_text(self.volume_status)
                        pygame.mixer.music.set_volume(1.0)

                
    def run_game(self):
        clock = pygame.time.Clock()
        self.playing = True
        
        while self.playing:
            dt = clock.tick(60) / 1000.0
            self.screen.fill((0, 0, 0))
            self.handle_button_events()
            self.manager.update(dt)
            if self.state == "menu":
                
                self.screen.blit(self.menu_screen, (0, 0))
                self.manager.draw_ui(self.screen)
                if self.lives < 1:
                    self.screen.blit(self.game_lost_font.render("Game Over", True, (255, 0, 0)), (740, 230))
                    self.screen.blit(self.game_lost_font.render(f"Score: {self.game_score}", True, (0, 0, 0)), (760, 300))
                    

            elif self.state == "playing":
                self.enemy_spawn_wait = randint(1,3)
                self.enemy_offset = randint(-50, 50)
                self.screen.blit(self.game_backround,(0,0))
                self.screen.blit(self.score_counter,(5,5))
                self.screen.blit(self.energy.render(f"Energy: {self.ammo}", True, (0, 0, 0)), (12, 25))
                if time.time() - self.time_cooldown >= 1:
                    self.ammo += self.energy_inc
                    self.time_cooldown = time.time()
                pressed_key = pygame.key.get_pressed()
                self.screen.blit(self.energy.render(f"Score: {self.game_score}", True, (0, 0, 0)), (12, 45))
                if time.time() - self.wave_modifier_cooldown >= 1:

                    """for enemy in self.enemy:
                        self.modify = randint(1,2)
                        if self.modify ==  1:
                            self.enemy.lifes += self.enemy.lifes/10

                        elif self.modify == 2:
                            self.enemy.speed += 0.1
                            print(self.enemy.speed)
                            self.wave_modifier_cooldown = time.time()"""
                    


                "plant call"
                #summons the plants
                if pressed_key[pygame.K_1] and len(self.sunflowers) == 0 and len(self.walnuts) == 0 and len(self.peas) < 2:
                    self.pea = Pea(self,120,150, 80,100)
                    self.peas.append(self.pea)
                    self.plantMove1 = 1
                    self.pea.putPlant = True
                    self.sprite_group.add(self.pea)

                if pressed_key[pygame.K_2] and len(self.peas) == 0 and len(self.walnuts) == 0 and len(self.sunflowers) < 2 :
                    self.sunflower = Sunflower(self,120,150, 80,100,5)
                    self.sunflowers.append(self.sunflower)
                    self.plantMove2 = 1
                    self.sunflower.putPlant = True
                    self.sprite_group.add(self.sunflower)
                   

                if pressed_key[pygame.K_3] and len(self.sunflowers) == 0 and len(self.peas) == 0 and len(self.walnuts) < 2:
                    self.walnut = Walnut(self,120,150, 80,100)
                    self.walnuts.append(self.walnut)
                    self.plantMove3 = 1
                    self.walnut.putPlant = True
                    self.sprite_group.add(self.walnut)
                    
                    
                if time.time() - self.enemy_spawn_cooldown >= self.enemy_spawn_wait:
                    spawn = randint(1,3)
                    enemy = Enemy(self, 120,150,1800,settings.Y_POS1+self.enemy_offset if spawn == 1 else settings.Y_POS2+self.enemy_offset if spawn == 2 else settings.Y_POS3+self.enemy_offset)
                    self.enemy_group.add(enemy)
                    
                    self.enemy_spawn_cooldown = time.time()


                if pressed_key[pygame.K_p]:
                    for pea in self.peas:
                        sprite_check = pygame.sprite.spritecollide(pea, self.plantPlaced1 + self.plantPlaced2 + self.plantPlaced3, dokill=False)
                        if not pea.is_placed and len(sprite_check) == 0 and self.ammo >= 150:
                            pea.fix_position()
                            self.plantPlaced1.append(pea)
                            self.last_shot_time[pea] = time.time()
                            self.ammo -= 150
                        else:
                            self.sprite_group.remove(pea)
                    self.peas.clear()
                    
                    for sunflower in self.sunflowers:
                        sprite_check = pygame.sprite.spritecollide(sunflower, self.plantPlaced1 + self.plantPlaced2 + self.plantPlaced3, dokill=False)
                        if not sunflower.is_placed and len(sprite_check) == 0 and self.ammo >= 50:
                            sunflower.fix_position()
                            self.plantPlaced2.append(sunflower)
                            self.energy_inc += self.sunflower.energy_gen
                            self.sunflower.energy_gen = 0
                            self.ammo -= 50
                        else:
                            self.sprite_group.remove(sunflower)
                        self.sunflowers.clear()

                    for walnut in self.walnuts:
                        sprite_check = pygame.sprite.spritecollide(walnut, self.plantPlaced1 + self.plantPlaced2 + self.plantPlaced3, dokill=False)
                        if not walnut.is_placed and len(sprite_check) == 0 and self.ammo >= 100:
                            walnut.fix_position()
                            self.plantPlaced3.append(walnut)
                            self.ammo -= 100
                        else:
                            self.sprite_group.remove(walnut)
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
                    bullet = pea.shoot_bullet(current_time,0.1)
                    
                    if bullet:
                        self.bullet_group.add(bullet)

                    
                for enemy in self.enemy_group:
                    if pygame.sprite.spritecollide(enemy, self.bullet_group, dokill=True):
                        enemy.lifes -= 25
                        if enemy.lifes <= 0:
                            self.enemy_group.remove(enemy)
                            self.game_score += 50
                            print(self.game_score)
                    if enemy.rect.x <= 0:
                        enemy.kill()
                        self.lives -= 1
                        print(self.lives)

                if self.lives < 1:
                    self.state = "menu"
                    self.ammo = 200
                    self.energy_inc = 5
                    self.enemy_group.empty()
                    self.plantPlaced1.clear()
                    self.plantPlaced2.clear()
                    self.plantPlaced3.clear()
                    self.sprite_group.empty()
                    self.play_button.show()
                    self.play_button.set_text("Play again")
                    self.quit_button.show()
                    self.hide_game_menu_button()
                   

                        
                for enemy in self.enemy_group:
                    if pygame.sprite.spritecollide(enemy, self.plantPlaced1 + self.plantPlaced2 + self.plantPlaced3, dokill=False):
                        self.pea.lifes -= 10
                        if self.pea.lifes <= 0:
                            self.sprite_group.remove(self.pea)
                        enemy.speed = 0
                            
                self.bullet_group.update()
                self.bullet_group.draw(self.screen)
                self.enemy_group.draw(self.screen)
                self.enemy_group.update()
                self.manager.draw_ui(self.screen)

            elif self.state == "paused":
                self.screen.blit(self.game_backround,(0,0))
                s = pygame.Surface((settings.BACKROUND_LENGHT, settings.BACKROUND_HEIGHT), pygame.SRCALPHA)
                s.fill((0, 0, 0, 128))
                self.screen.blit(s, (0, 0))
                self.manager.draw_ui(self.screen)
            pygame.display.flip()
if __name__ == '__main__':
    pd = Plant_defense()
    pd.run_game()
                    



