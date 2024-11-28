import hashlib
import json

def hacher_mot_de_passe(mot_de_passe):
    """Hache le mot de passe en utilisant SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(mot_de_passe.encode('utf-8'))
    return sha256.hexdigest()

def charger_mots_de_passe():
    """Charge les mots de passe hachés depuis un fichier JSON."""
    try:
        with open("mots_de_passe.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return [] 

def enregistrer_mots_de_passe(mots_de_passe):
    """Enregistre la liste des mots de passe dans un fichier JSON."""
    with open("mots_de_passe.json", "w") as fichier:
        json.dump(mots_de_passe, fichier, indent=4)

def ajouter_mot_de_passe():
    """Ajoute un nouveau mot de passe en vérifiant qu'il n'est pas déjà enregistré."""
    mot_de_passe = input("Veuillez saisir un mot de passe : ")
    mot_de_passe_hache = hacher_mot_de_passe(mot_de_passe)

    mots_de_passe = charger_mots_de_passe()


    if mot_de_passe_hache in mots_de_passe:
        print("Ce mot de passe a déjà été enregistré.")
    else:
        mots_de_passe.append(mot_de_passe_hache)
        enregistrer_mots_de_passe(mots_de_passe)
        print("Mot de passe enregistré avec succès.")

def afficher_mots_de_passe():
    """Affiche tous les mots de passe hachés enregistrés."""
    mots_de_passe = charger_mots_de_passe()
    if mots_de_passe:
        print("Mots de passe enregistrés :")
        for mot_de_passe in mots_de_passe:
            print(mot_de_passe)
    else:
        print("Aucun mot de passe enregistré.")

while True:
    print("\n1. Ajouter un mot de passe")
    print("2. Afficher les mots de passe")
    print("3. Quitter")

    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        ajouter_mot_de_passe()
    elif choix == "2":
        afficher_mots_de_passe()
    elif choix == "3":
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez réessayer.")
