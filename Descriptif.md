Détail de ce qu'il y a dans ma branche :

- fonctions pour appeller l'api et appeler le fichier .csv correspondant
- quelques graphiques directs basés sur la récupération de ces données
- des cartes _cartiflette_ pour représenter différentes variables par départements
- Une jonction avec une petite base de données économique
- Régression linéaire à partir de différentes variables (des deux bases de données)
- Prédiction à partir de cette régression linéaire

Introduction
Problématique globale
Contextualisation
Questions que l’on se pose : désert sportif

I/ Récupération et traitement de données
Les données proviennent d’une API.
Au niveau du nettoyage, il y a beaucoup de lignes avec des doublons car il y a plusieurs activités proposées à un même endroit, ou plusieurs infrastructures (par exemple : pour deux bassins dans une piscine, il y a deux lignes). Donc on a pris qu’une seule ligne pour chaque lieu où il y a des infrastructures et créer une nouvelle variable qui compte le nombre de lignes qu’il y avait avant.
Sinon, les données sont assez propres, même si beaucoup de cases ne sont pas renseignées.

II/ Analyse descriptive et représentation graphique
Décrire la base très simplement : les variables qu’il y a, comment se composent-elles  Expliquer celles que nous avons retenues.
Grandes tendances des données : visualisation par des cartes par exemple  Commenter les graphiques
Liste des visualisations :
-	Carte des infrastructures (légende par famille) où chaque point en France représente un lieu avec des infrastructures
-	
III/ Modélisation
Avoir une démarche scientifique

