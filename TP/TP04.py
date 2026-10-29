import random
import time
import numpy as np

A = [[1, 2, 2],
     [1, 3, -2],
     [3, 5, 8]]

##print(A[0])        # la premiere ligne
##print(A[0][2])     # ligne 0, colonne 2
##print(len(A), len(A[0]))   # nombre de lignes, nombre de colonnes

def transposee(A):
    resultat = []
    for j in range(len(A[0])):
        ligne = []
        for i in range(len(A)):
            ligne.append(A[i][j])
        resultat.append(ligne)
    return resultat


##print(transposee([[1, 2, 3], [4, 5, 6]]))

# Bonus
##print(transposee([[1, 2], [3, 4]]))
##print(transposee([[5], [6], [7]]))


#Ex2.1
def produit(A,B):
    L = len(A)
    C = len(A[0])
    if len(B) != C:
        return False
    C_2 = len(B[0])
    produit = [[0]*C_2 for z in range(L)]
    for i in range(L):
        for j in range(C_2):
            somme = 0
            for k in range(C):
                somme += A[i][k] * B[k][j]
            produit[i][j] = somme
    return produit


identite = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
##print(produit(A, identite) == A)
##print(produit([[1, 2], [3, 4]], [[0, 1], [1, 0]]))
##
##print(produit([[2, 3]], [[4], [5]]))
#Ex2.2
random.seed(42)

def matrice_aleatoire(n):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(random.random())
        matrice.append(ligne)
    return matrice

##tailles = [40, 80, 120]
##temps = []
##
##for n in tailles:
##    A = matrice_aleatoire(n)
##    B = matrice_aleatoire(n)
##
##    debut = time.perf_counter()
##    produit(A, B)
##    duree = time.perf_counter() - debut
##
##    temps.append(duree)
##    print("Taille :", n, "| Temps :", round(duree, 4), "secondes")
##
##for i in range(1, len(temps)):
##    rapport = temps[i] / temps[i - 1]
##    print("De", tailles[i - 1], "à", tailles[i],
##          ": temps multiplié par", round(rapport, 2))
#Ex3.1

A = np.array([[1.0, 2.0, 2.0],
              [1.0, 3.0, -2.0],
              [3.0, 5.0, 8.0]])
b = np.array([2.0, -1.0, 8.0])

##print(A.shape)
##print(A.T)
##print(A @ A)
##print(A * A)


mat1 = matrice_aleatoire(120)
mat2 = matrice_aleatoire(120)

##debut = time.perf_counter()
##produit(mat1, mat2)
##final = time.perf_counter() - debut
##print("Tps python : ", final)

#An, Bn = np.array(A), np.array(B)
#debut = time.perf_counter()
#An @ Bn
#tps = time.perf_counter() - debut
#print("Tps numpy : ", tps)

#Ex4.1
##def resoudre(A,b):
##    n = len(A)
##    copie = [list(A[i])+[b[i]] for i in range(n)]
##    for k in range(n):
##        meilleure = max(range(k, n), key=lambda i: abs(copie[i][k]))
##        if abs(copie[meilleure][k]) <= 1e-14:
##            raise ValueError("systeme singulier ou mal pose")
##        copie[k], copie[meilleure] = copie[meilleure], copie[k]
##        for i in range(k + 1, n):
##            facteur = copie[i][k] / copie[k][k]
##            for j in range(k, n + 1):
##                copie[i][j] = copie[i][j] - facteur * copie[k][j]
##
##    x = [0.0] * n
##    for i in range(n - 1, -1, -1):
##        somme = copie[i][n]
##        for j in range(i + 1, n):
##            somme = somme - copie[i][j] * x[j]
##        x[i] = somme / copie[i][i]
##    return x

##A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
##b = [2, -1, 8]
##x = resoudre(A, b)
##print([round(v, 10) for v in x])
##
##verif = [sum(A[i][j] * x[j] for j in range(3)) for i in range(3)]
##print([round(v, 10) for v in verif])

#Ex4.2
##random.seed(7)
##n = 50
##A = matrice_aleatoire(n)
##b = [random.random() for _ in range(n)]
##
##mienne = resoudre(A, b)
##celle_de_numpy = np.linalg.solve(np.array(A), np.array(b))
##
##ecart = max(abs(mienne[i] - celle_de_numpy[i]) for i in range(n))
##print("ecart maximal :", ecart)
##print(ecart < 1e-9)

#Ex5.1

def hilbert(n):
    return np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])

n = 12
H = hilbert(n)
x_vrai = np.ones(n)          # on choisit la solution d'avance
b = H @ x_vrai               # et on fabrique le second membre correspondant

##x_solve = np.linalg.solve(H, b)
##x_inverse = np.linalg.inv(H) @ b

#print("erreur avec solve   :", float(np.max(np.abs(x_solve - x_vrai))))
#print("erreur avec inv @ b :", float(np.max(np.abs(x_inverse - x_vrai))))
#print("conditionnement     : {:.3e}".format(float(np.linalg.cond(H))))

