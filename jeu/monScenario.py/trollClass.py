from random import *
class troll():
    def __init__(self):
        self.PV = 5
        self.dommage = 4
        self.attaqueChasseur = 2
        self.pseudo = "troll"
    def attaque(self,ennemi):
        if ennemi.type == "chasseur":
            ennemi.PV -= randint(0,self.attaqueChasseur)
        else:
            ennemi.PV -= randint(0,self.dommage)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False