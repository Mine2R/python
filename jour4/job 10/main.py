def verifier_nombre(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        return "Erreur : le nombre doit être un entier positif."
    if nombre % 2 == 0:
        return f"{nombre} est pair."
    else:
        return f"{nombre} est impair."
valeurs = [5, -3, 12, 0, 7.5, 20]
for valeur in valeurs:
    print(verifier_nombre(valeur))



