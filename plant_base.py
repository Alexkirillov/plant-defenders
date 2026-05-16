import pygame
import settings
import time as tm

class Walnut(pygame.sprite.Sprite): 
    def __init__(self, pd_game, plant_size_width, plant_side_height, plant_postionx, plant_positiony):
        super().__init__()
        self.screen = pd_game.screen
        self.image = pygame.transform.scale(pygame.image.load(settings.WALNUT_PHOTO), (plant_size_width, plant_side_height))
        self.rect = self.image.get_rect()
        self.rect.x = plant_postionx
        self.rect.y = plant_positiony
        self.putPlant = False
        self.movePlant = False

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_4]:
            self.rect.y = settings.Y_POS1
            
            self.count = 2
        elif pressed_keys[pygame.K_5]:
            self.rect.y = settings.Y_POS2

        elif pressed_keys[pygame.K_6]:
            self.rect.y = settings.Y_POS3
        

        if pressed_keys[pygame.K_7]:
            self.rect.x = settings.X_POS1
        
        if pressed_keys[pygame.K_8]:
            self.rect.x = settings.X_POS2
        if pressed_keys[pygame.K_9]:
            self.rect.x = settings.X_POS3
        
        if pressed_keys[pygame.K_0]:
            self.rect.x = settings.X_POS4
        
        if pressed_keys[pygame.K_MINUS]:
            self.rect.x = settings.X_POS5

    def blitme(self,):
        self.screen.blit(self.image, (self.rect.x,self.rect.y))
    


class Sunflower(pygame.sprite.Sprite):
    def __init__(self, pd_game, plant_size_width, plant_side_height, plant_postionx, plant_positiony):
        super().__init__()
        self.screen = pd_game.screen
        self.image = pygame.transform.scale(pygame.image.load(settings.SUNFLOWER_PHOTO), (plant_size_width, plant_side_height))
        self.rect = self.image.get_rect()
        self.rect.x = plant_postionx
        self.rect.y = plant_positiony
        self.putPlant = False
        self.movePlant = False
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_4]:
            self.rect.y = settings.Y_POS1
            
            self.count = 2
        elif pressed_keys[pygame.K_5]:
            self.rect.y = settings.Y_POS2

        elif pressed_keys[pygame.K_6]:
            self.rect.y = settings.Y_POS3
        

        if pressed_keys[pygame.K_7]:
            self.rect.x = settings.X_POS1
        
        if pressed_keys[pygame.K_8]:
            self.rect.x = settings.X_POS2
        if pressed_keys[pygame.K_9]:
            self.rect.x = settings.X_POS3
        
        if pressed_keys[pygame.K_0]:
            self.rect.x = settings.X_POS4
        
        if pressed_keys[pygame.K_MINUS]:
            self.rect.x = settings.X_POS5

    def blitme(self,):
        self.screen.blit(self.image, (self.rect.x,self.rect.y))







class Pea(pygame.sprite.Sprite):
    def __init__(self, pd_game, plant_size_width, plant_side_height, plant_postionx, plant_positiony):
        super().__init__()
        self.screen = pd_game.screen
        self.image = pygame.transform.scale(pygame.image.load(settings.PEA_PHOTO), (plant_size_width, plant_side_height))
        self.rect = self.image.get_rect()
        self.rect.x = plant_postionx
        self.rect.y = plant_positiony
        self.putPlant = False
        self.movePlant = False
    def blitme(self,):
        self.screen.blit(self.image, (self.rect.x,self.rect.y))

    def shoot_bullet(self):
        self.pea_bullet = PeaBullet(28, self.rect.centerx+20, self.rect.centery-40, 5)
        return self.pea_bullet  
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_4]:
            self.rect.y = settings.Y_POS1
            
            self.count = 2
        elif pressed_keys[pygame.K_5]:
            self.rect.y = settings.Y_POS2

        elif pressed_keys[pygame.K_6]:
            self.rect.y = settings.Y_POS3
        

        if pressed_keys[pygame.K_7]:
            self.rect.x = settings.X_POS1
        
        if pressed_keys[pygame.K_8]:
            self.rect.x = settings.X_POS2
        if pressed_keys[pygame.K_9]:
            self.rect.x = settings.X_POS3
        
        if pressed_keys[pygame.K_0]:
            self.rect.x = settings.X_POS4
        
        if pressed_keys[pygame.K_MINUS]:
            self.rect.x = settings.X_POS5

class PeaBullet(pygame.sprite.Sprite):
    def __init__(self, bullet_size,bullet_postionx, bullet_positiony,bullet_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(settings.BULLET_PHOTO) , (bullet_size,bullet_size))
        self.rect = self.image.get_rect()
        self.rect.x = bullet_postionx
        self.rect.y = bullet_positiony
        self.speed = bullet_speed
    
    def update(self):
        self.rect.x += self.speed
