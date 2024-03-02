# Portfolio

Ensemble des fichiers nécessaires pour faire tourner le site web portfolio

## Developpement

Fait avec python3.11, pour commencer à faire tourner le serveur en local :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver --settings=Portfolio.settings.development
```

## Production

Commande pour lancer le server comme en production :
```gunicorn -c config/gunicorn/dev.py```

Fichier .env typique :

```text

```

### Setup Nginx

Copier le fichier `portfolio.conf` de `config/nginx/` dans `/etc/nginx/sites-available` puis faire :

```sudo ln -s /etc/nginx/sites-available/portfolio.conf /etc/nginx/sites-enabled/portfolio.conf```

