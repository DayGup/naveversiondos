

import random
from game.components.enemies.enemy import Enemy, EnemyTwo, EnemyThree
from game.utils.constants import  SCREEN_HEIGHT


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] =[]
    
    
    def update(self, game):
        if not self.enemies: #cosas vacias seran falsas # []{} 0 "" y de lo contratri sera verdadero 
           list_enemies =[Enemy(),EnemyTwo(), EnemyThree()]    #esto para que haga que las naves vayan apareiencido cuando uno no este 
           enemy_random = random.choice(list_enemies)
           self.enemies.append(enemy_random)
           
            # self.enemies.append(Enemy())
            # self.enemies.append(EnemyTwo())
            # self.enemies.append(EnemyThree())
            
        
        for enemy in self.enemies:
           enemy.update(self.enemies, game)
     
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    # def get_enemies(self):
    #     return self.enemies