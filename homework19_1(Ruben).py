

class Weapon:

    def __init__(self,name,damage,range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self,actor,target):
        if  BaseCharacter.is_alive(target):
            pass
        else:
            print("the enemy is already defeated")


    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self,pos_x,pos_y,hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self,delta_x,delta_y):
        self.pos_x = delta_x
        self.pos_y = delta_y

    def is_alive(self):
        return self.hp > 0


    def get_damage(self,amount):
        if self.hp - amount > 0:
            return self.hp - amount
        else:
            return 0
    def get_cords(self):
        return self.pos_x,self.pos_y

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp,weapon):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self,target):
        if isinstance(target,MainHero):
            pass
        else:
            return "I can hit only main hero"

    def __str__(self):
        return f"enemy is in the position {self.pos_x,self.pos_y} with weapon {self.weapon}"

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp,weapon):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def heal(self,amount):
        if self.hp + amount <= 200:
            return self.hp + amount
        else:
            return 200
    def add_weapon(self,weapon):
        if isinstance(weapon,Weapon):
            return f"picked up {weapon}"








