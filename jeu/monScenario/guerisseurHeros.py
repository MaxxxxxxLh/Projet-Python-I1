from random import *
class guerisseur():
    def __init__(self):
        self.PV = 10
        self.dommage = 1
        self.soin = 2
        self.pseudo = "guerrisseur"
        self.type = "guerrisseur"
    def attaque(self,ennemi):
        ennemi.PV -= randint(0,self.dommage)
    def soin(self,allie):
        allie.PV += self.soin
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False