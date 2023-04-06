from random import *
class mage():
    def __init__(self):
        self.PV = 10
        self.dommage = 4
        self.AOE = 2
    def attaque(self,ennemi):
        ennemi.PV -= self.dommage
    def AOE(self,ennemi):
        ennemi.PV -= self.AOE
