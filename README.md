# Pyros — Site vitrine (Django)

Petit site Django (TAROT × PyRoS) : pages “Accueil”, “TAROT”, “PyRoS”, “Fonctionnalités”, “FAQ”, “Contact”.
Aucun accès base de données nécessaire pour tester en local.

## Prérequis
- Python 3.12+
- pip

## Installation (macOS / Linux)

# 1) Cloner
```bash
git clone https://github.com/ArthurMovellan/TAROT-Pyros.git
cd pyros
```

# 2) Environnement virtuel
```bash
python3 -m venv .venv
source .venv/bin/activate
```

# 3) Dépendances
```bash
pip install "Django==5.2.6"
```

# 4) Lancer le serveur
```bash
python manage.py runserver
```
Ouvrir http://127.0.0.1:8000/
