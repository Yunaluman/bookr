# -*- coding: utf-8 -*-
"""
Management command pour peupler la base de données avec les livres
Usage: python manage.py populate_books
"""
from django.core.management.base import BaseCommand
from backoffice.models import Livre, LivreType, LivreStatus


class Command(BaseCommand):
    help = 'Peuple la base de données avec les livres de test'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== Création des données ===\n'))

        # 1. Créer les LivreType
        self.stdout.write('1. Création des types de livres...')
        genre_roman, created = LivreType.objects.get_or_create(genre="roman")
        self.stdout.write(f"   - Type 'roman' {'créé' if created else 'existe déjà'}")

        genre_nouvelle, created = LivreType.objects.get_or_create(genre="nouvelle")
        self.stdout.write(f"   - Type 'nouvelle' {'créé' if created else 'existe déjà'}")

        genre_polar, created = LivreType.objects.get_or_create(genre="polar")
        self.stdout.write(f"   - Type 'polar' {'créé' if created else 'existe déjà'}")

        genre_biographie, created = LivreType.objects.get_or_create(genre="biographie")
        self.stdout.write(f"   - Type 'biographie' {'créé' if created else 'existe déjà'}\n")

        # 2. Créer les LivreStatus
        self.stdout.write('2. Création des statuts de livres...')
        status_publie, created = LivreStatus.objects.get_or_create(status="toujours publié")
        self.stdout.write(f"   - Statut 'toujours publié' {'créé' if created else 'existe déjà'}")

        status_arret, created = LivreStatus.objects.get_or_create(
            status="en arrêt de commercialisation"
        )
        self.stdout.write(f"   - Statut 'en arrêt de commercialisation' {'créé' if created else 'existe déjà'}")

        status_reimpression, created = LivreStatus.objects.get_or_create(status="réimpression")
        self.stdout.write(f"   - Statut 'réimpression' {'créé' if created else 'existe déjà'}\n")

        # 3. Créer les 3 Livres
        self.stdout.write('3. Création des livres...')

        livre1, created = Livre.objects.get_or_create(
            nom="Les Misérables",
            defaults={
                'prix': 8,
                'livre_type': genre_roman,
                'livre_status': status_publie
            }
        )
        self.stdout.write(f"   - 'Les Misérables' {'créé' if created else 'existe déjà'}")

        livre2, created = Livre.objects.get_or_create(
            nom="Madame Bovary",
            defaults={
                'prix': 7,
                'livre_type': genre_roman,
                'livre_status': status_publie
            }
        )
        self.stdout.write(f"   - 'Madame Bovary' {'créé' if created else 'existe déjà'}")

        livre3, created = Livre.objects.get_or_create(
            nom="Honoré de Balzac",
            defaults={
                'prix': 11,
                'livre_type': genre_roman,
                'livre_status': status_publie
            }
        )
        self.stdout.write(f"   - 'Honoré de Balzac' {'créé' if created else 'existe déjà'}\n")

        self.stdout.write(self.style.SUCCESS('=== Données créées avec succès! ==='))
        self.stdout.write(f"\nNombre total de livres: {Livre.objects.count()}")
        self.stdout.write(f"Nombre total de types: {LivreType.objects.count()}")
        self.stdout.write(f"Nombre total de statuts: {LivreStatus.objects.count()}")
