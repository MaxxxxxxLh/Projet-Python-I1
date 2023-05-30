def choixPersonnage(compteur, listeAttaquant):
    for i in range(len(listeAttaquant)):
        if compteur == i%len(listeAttaquant) :
            compteur += 1
            return listeAttaquant[i]
    