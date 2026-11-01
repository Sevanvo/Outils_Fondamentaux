# Créé par Sevan

import time
import matplotlib.pyplot as plt
import math

def duree(fonction, arg):
    debut = time.perf_counter()
    fonction(arg)
    return time.perf_counter() - debut

# On va comparer deux façons pour compter les nombres premiers : une méthode naïve et une optimisée

def est_premier_naif(n):
    cout = 0
    if n < 2:
        return False, cout
    for d in range(2, n):
        cout += 1
        if n % d == 0:
            return False, cout
    return True, cout

def nombre_liste_premiers_naif(limite):
    compteur = 0
    cout_total = 0
    liste = []
    if limite<0 :
        raise ValueError("La limite doit être positive.")
    for nb in range(2, limite+1):
        premier, cout = est_premier_naif(nb)
        cout_total += cout
        if premier :
            compteur += 1
            liste.append(nb)
    return liste, compteur, cout_total

def nombre_liste_premiers_optimise(limite):
    if limite < 0:
        raise ValueError("La limite doit être positive.")
    premiers = [True] * (limite + 1)
    if limite >= 0:
        premiers[0] = False
    if limite >= 1:
        premiers[1] = False
    cout = 0
    d = 2
    while d * d <= limite:
        if premiers[d]:
            for multiple in range(d * d, limite + 1, d):
                cout += 1
                premiers[multiple] = False
        d += 1
    liste = []
    for nb in range(2, limite + 1):
        if premiers[nb]:
            liste.append(nb)
    compteur = len(liste)
    return liste, compteur, cout

# Étape1

limite_comparaison = [100, 500, 1000, 2000, 5000, 10000] # Test de la méthode naïve et optimisée sur de "petits nombres"
limites = [100, 500, 1000, 2000, 5000, 10000, 100000, 500000, 1000000]

nombres_naifs = []
nombres_optimises = []
couts_naifs = []
couts_optimises = []
temps_naifs = []
temps_optimises = []

for limite in limite_comparaison:
    liste, compteur, cout = nombre_liste_premiers_naif(limite)
    nombres_naifs.append(compteur)
    couts_naifs.append(cout)
    temps_naifs.append(duree(nombre_liste_premiers_naif, limite))

    liste, compteur, cout = nombre_liste_premiers_optimise(limite)
    nombres_optimises.append(compteur)
    couts_optimises.append(cout)
    temps_optimises.append(duree(nombre_liste_premiers_optimise, limite))


# Affichage des résultats
print("Limites :", limite_comparaison)
print("Nombres de premiers :", nombres_naifs)
print("Coûts naïfs :", couts_naifs)
print("Coûts optimisés :", couts_optimises)
print("Temps naïfs :", temps_naifs)
print("Temps optimisés :", temps_optimises)

# Graphique 1 : coût des algorithmes
plt.figure(figsize=(9, 5))
plt.plot(limite_comparaison, couts_naifs, marker="o", label="Méthode naïve")
plt.plot(limite_comparaison, couts_optimises, marker="x", label="Méthode optimisée")
plt.xlabel("Limite N")
plt.ylabel("Nombre d'opérations comptées")
plt.title("Comparaison du coût des algorithmes")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Graphique 2 : temps d'exécution
plt.figure(figsize=(9, 5))
plt.plot(limite_comparaison, temps_naifs, marker="o", label="Méthode naïve")
plt.plot(limite_comparaison, temps_optimises, marker="x", label="Méthode optimisée")
plt.xlabel("Limite N")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Comparaison des temps d'exécution")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

## Pour conclure cette partie, on voit que la version optimisée est bien meilleure que la naïve.
## Elle est beaucoup plus rapide et moins couteuse
## De plus, la méthode naïve peut devenir très lente dès le nombre 100000 à testé.
## Quant à la version optimisée, elle peut gérer un million mais à des dizaines voire des centaines de millions, le temps et la mémoire deviennent plus contraignants

# Étape 2
# Pour répondre à notre problème, nous allons utilisé cette version
limite_centaines = limites[-1]

liste_premiers, nb_premiers, cout = nombre_liste_premiers_optimise(limite_centaines)

nb_centaines = limite_centaines // 100

# On va compter le nombre de nombre premiers de chaque centaines et on va les mettre dans comptes
comptes = [0] * nb_centaines
for p in liste_premiers:
    k = p // 100
    if k < nb_centaines:
        comptes[k] = comptes[k] + 1

debuts = []
reels = [] # Va contenir le nombre de nombres premiers trouvés dans chaque centaine
predits = []
for k in range(1, nb_centaines):
    debuts.append(100 * k)   # sert à positionner les pts sur l'axe des abscisses
    reels.append(comptes[k]) # Nombre de nombre premiers de la centaine à mettre dans le graphique
    predits.append(100 / math.log(100 * k + 50)) # Estimation à partir de la densité des premiers 1/ln(x) × 100 nombres, évaluée au milieu de la centaine

