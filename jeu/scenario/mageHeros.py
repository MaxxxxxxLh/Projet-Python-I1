from random import *
class mage():
    def __init__(self):
        self.PV = 10
        self.dommage = 4
        self.AOE = 2
        self.pseudo = "mage"
        self.type = "mage"
    def attaque(self,ennemis, monoCible):
        for i in ennemis:
            if i == monoCible:
                i.PV -= randint(0,self.dommage)
            else:
                i.PV -= randint(0, self.AOE)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False