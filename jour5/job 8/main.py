L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme=0
for nombre in L:
    if nombre % 2 == 0:
        somme += nombre
print("La somme de tous les nombre pair =",somme)
