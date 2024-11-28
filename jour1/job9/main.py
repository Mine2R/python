
nom ="chocolat"
prix_unitaire= 2
quantité_en_stock= 20

print(f"nom du produit:{nom}")
print(f"prix unitaire:{prix_unitaire}€")
print("quantité en stock :",quantité_en_stock)
quantité_à_acheter =int(input("quantité du produit : "))
quantité_en_stock-=quantité_à_acheter
print(quantité_en_stock)
print(prix_unitaire*1.10,"€")