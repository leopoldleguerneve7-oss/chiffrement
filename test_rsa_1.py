from rsagestion import RsaGestion

rsa = RsaGestion()
rsa.generation_clef("public_key.pem", "private_key.pem", 2048)

message = "Bonjour BTS CIEL, test RSA."
message_chiffre = rsa.chiffrement_rsa(message)
print("Message chiffré (base64) :", message_chiffre)

message_dechiffre = rsa.dechiffrement_rsa(message_chiffre)
print("Message déchiffré :", message_dechiffre)

assert message == message_dechiffre
print("Vérification OK.")
