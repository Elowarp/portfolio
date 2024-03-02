# Portfolio

Ensemble des fichiers nécessaires pour faire tourner le site web portfolio

On suppose dans la suite se trouver dans le répertoire principal du projet.

## Developpement

Fait avec python3.11, pour commencer à faire tourner le serveur en local :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver --settings=Portfolio.settings.development
```

## Production

La production est basée sur Nginx et Gunicorn avec une base de données MongoDB

Pour installer nginx :

```bash
sudo apt install nginx
```

Commande pour lancer le serveur comme en production :

```bash
gunicorn -c config/gunicorn/prod.py
```

Fichier .env typique :

```text
DB_USERNAME=
DB_PASSWORD=
DB_CLUSTER=
DB_NAME=
DJANGO_SECRET_KEY=
```

Rendre disponible les fichiers statiques :

```bash
sudo mkdir -pv /var/www/portfolio/static/
sudo chown -R $USER /var/www/portfolio/
python manage.py collectstatic --settings=Portfolio.settings.development
```

### Setup Nginx

Copier des fichiers de configurations et rechargement des logiciels :

```bash
sudo cp ./config/nginx/portfolio.conf /etc/nginx/sites-available/portfolio.conf
sudo ln -s /etc/nginx/sites-available/portfolio.conf /etc/nginx/sites-enabled/portfolio.conf
sudo systemctl restart nginx
```
