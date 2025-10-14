from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
    
    @abstractmethod
    def taking_damage(self, dmg):
        pass

class Zombie(Enemy):
    def __init__(self, hp, damage, shield):
        super().__init__(hp, damage)
        self.shield = shield

    def taking_damage(self, dmg):
        if self.shield <= dmg:
            self.hp -= (dmg - self.shield)
        else:
            pass
    
    def __str__(self):
        return f'zomb hp - {self.hp}'
    
class Skeleton(Enemy):
    def __init__(self, hp, damage, shield):
        super().__init__(hp, damage)
        self.shield = shield

    def taking_damage(self, dmg):
        if self.shield <= dmg:
            self.hp -= (dmg - self.shield)
        else:
            pass
    
    def __str__(self):
        return f'skel hp - {self.hp}'

