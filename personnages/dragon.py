from random import *
enemy_type = 1
hp = 150

def dragon_attacked():
    damage = randint(0,20)
    hp = hp - damage
    if hp > 0:
         print("Le dragon a perdu", damage, "PV !")
    elif hp <= 0:
        print('Le dragoin est mort !')


def dragon_attacking():
    if hp > 0:
        print('Le dragon attaque !')
        dragon_attack = randint(20, 30)
        if dragon_attack == 30:
            print("L'attaque du dragon est très efficace !")
        print('Vous perdez', dragon_attack, 'PV !')
