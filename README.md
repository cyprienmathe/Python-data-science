# Python-data-science
Notre repository pour notre projet de python pour la data science

CSV (test) : https://equipements.sports.gouv.fr/api/explore/v2.1/catalog/datasets/data-es/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B&select=equip_nom%2C%20equip_service_date%2C%20equip_douche%2C%20equip_sanit%2C%20equip_travaux_date&where=reg_nom%20like%20%27%C3%8Ele-de-France%27

API : https://equipements.sports.gouv.fr/explore/dataset/data-es/api/?q=%C3%8ELE+DE+FRANCE

Réutilisations antérieures : https://equipements.sports.gouv.fr/explore/dataset/data-es/information/

Dictionnaire de variables : https://www.data.gouv.fr/fr/datasets/recensement-des-equipements-sportifs-espaces-et-sites-de-pratiques/#/community-resources/1b49fb73-97a4-4ab5-b1bc-eb169661b4c9

Introduction : 
Depuis les Jeux Olympiques de Paris 2024, un certain nombre de jeunes se sont pris de passion pour le tennis de table et la natation. Cependant, cet engouement s’est heurté au manque d’infrastructure, à leur vétusté et au manque d’encadrant. Cela a de nouveau mis en lumière le problème de l'accessibilité au sport et des « déserts sportifs ». A l’instar des « déserts médicaux », les « déserts sportifs » sont des zones géographiques souvent rurales, où les infrastructures sportives et les encadrants manquent et où infrastructures existantes sont pour la plupart vétustes et mal équipées. Cela constitue un obstacle à la pratique sportive des habitants de ces zones.

Pourtant, il semble exister un consensus sur les bienfaits d’une pratique sportive régulière, en cela qu’elle permet de prévenir un grand nombre de maladies notamment cardiovasculaires ; mais aussi en tant que facteur d’intégration sociale. Aussi, nous avons souhaité questionner cette notion de « désert sportif » sur la base du recensement des équipements sportifs en France. Pour cela, il nous a semblé pertinent d’analyser plusieurs variables telles que la vétusté des infrastructures étudiées, l’offre de sport selon les territoires et l’accessibilité aux infrastructures via des transports en commun.

Notre projet a donc pour objectif de répondre à la problématique suivante : A quel point la situation géographique d’un individu est-elle déterminante dans sa capacité à poursuivre une activité sportive régulière ?

Table des matières :
- I/ Récupération et traitement des données 
    * A. Récupération des données : Prise en main de l'API
        + Ajout d'une petit base de données économiques
    * B. Nettoyage des données
        + Préparation des données de cartiflette et synthèse avec les données éco.
    * C. Création de nouvelles variables 
- II/ Analyse descriptive et représentation graphique
    * A. Description de la base de données utilisée
        + Nombre d'installations par type d'équipement
        + Indicateur de vétusté violin plot
    * B. Grandes tendances observées
        + Cartographie
        + Tris croisés
- III/ Modélisation
    * A. Vue globale des inégalités à l'aide d'un indice de Gini
    * B.Estimation des efforts à fournir pour égaliser les territoires
 
Ce projet se trouve sur le script main.ipynb, qu'il faut faire tourner pour y trouver notre travail.


