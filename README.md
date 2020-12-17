# Documentation utilisateur

# Installation

Dans un premier temps, pour pouvoir installer virtualenv dans son répertoire, faites :

```
sh installVirtualenv.sh
```

En suite, pour pouvoir récuperer les variables d'environnement, faites :

```
source venv/bin/activate
```

Dans un second temps, pour pouvoir installer matplotlib et pandas que nous allons utiliser pour effectuer nos différents scripts, faites :

```
sh installDependencies.sh
```

# Setup

## Pré-requis

Dans le dossier `data/dateSet/`, il faut mettre les 4 fichiers du jeu de donnée sur le darkWeb (en ne changeant pas les noms d'origine).

## Scripts

Pour effectuer les différents traitement des données faites :

```
sh setupData.sh
```

Si vous souhaitez afficher les graphes indiquant le nombre de ventes totales ainsi que le nombre total de chiffre d'affaire par catégorie et sous catégorie, faites :

```
sh runDisplay.sh
```

Pour supprimer les données extraites faites :

```
sh cleanData.sh
```

Pour utiliser tulip, récupérez notre fichier tulip:

```
project.tlpx
```

Le script qui permet de récupérer les vendeurs en fonction des sous-catégories est:

```
display_relation_seller_categories.py
```

Par défaut, il vide le graphe courant.
