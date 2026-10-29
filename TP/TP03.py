import time
import math
import matplotlib.pyplot as plt
#TP03


#Ex1.1
def evaluer_naif(P,x):
    px = 0
    k  = 0
    while k<len(P):
        px +=  P[k] *x **k
        k += 1
    return px

L = [2,3,0,5]

##print(evaluer_naif(L,2))
##print(evaluer_naif(L,0))
##
### Bonus
##print(evaluer_naif([1, 2], 3))
##print(evaluer_naif([4], 5))


#Ex2.1
def evaluer(P, x):
    total = 0
    i = len(P) - 1
    while i >= 0:
        total = total * x + P[i]
        i -= 1
    return total

P = [2, 3, 0, 5]

##print(evaluer_naif(L,2),evaluer(L,2))
##for x in (-2, 0, 1, 2, 10):
##    print(x, evaluer_naif(P, x), evaluer(P, x))
##
### Bonus
##print(evaluer([1, 2], 3))
##print(evaluer([4], 5))
##print(evaluer([1, 0, 1], 2))

#Ex2.2

def duree(fonction, arg1,arg2):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(arg1,arg2)
    return time.perf_counter() - debut

##for degre in (1000, 5000, 20000):
##    P = [1] * (degre + 1)
##    a = evaluer_naif(P, 1.0001)
##    b = evaluer(P, 1.0001)
##    t_naif = duree(evaluer_naif, P, 1.0001)
##    t_horner = duree(evaluer, P, 1.0001)
##    print("Degré :", degre)
##    print("Temps naïf :", t_naif)
##    print("Temps Horner :", t_horner)
##    print("Écart :", abs(a - b))

#Ex2.3

##for degre in (200, 400, 800):
##    P = [1] * (degre + 1)
##    a = evaluer_naif(P, 3)
##    b = evaluer(P, 3)
##    t_naif = duree(evaluer_naif, P, 3)
##    t_horner = duree(evaluer, P,3)
##    print("Degré :", degre)
##    print("Temps naïf :", t_naif)
##    print("Temps Horner :", t_horner)
##    print("Écart :", abs(a - b))

# L'IA vous le donne en 3 secondes 
L’IA m’a proposé une méthode naïve utilisant x ** i, puis une méthode de Horner, qui évite de recalculer plusieurs puissances de (x). J’ai appris que Horner peut être plus efficace, mais que le gain réel en Python doit être mesuré sur un polynôme de degré 20 000. Je retiens qu’il faut comparer les temps d’exécution plutôt que de se fier uniquement aux affirmations de l’IA.
#Ex3.1

def deriver(p):
    L = []
    for k in range(1,len(p)):
        L.append(p[k]*k)
    return L

##print(deriver([2, 3, 0, 5]))
##print(deriver([7]))

#Ex4.1
def dichotomie(f,a,b,tolerance):
    f_a = f(a)
    f_b = f(b)
    if f_a == 0 :
        return a
    elif f_b == 0:
        return b
    elif f_a * f_b > 0:
        print("Erreur, f(a) et f(b) doivent être de signes contraires")
        return
    while b - a > tolerance:
        centre = (a+b)/2
        if f(a)*f(centre) <= 0:
            b =centre
        else :
            a = centre
    return (a+b) / 2



def carre_moins_deux(x):
    return x * x - 2

##racine = dichotomie(carre_moins_deux, 0, 2, 1e-12)
##print(racine)
##print(abs(racine - 2 ** 0.5) < 1e-9)


#Ex4.2
def newton(P, depart, tolerance):
    derivee = deriver(P)
    for cp in range(100):
        val = evaluer(P, depart)
        pente = evaluer(derivee, depart)
        if pente == 0 :
            print("Tangente horizontale")
            return
        suivant = depart - val / pente
        print(suivant)
        if abs(suivant - depart) <= tolerance * max(1.0, abs(suivant)):
            return suivant, cp + 1
        depart = suivant
    print("Pas de convergence ")
    return

Q = [-5, -2, 0, 1]
##racine, tours = newton(Q, 2, 1e-12)
##print(racine, "en", tours, "tours")
##print(abs(evaluer(Q, racine)) < 1e-10)

#Ex4.3
##print(newton([2,-2,0,1],0, 1e-12))
##print(newton([-5,-2,0,1], math.sqrt(2/3), 1e-12))

#Ex4.4
##print(newton([-5,-2,0,1], 2, 1e-12))
##print(newton([-5,-2,0,1], 0, 1e-12))

#Ex5.1.
Q = [-5, -2, 0, 1]          # x^3 - 2x - 5
xs = [i / 100 for i in range(-300, 301)]
ys = [evaluer(Q, x) for x in xs]

