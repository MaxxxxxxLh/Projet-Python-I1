from random import *
class guerrier():
    def __init__(self):
        self.PV = 10
        self.dommage = 5
        self.pseudo = "guerrier"
        self.type = "guerrier"
    def attaque(self,ennemi):
        ennemi.PV -= randint(0,self.dommage)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False
