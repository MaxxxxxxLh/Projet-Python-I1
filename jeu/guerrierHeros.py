from random import *
class guerrier():
    def __init__(self):
        self.PV = 10
        self.dommage = 5
    def attaque(self,ennemi):
        ennemi.PV -= self.dommage