# On calcule les moyennes des nombres premiers par centaine
moyenne_reelle = sum(reels) / len(reels)
moyenne_predite = sum(predits) / len(predits)

print("moyenne réelle :", round(moyenne_reelle, 3))
print("moyenne prédite :", round(moyenne_predite, 3))


# Les valeurs sont très proches, cela veut donc dire que la prévision est bonne en moyenne

# On mesure leur écart
ecarts = []
for i in range(len(reels)):
    ecarts.append(reels[i] - predits[i])

moyenne_ecarts = sum(ecarts) / len(ecarts)
# On calcule l'écart-type pour savoir combien les écarts s'éloignent de leur moyenne
somme_carres = 0
for e in ecarts:
    somme_carres = somme_carres + (e - moyenne_ecarts) ** 2
ecart_type = math.sqrt(somme_carres / len(ecarts))

predits_diff = []
for k in range(1, nb_centaines):
    a = 100 * k
    b = 100 * k + 100
    predits_diff.append(b / math.log(b) - a / math.log(a))

moyenne_diff = sum(predits_diff) / len(predits_diff)

# Mesure de l'écart centaine par centaine

ecarts_diff = []
for i in range(len(reels)):
    ecarts_diff.append(reels[i] - predits_diff[i])

# Je calcule la moyenne des écarts, elle doit être proche de 0 si la prévision est correcte
moyenne_ecarts_diff = sum(ecarts_diff) / len(ecarts_diff)

print("moyenne prédite (différence n/ln n) :", round(moyenne_diff, 3))
print("écart moyen (différence n/ln n) :", round(moyenne_ecarts_diff, 3))


print("écart moyen :", round(moyenne_ecarts, 3))
print("écart-type observé :", round(ecart_type, 3))


# Graphique 3
plt.figure(figsize=(12, 5))
plt.plot(debuts, reels, ".", markersize=2, label="Réel")
plt.plot(debuts, predits, label="Prédit 100 / ln(x)")
plt.xlabel("Début de la centaine")
plt.ylabel("Nombre de premiers dans la centaine")
plt.title("Premiers par centaine : réel et prédit")
plt.legend()
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis="x", style="plain")
plt.show()
## On observe que le nombre réel de nombres premiers varie d'une centaine à l'autre, tandis que l'estimation suit une courbe régulière.
## On constate également que la formule prévoit globalement moins de nombres premiers lorsque les nombres étudiés deviennent plus grands.


## L'écart moyen est quasi nul : en moyenne, l'estimation ne se trompe pas dans un sens plutôt que dans l'autre.
## En revanche, d'une centaine à l'autre, le nombre réel s'écarte de l'estimation d'environ 2 premiers (écart-type de 2,04).

# On peut donc se demander sur quelles tailles d'intervalles la précision de l'estimation est insuffisante
## Nous allons rechercher les tailles d'intervalles pour lesquelles l'erreur relative moyenne dépasse 5 %.

debut_zone = 100000
fin_zone = 10000000

# On recalcule les nombres premiers jusqu'à 10 millions pour étudier une zone plus grande

liste_premiers, nb_premiers, cout = nombre_liste_premiers_optimise(fin_zone)

tailles_intervalles = [1, 10, 100, 1000, 10000, 100000, 1000000]
seuil_precision = 5

print("\nRecherche des intervalles où l'erreur dépasse 5 %")

# On garde les tailles testées et les écarts pour tracer le graphique
tailles_testees = []
ecarts_relatifs = []
erreurs_relatives = []

for taille in tailles_intervalles:
    comptes_reels = []
    predictions = []
    erreurs_absolues = []

    indice = 0

    # On ignore les nombres premiers avant la zone étudiée
    while indice < len(liste_premiers) and liste_premiers[indice] < debut_zone:
        indice += 1
    # On parcourt les intervalles complets sans dépasser la limite fixée
    for debut in range(debut_zone, fin_zone - taille + 1, taille):
        fin = debut + taille
        compte_reel = 0

        # Comptage réel des nombres premiers dans l'intervalle
        while indice < len(liste_premiers) and liste_premiers[indice] < fin:
            if liste_premiers[indice] >= debut:
                compte_reel += 1
            indice += 1

        # On estime le nombre de premiers dans l'intervalle à partir de son milieu
        milieu = (debut + fin) / 2
        prediction = taille / math.log(milieu)

        comptes_reels.append(compte_reel)
        predictions.append(prediction)
        erreurs_absolues.append(abs(compte_reel - prediction))

    # On calcule l'erreur moyenne puis on la compare à la prédiction moyenne
    moyenne_predite = sum(predictions) / len(predictions)
    erreur_moyenne = sum(erreurs_absolues) / len(erreurs_absolues)
    ecarts = []
    for i in range(len(comptes_reels)):
        ecarts.append(comptes_reels[i] - predictions[i])
    ecart_moyen = sum(ecarts) / len(ecarts)

    # Calcul des deux écarts relatifs en pourcentage
    ecart_relatif = ecart_moyen / moyenne_predite * 100
    erreur_relative = erreur_moyenne / moyenne_predite * 100
    tailles_testees.append(taille)
    ecarts_relatifs.append(ecart_relatif)
    erreurs_relatives.append(erreur_relative)

    print("\nTaille :", taille)
    print("Erreur relative moyenne :", round(erreur_relative, 2), "%")

    if erreur_relative > seuil_precision:
        print("Précision insuffisante.")
    else:
        print("Précision suffisante.")