##plt.figure()
##plt.plot(xs, ys, label="x^3 - 2x - 5")
##plt.axhline(0, linewidth=0.8)
##plt.axvline(0, linewidth=0.8)
##plt.ylim(-20, 20)
##plt.xlabel("x")
##plt.ylabel("P(x)")
##plt.legend()
##plt.title("Un polynome et son unique racine reelle")
##plt.show()

# Pour aller plus loin

def newton_trace(P, depart, tolerance):
    iterees = [depart]
    derivee = deriver(P)
    for cp in range(100):
        val = evaluer(P, depart)
        pente = evaluer(derivee, depart)
        if pente == 0 :
            print("Tangente horizontale")
            return
        suivant = depart - val / pente
        iterees.append(suivant)
        if abs(suivant - depart) <= tolerance * max(1.0, abs(suivant)):
            return iterees
        depart = suivant
    print("Pas de convergence ")
    return

##
##Q = [-5, -2, 0, 1]
##P = [2, -2, 0, 1]
##
##iteres1 = newton_trace(Q, 2, 1e-12)
##iteres2 = newton_trace(P, 0, 1e-12)
##
##plt.plot(iteres1, "o")
##plt.plot(iteres2, "o")
##plt.ylabel("Valeur de x")
##plt.axhline(0, linewidth=0.8)
##plt.axvline(0, linewidth=0.8)
##plt.ylim(-20, 20)
##plt.xlabel("x")
##plt.ylabel("P(x)")
##plt.grid()
##plt.legend()
##plt.show()

#Ex6.1

def somme(P,Q):
    longueur = max(len(P),len(Q))
    P  += [0]*(longueur - len(P))
    Q += [0]* (longueur - len(Q))
    for i in range(longueur):
        P[i] += Q[i]
    return P

def produit_poly(P, Q):
    if not P or not Q:
        return []
    produit =[0]*(len(P)+len(Q)-1)
    for i in range(len(P)):
        for j in range(len(Q)):
            produit[i + j] +=  P[i] * Q[j]
    return produit

##print(somme([1, 2], [0, 0, 3]))
##print(produit_poly([1, 1], [1, 1]))
##print(produit_poly([-1, 1], [1, 1]))

# Bonus
##print(somme([2, 3], [4]))
##print(produit_poly([2], [3, 4]))

P = [1, 2]
Q = [3, 4]
x = 2

R = produit_poly(P, Q)

##print("Produit :", R)
##print("Longueur attendue :", len(P) + len(Q) - 1)
##print("Longueur obtenue :", len(R))
##
##print("Évaluation du produit :", evaluer(R, x))
##print("Produit des évaluations :", evaluer(P, x) * evaluer(Q, x))
##
##print(evaluer(R, x) == evaluer(P, x) * evaluer(Q, x))

#Ex6.2
##liste = [1]
##for k in range(10):
##    liste = produit_poly(liste,[1, 1])
##print (liste)

#Ex7.1
def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h

def derivee_centree(f, x, h):
    return (f(x + h) - f(x)) / (2*h)
exacte = math.cos(1.0)
for h in (1e-1, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
    e_avant = abs(derivee_avant(math.sin, 1.0, h) - exacte)
    e_centree = abs(derivee_centree(math.sin, 1.0, h) - exacte)
    print(f"h = {h:.0e} : avant {e_avant:.1e} | centree {e_centree:.1e}")

#Ex8.1
def rectangles(f, a, b, n):
    h = (b - a) / n
    total = 0
    i = 0
    while i < n:
        total += f(a + i * h)
        i += 1
    return total * h

def trapezes(f, a, b, n):
    h = (b - a) / n
    interieur = sum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + interieur)

def simpson(f, a, b, n):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            total += 2 * f(a + i * h)
        else:
            total += 4 * f(a + i * h)
    return total * h / 3

def carre(x):
    return x * x


def arctangente_derivee(x):
    return 4 / (1 + x * x)

for n in (10, 100, 1000):
    e_rect = abs(rectangles(carre, 0, 1, n) - 1 / 3)
    e_trap = abs(trapezes(carre, 0, 1, n) - 1 / 3)
    e_simp = abs(simpson(carre, 0, 1, n) - 1 / 3)
    print(f"n = {n:>4} : rectangles {e_rect:.1e} | trapezes {e_trap:.1e} | simpson {e_simp:.1e}")

approx_trap = trapezes(arctangente_derivee, 0, 1, 1000)
approx_simp = simpson(arctangente_derivee, 0, 1, 1000)
print(approx_trap, abs(approx_trap - math.pi))
print(approx_simp, abs(approx_simp - math.pi))
