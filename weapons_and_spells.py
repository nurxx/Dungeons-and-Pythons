class Weapon:
    def __init__(self,name,damage):
        self.name = name 
        self.damage = damage

    def __str__(self):
        return '{0} - (damage {1})'.format(self.name,self.damage)

    def __eq__(self,other):
        return self.__dict__ == other.__dict__

class Spell:
    def __init__(self,name,damage,mana_cost,cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost =mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return '{0} - (damage {1}, mana_cost {2}, cast_range {3})'.format(self.name,self.damage,self.mana_cost,self.cast_range)

    def __eq__(self,other):
        return self.__dict__ == other.__dict__