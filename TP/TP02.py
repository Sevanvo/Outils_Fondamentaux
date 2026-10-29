import time

#Ex1.1
def diviseurs(n):
    div =[]
    for diviseur in range(1,n+1):
        if n%diviseur == 0 :
            div.append(diviseur)
    return div

##print(diviseurs(28))
##print(diviseurs(97))

# Bonus
##print(diviseurs(1))
##print(diviseurs(12))
##print(diviseurs(100))

#Ex2.1
def pgcd_naif(a,b):
    grand_div = 1
    for val in range(1, min(a,b)+1, 1):
        if a % val == 0 and b % val == 0 :
            grand_div = val
    return grand_div

def pgcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

##print(pgcd_naif(1071, 462), pgcd(1071, 462))

# Bonus
##print(pgcd_naif(12, 8))
##print(pgcd_naif(25, 15))
##print(pgcd_naif(17, 13))
##print(pgcd_naif(100, 10))

#Ex3.1

def est_premier_naif(n):
    """Teste la primalité en essayant tous les diviseurs jusqu'à n - 1."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def est_premier(n):
    """Teste la primalité en s'arrêtant à la racine carrée de n."""
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

def duree(fonction, argument):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut

n = 10007
##print(f"naif        : {duree(est_premier_naif, n):.4f} s pour n= ", n)
##print(f"jusqu'a rac : {duree(est_premier, n):.6f} s pour n= ", n)
n=100003
##print(f"naif        : {duree(est_premier_naif, n):.4f} s pour n= ", n)
##print(f"jusqu'a rac : {duree(est_premier, n):.6f} s pour n= ",n)
n = 1000003
##print(f"naif        : {duree(est_premier_naif, n):.4f} s pour n= ", n)
##print(f"jusqu'a rac : {duree(est_premier, n):.6f} s pour n= ",n)
##
##print(est_premier(1000000000039))

# L'IA vous le donne en trois secondes
def est_premier(n):
    """Renvoie True si n est premier, False sinon."""
    if n < 2:
        return False

    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False

    return True

##print("1 :", est_premier(1))
##print("2 :", est_premier(2))
##print("-7 :", est_premier(-7))
##n = 1_000_003
##print("Temps d'exécution :", duree(est_premier, n), "secondes")
# Nous avons vérifié que 1 n’est pas premier, que 2 est bien premier et que les nombres négatifs ne sont pas premiers. Nous avons également constaté qu’une boucle jusqu’à la racine carrée de (n) est beaucoup plus rapide qu’une boucle jusqu’à (n). Pour 1 000 003, cette optimisation réduit fortement le nombre de vérifications. Nous retenons qu’il faut tester plusieurs cas particuliers et choisir un algorithme efficace.
#Ex4.1

def crible(limite):
    """Renvoie la liste des nombres premiers de 2 à limite inclus."""
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d = d + 1
    return [n for n in range(limite + 1) if est_premier_tab[n]]

##premiers = crible(100000)
##print(premiers)
##print(len(premiers), "premiers jusqu'a 100000")
##print("temps pour le crible",duree(crible, 100000))
##
##nb_nb_prem = 0
##debut = time.perf_counter()
##for k in range(100001):
##    if est_premier(k):
##        nb_nb_prem +=1
##tps_est_premier = time.perf_counter() - debut
##print("temps en appelant est_premier:", tps_est_premier, nb_nb_prem)

#Ex5.1

def facteurs(n):
    L = []
    if n<1 :
        return []
    k = 2
    while k**2 <= n:
        while n%k == 0:
            n = n // k
            L.append(k)
        k += 1
    if n> 1:
        L.append(n)
    return L

f = facteurs(360)
##print(f)

produit = 1
for x in f:
    produit = produit * x
##print(produit)

# Bonus
##for n in [12, 49, 97, 100]:
##    f = facteurs(n)
##    produit = 1
##    for x in f:
##        produit = produit * x
##    print(n, ":", f, "| Produit :", produit)

# Pour aller plus loin

p = 100003
q = 100019

