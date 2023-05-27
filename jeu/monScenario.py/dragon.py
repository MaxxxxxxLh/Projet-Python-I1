from random import *

class dragon():
    def __init__(self):
        self.PV = 15
        self.dommage = randint(0,6)
        self.AOE = randint(0,2)
        self.pseudo = "dragon"
    def attaque(self, ennemis, attaquant):
        for i in ennemis:
            if i == attaquant:
                attaquant.PV -= randint(0,self.dommage)
            else:
                i.PV -= randint(0,self.AOE)
