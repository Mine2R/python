def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez entrer un entier positif représentant les minutes.")
        return
    heures = minutes // 60
    reste_minutes = minutes % 60
    heures_texte = f"{heures} heure{'s' if heures > 1 else ''}" if heures > 0 else ""
    minutes_texte = f"{reste_minutes} minute{'s' if reste_minutes > 1 else ''}" if reste_minutes > 0 else ""
    if heures_texte and minutes_texte:
        result = f"{heures_texte} et {minutes_texte}"
    else:
        result = heures_texte or minutes_texte  
    print(result)
time_to_text(160) 
time_to_text(150)  
