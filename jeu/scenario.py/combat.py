from chasseurHeros import *
from guerisseurHeros import * 
from guerrierHeros import *
from mageHeros import *
from troll import *
from dragon import *

#initialisation des heros
monChasseur = chasseur()
monGuerrier = guerrier()
monGuerisseur = guerisseur()
monMage = mage()



combattants = {"chasseur": monChasseur, "guerrier": monGuerrier, "guerisseur": monGuerisseur, "mage" : monMage} #mettre les différents heros dans un dictionnaire
listeCombattants = list(combattants.values()) #créer une liste avec les combattants en vie








def cible(ennemis): #choix de l'ennemi à attaquer
    if len(ennemis) != 1: #choisir si plusieurs ennemis
        print("Il y a "+ str(len(ennemis))+" ennemis")
        print("Qui voulez-vous attaquer?")
        print("Veuillez indiquer un nombre entre 1 et " + str(len(ennemis)))
        a = True
        while a:
            try:
                choix = int(input(""))
            except:
                print("Veuillez entrer un nombre seulement!!!")
            if 1 > choix or len(ennemis) < choix:
                print("Veuillez saisir un nombre compris entre 1 et "+ str(len(ennemis)))
                choix = input("")
            elif choix <= len(ennemis) and choix >= 1:
                a = False
    else:
        choix = 1
    return choix-1


def tourHeros(allies, ennemis): #attaquer les trolls
    for i in allies:
        if ennemis == []:
            break
        if i.estEnVie():
            if i.type == "mage":
                a = ennemis [cible(ennemis)]
                i.attaque(ennemis,a)
            else:
                a=ennemis[cible(ennemis)]
                i.attaque(a)
            if not a.estEnVie():
                ennemis.remove(a)
            a.attaque(i)
            if not i.estEnVie():
                allies.remove(i)
        







def combat(attaquant, compteur):
    vagueEnnemis = vagues(compteur)
    while listeCombattants != [] and vagueEnnemis != []:
        tourHeros(attaquant, vagueEnnemis)



def vagues(compteur):
    vagueTroll = []
    if compteur >= 1 and compteur <= 3:
        trollUn = troll()
        trollDeux = troll()
        trollTrois = troll()
        vagueTroll.append(trollUn)
        vagueTroll.append(trollDeux)
        vagueTroll.append(trollTrois)
        if compteur > 1 and compteur <= 3:
            trollQuatre = troll()
            vagueTroll.append(trollQuatre)
            if compteur == 3:
                trollCinq = troll()
                vagueTroll.append(trollCinq)
    if compteur == 4:
        bossDragon = dragon()
        vagueTroll.append(bossDragon)
    return vagueTroll





def jeu():
    for compteur in range(1,5):
        combat(listeCombattants, compteur)
    

jeu()