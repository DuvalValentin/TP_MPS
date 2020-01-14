# TP_MPS

## Lancer avec Docker

### TP3

Dans le répertoire du projet il faut entrer les commandes suivantes :

    docker build -t python-docker-build .
    docker run --name python-docker-run -p 8888:8888  python-docker-build

Un jupyter notebook sera alors lancé, il sera accessible via les liens affichés dans la console.

Un fois le notebook accedé il faut lancer TP3_turtles.ipynb pour acceder au TP3.

Exécuter les cellules et regarder les tortues tracer leurs figures

### TP4

Dans un autre terminal et toujours dans le répertoire du projet et en ayant effectué les commandes pour le TP3 lancer les commandes : 

    docker exec -it python-docker-run bash
    cd work/
    TP4_Potions.py

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