# Pyros — Site vitrine (Django)

Petit site Django (TAROT × PyRoS) : pages “Accueil”, “TAROT”, “PyRoS”, “Fonctionnalités”, “FAQ”, “Contact”.
Aucun accès base de données nécessaire pour tester en local.

## Prérequis
- Python 3.12+
- pip

## Installation (macOS / Linux)

# 1) Cloner
git clone https://github.com/<ton-user>/pyros.git
cd pyros

# 2) Environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# 3) Dépendances
pip install "Django==5.2.6"

# 4) Lancer le serveur
python manage.py runserver
# Ouvrir http://127.0.0.1:8000/
