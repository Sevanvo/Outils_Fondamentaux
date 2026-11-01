# Outils_Fondamentaux

Projet individuel 
Sevan VOVILIER
S1C2
# Étude sur la répartition des nombres premiers

## Introduction
  Lorsque le professeur de mathématiques nous a fait un cours sur les nombres premiers, il nous a dit que plus un nombre était grand, moins il avait de chances d’être premier. Cela m’a amené à me poser la question suivante : comment évolue la répartition des nombres premiers ?

Cette question m’a paru intéressante, et ce projet va nous permettre d’étudier ce phénomène plus en détail.

Pour cela, j’ai choisi de me concentrer sur une question plus précise : **comment estimer le nombre de nombres premiers dans un intervalle et évaluer la précision de cette estimation ?**

## Étape 1
  J'ai comparé deux méthodes pour obtenir le nombre de nombres premiers jusqu'à une limite. La méthode naïve teste les diviseurs possibles de chaque nombre afin de déterminer s’il est premier. La deuxième méthode élimine progressivement les multiples des nombres premiers afin de conserver uniquement les nombres premiers.

  Pour voir laquelle était la plus efficace et la moins coûteuse, dans chaque fonction, j'ai ajouté une variable qui va compter le nombre d'opérations effectuées.

  Le programme lance deux pages contenant deux courbes : la première pour leurs coût et une seconde pour  leurs temps d’exécution. Par exemple, pour une limite égale à N = 10 000, 5 775 223 opérations en 0.2 secondes sont faites par la méthode naïve. 16 981 opérations en 0,0006 secondes sont faites par la méthode optimisée.

  C'est donc cette méthode que l'on va utiliser dans la suite du projet
## Étape 2
J’ai  étudié le nombre de nombres premiers présents dans des intervalles successifs de 100 nombres, jusqu’à 1 000 000. Par exemple, j’ai compté les nombres premiers entre 1 et 100, puis entre 101 et 200, et ainsi de suite.

Pour chaque intervalle, j’ai comparé le nombre de nombres premiers réellement trouvés par l’ordinateur à deux estimations mathématiques. La première formule consiste à diviser la taille de l’intervalle par le logarithme népérien de son milieu. Elle utilise donc la valeur située au centre de l’intervalle pour estimer combien de nombres premiers il contient.

La deuxième formule repose sur la fonction n/ln(n). Elle estime le nombre de nombres premiers jusqu’à la borne supérieure, puis soustrait l’estimation jusqu’à la borne inférieure. La différence obtenue sert à estimer le nombre de nombres premiers présents dans l’intervalle.

Pour ces formules,  je me suis appuyé sur le théorème des nombres premiers et son approximation présentés sur le site du NIST

En calculant les moyennes de tous les résultats, j’ai obtenu 7,848 nombres premiers par intervalle en réalité, contre 7,861 avec la première formule et 7,237 avec la deuxième. La première formule donne donc une moyenne plus proche du nombre réellement observé dans cette expérience.

J’ai également calculé l’écart-type des nombres premiers observés, qui vaut 2,036, et l’ai comparé à celui d’un modèle de hasard pur, égal à 2,691. L’écart-type mesure la dispersion des valeurs autour de leur moyenne. Les nombres premiers observés varient donc moins que dans ce modèle de comparaison.

L’estimation est très proche de la moyenne réelle pour les intervalles de 100 nombres. Mais est-ce toujours le cas lorsque l’on change la taille des intervalles ?

## Étape 3
Comme on a 
