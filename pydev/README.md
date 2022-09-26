# pydev

Cet application convertit le document pdf en audio mp3. vous pouvez écouter l'audio directement sur l'application ou vous pouvez également le télécharger.

# Recuperer une copie de ce projet

Ce projet est entièrement concu avec python/django et quelques javascript. <br />
 Tous les dependances sont dans le fichier ```PipeFile``` ou ```requirements.txt```
 
 ## Requirements
 - Ce projet requiert l'interpreteur python. Si vous n'avez pas python installé dans votre bécane, <a href="https://www.python.org/">rendez-vous ici</a> pour l'obtenir

## kills Required

- Un minimum connaissance sur python est obligatoire.
- Connaître la structure de framework django est obligatoire.

## Pour tester ce projet sur votre bécane, proceder comme suite:
# Ouvrez votre terminal et executer 
- optionnel : Vous pouvez créer une environnement virtuel, mais c'est pas obligatoire. Pour créer et activer un venv <a href="https://docs.python.org/fr/3/library/venv.html">visiter ici</a>

```git clone https://github.com/makan-dianka/pydev.git```

```cd pydev```
- faite ```ls``` sur linux ```dir``` sur windows et assurez-vous que ce fichier ```manage.py``` est présent 

```pip install -r requirements.txt ```

```python manage.py makemigrations```

```python manage.py migrate```

Créer un superuser, tapez cette commande ```python manage.py createsuperuser```  et renseigner les informations demandé.

démarrer le serveur avec la commande suivante ```python manage.py runserver```

par défaut le serveur de django écoute sur le port ```8000```
rendez-vous dans le navigateur tapez ```localhost:8000``` ou ```127.0.0.1:8000```  puis connecter vous

## ET voilà ! 

