# TP_MPS

## Lancer avec Docker

### 1) Récupération de l'image docker

#### Création à partir du Dockerfile

    docker build -t python-docker-build .

#### Ou récupération avec Dockerhub

    docker pull valentinduval/python-docker-build:latest

### 2) Lancer l'image dans un container

    docker run --name python-docker-run -p 8888:8888  python-docker-build

Un jupyter-notebook sera alors lancé, il sera accessible via les liens affichés dans la console.

### 3) Exécuter le TP3

Se rendre à l'une des adresses indiquées dans la console, puis aller dans le dossier work/ puis lancer TP3_turtles.ipynb.

Exécuter les cellules et regarder les tortues tracer leurs figures.

### 4) Lancer un terminal dans le container

Dans un autre terminal et toujours dans le répertoire du projet et en ayant effectué les commandes pour le TP3 lancer la commande : 

    docker exec -it python-docker-run bash

### 5) Exécuter le TP4

Entrer les commandes

    cd work/
    python3 TP4_Potions.py

Le programme s'occupe de déterminer le contenu des potions.

## Lancer avec jupyter-notebook et python

En considérant que jupyter-notebook et python sont installés

### TP3

Entrer la commande : 

    jupyter-notebook TP3_turtles.ipynb

Exécuter les cellules et regarder les tortues tracer leurs figures

### TP4

Entrer la commande

    python3 TP4_Potions.py

Le programme s'occupe de déterminer le contenu des potions.