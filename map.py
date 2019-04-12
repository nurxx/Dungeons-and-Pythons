from heroes_and_enemies import *
from treasures import *
import os 

class Map:
    def __init__(self,_map,hero):
        self._map = _map
        self.rows = len(_map)
        self.columns = len(_map[-1])

        if not isinstance(hero,Hero):
            raise TypeError('Map heroes must be class Hero!')
        self.hero = hero

    def print_map(self):
        game_map = [''.join(line) for index,line in enumerate(self._map)]
        print(''.join(game_map))

    def move_hero(self,direction):
        if direction == 'up' and self._map[hero.state_row-1][hero.state_column] != '#':
            return self.hero.state_row - 1 >= 0
        if direction == 'down' and self._map[hero.state_row+1][hero.state_column] != '#':
            return self.hero.state_row + 1 < self.rows
        if direction == 'left' and self._map[hero.state_row][hero.state_column-1] != '#':
            return self.hero.state_column - 1 >=0
        if direction == 'right' and self._map[hero.state_row][hero.state_column+1] != '#':
            return self.hero.state_column + 1 < self.columns

    def spawn(self):
        letter = hero.known_as()[0].upper()
        _map[0][0] = letter
        return True

    def is_treasure(self):
        return self._map[hero.state_row][hero.state_column] == 'T'

    def take_treasure(self):
        treasure = pick_treasure()
        if treasure[0] == 'Health Potion':
            choice = input('It\'s a health potion! Dou you want to take it? (y/n)')
            if choice == 'y':
                health_potion = treasure[1]
                self.hero.take_healing(health_potion.points)
        if treasure[0] == 'Mana Potion':
            choice = input('It\'s a mana potion! Do you want to take it? (y/n)')
            if choice == 'y':
                mana_potion = treasure[1]
                self.hero.take_mana(mana_potion.points)
        if treasure[0] =='Weapon':
            print('It\'s a weapon!')
            weapon = treasure[1]
            self.hero.equip(weapon)
        if treasure[0]=='Spell':
            print('It\'s a spell!')
            spell = treasure[1]
            self.hero.learn(spell)

levels = os.listdir('levels')
hero = Hero(name="Bron", title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=2)
hero.state_row = 0
hero.state_column = 0

print('\nMove your hero!')
print('Press 4 to move left!\nPress 6 to move right!\nPress 8 to move up!\nPress 2 to move down!\n')
for index,level in enumerate(levels):
    with open('levels/{0}'.format(level),'r') as f:
        _map = f.readlines()

    _map = [list(line) for index,line in enumerate(_map)]
    game = Map(_map,hero)

    while hero.is_alive() and game._map[game.hero.state_row][game.hero.state_column] != 'G':
        game.print_map()
        print()
        choice = input()
        if choice == '2' and game.move_hero('down')==True:
            game._map[game.hero.state_row][game.hero.state_column] = '.'
            game.hero.state_row+=1
            if game.is_treasure():
                print('Found treasure!')
                game.take_treasure()
            if game._map[game.hero.state_row][game.hero.state_column] == 'G':
                print('Congratulations, you\'ve passed to next level!')
            game._map[game.hero.state_row][game.hero.state_column] = 'S'
            continue

        if choice == '4' and game.move_hero('left')==True:
            game._map[game.hero.state_row][game.hero.state_column] = '.'
            game.hero.state_column-=1
            if game.is_treasure():
                print('Found treasure!')
                game.take_treasure()
            if game._map[game.hero.state_row][game.hero.state_column] == 'G':
                print('Congratulations, you\'ve passed to next level!')
            game._map[game.hero.state_row][game.hero.state_column] = 'S'
            continue

        if choice == '6' and game.move_hero('right') == True:
            game._map[game.hero.state_row][game.hero.state_column] = '.'
            game.hero.state_column+=1
            if game.is_treasure():
                print('Found treasure!')
                game.take_treasure()
            if game._map[game.hero.state_row][game.hero.state_column] == 'G':
                print('Congratulations, you\'ve passed to next level!')
            game._map[game.hero.state_row][game.hero.state_column] = 'S'
            continue

        if choice == '8' and game.move_hero('up')==True:
            game._map[game.hero.state_row][game.hero.state_column] = '.'
            game.hero.state_row-=1
            if game.is_treasure():
                print('Found treasure!')
                game.take_treasure()
            if game._map[game.hero.state_row][game.hero.state_column] == 'G':
                print('Congratulations, you\'ve passed to next level!')
            game._map[game.hero.state_row][game.hero.state_column] = 'S'
            continue

        else:
            print('Oops, an obstacle :( Please try moving to a differrent direction!')


