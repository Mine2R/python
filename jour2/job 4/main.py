N = int(input("Choisir un nombre entier supérieur à zéro : "))
print(f"table de multiplication {N}:")
for nombre in range (1, N+1):
    for i in range (1,11):    
        print(f"{i}x{nombre}={i*nombre}")

