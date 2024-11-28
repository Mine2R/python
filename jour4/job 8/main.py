def string(type,saison):
    if type == "fruits" and saison == "hiver":
        return "Orange,mandarine et kiwi"
    elif type == "fruits" and saison == "été":
        return "Poire, fraise, cassis"
    elif type == "légume" and saison == "hiver":
        return "Carotte, topinambour, endive"
    elif type == "légume" and saison == "été":
        return "Artichaut,aubergine,navet"
print(string("fruits","été"))