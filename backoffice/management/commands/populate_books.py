# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from backoffice.models import Auteur, Livre, LivreType, LivreStatus


class Command(BaseCommand):
    help = 'Peuple la base de données avec des données diversifiées'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== Création des données ===\n'))

        # ── Genres ────────────────────────────────────────────────────────────
        self.stdout.write('1. Genres...')
        roman, _       = LivreType.objects.get_or_create(genre="roman")
        nouvelle, _    = LivreType.objects.get_or_create(genre="nouvelle")
        polar, _       = LivreType.objects.get_or_create(genre="polar")
        biographie, _  = LivreType.objects.get_or_create(genre="biographie")
        classique, _   = LivreType.objects.get_or_create(genre="classique")
        self.stdout.write('   OK\n')

        # ── Statuts ───────────────────────────────────────────────────────────
        self.stdout.write('2. Statuts...')
        publie, _       = LivreStatus.objects.get_or_create(status="toujours publié")
        arret, _        = LivreStatus.objects.get_or_create(status="en arrêt de commercialisation")
        reimpression, _ = LivreStatus.objects.get_or_create(status="réimpression")
        self.stdout.write('   OK\n')

        # ── Auteurs (5 nationalités différentes) ──────────────────────────────
        self.stdout.write('3. Auteurs...')
        auteurs_data = [
            ("Victor",      "Hugo",          "Française"),
            ("Gustave",     "Flaubert",      "Française"),
            ("Honoré de",   "Balzac",        "Française"),
            ("Alexandre",   "Dumas",         "Française"),
            ("Albert",      "Camus",         "Française"),
            ("George",      "Orwell",        "Britannique"),
            ("Arthur",      "Conan Doyle",   "Britannique"),
            ("Agatha",      "Christie",      "Britannique"),
            ("Ernest",      "Hemingway",     "Américaine"),
            ("Stephen",     "King",          "Américaine"),
            ("Franz",       "Kafka",         "Autrichienne"),
            ("Fyodor",      "Dostoïevski",   "Russe"),
        ]
        auteurs = {}
        for prenom, nom, nat in auteurs_data:
            a, created = Auteur.objects.get_or_create(
                prenom=prenom, nom=nom,
                defaults={'nationalite': nat}
            )
            auteurs[nom] = a
            self.stdout.write(f"   - {prenom} {nom} {'créé' if created else 'existe déjà'}")
        self.stdout.write('')

        # ── Livres ────────────────────────────────────────────────────────────
        self.stdout.write('4. Livres...')
        livres_data = [
            # (nom, prix, auteur_nom, genre, statut)
            ("Les Misérables",              8.50,  "Hugo",         roman,      publie),
            ("Notre-Dame de Paris",         9.90,  "Hugo",         roman,      publie),
            ("Les Contemplations",          6.00,  "Hugo",         nouvelle,   reimpression),
            ("Madame Bovary",               7.00,  "Flaubert",     roman,      publie),
            ("L'Éducation sentimentale",    8.00,  "Flaubert",     roman,      publie),
            ("Le Père Goriot",             11.00,  "Balzac",       roman,      publie),
            ("Eugénie Grandet",             9.50,  "Balzac",       roman,      publie),
            ("Les Trois Mousquetaires",    12.00,  "Dumas",        roman,      publie),
            ("Le Comte de Monte-Cristo",   14.90,  "Dumas",        roman,      publie),
            ("L'Étranger",                  7.50,  "Camus",        roman,      publie),
            ("La Peste",                    8.00,  "Camus",        roman,      publie),
            ("1984",                       10.00,  "Orwell",       roman,      publie),
            ("La Ferme des animaux",        6.50,  "Orwell",       nouvelle,   publie),
            ("Sherlock Holmes",             9.00,  "Conan Doyle",  polar,      reimpression),
            ("Le Chien des Baskerville",   10.50,  "Conan Doyle",  polar,      publie),
            ("Dix Petits Nègres",           8.90,  "Christie",     polar,      publie),
            ("Le Crime de l'Orient-Express",9.90,  "Christie",     polar,      publie),
            ("L'Adieu aux armes",           8.00,  "Hemingway",    roman,      arret),
            ("Le Vieil Homme et la Mer",    7.00,  "Hemingway",    nouvelle,   publie),
            ("Shining",                    13.00,  "King",         polar,      publie),
            ("Ça",                         15.90,  "King",         polar,      publie),
            ("La Métamorphose",             5.50,  "Kafka",        nouvelle,   reimpression),
            ("Le Procès",                   8.50,  "Kafka",        roman,      publie),
            ("Crime et Châtiment",         11.50,  "Dostoïevski",  roman,      publie),
            ("L'Idiot",                    12.00,  "Dostoïevski",  roman,      reimpression),
        ]

        nb_crees = 0
        for nom, prix, auteur_nom, genre, statut in livres_data:
            _, created = Livre.objects.get_or_create(
                nom=nom,
                defaults={
                    'prix': prix,
                    'auteur': auteurs[auteur_nom],
                    'livre_type': genre,
                    'livre_status': statut,
                }
            )
            if created:
                nb_crees += 1
            self.stdout.write(f"   - '{nom}' {'créé' if created else 'existe déjà'}")

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=== Données créées avec succès! ==='))
        self.stdout.write(
            f"Livres: {Livre.objects.count()} ({nb_crees} nouveaux) | "
            f"Auteurs: {Auteur.objects.count()} | "
            f"Genres: {LivreType.objects.count()} | "
            f"Statuts: {LivreStatus.objects.count()}"
        )
