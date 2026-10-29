from collections import Counter
import unicodedata
import math

#Ex1.1
#print(ord("A"), ord("Z"), chr(72))

def lettre_vers_nombre(c):
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    return chr(n % 26 + ord("A"))

#print(lettre_vers_nombre("C"))
#print(nombre_vers_lettre(2))

# Bonus
##print(lettre_vers_nombre("A"))
##print(lettre_vers_nombre("Z"))
##print(nombre_vers_lettre(0))
##print(nombre_vers_lettre(25))
##print(nombre_vers_lettre(26))
##print(nombre_vers_lettre(27))

#Ex1.2

def nettoyer(texte):
    """Majuscules sans accents, lettres A-Z uniquement."""
    sans_accent = unicodedata.normalize("NFD", texte)
    resultat = ""
    for c in sans_accent:
        if unicodedata.category(c) != "Mn":
            resultat += c
    texte_final = ""
    for c in resultat.upper():
        if "A" <= c <= "Z":
            texte_final += c
    return texte_final

##print(nettoyer("Été, à Paris !"))

#Ex2.1
def chiffrer(texte, a, b):
    mot_chiffre = ""
    for elt in nettoyer(texte):
        mot_chiffre += nombre_vers_lettre(((a * lettre_vers_nombre(elt) + b)%26))
    return mot_chiffre

message = "ATTAQUEALAUBE"
#print(chiffrer(message, 5, 8))
#print(chiffrer(message, 1, 3))

# Bonus
##print(chiffrer("ABC", 1, 0))
##print(chiffrer("ABC", 1, 1))
##print(chiffrer("XYZ", 1, 3))
##print(chiffrer("Été !", 1, 0))

#Ex3.1
def PGCD(a,b):
    while b!=0:
        a, b = b, a%b
    return a

valides = []
for a in range(1, 26):
    if PGCD(a, 26) == 1:
        valides.append(a)

#print(valides)
#print(len(valides), "valeurs possibles pour a")

### Bonus
##print(PGCD(12, 26))
##print(PGCD(13, 26))
##print(PGCD(7, 26))
##print(PGCD(1, 26))


#Ex3.2
def inverse_modulaire(a, n):
    a %= n
    for inverse in range(1, n):
        if (a* inverse)%n == 1 :
            return inverse
    raise ValueError("Le nombre n'est pas inversible modulo n.")

#print(inverse_modulaire(5, 26))
#print((5 * 21) % 26)

try:
    inverse_modulaire(2, 26)
except ValueError as erreur:
    print("Refus de la clé :", erreur)

### Bonus
##print(inverse_modulaire(3, 26))
##print(inverse_modulaire(1, 26))
##print(inverse_modulaire(25, 26))

# L'IA vous le donne en quatre secondes
def chiffrement_affine(texte, a, b):
    """Chiffre un texte en utilisant la formule (a * x + b) % 26."""
    clef_valide = False
    # Vérification que 'a' est premier avec 26
    for i in range(26):
        if (a * i) % 26 == 1:
            clef_valide = True
            break

    if not clef_valide:
        raise ValueError("Le coefficient 'a' doit être premier avec 26.")

    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            # Gestion des majuscules et minuscules
            debut = ord('A') if caractere.isupper() else ord('a')
            # Application de la formule affine
            nouveau_code = (a * (ord(caractere) - debut) + b) % 26
            resultat += chr(nouveau_code + debut)
        else:
            # On laisse les espaces et la ponctuation intacts
            resultat += caractere
    return resultat

def dechiffrement_affine(texte, a, b):
    """Déchiffre un texte en trouvant l'inverse modulaire de 'a'."""
    # Recherche de l'inverse de 'a' modulo 26
    a_inverse = -1
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    if a_inverse == -1:
        raise ValueError("Le coefficient 'a' n'a pas d'inverse modulo 26.")

    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            debut = ord('A') if caractere.isupper() else ord('a')
            # Application de la formule inverse : a^-1 * (y - b) % 26
            nouveau_code = (a_inverse * ((ord(caractere) - debut) - b)) % 26
            resultat += chr(nouveau_code + debut)
        else:
            resultat += caractere
    return resultat

# --- TEST DES FONCTIONS ---
message_original = "Bonjour"
cle_a = 5
cle_b = 8

