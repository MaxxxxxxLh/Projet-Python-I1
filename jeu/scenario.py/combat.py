from chasseurHeros import *
from guerisseurHeros import * 
from guerrierHeros import *
from mageHeros import *
from troll import *


#initialisation des heros
monChasseur = chasseur()
monGuerrier = guerrier()
monGuerisseur = guerisseur()
monMage = mage()


combattants = {"chasseur": monChasseur, "guerrier": monGuerrier, "guerisseur": monGuerisseur, "mage" : monMage} #mettre les différents heros dans un dictionnaire
listeCombattants = list(combattants.values()) #créer une liste avec les combattants en vie
listeCombattantsDemo = [monGuerrier] #séance trois

trollUn = troll() #initialise le troll
vagueTroll = []
vagueTroll.append(trollUn) #ajout du troll dans la vague

def demoCombat(heros,troll):
    while heros != [] and troll != []:
        tourHeros(heros,troll)
        tourTroll(troll,heros[0])
        try :
            print("le "+ heros[0].pseudo+" a "+str(heros[0].PV)+" PV")
        except:
            print("Le heros est mort")
        try :
            print("le "+ troll[0].pseudo+" a "+str(troll[0].PV)+"PV")
        except:
            print("le troll est mort")



def cible(ennemis): #choix de l'ennemi à attaquer
    if len(ennemis) != 1: #choisir si plusieurs ennemis
        print("Il y a "+ len(ennemis)+" ennemis")
        print("Qui voulez-vous attaquer?")
        print("Veuillez indiquer un nombre entre 1 et " + len(ennemis))
        choix = input("")
        while True:
            try:
                if 1 > choix or len(ennemis) < choix:
                    print("Veuillez saisir un nombre compris entre 1 et "+ len(ennemis))
                    choix = input("")
                else:
                    break
            except:
                print("Veuillez entrer un nombre seulement!!!")
    else:
        choix = 1
    return choix-1


def tourHeros(allies, ennemis): #attaquer les trolls
    for i in allies:
        if i.estEnVie():
            a=ennemis[cible(ennemis)]
            i.attaque(a)
        if not a.estEnVie():
            ennemis.remove(a)
        

def tourTroll(mechant, hero): #attaquer les heros
    for i in mechant:
        i.attaque(hero)






'''
def combat(attaquant,ennemi):
    while listeCombattants != [] and vagueTroll != []:
        tourHeros(attaquant, ennemi)
        tourTroll(attaquant,ennemi)
'''


demoCombat(listeCombattantsDemo,vagueTroll)