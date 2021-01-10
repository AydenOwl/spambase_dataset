# spambase_dataset
## Présentation du jeu de données
Le jeu de données « Spambase » présente des informations collectées sur **4601 mails**, ces derniers étant classés en deux catégories: **spam** ou **mail normal** (mail personnel, professionnel, etc).

Pour rappel, un spam (ou pourriel), est un **« Envoi répété d'un message électronique, souvent publicitaire, à un grand nombre d'internautes sans leur consentement »**. Les systèmes de messagerie cherchent donc depuis des années à améliorer leurs filtres de spams, qui sont une nuisance pour les utilisateurs.

## But de l'étude
Ce jeu de données a été créé dans le but de **réaliser un filtre anti-spam personnalisé pour le donneur**, George Forman. En effet, il contient des variables spécifiques aux mails que recevaient Forman (la fréquence du mot « George » et celle du code « 650 » sont deux variables du jeu de données). Il n’y a pas assez de données dans ce jeu pour pouvoir créer un filtre général.

Ici, j'ai aussi cherché à créer un classificateur de spam à partir de ce jeu de données.

Après avoir étudié le jeu de données, j'ai réalisé une API en Flask afin de pouvoir donner en entrée un texte et d'utiliser la prédiction du modèle d'IA pour classer ce dernier (mail ou spam).

## Conclusion
Il aurait été intéressant d’avoir les textes d’où proviennent les données du jeu, pour les comparer à des mails plus récents.
Cependant, certaines choses n’ont pas changé: l’utilisation de points d’exclamation et de majuscules par exemple, ou encore l’utilisation de certains mots.
Par exemple, vous pourrez trouver à ces deux liens des techniques pour éviter que le mail envoyé soit classé comme un spam par les filtres actuels:

https://www.yesware.com/blog/email-spam/
https://www.simplycast.com/blog/100-top-email-spam-trigger-words-and-phrases-to-avoid/#post 

Mais pour reprendre la description du jeu de données, pour construire un filtre personnalisé, c’est au cas par cas. Tout le monde ne considère pas les mêmes choses comme spam par exemple. Ce jeu de données n'a donc pas permis de créer un filtre général, mais un filtre personnalisé pour le donneur, George Forman.


