from random import *
class chasseur():
    def __init__(self):
        self.PV = 10
        self.dommage = 3
        self.fleche = 5
        self.pseudo = "chasseur"
        self.type = "chasseur"
    def attaque(self,ennemi):
        if self.fleche > 0:
            ennemi.PV -= randint(0,self.dommage)
            self.fleche -= 1
        else:
            ennemi.PV -= randint(0,1)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False
