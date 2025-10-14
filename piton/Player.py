class Player:
    def __init__(self, hp, damage, shield):
        self.hp = hp
        self.damage = damage
        self.shield = shield

    def __str__(self):
        return f'hp - {self.hp}, damage - {self.damage}, shield - {self.shield}'
    
    def taking_damage(self, dmg):
        self.hp -= dmg

