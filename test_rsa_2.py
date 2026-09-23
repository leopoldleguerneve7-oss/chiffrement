from rsagestion import RsaGestion

rsa = RsaGestion()
rsa.chargement_clefs("public_key.pem", "private_key.pem")

rsa.chiffre_dans_fichier("Message secret RSA", "message_chiffre.txt")

message = rsa.dechiffre_fichier("message_chiffre.txt")
print("Message déchiffré :", message)
