import unittest 
from heroes_and_enemies import *

class TestHeroesAndEnemies(unittest.TestCase):
    def test_validate_hero_title_is_type_str(self):
        with self.assertRaises(TypeError):
            hero = Hero(name="Bron", title=5, health=100, mana=100, mana_regeneration_rate=2)

    def test_validate_hero_name_is_type_str(self):
        with self.assertRaises(TypeError):
            hero = Hero(name=1, title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    def test_validate_hero_health_is_type_int_or_float(self):
        with self.assertRaises(TypeError):
            hero = Hero(name="Bron", title="Dragonslayer", health="100", mana=100, mana_regeneration_rate=2)

    def test_validate_hero_mana_is_type_int_or_floats(self):
        with self.assertRaises(TypeError):
            hero = Hero(name="Bron", title="Dragonslayer", health=100, mana="100", mana_regeneration_rate=2)

    def test_validate_hero_health_positive_number(self):
        with self.assertRaises(ValueError):
            hero = Hero(name="Bron", title="Dragonslayer", health=-1, mana=100, mana_regeneration_rate=2)

    def test_validate_hero_mana_positive_number(self):
        with self.assertRaises(ValueError):
            hero = Hero(name="Bron",title ="Dragonslayer",health = 100, mana = -1, mana_regeneration_rate=2)

    def test_validate_enemy_health_is_type_int_or_float(self):
        with self.assertRaises(TypeError):
            enemy = Enemy(health="100",mana =100,damage = 20)

    def test_validate_enemy_health_positive_number(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(health=-100,mana =100,damage = 20)

    def test_validate_enemy_mana_positive_number(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(health=100,mana =-100,damage = 20)

    def tets_validate_enemy_mana_is_type_int_or_float(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(health=100,mana ="100",damage = 20)

    def test_validate_enemy_damage_positive_number(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(health=100,mana =100,damage = -20)

    def test_validate_enemy_damage_is_type_int_or_float(self):
        with self.assertRaises(TypeError):
            enemy = Enemy(health=100,mana =100,damage = '-20')

    def test_hero_known_as(self):
        expected_output = "Bron the Dragonslayer"
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertTrue(hero.known_as(),expected_output)

    def test_unit_get_health(self):
        expected_output = 100
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(expected_output,hero.get_health())

    def test_unit_get_mana(self):
        expected_output = 100
        enemy = Enemy(health=100,mana = 100,damage = 20)
        self.assertEqual(expected_output,enemy.get_mana())

    def test_unit_is_alive(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=0, mana=100, mana_regeneration_rate=2)
        self.assertEqual(False,hero.is_alive())

    def test_unit_can_cast(self):
        enemy = Enemy(health=100,mana = 0,damage = 20)
        self.assertEqual(False,enemy.can_cast())

    def test_unit_take_damage_when_damage_grater_than_health(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(0,hero.take_damage(200))

    def test_unit_take_damage(self):
        enemy = Enemy(health = 100, mana = 20, damage = 20)
        self.assertEqual(50,enemy.take_damage(50))

    def test_unit_take_healing_when_unit_not_alive(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=0, mana=100, mana_regeneration_rate=2)
        self.assertEqual(False,hero.take_healing(10))

    def test_unit_take_healing_when_unit_health_at_max(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual('Health is already at max',hero.take_healing(10))

    def test_unit_take_healing(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        hero.take_damage(20)
        self.assertEqual(90,hero.take_healing(10))

    def test_unit_take_mana_when_unit_mana_already_at_max(self):
        enemy = Enemy(health =100,mana = 100, damage =20)
        self.assertEqual('Mana is already at max',enemy.take_mana(20))

    def test_unit_take_mana(self):
        enemy = Enemy(health = 100, mana = 100, damage = 20)
        enemy.mana -= 50
        self.assertEqual(70,enemy.take_mana(20))

    def test_hero_equip(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        weapon = Weapon(name="The Axe of Destiny", damage=20)

        hero.equip(weapon)
        self.assertTrue(True,hero.is_equiped)
        self.assertTrue(weapon,hero.current_weapon)
    
    def test_hero_attack(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        weapon = Weapon(name="The Axe of Destiny", damage=20)

        hero.equip(weapon)
        self.assertTrue(hero.attack(by="weapon"), 20)

    def test_hero_learn_spell(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        spell = Spell(name ='Mystic Flare',damage =40, mana_cost =20, cast_range =2)
        hero.learn(spell)
        self.assertTrue(True,hero.learned_spell)
        self.assertTrue(spell,hero.current_spell)

if __name__ == '__main__':
    unittest.main()


