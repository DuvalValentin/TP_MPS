# TP_MPS

## Lancer avec Docker

docker build -t python-docker-build .

docker run --name python-docker-run -p 8888:8888  python-docker-build

Un jupyter notebook sera alors lancé, il sera accessible via les liens affichés dans la console.

Un fois le notebook accedé il faut lancer TP3_turtles.ipynb pour acceder au TP3.

Exécuter les cellules et regarder les tortues tracer leurs figures

Dans un autre terminal lancer la commande : 

docker exec -it python-docker-run
cd work/
python3 TP4_Potions.py

Le programme s'occupe de déterminer les potions.
