investissement = 10000
rendement_annuel = 0.06
gain_annuel = investissement*rendement_annuel

print(f"{gain_annuel}€")

ajout_capital = 5000
nouveau_taux = rendement_annuel + 0.02
nouveau_capital = investissement+ajout_capital
nouveau_gain = nouveau_capital*nouveau_taux

print(f"{nouveau_gain}€")

retrait = (investissement+ajout_capital)*0.10 
montant_final = nouveau_capital-retrait
print(f"{montant_final}€")


chaine = input("Entrez une chaîne : ")

if 'e' in chaine:
    print("Oui, la chaîne contient le caractère 'e'.")
else:
    print("Non, la chaîne ne contient pas le caractère 'e'.")





