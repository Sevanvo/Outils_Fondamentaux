### Outils_Fondamentaux

Projet individuel\
Sevan VOVILIER\
S1C2
# Étude sur la répartition des nombres premiers

## Introduction
  Lorsque le professeur de mathématiques nous a fait un cours sur les nombres premiers, il nous a dit que plus un nombre était grand, moins il avait de chances d’être premier. Cela m’a amené à me poser la question suivante : comment évolue la répartition des nombres premiers ?

Cette question m’a paru intéressante, et ce projet va nous permettre d’étudier ce phénomène plus en détail.

Pour cela, j’ai choisi de me concentrer sur une question plus précise : comment estimer le nombre de nombres premiers dans un intervalle et évaluer la précision de cette estimation ?

## Étape 1
J'ai comparé deux méthodes pour obtenir le nombre de nombres premiers jusqu'à une limite. La méthode naïve teste les diviseurs possibles de chaque nombre afin de déterminer s’il est premier. La deuxième méthode élimine progressivement les multiples des nombres premiers afin de conserver uniquement les nombres premiers.

Pour voir laquelle était la plus efficace et la moins coûteuse, dans chaque fonction, j'ai ajouté une variable qui va compter le nombre d'opérations effectuées.

Le programme affiche deux graphiques : le premier compare le nombre d’opérations effectuées par chaque méthode, tandis que le second compare leurs temps d’exécution. Par exemple, pour une limite égale à N = 10 000, 5 775 223 opérations en 0.2 secondes sont faites par la méthode naïve. 16 981 opérations en 0,0006 secondes sont faites par la méthode optimisée.

  C'est donc cette méthode que l'on va utiliser dans la suite du projet
## Étape 2
J’ai  étudié le nombre de nombres premiers présents dans des intervalles successifs de 100 nombres, jusqu’à 1 000 000. Par exemple, j’ai compté les nombres premiers entre 1 et 100, puis entre 101 et 200, et ainsi de suite.

Pour chaque intervalle, j’ai comparé le nombre de nombres premiers réellement trouvés par l’ordinateur à deux estimations mathématiques. La première formule consiste à diviser la taille de l’intervalle par le logarithme népérien de son milieu. Elle utilise donc la valeur située au centre de l’intervalle pour estimer combien de nombres premiers il contient.

La deuxième formule repose sur la fonction n/ln(n). Elle estime le nombre de nombres premiers jusqu’à la borne supérieure, puis soustrait l’estimation jusqu’à la borne inférieure. La différence obtenue sert à estimer le nombre de nombres premiers présents dans l’intervalle.

Pour ces formules,  je me suis appuyé sur le théorème des nombres premiers et son approximation présentés sur le site du NIST

En calculant les moyennes de tous les résultats, j’ai obtenu 7,848 nombres premiers par intervalle en réalité, contre 7,861 avec la première formule et 7,237 avec la deuxième. La première formule donne donc une moyenne plus proche du nombre réellement observé dans cette expérience.

J’ai également calculé l’écart-type des écarts entre le nombre réel et l’estimation qui vaut 2,036. L’écart-type mesure la dispersion des valeurs autour de leur moyenne. 

L’estimation est très proche de la moyenne réelle pour les intervalles de 100 nombres. Mais est-ce toujours le cas lorsque l’on change la taille des intervalles ?

## Étape 3
Comme j'ai déjà travaillé sur le nombre de nombres premiers jusqu'à 1 000 000, j'ai choisi de poursuivre l’étude sur les nombres compris entre 100 000 et 10 000 000, en testant des intervalles de tailles différentes, allant de 1 à 1 000 000.

Pour chaque taille d’intervalle, j’ai comparé le nombre de nombres premiers réellement trouvés avec celui donné par la formule d’estimation. J’ai ensuite calculé deux indicateurs : l’erreur relative moyenne absolue, qui mesure l’importance moyenne des erreurs, et l’erreur relative moyenne signée, qui permet de voir si l’estimation a plutôt tendance à surestimer ou à sous-estimer le nombre de nombres premiers.

