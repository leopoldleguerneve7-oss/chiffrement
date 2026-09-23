## Q3 - Différence hachage / chiffrement
Le hachage transforme une donnée en une empreinte de taille fixe, de façon irréversible.
Le chiffrement transforme une donnée en une version illisible, mais réversible avec la bonne clé.

## Q4 - But du hachage
Intégrité : vérifier qu'une donnée n'a pas été modifiée.

## Q5 - Commande de hash SHA256
- Windows (PowerShell) : Get-FileHash fichier.txt -Algorithm SHA256
- Linux : sha256sum fichier.txt


## Q6 - Génération Doxygen + calcul et vérification des hash

Le programme test_hash.py utilise la classe HashGestion pour :
- Calculer le hash SHA256 d'une chaîne de caractères
- Calculer le hash SHA256 d'un fichier texte (test.txt)
- Calculer le hash SHA256 d'un fichier binaire (test.bin)

Chaque hash a été vérifié en le comparant à celui obtenu via CyberChef
(recipe SHA2, taille 256, 64 rounds), en utilisant l'option "Open file"
pour charger les fichiers directement. Les résultats sont identiques
(voir captures d'écran en annexe).


## Q7 - But de l'AES
Confidentialité : rendre les données illisibles sans la clé.

## Q8 - Pourquoi "comme son nom l'indique" AesGestion permet de chiffrer
La classe encapsule l'algorithme AES (Advanced Encryption Standard), un chiffrement
symétrique par blocs. Son nom indique directement l'algorithme utilisé pour chiffrer
et déchiffrer les données avec une même clé secrète.

## Q9 - Caractéristiques de l'AES
- Algorithme symétrique (une seule clé partagée pour chiffrer et déchiffrer)
- Chiffrement par blocs de 128 bits
- Tailles de clé possibles : 128, 192 ou 256 bits (ici 256 bits utilisés)
- Très rapide, adapté aux gros volumes de données
- Nécessite un mode opératoire (ici CBC) et un vecteur d'initialisation (IV)

## Q10 - Autre grande famille d'algorithmes
Le chiffrement asymétrique (à clé publique).

## Q11 - Exemple d'algorithme asymétrique
RSA


## Q12 - Quel est le but du chiffrement 

Confidentialité 