print("Tailles :", tailles_testees)
print("Écarts relatifs :", ecarts_relatifs)
print("Erreurs relatives :", erreurs_relatives)

# On compare l'écart moyen et l'erreur absolue moyenne selon les intervalles
plt.figure(figsize=(9, 5))

plt.plot(tailles_testees, ecarts_relatifs, marker="o",
         label="Écart relatif moyen")
plt.plot(tailles_testees, erreurs_relatives, marker="x",
         label="Erreur relative absolue moyenne")

plt.axhline(y=0, linestyle="--", label="Écart nul")

plt.axhline(y=seuil_precision, linestyle="--",label="Seuil de 5 %")
plt.xscale("log")
plt.xticks(tailles_testees, [str(taille) for taille in tailles_testees])

plt.xlabel("Taille des intervalles")
plt.ylabel("Écart relatif (%)")
plt.title("Écarts relatifs entre les nombres réels et estimés")
plt.legend()
plt.grid(True, which="both")
plt.tight_layout()
plt.show()

# Conclusion
## Le choix de l'algorithme a une grande importance, car une méthode optimisée permet de réaliser les calculs beaucoup plus rapidement.
## Pour N = 10 000, la méthode naïve compte 5 775 223 opérations contre 16 981 pour la méthode optimisé
## En moyenne, l'estimation 100 / ln(x) est très bonne : 7,861 prédit contre 7,848 réel, soit 0,16 % d'écart jusqu'à un million.
## On a pu comparer cette moyenne à celle des estimations obtenues grâce à une formule mathématique fondée sur une formule mathématique telle que n/ln(n)
## Cependant, les résultats peuvent varier d'une centaine à l'autre.
## La différence de n/ln(n) entre les deux bords de la centaine, est moins bonne : elle prédit 7,237 contre 7,848 réel (écart moyen de +0,611).
## Cela nous a amené à une question, est ce qu'une estimation est-elle aussi précise pour des intervalles plus petits ou plus grands que 100 ?
## Avec le graphe, on comprend directement que dans l'intervalle[1, 1000], les erreurs relatives sont élevées.
## L'erreur relative absolue moyenne vaut 187 % pour un intervalle de 1 nombre, 95 % pour 10 nombres, 24 % pour 100 nombres et 6,6 % pour 1000 nombres.
## Nous constatons que l'erreur relative absolue moyenne diminue globalement lorsque la taille des intervalles augmente. L'estimation devient donc généralement plus précise sur les grands intervalles.
## Elle tombe à 1,7 % pour 10 000 nombres, 0,41 % pour 100 000 nombres et 0,24 % pour 1 000 000 de nombres.
## Notre seuil de 5 % permet de repérer les tailles d'intervalles pour lesquelles l'erreur relative absolue moyenne devient inférieure à cette valeur.
## Ce seuil est franchi entre 1 nombres et 1 000 nombres.
## Nous pouvons donc conclure que la formule donne une estimation de plus en plus précise lorsque l'on considère des intervalles plus grands.
## En revanche, pour de petits intervalles, le nombre de nombres premiers varie davantage d'un intervalle à l'autre, ce qui rend l'estimation moins précise.
## L'écart relatif moyen reste proche de 0 quelle que soit la taille : l'estimation n'est pas biaisée, elle est seulement imprécise quand l'intervalle est petit.
## Limite de l'étude : pour la taille 1000000, la zone ne contient qu'environ 9 intervalles complets, la moyenne sur si peu de points n'a donc pas de réelle valeur statistique.
## L'étude s'arrête à 10 millions. Nous n'avons pas pu vérifié si ces résultats restent valables pour de très grands nombres.
## En effet, si je voulais faire l'étude sur de plus grands intervalles issus de plus grands nombres, j'aurais du trouver une autre méthode car la méthode sur laquelle je me suis appuyer tout au long du projet a tout de meme une limite.
## La méthode optimisée garde les nombres en mémoire et la mémoire peut devenir un obstacle pour de grands nombres


