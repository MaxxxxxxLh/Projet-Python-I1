from random import *

def dragon():
    enemy_type = fire
    hp = 150
    damage = randint(0,20)
    hp = hp - damage
    if hp > 0:
         print("Le dragon a perdu", damage, "PV !")
    elif hp <= 0:
        print('Le dragoin est mort !')
