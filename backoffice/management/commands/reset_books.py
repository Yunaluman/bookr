# -*- coding: utf-8 -*-
"""
Management command pour réinitialiser complètement la base de données
Usage: python manage.py reset_books
"""
from django.core.management.base import BaseCommand
from backoffice.models import Livre, LivreType, LivreStatus


class Command(BaseCommand):
    help = 'Supprime toutes les données et recrée les données initiales'

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-input',
            action='store_true',
            help='Ne pas demander de confirmation',
        )

    def handle(self, *args, **options):
        # Demander confirmation si --no-input n'est pas utilisé
        if not options['no_input']:
            confirm = input(
                self.style.WARNING(
                    '\n⚠️  ATTENTION: Cette opération va SUPPRIMER toutes les données!\n'
                    'Voulez-vous continuer? (oui/non): '
                )
            )
            if confirm.lower() not in ['oui', 'yes', 'y', 'o']:
                self.stdout.write(self.style.ERROR('Opération annulée.'))
                return

        self.stdout.write(self.style.SUCCESS('\n=== Réinitialisation de la base de données ===\n'))

        # 1. Supprimer toutes les données existantes
        self.stdout.write('1. Suppression des données existantes...')
        livre_count = Livre.objects.count()
        type_count = LivreType.objects.count()
        status_count = LivreStatus.objects.count()
        
        Livre.objects.all().delete()
        LivreType.objects.all().delete()
        LivreStatus.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS(
            f'   [OK] {livre_count} livres, {type_count} types et {status_count} statuts supprimes\n'
        ))

        # 2. Créer les LivreType
        self.stdout.write('2. Creation des types de livres...')
        genre_roman = LivreType.objects.create(genre="roman")
        self.stdout.write('   [OK] Type "roman" cree')

        genre_nouvelle = LivreType.objects.create(genre="nouvelle")
        self.stdout.write('   [OK] Type "nouvelle" cree')

        genre_polar = LivreType.objects.create(genre="polar")
        self.stdout.write('   [OK] Type "polar" cree')

        genre_biographie = LivreType.objects.create(genre="biographie")
        self.stdout.write('   [OK] Type "biographie" cree\n')

        # 3. Créer les LivreStatus
        self.stdout.write('3. Creation des statuts de livres...')
        status_publie = LivreStatus.objects.create(status="toujours publié")
        self.stdout.write('   [OK] Statut "toujours publie" cree')

        status_arret = LivreStatus.objects.create(status="en arrêt de commercialisation")
        self.stdout.write('   [OK] Statut "en arret de commercialisation" cree')

        status_reimpression = LivreStatus.objects.create(status="réimpression")
        self.stdout.write('   [OK] Statut "reimpression" cree\n')

        # 4. Créer les 3 Livres
        self.stdout.write('4. Creation des livres initiaux...')

        livre1 = Livre.objects.create(
            nom="Les Misérables",
            prix=8,
            livre_type=genre_roman,
            livre_status=status_publie
        )
        self.stdout.write('   [OK] "Les Miserables" cree')

        livre2 = Livre.objects.create(
            nom="Madame Bovary",
            prix=7,
            livre_type=genre_roman,
            livre_status=status_publie
        )
        self.stdout.write('   [OK] "Madame Bovary" cree')

        livre3 = Livre.objects.create(
            nom="Honoré de Balzac",
            prix=11,
            livre_type=genre_roman,
            livre_status=status_publie
        )
        self.stdout.write('   [OK] "Honore de Balzac" cree\n')

        self.stdout.write(self.style.SUCCESS('=== Reinitialisation terminee avec succes! ==='))
        self.stdout.write(f"\n[STATS] Statistiques:")
        self.stdout.write(f"   - Livres: {Livre.objects.count()}")
        self.stdout.write(f"   - Types: {LivreType.objects.count()}")
        self.stdout.write(f"   - Statuts: {LivreStatus.objects.count()}\n")

        # Vérification des accents
        self.stdout.write("[VERIFICATION] Liste des livres crees:")
        for livre in Livre.objects.all():
            self.stdout.write(f"   - {livre.nom}")
