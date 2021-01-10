# API Spammy 90's 
Pour éviter à l'utilisateur de devoir calculer par lui même les différentes valeurs nécessaires (fréquences des mots, nombre de majuscules, etc), j'ai préféré implémenter un petit site web d'une page, afin que l'utilisateur n'ait juste à copier/coller son texte.
J'ai repris le template Twenty, disponible à l'adresse suivante: https://html5up.net/twenty 

## Installation
Je n'ai malheureusement pas réussi à récupérer les requirements nécessaires, à cause de difficultés avec mes environnements virtuels. 
Un environnement basique devrait faire l'affaire, il faut cependant installer les librairies suivantes:
``pip install Flask``
``pip install joblib``
``pip install flask_cors``

## Lancement 
Lancer l'application:
``python app.py``

Le site est disponible à l'adresse suivante: http://localhost:5000/

## Utilisation de l'API seule
Si vous souhaitez uniquement utiliser l'API, il vous suffit de faire une requête GET à l'adresse suivante: http://localhost:5000/prediction, et d'envoyer votre tableau de taille 57. 