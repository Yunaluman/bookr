"""
Script pour peupler la base de données avec les livres
"""
from backoffice.models import Livre, LivreType, LivreStatus

print("=== Création des données ===\n")

# 1. Créer les LivreType
print("1. Création des types de livres...")
genre_roman, created = LivreType.objects.get_or_create(genre="roman")
print(f"   - Type 'roman' {'créé' if created else 'existe déjà'}")

genre_nouvelle, created = LivreType.objects.get_or_create(genre="nouvelle")
print(f"   - Type 'nouvelle' {'créé' if created else 'existe déjà'}")

genre_polar, created = LivreType.objects.get_or_create(genre="polar")
print(f"   - Type 'polar' {'créé' if created else 'existe déjà'}")

genre_biographie, created = LivreType.objects.get_or_create(genre="biographie")
print(f"   - Type 'biographie' {'créé' if created else 'existe déjà'}\n")

# 2. Créer les LivreStatus
print("2. Création des statuts de livres...")
status_publie, created = LivreStatus.objects.get_or_create(status="toujours publié")
print(f"   - Statut 'toujours publié' {'créé' if created else 'existe déjà'}")

status_arret, created = LivreStatus.objects.get_or_create(status="en arrêt de commercialisation")
print(f"   - Statut 'en arrêt de commercialisation' {'créé' if created else 'existe déjà'}")

status_reimpression, created = LivreStatus.objects.get_or_create(status="réimpression")
print(f"   - Statut 'réimpression' {'créé' if created else 'existe déjà'}\n")

# 3. Créer les 3 Livres
print("3. Création des livres...")

livre1, created = Livre.objects.get_or_create(
    nom="Les Misérables",
    defaults={
        'prix': 8,
        'livre_type': genre_roman,
        'livre_status': status_publie
    }
)
print(f"   - 'Les Misérables' {'créé' if created else 'existe déjà'}")

livre2, created = Livre.objects.get_or_create(
    nom="Madame Bovary",
    defaults={
        'prix': 7,
        'livre_type': genre_roman,
        'livre_status': status_publie
    }
)
print(f"   - 'Madame Bovary' {'créé' if created else 'existe déjà'}")

livre3, created = Livre.objects.get_or_create(
    nom="Honoré de Balzac",
    defaults={
        'prix': 11,
        'livre_type': genre_roman,
        'livre_status': status_publie
    }
)
print(f"   - 'Honoré de Balzac' {'créé' if created else 'existe déjà'}\n")

print("=== Données créées avec succès! ===")
print(f"\nNombre total de livres: {Livre.objects.count()}")
print(f"Nombre total de types: {LivreType.objects.count()}")
print(f"Nombre total de statuts: {LivreStatus.objects.count()}")
