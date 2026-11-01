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

Pour chaque groupe de 100 nombres, j’ai comparé le nombre de nombres premiers réellement trouvés grâce à l'ordinateur à une estimation mathématique. Cette estimation repose sur le logarithme népérien : elle consiste à diviser la taille de l’intervalle par le logarithme de son milieu.
J’ai ensuite comparé les résultats réels et les estimations à l’aide d’un graphique. J’ai également calculé des moyennes et un écart-type afin de mieux étudier les différences entre les valeurs obtenues.

Cette étape permet d’observer si la formule donne une estimation proche du nombre réel de nombres premiers, même si elle ne permet pas nécessairement de prévoir exactement leur nombre dans chaque groupe.
