from weapons_and_spells import *

class Unit:
    __max_health = 0
    __max_mana = 0
    def __init__(self, health, mana):
        if not isinstance(health,int) and not isinstance(health,float) and health < 0 and not isinstance(mana,int) and not isinstance(mana,float) and mana < 0:
            raise ValueError('Health and Mana must be positive numbers of type < int,float > ')
        self.health = health
        self.mana = mana
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
        if self.is_alive()==False:
            return False
        elif self.health == self.__max_hp:
            return 'Health is already at max'
        elif self.health + healing_points < self.__max_hp:
            
            self.health += healing_points
            return self.health
        else:
            self.health = self.max_hp
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
        self.name = name
        self.title =title
        self.is_equiped = False
        self.learned_spell = False
        self.current_weapon = None
        self.current_spell = None

    def known_as(self):
        return '{0} the {1}'.format(self.name, self.title)

    def get_health(self):
        super().get_health()

    def get_mana(self):
        super().get_mana()

    def is_alive(self):
        super().is_alive()
            
    def can_cast(self):
        super().can_cast()

    def take_damage(self):
        super().take_damage()

    def take_healing(self):
        super().take_healing()

    def take_mana(self):
        super().take_mana()

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
        self.damage = damage

    def get_health(self):
        super().get_health()

    def get_mana(self):
        super().get_mana()

    def is_alive(self):
        super().is_alive()
            
    def can_cast(self):
        super().can_cast()

    def take_damage(self):
        super().take_damage()

    def take_healing(self):
        super().take_healing()

    def take_mana(self):
        super().take_mana()


h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)

h.equip(w)

h.attack(by="weapon") == 20