debut = time.perf_counter()
n = p * q
temps_multiplication = time.perf_counter() - debut
##
##print("Produit :", n)
##print("Temps de multiplication :", temps_multiplication, " s")


debut = time.perf_counter()
f = facteurs(n)
temps_factorisation = time.perf_counter() - debut
##
##print("Facteurs trouvés :", f)
##print("Temps de factorisation :", temps_factorisation, "s")

#Ex6.1

def fibonacci_recursif(n):
    """F(n) en suivant la définition, par récurrence."""
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

##print("temps pour fibonnaci pour n = 20,",duree(fibonacci_recursif, 20))
##print("temps pour fibonnaci pour n = 25,",duree(fibonacci_recursif, 25))
##print("temps pour fibonnaci pour n = 30,",duree(fibonacci_recursif, 30))


#Ex6.2
appel = {}
def fibonacci_recursif_ex_6(n):
    """F(n) en suivant la définition, par récurrence."""
    if n in appel:
        appel[n] += 1
    else :
        appel[n] = 1
    if n < 2:
        return n
    return fibonacci_recursif_ex_6(n - 1) + fibonacci_recursif_ex_6(n - 2)

##resultat = fibonacci_recursif_ex_6(30)
##print("F(30) =", resultat)
##print("appels a F(1) :", appel[1])
##print("appels en tout :", sum(appel.values()))

#Ex6.3
def fibonacci(n):
    courante = 1
    precedente = 0
    for k in range(n):
        temporaire = courante
        courante += precedente
        precedente = temporaire
    return precedente
##
##print(all(fibonacci(n) == fibonacci_recursif(n) for n in range(26)))
##print(f"F(30) en {duree(fibonacci, 30):.6f} s")
##grand = fibonacci(10000)
##print(len(str(grand)), "chiffres")

#Bonus

##print("F(0) =", fibonacci(0))
##print("F(1) =", fibonacci(1))
##print("F(2) =", fibonacci(2))
##print("F(10) =", fibonacci(10))
##print("F(20) =", fibonacci(20))
##print("F(50) =", fibonacci(50))


#Pour aller plus loin

def temps_de_vol(n):
    cp = 0
    plafond = 100000
    while n!=1 and  cp<plafond:
        if n % 2 == 0:
            n = n//2
        else :
            n = 3*n + 1
        cp += 1
    return cp
##print(temps_de_vol(27))


vol_plus = 0
nb = 0

for n in range(1,10001):
    vol = temps_de_vol(n)
    if vol > vol_plus :
        vol_plus = vol
        nb = n
##print(nb, vol_plus)


#Ex7.1
def euclide_etendu(a, b):
    if b == 0 :
        return a, 1, 0
    g, u, v = euclide_etendu(b, a %b)
    u, v = v, u - (a // b) * v
    return g, u, v


g, u, v = euclide_etendu(1071, 462)
##print(g, u, v, 1071 * u + 462 * v == g)
##print(euclide_etendu(5,26))

# Bonus
##g, u, v = euclide_etendu(12, 8)
##print(g, u, v, 12 * u + 8 * v == g)
##g, u, v = euclide_etendu(15, 5)
##print(g, u, v, 15 * u + 5 * v == g)
##g, u, v = euclide_etendu(7, 3)
##print(g, u, v, 7 * u + 3 * v == g)

#Ex7.2
def puissance_mod_naive(a, e, n):
    resultat = 1
    for k in range(e):
        resultat = resultat * a % n
    return resultat

def puissance_mod(a, e, n):
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = resultat * a % n
        a = a * a % n
        e //=2
    return resultat

print(puissance_mod(7,10**7,1000003)==pow(7,10**7,1000003)==puissance_mod(7,10**7,1000003))

debut = time.perf_counter()
puissance_mod(7,10**7,1000003)
temp=time.perf_counter() - debut

debut2 = time.perf_counter()
puissance_mod_naive(7,10**7,1000003)
temp2=time.perf_counter() - debut

print(temp,temp2)

print(puissance_mod(2, 3, 5))
print(puissance_mod(3, 2, 7))
print(puissance_mod(5, 0, 3))
print(puissance_mod(4, 3, 10))
