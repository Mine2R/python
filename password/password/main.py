import hashlib

def verification_mot_de_passe(mot_de_passe):
    """Vérifie si un mot de passe respecte les règles définies."""
    if len(mot_de_passe) < 8:
        print("Le mot de passe doit avoir 8 caractères minimum.")
        return False
    if not any(c.isupper() for c in mot_de_passe):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        return False
    if not any(c.islower() for c in mot_de_passe):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        return False
    if not any(c.isdigit() for c in mot_de_passe):
        print("Le mot de passe doit contenir au moins un chiffre.")
        return False
    caractere_special = "!@#$%^&*()_+[]|;:,.<>?/~"
    if not any(c in caractere_special for c in mot_de_passe):
        print("le Mot de passe doit contenir au moins un caractère spècial")
        return False
    return True

mot_de_passe=input("Veuillez saisir un mot de passe : ")
while not verification_mot_de_passe(mot_de_passe):
    mot_de_passe = input("Le mot de passe est invalide veuillez saisir un mot de passe : ")

if verification_mot_de_passe(mot_de_passe):
    print("mot de passe valide") 


def hacher_mot_de_passe(mot_de_passe):
    """Hache le mot de passe en utilisant SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(mot_de_passe.encode('utf-8'))
    return sha256.hexdigest()


mot_de_passe = input("Veuillez saisir un mot de passe : ")

while not verification_mot_de_passe(mot_de_passe):
    mot_de_passe = input("Le mot de passe est invalide, veuillez réessayer : ")

hash_mot_de_passe = hacher_mot_de_passe(mot_de_passe)
print("\nMot de passe valide !")
print("Hash SHA-256 du mot de passe :", hash_mot_de_passe)




