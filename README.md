# Python-data-science
Notre repository pour notre projet de python pour la data science

CSV (test) : https://equipements.sports.gouv.fr/api/explore/v2.1/catalog/datasets/data-es/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B&select=equip_nom%2C%20equip_service_date%2C%20equip_douche%2C%20equip_sanit%2C%20equip_travaux_date&where=reg_nom%20like%20%27%C3%8Ele-de-France%27

API : https://equipements.sports.gouv.fr/explore/dataset/data-es/api/?q=%C3%8ELE+DE+FRANCE

Réutilisations antérieures : https://equipements.sports.gouv.fr/explore/dataset/data-es/information/

Dictionnaire de variables : https://www.data.gouv.fr/fr/datasets/recensement-des-equipements-sportifs-espaces-et-sites-de-pratiques/#/community-resources/1b49fb73-97a4-4ab5-b1bc-eb169661b4c9

Intro (1er jet) : 

Similairement aux déserts médicaux, les déserts sportifs sont des zones géographiques, souvent rurales, où les infrastructures sportives sont peu nombreuses, vétustes ou mal équipées. Leur existence est liée à l’absence de “moyens, de volonté politique parfois aussi”, d’après un article de Franceinfo publié en 2023 [1], et celle-ci pose un problème en termes de santé publique et de bien-être pour la population française rurale. Pour le résoudre, plusieurs pistes sont évoquées, notamment la décision d’une hausse des dépenses publiques par le Ministère des Sports, mais aussi une intervention des acteurs privés [2], qui pourraient collaborer avec les autorités publiques pour mettre en place des infrastructures de qualité dans les zones qui en ont le plus besoin. Mais quelles sont ces zones prioritaires ? 

En admettant l’existence d’une causalité entre sport et bien-être, l’objectif de ce projet sera donc dans un premier temps de repérer les zones les plus enclavées, aux infrastructures les moins nombreuses et les plus vétustes, afin d’essayer d’estimer d’une part le nombre d’infrastructures à ajouter, et d’autre part le montant à investir en rénovations. Nous ferons dans un second temps la distinction entre les différents types de sport, et nous étudierons la corrélation entre le type de sport et le niveau de richesse, afin d’éventuellement offrir une plus grande diversité d’activités à la population.

Intro (2ème jet, Jules) : 
Après les JO/JP, il y a eu un engouement des jeunes Français pour les clubs de tennis de table ou les piscines, mais il s'est heurté aux infrastructures, trop peu nombreuses ou trop vétustes, ou au manque d'encadrants.
De l'autre côté, le sport a une place centrale dans notre société. Il fait partie intégrante du processus d'intégration sociale et de lutte contre l'isolement social, et il porte une forte dimension politique en cela que les valeurs qu'il porte sont souvent associées à celles du travail (goût de l'effort, confiance en soi, ascension sociale). Enfin, le sport est un levier des politiques publiques de la santé, car l'activité physique permettrait de réduire la prévalence des maladies cardiovasculaires, des dépressions et de l'obésité, pour ne citer que ces pathologies. 
On voudrait se questionner dans ce projet sur la notion de "désert sportif", sur le même modèle que celle de "désert médical", à partir du recensement des équipements sportifs en France. Plusieurs variables peuvent être intéressantes à analyser : la vétusté, l'offre de sport par commune, l'accessibilité en transports en commun, l'accessibilité aux PMR. Et de comparer en dernier lieux ces résultats, aux des données socio-économiques à l'échelle du département par exemple (ruralité, taux de pauvreté, prévalence de certaines maladies...) par le biais de régression linéaires ou tris croisés.
