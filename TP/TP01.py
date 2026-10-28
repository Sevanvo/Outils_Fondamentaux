#https://cours.gclab.fr/outils-fondamentaux/tp1-calcul-numerique/#etape-5-une-vraie-methode-numerique-heron-20-min
# print(2026//7, 2026%7)

import math
from fractions import Fraction
import sys

##print(2**10)
##print(2**200)

#Ex1.1

quotient = 2026 // 7
reste = 2026 % 7
##print(quotient, reste)
##print(quotient * 7 + reste == 2026)

#Ex1.2
nombre_teste = 123456789
##print(nombre_teste % 10)
##print(nombre_teste // 10)

# print(0.1 + 0.2)

a = 0.1 + 0.2
b = 0.3
##print(abs(a - b) < 1e-9)
##print(math.isclose(a, b))

#Ex2.1
resultat = 0.0
for k in range(1000):
    resultat = resultat +0.1
# print(resultat)
# print(resultat-100)

#Ex2.2
def presque_egaux(a, b):
    absolu = abs(a - b)
    if absolu <= 1e-9 :
        print (True)
    else :
        print(False)

##print(presque_egaux(0.1 + 0.2, 0.3))
##print(presque_egaux(1.0, 1.5))
##
###Bonus
##print(presque_egaux(2.000000001, 2.0))
##print(presque_egaux(5.0, 5.0001))
##print(presque_egaux(-3.0, -3.0))

#L'IA vous le donne en 3 seconde
##En testant cette fonction, nous constatons qu’une tolérance fixe de 1e-9 est mal adaptée aux nombres de l’ordre de 1e20. En effet, cette tolérance est extrêmement petite par rapport à ces nombres. Deux nombres peuvent donc être très proches relativement à leur taille, mais être considérés comme différents par la fonction.
##
##Il faut adapter la tolérance à l’ordre de grandeur des nombres comparés. Une tolérance relative, comme celle utilisée par math.isclose, est souvent plus adaptée qu’une tolérance fixe.


##n = 17
##if n % 2 == 0:
##    print("pair")
##else:
##    print("impair")

##for i in range(1, 6):
##    print(i, i * i)

##n = 1
##while n * n < 1000:
##    n = n + 1
##    print(n)

#Ex3.1
#for i in range(1, 11):
#    print(7, "x", i, "=", 7 * i)

#Ex3.2
total = 0
for k in range(101):
    total += k
#print (total)
#print (100*(100+1)//2)

def celsius_vers_fahrenheit(c):
    """Convertit une température de degrés Celsius en degrés Fahrenheit."""
    return c * 9 / 5 + 32

##print(celsius_vers_fahrenheit(100))
##print(celsius_vers_fahrenheit(-40))

#Ex4.1

def nombre_de_chiffres(n):
    cp = 1
    while n >= 10:
        n = n // 10
        cp += 1
    return cp

##print(nombre_de_chiffres(2026))
##print(nombre_de_chiffres(7))
##print(nombre_de_chiffres(10 ** 60))

### Bonus
##print(nombre_de_chiffres(0))
##print(nombre_de_chiffres(10))
##print(nombre_de_chiffres(999))
##print(nombre_de_chiffres(1000))
##print(nombre_de_chiffres(123456789))

#Ex5.1
def heron(a):
    if a<0 :
        print("Impossible")
        return
    elif a == 0 :
        return 0.0
    x = float(a)
    tours = 0
    while True:
        suivant = (x + a / x)/2
        tours += 1
        if abs(suivant - x) <= 1e-12 * abs(suivant):
            return suivant,tours
        x = suivant

##print(heron(2))
##print(math.sqrt(2))
##print(abs(heron(2) - math.sqrt(2)) < 1e-12)

###Bonus
##print(heron(9), math.sqrt(9))
##print(heron(25), math.sqrt(25))
##print(heron(0))

# Pour aller plus loin

##print(heron(2))
##print(heron(1e6))
##print(heron(1e30))

#print(bin(37))
#print(int("100101", 2))
#print(Fraction(0.1))

#Ex6.1
def vers_binaire(n):
    binaire = ""
    if n== 0:
        return "0"
    while (n!=0):
        if n%2 == 0 :
            binaire = "0" + binaire
        else :
            binaire = "1" + binaire
        n = n//2
    return binaire


##print(vers_binaire(37), vers_binaire(0), vers_binaire(1024))
##print(all(vers_binaire(n) == bin(n)[2:] for n in range(2000)))


###Bonus
##print(vers_binaire(1))
##print(vers_binaire(8))
##print(vers_binaire(15))
##print(vers_binaire(255))

#Ex6.2
epsilon = 1.0
while 1.0+epsilon *0.5 != 1.0 :
    epsilon /= 2

##print(epsilon)
##print(sys.float_info.epsilon)
##print(epsilon == 2 ** -52)

#Ex7.1
def racines_naif(a,b,c):
    delta = b **2 - 4 * a * c
    if delta < 0:
        print("pas de racine réelle")
        return
    racine = math.sqrt(delta)
    x1 = (-b - racine) / (2 * a)
    x2 = (-b + racine) / (2 * a)
    return x1, x2

petite, grande = racines_naif(1.0, -1e8, 1.0)
##print(petite, grande)
##print("Produit :", petite * grande, "attendu : 1")

# Bonus
r1, r2 = racines_naif(1.0, -10.0, 1.0)
##print("Autres racines :", r1, r2)
##print("Autre produit :", r1 * r2, "attendu : 1")

#Ex7.2
def racines(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0 :
        print("Impossible")
        return
    r = math.sqrt(delta)
    if b>= 0:
        rac = (-b - r) / (2 * a)
    else :
        rac = (-b + r) / (2*a)
    autre = c / (a * rac)
    return min(autre, rac), max(autre,rac)

##petite, grande = racines(1.0, -1e8, 1.0)
##print(petite, grande)
##print("produit :", petite * grande)
##for x in (petite, grande):
##    residu = x * x - 1e8 * x + 1
##    print(f"residu : {residu:.1e}, soit {residu / max(x * x, 1.0):.1e} en relatif")

#Ex7.3
total = Fraction(0)
for i in range(1000):
    total += Fraction(1, 10)
##print(total, total == 100)
##print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))

# Pour aller plus loin

from decimal import Decimal, getcontext

getcontext().prec = 50

print(Decimal(1) / Decimal(7))

a = Decimal("0.1")
b = Decimal("0.2")
c = Decimal("0.3")

print(a + b)
print(a + b == c)

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)


