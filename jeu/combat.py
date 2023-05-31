from trollClass import *
from dragonClass import *

def tourHeros(attaquant,allies, ennemis, cibleEnnemis): #attaquer les trolls
    if attaquant.estEnVie():
        if attaquant.type == "mage":
            attaquant.attaque(ennemis,cibleEnnemis)
        else:
            attaquant.attaque(cibleEnnemis)
            
        if cibleEnnemis.estEnVie():
            if cibleEnnemis.type == "dragon":
                cibleEnnemis.attaque(allies, attaquant)
            else:
                cibleEnnemis.attaque(attaquant)
              
        else:
            ennemis.remove(cibleEnnemis)
            
        if not attaquant.estEnVie():
            allies.remove(attaquant)
            
       
        
        
def choisirEnnemis(cible, vague):
    if cible.type == "ennemi":
        for j in vague:
            if j.pseudo == cible.pseudo:
                return j







def combat(attaquantListe, cible,vagueEnnemis):
    while attaquantListe != [] and vagueEnnemis != []:
        for j in attaquantListe:
            tourHeros(j,attaquantListe, vagueEnnemis,cible)
    if attaquantListe != []:
        for k in attaquantListe:
            k.level += 1



def vagues(compteur,x,y):
    vagueTroll = []
    if compteur >= 1 and compteur <= 3:
        trollUn = troll(x,y,70,57,"troll un")
        trollDeux = troll(x,y,70,39, "troll deux")
        trollTrois = troll(x,y,70,21, "troll trois")
        vagueTroll.append(trollUn)
        vagueTroll.append(trollDeux)
        vagueTroll.append(trollTrois)
        if compteur > 1 and compteur <= 3:
            trollQuatre = troll(x,y,70,75, "troll quatre")
            vagueTroll.append(trollQuatre)
            if compteur == 3:
                trollCinq = troll(x,y,70,3, "troll cinq")
                vagueTroll.append(trollCinq)
    if compteur == 4:
        bossDragon = dragon(x,y,70,39,"dragonneau")
        vagueTroll.append(bossDragon)
    return vagueTroll




