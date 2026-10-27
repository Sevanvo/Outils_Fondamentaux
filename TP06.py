import math
import random
import matplotlib.pyplot as plt

#Ex1.1

##A = (1, 2)
##B = (4, 6)
##AB = (B[0] - A[0], B[1] - A[1])
##print(AB)

def vecteur(a,b):
    return b[0] - a[0], b[1] - a[1]

def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]

def norme(u):
    return math.sqrt(u[0] ** 2 + u[1] ** 2)

def angle(u, v):
    ps = produit_scalaire(u, v)
    n1 = norme(u)
    n2 = norme(v)
    cosinus = ps / (n1 * n2)
    if cosinus > 1:
        cosinus = 1
    if cosinus < -1:
        cosinus = -1
    angle_radians = math.acos(cosinus)
    return math.degrees(angle_radians)

##print(norme((3, 4)))
##print(produit_scalaire((1, 2), (3, 4)))
##print(angle((1, 0), (1, 1)))
##print(angle((1, 0), (0, 1)))

# Ex1.2

def determinant(u, v):
    x = u[0] * v[1]
    y = u[1] * v[0]
    return x - y

def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    det = determinant(AB, AP)
    longueur = norme(AB)
    return abs(det) / longueur

##print(distance_point_droite((0, 0), (0, 1), (1, 0)), math.sqrt(2) / 2)
##print(distance_point_droite((3, 4), (0, 0), (1, 0)))
##
###Bonus
##print(determinant((1, 0), (0, 1)))
##print(determinant((0, 1), (1, 0)))
##print(determinant((2, 4), (1, 2)))
##
##print(distance_point_droite((2, 3), (0, 0), (4, 0)))
##print(distance_point_droite((2, 0), (0, 0), (4, 0)))
##print(distance_point_droite((0, 2), (0, 0), (0, 4)))

# Ex 2.1

def orientation(A, B, C):
    AB = vecteur(A, B)
    AC = vecteur(A, C)
    d = determinant(AB, AC)
    if d > 0:
        return 1
    if d < 0:
        return -1
    return 0

##print(orientation((0, 0), (1, 0), (1, 1)))
##print(orientation((0, 0), (1, 0), (1, -1)))
##print(orientation((0, 0), (1, 1), (2, 2)))
##
###Bonus
##print(orientation((0, 0), (2, 0), (1, 3)))
##print(orientation((0, 0), (2, 0), (1, -3)))
##print(orientation((1, 1), (3, 3), (5, 5)))
##print(orientation((2, 2), (2, 2), (4, 5)))

# Ex2.2
def aire(polygone):
    somme = 0
    n = len(polygone)
    for i in range(n):
        x1 = polygone[i][0]
        y1 = polygone[i][1]
        j = (i + 1) % n
        x2 = polygone[j][0]
        y2 = polygone[j][1]
        somme = somme + (x1 * y2 - x2 * y1)
    return abs(somme) / 2


carre = [(0, 0), (1, 0), (1, 1), (0, 1)]
triangle = [(0, 0), (4, 0), (0, 3)]
maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]
##
##print(aire(carre))
##print(aire(triangle))
##print(aire(maison))
##
### Bonus
##rectangle = [(0, 0), (4, 0), (4, 2), (0, 2)]
##print(aire(rectangle))
##
##triangle2 = [(0, 0), (2, 0), (1, 3)]
##print(aire(triangle2))

# Ex3.1

def se_coupent(A, B, C, D):
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    return False

##print(se_coupent((0, 0), (1, 1), (0, 1), (1, 0)))
##print(se_coupent((0, 0), (1, 0), (0, 1), (1, 1)))
##print(se_coupent((0, 0), (1, 1), (2, 2), (3, 3)))
##
### Bonus
##print(se_coupent((0, 0), (4, 4), (0, 4), (4, 0)))
##print(se_coupent((0, 0), (2, 0), (3, 1), (3, 3)))
##print(se_coupent((0, 0), (2, 2), (1, 1), (3, 0)))

# Ex3.2

def intersection(A, B, C, D):
    AB = vecteur(A, B)
    CD = vecteur(C, D)
    denominateur = determinant(AB, CD)
    if denominateur == 0:
        return None
    AC = vecteur(A, C)
    t = determinant(AC, CD) / denominateur
    u = determinant(AC, AB) / denominateur
    if 0 <= t <= 1 and 0 <= u <= 1:
        x = A[0] + t * AB[0]
        y = A[1] + t * AB[1]
        return (x, y)
    return None

##print(intersection((0, 0), (2, 2), (0, 2), (2, 0)))
##print(intersection((0, 0), (1, 0), (0, 1), (1, 1)))
##print(intersection((0, 0), (1, 1), (2, 2), (3, 3)))
##
### Bonus
##print(intersection((0, 0), (4, 4), (0, 4), (4, 0)))
##print(intersection((0, 0), (2, 0), (1, -1), (1, 1)))
##print(intersection((0, 0), (1, 0), (2, -1), (2, 1)))


