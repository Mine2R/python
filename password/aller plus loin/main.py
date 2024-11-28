import hashlib
mot_de_passe = input("Veuillez saisir un mot de passe : ")
hash_object = hashlib.sha256()
hash_object.update(mot_de_passe.encode())
mot_de_passe_hache = hash_object.hexdigest()
print(f"Le mot de passe haché (SHA-256) est : {mot_de_passe_hache}")
