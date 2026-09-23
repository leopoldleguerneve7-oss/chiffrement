from aesgestion import AesGestion

aes = AesGestion()

# Génère une paire de clefs (ici clé symétrique AES)
aes.generate_aes_key()
print("Clé AES générée (256 bits).")

# Chiffre un message de type string
message = "Bonjour BTS CIEL, ceci est un test AES."
message_chiffre = aes.encrypt_string_to_base64(message)
print("Message chiffré (base64) :", message_chiffre)

# Déchiffre le message sur le même PC
message_dechiffre = aes.decrypt_string_from_base64(message_chiffre)
print("Message déchiffré :", message_dechiffre)

assert message == message_dechiffre
print("Vérification OK : le message déchiffré correspond à l'original.")
