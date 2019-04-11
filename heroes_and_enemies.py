from weapons_and_spells import *

class Unit:
    def __init__(self, health, mana):
        if not isinstance(health,int) and not isinstance(health,float) and not isinstance(mana,int) and not isinstance(mana,float):
            raise TypeError('Health and Mana must be of type < int > or < float > ! ')
        if  mana < 0 or health < 0:
            raise ValueError('Health and Mana must be positive!')
        self.health = health
        self.mana = mana
        self.__max_health = self.health
        self.__max_mana = self.mana
    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def take_damage(self, damage_points):
        if damage_points >= self.health:
            self.health = 0
        else:
            self.health -= damage_points
        return self.health

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False
        elif self.health == self.__max_health:
            return 'Health is already at max'
        elif self.health + healing_points < self.__max_health:
            self.health += healing_points
            return self.health
        else:
            self.health = self.__max_health
            return self.health

    def take_mana(self, mana_points):
        if self.mana == self.__max_mana:
            return 'Mana is already at max'
        elif self.mana + mana_points < self.__max_mana:
            self.mana += mana_points
            return self.mana
        else:
            self.mana = self.__max_mana
            return self.mana

class Hero(Unit):
    def __init__(self, health, mana, name, title, mana_regeneration_rate):
        super().__init__(health,mana)
        if not isinstance(name,str):
            raise TypeError('Hero name must be type < str > !')
        self.name = name
        if not isinstance(title,str):
            raise TypeError('Hero title must be type < str > !')
        self.title =title
        self.is_equiped = False
        self.learned_spell = False
        self.current_weapon = None
        self.current_spell = None

    def known_as(self):
        return '{0} the {1}'.format(self.name, self.title)

    def get_health(self):
        return super().get_health()

    def get_mana(self):
        return super().get_mana()

    def is_alive(self):
        return super().is_alive()
            
    def can_cast(self):
        return super().can_cast()

    def take_damage(self, damage_points):
        return super().take_damage(damage_points)

    def take_healing(self, healing_points):
        return super().take_healing(healing_points)

    def take_mana(self, mana_points):
        return super().take_mana(mana_points)

    def equip(self,weapon):
        if self.is_equiped == False:
            self.current_weapon = weapon
            self.is_equiped = True
        else:
            choice = input('Your current weapon is {}. Dou you want to change it? (y/n)'.format(self.current_weapon))
            if choice == 'y':
                self.current_weapon = weapon

    def learn(self,spell):
        if self.learned_spell == False:
            self.current_spell = spell
            self.learned_spell = True
        else:
            choice = input('You already know the spell {}. Do you want forget it and learn the new spell? (y/n)'.format(self.current_spell))
            if choice == 'y':
                self.current_spell = spell

    def attack(self,by):
        if by == 'weapon':
            if self.is_equiped == True:
                return self.current_weapon.damage
            else:
                return 0
        elif by == 'magic':
            if self.learned_spell == True:
                return self.current_spell.damage
            else: 
                return 0

class Enemy(Unit):
    def __init__(self,health,mana, damage):
        super().__init__(health=health,mana=mana)
        if type(damage) is not int and type(damage) is not float:
            raise TypeError('Enemy\'s damage must be type < int > or < float > !')
        if damage < 0:
            raise ValueError('Enemy damage must be positive !')
        self.damage = damage

    def get_health(self):
        return super().get_health()

    def get_mana(self):
        return super().get_mana()

    def is_alive(self):
        return super().is_alive()
            
    def can_cast(self):
        return super().can_cast()

    def take_damage(self, damage_points):
        return super().take_damage(damage_points)

    def take_healing(self, healing_points):
        return super().take_healing(healing_points)

    def take_mana(self , mana_points):
        return super().take_mana(mana_points)

