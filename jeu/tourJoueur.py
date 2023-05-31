def choixPersonnage(compteur, listeAttaquant):
    for i in range(len(listeAttaquant)):
        if i == compteur%len(listeAttaquant) :
            return listeAttaquant[i]
    