J’ai représenté ces résultats sur des graphiques afin d’observer l’influence de la taille des intervalles sur la précision de l’estimation.

Les résultats montrent que l’erreur moyenne diminue globalement lorsque la taille des intervalles augmente. Pour les petits intervalles, notamment ceux de taille 1 à 1 000, les erreurs sont plus importantes. L’estimation est donc moins précise à cette échelle.

## Conclusion / Résumé
Le choix de l'algorithme a une grande importance, car une méthode optimisée permet de réaliser les calculs beaucoup plus rapidement. A N = 10 000, la méthode naïve compte 5 775 223 opérations contre 16 981 pour la méthode optimisée. En moyenne, l'estimation 100 / ln(x) est très bonne : 7,861 prédit contre 7,848 réel, soit 0,16 % d'écart jusqu'à un million. On a pu comparer cette moyenne à celle des estimations obtenues grâce à une formule mathématique fondée sur une formule mathématique telle que n/ln(n). Les moyennes réelle et prédite sont proches, ce qui montre que la formule donne une estimation globale cohérente. Cependant, les résultats peuvent varier d'une centaine à l'autre. La différence de n/ln(n) entre les deux bords de la centaine, est moins bonne : elle prédit 7,237 contre 7,848 réel. Cela nous a amené à une question, est ce qu'une estimation est-elle aussi précise pour des intervalles plus petits ou plus grands que 100 ? Avec le graphe, on comprend directement que dans l'intervalle[1, 1000], les moyennes des erreurs relatives sont élevées. L'erreur relative absolue moyenne vaut 187 % pour un intervalle de 1 nombre, 95 % pour 10 nombres, 24 % pour 100 nombres et 6,6 % pour 1000 nombres. Nous constatons que l'erreur relative absolue moyenne diminue globalement lorsque la taille des intervalles augmente. L'estimation devient donc généralement plus précise sur les grands intervalles. Elle tombe à 1,7 % pour 10 000 nombres, 0,41 % pour 100 000 nombres et 0,24 % pour 1 000 000 de nombres. Notre seuil de 5 % permet de repérer les tailles d'intervalles pour lesquelles l'erreur relative absolue moyenne devient inférieure à cette valeur. J’ai choisi un seuil de 5 % afin de disposer d’un critère simple pour évaluer la précision des estimations et déterminer à partir de quelle taille d’intervalle l’erreur relative absolue moyenne devient suffisamment faible. Nous pouvons donc conclure que la formule donne une estimation de plus en plus précise lorsque l'on considère des intervalles plus grands. En revanche, pour de petits intervalles, le nombre de nombres premiers varie davantage d'un intervalle à l'autre, ce qui rend l'estimation moins précise. L'écart relatif moyen reste proche de 0 quelle que soit la taille : l'estimation n'est pas biaisée, elle est seulement imprécise quand l'intervalle est petit. Le graphique montre que l’erreur relative moyenne absolue reste supérieure à 5 % pour les intervalles de tailles 1, 10 et 100. Dans notre étude, une taille d’intervalle d’au moins 10 000 nombres permet donc d’obtenir une erreur relative moyenne absolue inférieure à 5 %.

## Limite de l'étude :
Pour la taille 1000000, la zone ne contient qu'environ 9 intervalles complets, la moyenne sur si peu de points n'a donc pas de réelle valeur statistique. L'étude s'arrête à 10 millions. Nous n'avons pas pu vérifier si ces résultats restent valables pour de très grands nombres. En effet, si je voulais faire l'étude sur de plus grands intervalles issus de plus grands nombres, j'aurais dû trouver une autre méthode car la méthode sur laquelle je me suis appuyé tout au long du projet a tout de même une limite. La méthode optimisée garde les nombres en mémoire et la mémoire peut devenir un obstacle pour de grands nombres. 

## Comment faire fonctionner le code
Le code a juste à être exécuté.
Plusieurs courbes apparaîtront et des données arriveront dans la console.

## Usage de l'IA
Elle m'a aidé dans la création des graphiques, je n'avais encore jamais manipulé matplotlib.pyplot.
