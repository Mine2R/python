for N in range (1, 13):
    if N ==1:
        precedent=0
        resultat = precedent + 2
    else:
        precedent=resultat
        resultat=precedent+2
    print(f"Tour {N} : {resultat}")
    