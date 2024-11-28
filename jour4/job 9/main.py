def moyenne(a, b, c):
    return(a + b + c) / 3
note1 = int(input("Saisir une 1ère note de 0 à 20 : "))
note2 = int(input("Saisir une 2ème note de 0 à 20 : "))
note3 = int(input("Saisir une 3ème note de 0 à 20 : "))

moyenne_etudiant = moyenne(note1, note2, note3 )
print(f"moyenne de l'étudiant est de : {moyenne_etudiant : .2f}")
if 15<=moyenne_etudiant<=20:
    print("Très bon élève") 
elif 11<=moyenne_etudiant<14:
    print("Bon élève")
elif 8<=moyenne_etudiant<10:
    print("Elève moyen")
elif 0<=moyenne_etudiant<7:
    print("Elève devant faire des efforts")
else:
    print("Erreur : Les notes données ne sont pas valides")
def saisir_note(nom):
    while True:
        try:
            note = int(input(f"Saisir {nom} (de 0 à 20) : "))
            if 0 <= note <= 20:
                return note
            else:
                print("Erreur : La note doit être entre 0 et 20.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")

note1 = saisir_note("la 1ère note")
note2 = saisir_note("la 2ème note")
note3 = saisir_note("la 3ème note")
