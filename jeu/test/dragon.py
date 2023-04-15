from random import *

class dragon():
    def __init__(self):
        self.PV = 15
        self.dommage = randint(0,6)
        self.AOE = randint(0,2)
        self.pseudo = "dragon"
    def attaque(self, ennemis):
        ennemis.PV -= random(0,self.dommage)
        