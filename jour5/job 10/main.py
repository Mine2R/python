L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
valeur_min= 25
valeur_max= 90
produit=1
for nombre in L:
    if valeur_min <=nombre>= valeur_max:
        produit*=1
print("Le produit des valeurs dans l intervalle 25 à 90 est de :", produit)
