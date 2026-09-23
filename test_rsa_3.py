from rsagestion import RsaGestion

rsa = RsaGestion()
rsa.chargement_clef_privee("private_key.pem")

message = rsa.dechiffre_fichier("message_chiffre.txt")
print("Message déchiffré sur un autre PC :", message)