# La solution exacte vaut 1 pour chaque composante. Pourtant, solve commet une erreur d’environ 0,7, contre 21 pour inv, soit une erreur environ 30 fois plus grande. Aucune des deux méthodes ne donne ici un résultat satisfaisant.

# L'IA vous le donne en 3 secondes
##Il utilise np.linalg.solve(A, b), il dit que c'est préférable  car c'est plus rapide, plus efficace et concue pour calculer la solution exacte d'un systeme carré bien passé
##J’ai appris que les deux méthodes peuvent fonctionner, mais que numpy.linalg.solve(A, b) est préférable, car elle est généralement plus efficace et plus stable numériquement. Je retiens qu’il faut poser des questions précises à l’IA pour obtenir les bonnes recommandations et ne pas se contenter de sa première réponse
#Ex6.1
import matplotlib.pyplot as plt

def rotation(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s], [s, c]])

maison = np.array([[0, 0], [2, 0], [2, 1.5], [1, 2.5], [0, 1.5], [0, 0]])

##plt.figure(figsize=(5, 5))
##plt.plot(maison[0], maison[1], label="depart")
##for angle in (np.pi / 6, np.pi / 3, np.pi / 2):
##    image = rotation(angle) @ maison
##    plt.plot(image[0], image[1], label=f"rotation {int(np.degrees(angle))} degres")
##plt.axis("equal")
##plt.legend()
##plt.title("Une matrice fait tourner une figure")
##plt.show()

gauche = rotation(np.pi / 3) @ rotation(np.pi / 6)
droite = rotation(np.pi / 2)
#print(np.allclose(gauche, droite))
#print(np.round(droite, 10))

# Pour aller plus loin
##P = np.array([[0, 2, 1],
##              [0, 0, 2]])
##angle = np.pi / 4
##R = np.array([[np.cos(angle), -np.sin(angle)],
##              [np.sin(angle),  np.cos(angle)]])
##H = np.array([[2, 0],
##              [0, 2]])
##S = np.array([[1, 0],
##              [0, -1]])
##rotation_symetrie = R @ S
##symetrie_rotation = S @ R
##fig, axes = plt.subplots(1, 2, figsize=(10, 5))
##
##axes[0].plot(P[0], P[1], "o-")
##axes[0].plot((rotation_symetrie @ P)[0],
##             (rotation_symetrie @ P)[1], "o-")
##axes[0].set_title("Rotation après symétrie")
##axes[0].grid()
##
##axes[1].plot(P[0], P[1], "o-")
##axes[1].plot((symetrie_rotation @ P)[0],
##             (symetrie_rotation @ P)[1], "o-")
##axes[1].set_title("Symétrie après rotation")
##axes[1].grid()
##
##plt.show()
##
##print("R @ S :")
##print(rotation_symetrie)
##
##print("S @ R :")
##print(symetrie_rotation)

#Ex7.1
def determinant(A):
    n = len(A)
    copie = [list(A[i]) for i in range(n)]
    resultat = 1.0
    for colonne in range(n):
        pivot = colonne
        for ligne in range(colonne + 1, n):
            if abs(copie[ligne][colonne]) > abs(copie[pivot][colonne]):
                pivot = ligne
        if abs(copie[pivot][colonne]) < 1e-14:
            return 0.0
        if pivot != colonne:
            copie[colonne], copie[pivot] = copie[pivot], copie[colonne]
            resultat = -resultat
        resultat *= copie[colonne][colonne]
        for ligne in range(colonne + 1, n):
            facteur = copie[ligne][colonne] / copie[colonne][colonne]
            for j in range(colonne, n):
                copie[ligne][j] -= facteur * copie[colonne][j]
    return resultat

A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
##print(determinant(A), float(np.linalg.det(np.array(A, dtype=float))))
##print(determinant([[1, 2], [2, 4]]))

from fractions import Fraction

def hilbert_exacte(n):
    H = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1, i + j + 1))
        H.append(ligne)
    return H


n = 12
H_exacte = hilbert_exacte(n)
b_exact = []
for ligne in H_exacte:
    b_exact.append(sum(ligne))
##
##try:
##    resoudre(H_exacte, b_exact)
##except ValueError as erreur:
##    print("premier essai :", erreur)

##x_exact = resoudre(H_exacte, b_exact)
##print(x_exact)
##print(all(v == 1 for v in x_exact))

#Ex9.1

def translation(tx, ty):
    return np.array([[1.0, 0.0, tx],
                     [0.0, 1.0, ty],
                     [0.0, 0.0, 1.0]])

def rotation_h(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, 0.0],
                     [s, c, 0.0],
                     [0.0, 0.0, 1.0]])

point = np.array([1.0, 0.0, 1.0])
T = translation(3, 1)
R = rotation_h(np.pi / 2)
##
##print(np.round(R @ T @ point, 10))
##print(np.round(T @ R @ point, 10))

# Bonus

point2 = np.array([2.0, 2.0, 1.0])
T2 = translation(1, -2)
R2 = rotation_h(np.pi)

print(np.round(T2 @ point2, 10))

print(np.round(R2 @ point2, 10))

s
print(np.round(R2 @ T2 @ point2, 10))
print(np.round(T2 @ R2 @ point2, 10))
