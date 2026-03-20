# Bookr — Application de gestion de bibliothèque

Projet Django développé dans le cadre du cours M2. Application complète avec site public, espace backoffice et gestion de la base via des commandes Django.

---

## Stack technique

| Outil | Version |
|---|---|
| Python | 3.13 |
| Django | 6.0.3 |
| PostgreSQL | — |
| Tailwind CSS | 4.x (via django-tailwind) |
| Node.js | requis pour le build Tailwind |

---

## Structure du projet

```
bookr/                          ← racine Django (manage.py ici)
├── bookr/                      ← configuration projet
│   ├── settings.py
│   └── urls.py
├── bookr_app/                  ← site public
│   ├── views.py                ← catalogue, auteurs
│   ├── urls.py
│   └── templates/bookr_app/
│       ├── base.html
│       ├── index.html          ← catalogue + recherche + filtres genre
│       ├── auteurs.html        ← liste auteurs + filtre nationalité
│       └── auteur_detail.html  ← fiche auteur
├── backoffice/                 ← espace de gestion
│   ├── models.py               ← Auteur, Livre, LivreType, LivreStatus
│   ├── views.py                ← dashboard + CRUD livres & auteurs
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/backoffice/
│       ├── base.html
│       ├── index.html          ← dashboard (requêtes + gestion livres)
│       ├── livres/             ← list, form, confirm_delete
│       └── auteurs/            ← list, form, confirm_delete
├── theme/                      ← app django-tailwind
│   └── static_src/             ← sources Node (package.json, styles.css)
└── manage.py
```

---

## Installation

### 1. Dépendances Python

```bash
pip install django psycopg2-binary django-tailwind[cookiecutter,honcho,reload]
```

### 2. Base de données PostgreSQL

Créer la base avant de migrer :

```sql
CREATE DATABASE bookr_db ENCODING 'UTF8';
```

Configurer `bookr/settings.py` si nécessaire (HOST, PORT, USER, PASSWORD).

### 3. Migrations

```bash
python manage.py migrate
```

### 4. Données initiales

```bash
python manage.py populate_books
```

Crée 12 auteurs (5 nationalités), 25 livres, 5 genres et 3 statuts.

### 5. Build Tailwind CSS

```bash
python manage.py tailwind install   # première fois uniquement
python manage.py tailwind build     # compile le CSS
```

### 6. Lancer le serveur

```bash
python manage.py runserver
```

---

## URLs

| URL | Description |
|---|---|
| `/` | Catalogue public — recherche + filtre par genre |
| `/auteurs/` | Liste des auteurs — filtre par nationalité |
| `/auteurs/<id>/` | Fiche auteur + ses livres |
| `/backoffice/` | Dashboard — requêtes Django + gestion livres |
| `/backoffice/livres/` | Liste complète des livres |
| `/backoffice/livres/ajouter/` | Formulaire d'ajout |
| `/backoffice/livres/<id>/modifier/` | Formulaire d'édition |
| `/backoffice/livres/<id>/supprimer/` | Confirmation de suppression |
| `/backoffice/auteurs/` | Gestion des auteurs (même structure) |
| `/admin/` | Interface d'administration Django |

---

## Modèles

```
Auteur        prenom, nom, nationalite
LivreType     genre (roman, nouvelle, polar, biographie, classique)
LivreStatus   status (toujours publié, réimpression, en arrêt de commercialisation)
Livre         nom, prix, auteur (FK), livre_type (FK), livre_status (FK)
```

---

## Commandes de gestion

```bash
# Peupler la base avec les données de démonstration (idempotent)
python manage.py populate_books

# Modifier certains statuts de livres (exercice)
python manage.py modify_books

# Remettre la base à zéro
python manage.py reset_books
python manage.py reset_books --no-input   # sans confirmation
```

---

## Développement avec Tailwind

Deux terminaux en parallèle :

```bash
# Terminal 1
python manage.py runserver

# Terminal 2 — recompile le CSS à chaque modification de template
python manage.py tailwind start
```

> Sur Windows, `tailwind dev` (qui lance les deux simultanément) n'est pas supporté.

---

## Administration Django

```bash
python manage.py createsuperuser
```

Accessible sur `/admin/` — gestion complète des modèles avec filtres, recherche et fieldsets configurés.

---

## Requêtes Django (dashboard backoffice)

Le dashboard `/backoffice/` illustre 8 requêtes ORM :

1. `Livre.objects.all()`
2. `Livre.objects.filter(nom__startswith="L")`
3. `Livre.objects.filter(nom__icontains="Misérables")`
4. `Livre.objects.filter(prix__gte=10)`
5. `Livre.objects.filter(prix__gte=10, livre_status__status="toujours publié")`
6. `Livre.objects.order_by('-prix').first()`
7. `LivreStatus.objects.all()`
8. `Livre.objects.count()`
