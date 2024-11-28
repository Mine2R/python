def calcule(num1,operator,num2):
    if operator == "+":
        resultat=num1 + num2
    elif operator == "-":
        resultat=num1 - num2
    elif operator == "*":  
        resultat=num1 * num2
    elif operator == "/":
        if num2 == 0:
            return " Erreur : division par zéro"
        resultat=num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Erreur : division par zéro"
        resultat=num1 % num2
    else: 
        return "opérateur invalide"   
    return resultat 
print(calcule(5,"*", 2))

