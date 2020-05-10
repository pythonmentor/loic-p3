# Commentaires en vrac

## requirements.txt
Les commentaires pour le fichier de requirements.txt ont été ajoutés directement 
dans le fichier.

## Structure du projet

- mettre tous les modules du code source à la racine du projet n'est pas 
  nécessairement une pratique recommandée. Créer un package pour le projet avec 
  un fichier __init__.py et un __main__.py. Je recommande également de séparer 
  les modules de logique et les modules d'interface utilisateur dans des 
  sous-packages séparés.
- Dans le package lib, tu as un module appelé `__init.py__`. Tu as certainement 
  voulu le nommer `__init__.py` et commis une erreur.
- funct n'est pas un bon nom pour un module python, tout comme functions ou
  d'autres noms associés au "comment". Nommer un module par rapport à son rôle
  dans le projet.