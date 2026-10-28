# Bookr — Library management app

**English** · [Français](README.fr.md)

A Django project built for a Master's (M2) course. A complete app with a public site, a back-office and database management through Django commands.

---

## Tech stack

| Tool | Version |
|---|---|
| Python | 3.13 |
| Django | 6.0.3 |
| PostgreSQL | — |
| Tailwind CSS | 4.x (via django-tailwind) |
| Node.js | required for the Tailwind build |

---

## Project structure

```
bookr/                          ← Django root (manage.py here)
├── bookr/                      ← project configuration
│   ├── settings.py
│   └── urls.py
├── bookr_app/                  ← public site
│   ├── views.py                ← catalog, authors
│   ├── urls.py
│   └── templates/bookr_app/
│       ├── base.html
│       ├── index.html          ← catalog + search + genre filters
│       ├── auteurs.html        ← author list + nationality filter
│       └── auteur_detail.html  ← author page
├── backoffice/                 ← management area
│   ├── models.py               ← Auteur, Livre, LivreType, LivreStatus
│   ├── views.py                ← dashboard + books & authors CRUD
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/backoffice/
│       ├── base.html
│       ├── index.html          ← dashboard (queries + book management)
│       ├── livres/             ← list, form, confirm_delete
│       └── auteurs/            ← list, form, confirm_delete
├── theme/                      ← django-tailwind app
│   └── static_src/             ← Node sources (package.json, styles.css)
└── manage.py
```

---

## Installation

### 1. Python dependencies

```bash
pip install django psycopg2-binary django-tailwind[cookiecutter,honcho,reload]
```

### 2. PostgreSQL database

Create the database before migrating:

```sql
CREATE DATABASE bookr_db ENCODING 'UTF8';
```

Adjust `bookr/settings.py` if needed (HOST, PORT, USER, PASSWORD).

### 3. Migrations

```bash
python manage.py migrate
```

### 4. Seed data

```bash
python manage.py populate_books
```

Creates 12 authors (5 nationalities), 25 books, 5 genres and 3 statuses.

### 5. Build Tailwind CSS

```bash
python manage.py tailwind install   # first time only
python manage.py tailwind build     # compiles the CSS
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## URLs

| URL | Description |
|---|---|
| `/` | Public catalog — search + genre filter |
| `/auteurs/` | Author list — nationality filter |
| `/auteurs/<id>/` | Author page + their books |
| `/backoffice/` | Dashboard — Django queries + book management |
| `/backoffice/livres/` | Full book list |
| `/backoffice/livres/ajouter/` | Add form |
| `/backoffice/livres/<id>/modifier/` | Edit form |
| `/backoffice/livres/<id>/supprimer/` | Delete confirmation |
| `/backoffice/auteurs/` | Author management (same structure) |
| `/admin/` | Django admin |

---

## Models

```
Auteur        prenom, nom, nationalite
LivreType     genre (novel, short story, crime, biography, classic)
LivreStatus   status (still in print, reprint, out of print)
Livre         nom, prix, auteur (FK), livre_type (FK), livre_status (FK)
```

Model and field names are in French (`Auteur` = author, `Livre` = book, `prix` = price).

---

## Management commands

```bash
# Seed the database with demo data (idempotent)
python manage.py populate_books

# Change some book statuses (exercise)
python manage.py modify_books

# Reset the database
python manage.py reset_books
python manage.py reset_books --no-input   # without confirmation
```

---

## Developing with Tailwind

Two terminals side by side:

```bash
# Terminal 1
python manage.py runserver

# Terminal 2 — recompiles the CSS on every template change
python manage.py tailwind start
```

> On Windows, `tailwind dev` (which runs both at once) is not supported.

---

## Django admin

```bash
python manage.py createsuperuser
```

Available at `/admin/` — full model management with filters, search and configured fieldsets.

---

## Django queries (back-office dashboard)

The `/backoffice/` dashboard demonstrates 8 ORM queries:

1. `Livre.objects.all()`
2. `Livre.objects.filter(nom__startswith="L")`
3. `Livre.objects.filter(nom__icontains="Misérables")`
4. `Livre.objects.filter(prix__gte=10)`
5. `Livre.objects.filter(prix__gte=10, livre_status__status="toujours publié")`
6. `Livre.objects.order_by('-prix').first()`
7. `LivreStatus.objects.all()`
8. `Livre.objects.count()`
