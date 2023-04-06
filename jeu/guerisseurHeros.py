from random import *
class guerisseur():
    def __init__(self):
        self.PV = 10
        self.dommage = 1
        self.soin = 2
    def attaque(self,ennemi):
        ennemi.PV -= self.dommage
    def soin(self,allie):
        allie.PV += self.soin
