# Portfolio

Ensemble des fichiers nécessaires pour faire tourner le site web portfolio

On suppose dans la suite se trouver dans le répertoire principal du projet.

## Developpement

**Fait avec Python 3.11, le serveur peut marcher avec des versions précédentes mais ça n'à pas été testé.**

Pour commencer à faire tourner le serveur en local :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver --settings=Portfolio.settings.development
```

_Description : Création d'un environnement de développement, installations des dépendances puis démarrage du serveur web._

## Production

La production est basée sur Nginx et Gunicorn avec une base de données MongoDB. Nginx étant l'interface avec le monde extérieur et le serveur web, et Gunicorn qui gère le serveur web.

Fichier .env typique pour se connecter à la base de données :

```text
DB_USERNAME=
DB_PASSWORD=
DB_CLUSTER=
DB_NAME=
DJANGO_SECRET_KEY=
```

Commande pour lancer le serveur comme en production :

```bash
gunicorn -c config/gunicorn/prod.py
```

_Note: Vous aurez surement des problèmes à charger les fichiers statiques, c'est parce qu'il va les chercher à des endroits bien spécial du système, cf la partie Nginx._

### Setup Nginx

Pour installer nginx :

```bash
sudo apt install nginx
```

On utilise une certificat let's encrypt pour le https [[source]](https://www.it-connect.fr/nginx-ajouter-un-certificat-ssl-lets-encrypt-pour-passer-en-https/) (Vérifier à bien mettre les fichiers aux bons endroits, conformément au fichier `./config/nginx/portfolio.conf`)

Rendre la configuration Nginx opérande :

```bash
sudo cp ./config/nginx/portfolio.conf /etc/nginx/sites-available/portfolio.conf
sudo ln -s /etc/nginx/sites-available/portfolio.conf /etc/nginx/sites-enabled/portfolio.conf
sudo systemctl restart nginx
```

_Description : Copie du fichier de configurations dans les dossier prévu par Nginx puis redémarrage de Nginx pour appliquer les changements._

Rendre disponible les fichiers statiques par le serveur web :

```bash
sudo mkdir -pv /var/www/portfolio/static/
sudo chown -R $USER /var/www/portfolio/
python manage.py collectstatic --settings=Portfolio.settings.development
```
