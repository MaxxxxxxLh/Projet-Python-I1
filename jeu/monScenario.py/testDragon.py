from dragon import *
from troll import *

#on initialise le dragon, les trois trolls et la liste qui va contenir les trolls
dragoneau = dragon()
trollUn = troll()
trollDeux = troll()
trollTrois = troll()
vagueTroll = []
 
#on ajoute à la liste les trois trolls
vagueTroll.append(trollUn)
vagueTroll.append(trollDeux)
vagueTroll.append(trollTrois)


dragoneau.attaque(vagueTroll, vagueTroll[0])

for i in vagueTroll:
    print("Le troll "+str(vagueTroll.index(i)+1)+" a "+str(i.PV)) #on affiche les pvs des différents trolls

