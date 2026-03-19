# -*- coding: utf-8 -*-
"""
Management command pour modifier les données selon les exigences du projet
Usage: python manage.py modify_books
"""
from django.core.management.base import BaseCommand
from backoffice.models import Livre, LivreStatus


class Command(BaseCommand):
    help = 'Modifie les statuts et supprime le 3ème livre'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== Modifications des données ===\n'))

        # Récupérer tous les livres
        livres = Livre.objects.all().order_by('id')

        if livres.count() >= 3:
            # 1. Modifier le statut du 2ème livre de "toujours publié" à "réimpression"
            livre2 = livres[1]
            status_reimpression = LivreStatus.objects.get(status="réimpression")
            
            self.stdout.write(f"1. Modification du statut du 2ème livre: {livre2.nom}")
            self.stdout.write(f"   Ancien statut: {livre2.livre_status.status}")
            livre2.livre_status = status_reimpression
            livre2.save()
            self.stdout.write(self.style.SUCCESS(f"   ✓ Nouveau statut: {livre2.livre_status.status}\n"))
            
            # 2. Modifier le statut du 3ème livre à "en arrêt de commercialisation"
            livre3 = livres[2]
            status_arret = LivreStatus.objects.get(status="en arrêt de commercialisation")
            
            self.stdout.write(f"2. Modification du statut du 3ème livre: {livre3.nom}")
            self.stdout.write(f"   Ancien statut: {livre3.livre_status.status}")
            livre3.livre_status = status_arret
            livre3.save()
            self.stdout.write(self.style.SUCCESS(f"   ✓ Nouveau statut: {livre3.livre_status.status}\n"))
            
            # 3. Supprimer le 3ème livre
            self.stdout.write(f"3. Suppression du 3ème livre: {livre3.nom}")
            livre3_nom = livre3.nom
            livre3.delete()
            self.stdout.write(self.style.SUCCESS(f"   ✓ '{livre3_nom}' a été supprimé\n"))
        else:
            self.stdout.write(self.style.ERROR("Erreur: Pas assez de livres dans la base de données"))
            return

        # 4. Afficher le nombre total de livres restants
        nombre_livres = Livre.objects.count()
        self.stdout.write(self.style.SUCCESS(f"=== Nombre total de livres restants: {nombre_livres} ==="))

        # Afficher les livres restants
        self.stdout.write("\nLivres restants:")
        for livre in Livre.objects.all():
            self.stdout.write(f"  - {livre.nom} ({livre.prix}€) - Status: {livre.livre_status.status}")
