from pygame.sprite import Sprite
import pygame

from game.utils.constants import BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT, PLAYER_TYPE, BULLET

class Bullet(Sprite):
     SPEED = 20
     PLAYER_BULLET_IMAGE = pygame.transform.scale(BULLET, (9,32))
     ENEMY_BULLET_IMG=pygame.transform.scale(BULLET_ENEMY, (9,32))
     BULLETS = { ENEMY_TYPE : ENEMY_BULLET_IMG, PLAYER_TYPE:PLAYER_BULLET_IMAGE}
    
     def __init__(self,spaceship):
         self.image = self.BULLETS[spaceship.type]
         self.rect =self.image.get_rect()
         self.rect.center = spaceship.rect.center
         self.owner = spaceship.type
        
     def update(self, bullets):
        #PLAYER TIPE
        # if self.owner ==PLAYER_TYPE:
        #      self.rect.y += self.SPEED
        #      if self.rect.y >= SCREEN_HEIGHT:
        #          bullets.remove(self)
        #          if self.owner == PLAYER_TYPE:
        #             self.rect.y += self.SPEED
        #          else:
        #              self.rect.y -= self.SPEED
        #              bullets.remove(self)
        #              if self.rect.y >= SCREEN_HEIGHT or self.rect.bottom <= 0:
        #                  if self in bullets:
        #                      bullets.remove(self)
        
        
        
        if self.owner ==ENEMY_TYPE:
             self.rect.y += self.SPEED
        else:
             self.rect.y -= self.SPEED
        if self.rect.y >= SCREEN_HEIGHT or self.rect.bottom <= 0:
            bullets.remove(self)
            #  if self.rect.y >= SCREEN_HEIGHT:
            #      bullets.remove(self)
            #      if self.owner == ENEMY_TYPE:
            #         self.rect.y += self.SPEED
                
                    #  bullets.remove(self)
                     
            
        #      else:
        #          for enemy in enemies:
        #          if self.rect.colliderect(enemy.rect):
        #              bullets.remove(self)
        #              enemies.remove(enemy)
        #              break
        #          if self.owner == ENEMY_TYPE:
        #              self.rect.y += self.SPEED
        #          else:
        #              self.rect.y += self.SPEED
        #              if self.rect.y >= SCREEN_HEIGHT or self.rect.bottom <= 0:
        #                  bullets.remove(self)
             
        #  if self.owner == ENEMY_TYPE:
        #      self.rect.y += self.SPEED
        #  else:
        #      self.rect.y += self.SPEED
            
        #  if self.rect.y >= SCREEN_HEIGHT or self.rect.bottom <= 0:
        #      bullets.remove(self)
        #  AGREGAR EL OTRO TYPE
        #  if self.rect.y >= SCREEN_HEIGHT:
        #      bullets.remove(self)
        
        #  if self.owner == PLAYER_TYPE:
        #       self.rect.y -= self.SPEED
        #       if self.rect.y <=0:
        #           bullets.remove(self)
        #       else:
        #           for enemy in enemies:
        #               if self.rect.colliderect(enemy.rect):
        #                   bullets.remove(self)
        #                   enemies.remove(enemy)
        #                   break
          
     
     def draw(self,screen):
         screen.blit(self.image,(self.rect.x, self.rect.y))