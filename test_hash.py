from hashgestion import HashGestion

h = HashGestion()

# Hash d'une chaîne de caractères
resultat_string = h.calculate_sha256("Bonjour BTS CIEL")
print("Hash de la chaîne :", resultat_string)

# Hash d'un fichier texte
resultat_texte = h.calculate_file_sha256("test.txt")
print("Hash fichier texte :", resultat_texte)

# Hash d'un fichier binaire
resultat_binaire = h.calculate_file_sha256("test.bin")
print("Hash fichier binaire :", resultat_binaire)