# Ex4.1
def dedans(P, polygone):
    """Vrai si P est à l'intérieur du polygone, par lancer de rayon horizontal."""
    x, y = P
    n = len(polygone)
    interieur = False
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            x_croisement = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_croisement:
                interieur = not interieur
    return interieur


# Tests de l'énoncé
for P in ((1, 1), (1, 2.4), (3, 1), (0.2, 2.2)):
    print(P, dedans(P, maison))


# Bonus
rectangle = [(0, 0), (4, 0), (4, 3), (0, 3)]

##print(dedans((2, 1), rectangle))
##print(dedans((5, 1), rectangle))
##print(dedans((-1, 1), rectangle))
##print(dedans((2, 4), rectangle))

# Ex4.2

random.seed(0)
tirages = 200000
touches = 0

for k in range(tirages):
    P = (random.uniform(0, 2), random.uniform(0, 2.5))
    if dedans(P, maison):
        touches += 1

aire_rectangle = 2 * 2.5
aire_estimee = aire_rectangle * touches / tirages

##print("Aire estimee par Monte-Carlo :", aire_estimee)
# Ex5

def tracer_polygone(polygone, points=()):
    xs = [s[0] for s in polygone] + [polygone[0][0]]
    ys = [s[1] for s in polygone] + [polygone[0][1]]
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, color="black")
    for P in points:
        couleur = "green" if dedans(P, polygone) else "red"
        plt.scatter([P[0]], [P[1]], color=couleur)
    plt.axis("equal")
    plt.title("Vert : dedans, rouge : dehors")
    plt.show()

##random.seed(1)
##nuage = [(random.uniform(-0.5, 2.5), random.uniform(-0.5, 3)) for _ in range(60)]
##tracer_polygone(maison, nuage)

# Ex5.1

etoile = []

for k in range(10):
    if k % 2 == 0:
        rayon = 2
    else:
        rayon = 0.8
    theta = math.pi / 2 + k * math.pi / 5
    x = rayon * math.cos(theta)
    y = rayon * math.sin(theta)
    etoile.append((x, y))

##print(round(aire(etoile), 4))
##print(dedans((0, 0), etoile), dedans((0, 1.5), etoile), dedans((1.2, 1.2), etoile))
##tracer_polygone(etoile, [(0, 0), (0, 1.5), (1.2, 1.2), (0, 1.9)])

# Ex6.1
def zone_de(P, zones):
    for i, zone in enumerate(zones):
        if dedans(P, zone):
            return i
    return None

zones = [
    maison,
    [(3, 0), (4, 0), (4, 1), (3, 1)]
]

for P in ((1, 1), (3.5, 0.5), (2.5, 0.5)):
    print(P, zone_de(P, zones))

# Bonus
print("Point dans la maison :", zone_de((0.5, 1), zones))
print("Point dans le rectangle :", zone_de((3.8, 0.2), zones))
print("Point loin des zones :", zone_de((6, 6), zones))
print("Point entre les deux zones :", zone_de((2.5, 0.5), zones))

# Pour aller plus loin


import random

def enveloppe(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    inferieure = []
    for P in points:
        while len(inferieure) >= 2 and orientation(
            inferieure[-2], inferieure[-1], P
        ) <= 0:
            inferieure.pop()
        inferieure.append(P)
    superieure = []
    for P in reversed(points):
        while len(superieure) >= 2 and orientation(
            superieure[-2], superieure[-1], P
        ) <= 0:
            superieure.pop()
        superieure.append(P)
    return inferieure[:-1] + superieure[:-1]


carre = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
resultat = enveloppe(carre)
##print("Enveloppe du carre :", resultat)
##print("Nombre de sommets :", len(resultat))
##
##
##alignes = [(0, 0), (1, 1), (2, 2), (3, 3)]
##print("Enveloppe des points alignes :", enveloppe(alignes))

# L'IA vous le donne en 3 secondes

# Chat GPT :
def dedans(P, polygone):
    x, y = P
    interieur = False

    for i in range(len(polygone)):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % len(polygone)]

        # Le segment encadre-t-il la hauteur du point ?
        if (y1 > y) != (y2 > y):
            x_croisement = x1 + (y - y1) * (x2 - x1) / (y2 - y1)

            print("Segment :", (x1, y1), (x2, y2))
            print("Croisement avec le rayon :", x_croisement)

            if x < x_croisement:
                interieur = not interieur
                print("Nombre de croisements : impair / pair alterne")
            else:
                print("Croisement situe a gauche du point")

    return interieur


maison = [(0, 0), (2, 0), (2, 2), (1, 3), (0, 2)]

print("Test a la hauteur du sommet :")
print("Resultat :", dedans((1, 1.5), maison))

print("\nTest sur le cote inferieur :")
print("Resultat :", dedans((1, 0), maison))



