import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE

class BulletManager:
    def __init__(self):
        self.bullets:list[Bullet]=[]
        self.enemy_bullets:list[Bullet]=[]
   
        #Añadiendo las bals de la nave 
        #self.spaceship_bullets: list[Bullet]=[]
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
                
                
    def draw(self,screen):
      for bullet in self.enemy_bullets + self.bullets:
          bullet.draw(screen)
    
    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == PLAYER_TYPE and len(self.enemy_bullets) < 3:
             self.enemy_bullets.append(bullet)
        