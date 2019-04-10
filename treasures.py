from weapons_and_spells import *
from random import randint 
    
class Potion():
    def __init__(self,points):
        self.points = points

    def __str__(self):
        return 'Potion with {} points'.format(self.points)

def pick_weapon():
    weapons = [Weapon('Battle Axes',40),Weapon('Swords',15),Weapon('War Hammers',20),Weapon('War Scythes',60),Weapon('Shotguns',30),Weapon('Whips and Lassos',20),Weapon('Daggers',30)]

    return weapons[randint(0,len(weapons)-1)]

def pick_spell():
    spells = [Spell('Solar Blast',10,20,1),Spell('Mystic Flare',20,40,2),Spell('Evocation of Blessings',30,50,5)]

    return spells[randint(0,len(spells)-1)]

def pick_treasure():
    treasures = [('Mana Potion',Potion(randint(1,50))),('Health Potion',Potion(randint(1,50))),('Weapon',pick_weapon()),('Spell',pick_spell())]

    return treasures[randint(0,len(treasures)-1)]