# Exécution
message_chiffre = chiffrement_affine(message_original, cle_a, cle_b)
message_dechiffre = dechiffrement_affine(message_chiffre, cle_a, cle_b)

## Cette version vérifie que le coefficient a possède un inverse modulo 26 avant de chiffrer ou de déchiffrer. Nous avons constaté que cette vérification est nécessaire pour pouvoir retrouver le message initial. Les tests permettent de vérifier que le déchiffrement fonctionne.
# Affichage des résultats
##print(f"Message d'origine : {message_original}")
##print(f"Message chiffré   : {message_chiffre}")
##print(f"Message déchiffré : {message_dechiffre}")

#Ex4
def dechiffrer(texte, a, b):
    inverse = inverse_modulaire(a, 26)
    resultat = []
    texte_final = ""
    for elt in nettoyer(texte):
        nb_lettre = lettre_vers_nombre(elt)
        resultat.append(nombre_vers_lettre(inverse * (nb_lettre - b)%26))
    for elt in resultat :
        texte_final += elt
    return texte_final

message_original = nettoyer("Attaque a l'aube")
message_chiffre = chiffrer(message_original, 5, 8)
message_dechiffre = dechiffrer(message_chiffre, 5, 8)

print("Message original :", message_original)
print("Message chiffre :", message_chiffre)
print("Message dechiffre :", message_dechiffre)
print("Aller-retour reussi :",
      message_original == message_dechiffre)

#Ex 5
def toutes_les_cles(secret):
    result = []
    for a in valides :
        for b in range(26):
            result.append((a, b, dechiffrer(secret, a, b)))
    return result

essais = toutes_les_cles(secret)
##print(len(essais), "cles essayees")
##bons = [e for e in essais if e[2] == message]
##print("la bonne clé :", bons[0][0], bons[0][1])

# Bonus
##print("Nombre de clés possibles :", len(valides) * 26)
##print("Nombre de résultats obtenus :", len(essais))
##for i in range(3):
##    print(essais[i])

#Ex6.1

texte = nettoyer(
    "Le chiffrement affine est un chiffrement par substitution monoalphabetique. "
    "Chaque lettre du message est remplacee par une autre lettre, toujours la meme, "
    "ce qui laisse intactes les frequences relatives des lettres et permet de casser "
    "le code sans essayer toutes les clefs possibles."
)

texte_chiffre = chiffrer(texte, 7, 12)

compteur_lettres = Counter(texte_chiffre)
lettre_la_plus_frequente = compteur_lettres.most_common(1)[0][0]

print("Lettre la plus frequente :", lettre_la_plus_frequente)
print("Nombre d'occurrences :", compteur_lettres[lettre_la_plus_frequente])

numero_lettre_cible = lettre_vers_nombre(lettre_la_plus_frequente)
dechiffrements_possibles = []

for coefficient_a in valides:
    decalage_b = (numero_lettre_cible - 4 * coefficient_a) % 26
    texte_dechiffre = dechiffrer(texte_chiffre, coefficient_a, decalage_b)

    dechiffrements_possibles.append(
        (coefficient_a, decalage_b, texte_dechiffre)
    )

print(len(dechiffrements_possibles), "candidats au lieu de 312")

for coefficient_a, decalage_b, texte_dechiffre in dechiffrements_possibles:
    if texte_dechiffre.startswith("LECHIFFREMENT"):
        print("Cle retrouvee :", coefficient_a, decalage_b)
        print("Debut du message :", texte_dechiffre[:60])

##### Sur un texte court, les fréquences des lettres peuvent être très différentes des fréquences habituelles du français. La lettre la plus fréquente ne correspond donc pas nécessairement à E. L'attaque par fréquences peut alors proposer une mauvaise clé

# Pour aller plus loin
frequences_francaises = {
    "A": 0.081, "B": 0.009, "C": 0.033, "D": 0.037,
    "E": 0.147, "F": 0.011, "G": 0.010, "H": 0.011,
    "I": 0.075, "J": 0.003, "K": 0.001, "L": 0.055,
    "M": 0.030, "N": 0.071, "O": 0.052, "P": 0.030,
    "Q": 0.013, "R": 0.066, "S": 0.079, "T": 0.072,
    "U": 0.063, "V": 0.018, "W": 0.001, "X": 0.004,
    "Y": 0.003, "Z": 0.001
}

def calculer_score(texte):
    """Compare les fréquences du texte à celles du français."""
    nombre_lettres = len(texte)
    if nombre_lettres == 0:
        return 0

    occurrences = Counter(texte)
    score = 0

    for lettre in frequences_francaises:
        frequence_observee = occurrences[lettre] / nombre_lettres
        frequence_attendue = frequences_francaises[lettre]
        score += frequence_observee * frequence_attendue

    return score


def trouver_meilleure_clef(texte_chiffre):
    """Renvoie la clé et le texte ayant le meilleur score."""
    meilleur_score = -1
    meilleure_clef = None
    meilleur_texte = ""
    for coefficient_a in valides:
        for decalage_b in range(26):
            texte_dechiffre = dechiffrer(
                texte_chiffre, coefficient_a, decalage_b
            )
            score = calculer_score(texte_dechiffre)
            if score > meilleur_score:
                meilleur_score = score
                meilleure_clef = (coefficient_a, decalage_b)
                meilleur_texte = texte_dechiffre

    return meilleure_clef, meilleur_texte, meilleur_score


clef_trouvee, texte_retrouve, score_obtenu = trouver_meilleure_clef(texte_chiffre)

##print("Meilleure cle :", clef_trouvee)
##print("Message retrouve :", texte_retrouve[:100])
##print("Score :", round(score_obtenu, 5))

# Ex7.1

import random
from collections import Counter

def indice_coincidence(texte):
    nombre_lettres = len(texte)
    if nombre_lettres < 2:
        return 0.0
    occurrences = Counter(texte)
    somme_coincidences = 0
    for nombre_occurrences in occurrences.values():
        somme_coincidences += nombre_occurrences * (nombre_occurrences - 1)
    return somme_coincidences / (nombre_lettres * (nombre_lettres - 1))

random.seed(1)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
texte_aleatoire = ""

for i in range(len(texte)):
    texte_aleatoire += random.choice(alphabet)

##print("Texte clair   :", round(indice_coincidence(texte), 4))
##print("Texte chiffre :", round(indice_coincidence(texte_chiffre), 4))
##print("Texte aleatoire :", round(indice_coincidence(texte_aleatoire), 4))

# Ex8.1

def vigenere(texte, cle):
    """Chiffre un texte avec la méthode de Vigenère."""
    texte_nettoye = nettoyer(texte)
    cle_nettoyee = nettoyer(cle)
    texte_chiffre = ""
    if len(cle_nettoyee) == 0:
        print("La clé ne peut pas être vide.")
        return
    for position in range(len(texte_nettoye)):
        lettre = texte_nettoye[position]
        lettre_cle = cle_nettoyee[position % len(cle_nettoyee)]
        valeur_lettre = lettre_vers_nombre(lettre)
        decalage = lettre_vers_nombre(lettre_cle)
        nouvelle_lettre = nombre_vers_lettre(valeur_lettre + decalage)
        texte_chiffre += nouvelle_lettre
    return texte_chiffre

secret_vigenere = vigenere(texte, "CLE")

print(secret_vigenere[:40])
print("Indice de coïncidence :", round(
    indice_coincidence(secret_vigenere), 4
))

# Bonus
print(vigenere("ABC", "B"))       # BCD
print(vigenere("BONJOUR", "A"))   # BONJOUR
print(vigenere("", "CLE"))        # Chaîne vide

# Ex8.2

# Recherche de la longueur probable de la clé
for longueur_cle in range(1, 8):
    colonnes = []

    for position in range(longueur_cle):
        colonne = secret_vigenere[position::longueur_cle]
        colonnes.append(colonne)

    somme_indices = 0

    for colonne in colonnes:
        somme_indices += indice_coincidence(colonne)

    indice_moyen = somme_indices / longueur_cle

    print(
        "Longueur :", longueur_cle,
        "| Indice moyen :", round(indice_moyen, 4)
    )

for longueur_cle in [3, 6]:
    colonnes = []
    for position in range(longueur_cle):
        colonnes.append(secret_vigenere[position::longueur_cle])
    somme_indices = 0
    for colonne in colonnes:
        somme_indices += indice_coincidence(colonne)
    indice_moyen = somme_indices / longueur_cle
    print("Vérification pour", longueur_cle,":", round(indice_moyen, 4))
